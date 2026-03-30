"""Issue commands for bklg."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from bklg.api.client import BacklogAPIError, BacklogClient
from bklg.config.settings import get_settings
from bklg.models.attachment import Attachment
from bklg.models.issue import Comment, Issue
from bklg.resolver.base import ResolverError
from bklg.resolver.cache import ResolverCache
from bklg.resolver.issue_type import IssueTypeResolver
from bklg.resolver.priority import PriorityResolver
from bklg.resolver.project import ProjectResolver
from bklg.resolver.status import StatusResolver
from bklg.resolver.user import UserResolver
from bklg.utils.exporter import IssueExporter
from bklg.utils.formatter import IssueFormatter

app = typer.Typer(help="Issue commands")
comment_app = typer.Typer(help="Comment commands")
attachment_app = typer.Typer(help="Attachment commands")
app.add_typer(comment_app, name="comment")
app.add_typer(attachment_app, name="attachment")

console = Console()
err_console = Console(stderr=True)


def parse_issue_identifier(identifier: str) -> str:
    """Parse issue identifier from various formats.

    Supports:
    - Issue key: PROJ-123
    - Numeric ID: 12345
    - URL: https://example.backlog.com/view/PROJ-123

    Args:
        identifier: Issue identifier in any supported format.

    Returns:
        Issue key or ID suitable for API.
    """
    # Check if it's a URL
    url_match = re.search(r"/view/([A-Z0-9_]+-\d+)", identifier, re.IGNORECASE)
    if url_match:
        return url_match.group(1)

    return identifier


@app.command("list")
def list_issues(
    project: Annotated[
        str | None,
        typer.Option("--project", "-p", help="Project key or ID"),
    ] = None,
    all_projects: Annotated[
        bool,
        typer.Option("--all-projects", help="Search across all projects"),
    ] = False,
    status: Annotated[
        str | None,
        typer.Option("--status", "-s", help="Filter by status name"),
    ] = None,
    assignee: Annotated[
        str | None,
        typer.Option("--assignee", "-a", help="Filter by assignee (@me for self)"),
    ] = None,
    keyword: Annotated[
        str | None,
        typer.Option("--keyword", "-k", help="Search keyword"),
    ] = None,
    due_date_since: Annotated[
        str | None,
        typer.Option("--due-date-since", help="Filter by due date from (YYYY-MM-DD)"),
    ] = None,
    due_date_until: Annotated[
        str | None,
        typer.Option("--due-date-until", help="Filter by due date until (YYYY-MM-DD)"),
    ] = None,
    overdue: Annotated[
        bool,
        typer.Option("--overdue", help="Show only overdue issues"),
    ] = False,
    limit: Annotated[
        int,
        typer.Option("--limit", "-l", help="Number of issues to fetch"),
    ] = 20,
    offset: Annotated[
        int,
        typer.Option("--offset", help="Offset for pagination"),
    ] = 0,
    sort: Annotated[
        str,
        typer.Option("--sort", help="Sort field (created, updated, dueDate, etc.)"),
    ] = "updated",
    order: Annotated[
        str,
        typer.Option("--order", help="Sort order (asc, desc)"),
    ] = "desc",
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """List issues with optional filters."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        err_console.print("Run 'bklg auth login' to authenticate.")
        raise typer.Exit(1)

    # Validate project/all-projects options
    if project and all_projects:
        err_console.print("[red]Cannot specify both --project and --all-projects.[/red]")
        raise typer.Exit(1)
    if not project and not all_projects:
        err_console.print("[red]Must specify either --project or --all-projects.[/red]")
        raise typer.Exit(1)

    # Handle --overdue flag
    effective_due_date_until = due_date_until
    if overdue:
        from datetime import date, timedelta

        yesterday = date.today() - timedelta(days=1)
        effective_due_date_until = yesterday.strftime("%Y-%m-%d")

    try:
        with BacklogClient(settings=settings) as client:
            cache = ResolverCache()
            params: dict[str, str | int | list[int]] = {
                "count": limit,
                "offset": offset,
                "sort": sort,
                "order": order,
            }

            # Resolve project (only if not --all-projects)
            if project:
                project_resolver = ProjectResolver(client, cache)
                project_id = project_resolver.resolve(project)
                params["projectId[]"] = [project_id]

            # Resolve assignee
            if assignee:
                user_resolver = UserResolver(client, cache)
                assignee_id = user_resolver.resolve(assignee)
                params["assigneeId[]"] = [assignee_id]

            # Add keyword
            if keyword:
                params["keyword"] = keyword

            # Add due date filters
            if due_date_since:
                params["dueDateSince"] = due_date_since
            if effective_due_date_until:
                params["dueDateUntil"] = effective_due_date_until

            # Resolve status
            if status:
                if project:
                    project_resolver = ProjectResolver(client, cache)
                    proj = project_resolver.get_project(project)
                    # Fetch statuses for this project
                    status_data = client.get(f"/projects/{proj.id}/statuses")
                    status_map = {s["name"]: s["id"] for s in status_data}  # type: ignore[union-attr]
                    if status in status_map:
                        params["statusId[]"] = [status_map[status]]
                else:
                    # For --all-projects, we cannot filter by status name
                    # since different projects may have different status IDs
                    err_console.print(
                        "[yellow]Warning: --status filter requires --project to be specified.[/yellow]"
                    )

            # Fetch issues
            data = client.get("/issues", params=params)
            issues = [Issue.model_validate(i) for i in data]  # type: ignore[union-attr]

            # If --overdue, filter out completed issues
            if overdue:
                # Filter by status: exclude "完了" (Closed) status
                issues = [i for i in issues if i.status.name != "完了"]

        if json_output:
            import json

            out = [i.model_dump(by_alias=True, mode="json") for i in issues]
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        if not issues:
            console.print("[yellow]No issues found.[/yellow]")
            return

        formatter = IssueFormatter(console)
        title = "Issues"
        if project:
            title = f"Issues: {project}"
        elif all_projects:
            title = "Issues: All Projects"

        table = formatter.format_issue_table(issues, title=title)
        console.print(table)

        # Show pagination info
        if len(issues) == limit:
            console.print(
                f"\n[dim]Showing {offset + 1}-{offset + len(issues)}. "
                f"Use --offset {offset + limit} for more.[/dim]"
            )

    except ResolverError as e:
        err_console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e
    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("view")
def view_issue(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    comments: Annotated[
        bool,
        typer.Option("--comments", "-c", help="Show comments"),
    ] = False,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
    web: Annotated[
        bool,
        typer.Option("--web", "-w", help="Open in browser"),
    ] = False,
) -> None:
    """View issue details."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        err_console.print("Run 'bklg auth login' to authenticate.")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    # Open in browser if requested
    if web:
        import webbrowser

        url = f"{settings.space_url}/view/{issue_key}"
        webbrowser.open(url)
        console.print(f"Opening {url} in browser...")
        return

    try:
        with BacklogClient(settings=settings) as client:
            # Fetch issue
            data = client.get(f"/issues/{issue_key}")
            issue = Issue.model_validate(data)

            # Fetch comments if requested
            issue_comments: list[Comment] = []
            if comments:
                comment_data = client.get(f"/issues/{issue_key}/comments")
                issue_comments = [
                    Comment.model_validate(c) for c in comment_data  # type: ignore[union-attr]
                ]

        if json_output:
            import json

            out = issue.model_dump(by_alias=True, mode="json")
            if comments:
                out["comments"] = [
                    c.model_dump(by_alias=True, mode="json") for c in issue_comments
                ]
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        formatter = IssueFormatter(console)
        formatter.format_issue_detail(issue, space_url=settings.space_url)

        if comments:
            formatter.format_comments(issue_comments)

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Issue '{issue_key}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("open")
def open_issue(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
) -> None:
    """Open issue in browser."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    import webbrowser

    issue_key = parse_issue_identifier(issue_id)
    url = f"{settings.space_url}/view/{issue_key}"
    webbrowser.open(url)
    console.print(f"Opening {url} in browser...")


@app.command("create")
def create_issue(
    project: Annotated[
        str,
        typer.Option("--project", "-p", help="Project key or ID"),
    ],
    summary: Annotated[
        str,
        typer.Option("--summary", "-s", help="Issue summary/title"),
    ],
    issue_type: Annotated[
        str,
        typer.Option("--type", "-t", help="Issue type name"),
    ],
    description: Annotated[
        str | None,
        typer.Option("--description", "-d", help="Issue description"),
    ] = None,
    priority: Annotated[
        str,
        typer.Option("--priority", help="Priority name (default: 中)"),
    ] = "中",
    assignee: Annotated[
        str | None,
        typer.Option("--assignee", "-a", help="Assignee (@me for self)"),
    ] = None,
    due_date: Annotated[
        str | None,
        typer.Option("--due-date", help="Due date (YYYY-MM-DD)"),
    ] = None,
    start_date: Annotated[
        str | None,
        typer.Option("--start-date", help="Start date (YYYY-MM-DD)"),
    ] = None,
    estimated_hours: Annotated[
        float | None,
        typer.Option("--estimated-hours", help="Estimated hours"),
    ] = None,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Create a new issue."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        err_console.print("Run 'bklg auth login' to authenticate.")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            cache = ResolverCache()

            # Resolve project
            project_resolver = ProjectResolver(client, cache)
            proj = project_resolver.get_project(project)

            # Resolve issue type
            issue_type_resolver = IssueTypeResolver(
                client, cache, proj.id, proj.project_key
            )
            issue_type_id = issue_type_resolver.resolve(issue_type)

            # Resolve priority
            priority_resolver = PriorityResolver(client, cache)
            priority_id = priority_resolver.resolve(priority)

            # Build request data
            data: dict[str, str | int | float] = {
                "projectId": proj.id,
                "summary": summary,
                "issueTypeId": issue_type_id,
                "priorityId": priority_id,
            }

            if description:
                data["description"] = description

            # Resolve assignee if provided
            if assignee:
                user_resolver = UserResolver(client, cache)
                assignee_id = user_resolver.resolve(assignee)
                data["assigneeId"] = assignee_id

            if due_date:
                data["dueDate"] = due_date

            if start_date:
                data["startDate"] = start_date

            if estimated_hours is not None:
                data["estimatedHours"] = estimated_hours

            # Create issue
            result = client.post("/issues", data=data)
            issue = Issue.model_validate(result)

        if json_output:
            import json

            out = issue.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        console.print(f"[green]Created issue: {issue.issue_key}[/green]")
        console.print(f"  Summary: {issue.summary}")
        console.print(f"  URL: {settings.space_url}/view/{issue.issue_key}")

    except ResolverError as e:
        err_console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e
    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("update")
def update_issue(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    summary: Annotated[
        str | None,
        typer.Option("--summary", "-s", help="New summary/title"),
    ] = None,
    description: Annotated[
        str | None,
        typer.Option("--description", "-d", help="New description"),
    ] = None,
    status: Annotated[
        str | None,
        typer.Option("--status", help="New status name"),
    ] = None,
    priority: Annotated[
        str | None,
        typer.Option("--priority", help="New priority name"),
    ] = None,
    assignee: Annotated[
        str | None,
        typer.Option("--assignee", "-a", help="New assignee (@me for self)"),
    ] = None,
    due_date: Annotated[
        str | None,
        typer.Option("--due-date", help="New due date (YYYY-MM-DD)"),
    ] = None,
    start_date: Annotated[
        str | None,
        typer.Option("--start-date", help="New start date (YYYY-MM-DD)"),
    ] = None,
    estimated_hours: Annotated[
        float | None,
        typer.Option("--estimated-hours", help="Estimated hours"),
    ] = None,
    actual_hours: Annotated[
        float | None,
        typer.Option("--actual-hours", help="Actual hours"),
    ] = None,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Update an issue."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        err_console.print("Run 'bklg auth login' to authenticate.")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    # Check if any update field is provided
    if all(
        v is None
        for v in [
            summary,
            description,
            status,
            priority,
            assignee,
            due_date,
            start_date,
            estimated_hours,
            actual_hours,
        ]
    ):
        err_console.print("[yellow]No update options provided.[/yellow]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            cache = ResolverCache()

            # Build update data
            data: dict[str, str | int | float] = {}

            if summary:
                data["summary"] = summary

            if description:
                data["description"] = description

            # Resolve status if provided (needs project info from issue)
            if status:
                # First fetch the issue to get project info
                issue_data = client.get(f"/issues/{issue_key}")
                issue = Issue.model_validate(issue_data)
                status_resolver = StatusResolver(
                    client,
                    cache,
                    issue.project_id,
                    issue.issue_key.rsplit("-", 1)[0],
                )
                status_id = status_resolver.resolve(status)
                data["statusId"] = status_id

            if priority:
                priority_resolver = PriorityResolver(client, cache)
                priority_id = priority_resolver.resolve(priority)
                data["priorityId"] = priority_id

            if assignee:
                user_resolver = UserResolver(client, cache)
                assignee_id = user_resolver.resolve(assignee)
                data["assigneeId"] = assignee_id

            if due_date:
                data["dueDate"] = due_date

            if start_date:
                data["startDate"] = start_date

            if estimated_hours is not None:
                data["estimatedHours"] = estimated_hours

            if actual_hours is not None:
                data["actualHours"] = actual_hours

            # Update issue
            result = client.patch(f"/issues/{issue_key}", data=data)
            updated_issue = Issue.model_validate(result)

        if json_output:
            import json

            out = updated_issue.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        console.print(f"[green]Updated issue: {updated_issue.issue_key}[/green]")
        console.print(f"  Summary: {updated_issue.summary}")
        console.print(f"  Status: {updated_issue.status.name}")

    except ResolverError as e:
        err_console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e
    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Issue '{issue_key}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("delete")
def delete_issue(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Skip confirmation"),
    ] = False,
) -> None:
    """Delete an issue."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    if not force:
        confirm = typer.confirm(f"Delete issue {issue_key}?")
        if not confirm:
            console.print("[yellow]Cancelled.[/yellow]")
            raise typer.Abort()

    try:
        with BacklogClient(settings=settings) as client:
            # Fetch issue first to show info
            issue_data = client.get(f"/issues/{issue_key}")
            issue = Issue.model_validate(issue_data)

            # Delete issue
            client.delete(f"/issues/{issue_key}")

        console.print(f"[green]Deleted issue: {issue.issue_key}[/green]")
        console.print(f"  Summary: {issue.summary}")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Issue '{issue_key}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


# Comment subcommands


@comment_app.command("list")
def list_comments(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    limit: Annotated[
        int,
        typer.Option("--limit", "-l", help="Number of comments to fetch"),
    ] = 20,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """List comments on an issue."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get(
                f"/issues/{issue_key}/comments",
                params={"count": limit, "order": "asc"},
            )
            comments = [Comment.model_validate(c) for c in data]  # type: ignore[union-attr]

        if json_output:
            import json

            out = [c.model_dump(by_alias=True, mode="json") for c in comments]
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        if not comments:
            console.print(f"[yellow]No comments on {issue_key}.[/yellow]")
            return

        formatter = IssueFormatter(console)
        formatter.format_comments(comments)

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Issue '{issue_key}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@comment_app.command("add")
def add_comment(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    content: Annotated[
        str,
        typer.Argument(help="Comment content"),
    ],
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Add a comment to an issue."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    try:
        with BacklogClient(settings=settings) as client:
            result = client.post(
                f"/issues/{issue_key}/comments",
                data={"content": content},
            )
            comment = Comment.model_validate(result)

        if json_output:
            import json

            out = comment.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        console.print(f"[green]Added comment to {issue_key}[/green]")
        console.print(f"  Comment ID: {comment.id}")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Issue '{issue_key}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@comment_app.command("update")
def update_comment(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    comment_id: Annotated[
        int,
        typer.Argument(help="Comment ID"),
    ],
    content: Annotated[
        str,
        typer.Argument(help="New comment content"),
    ],
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Update a comment."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    try:
        with BacklogClient(settings=settings) as client:
            result = client.patch(
                f"/issues/{issue_key}/comments/{comment_id}",
                data={"content": content},
            )
            comment = Comment.model_validate(result)

        if json_output:
            import json

            out = comment.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        console.print(f"[green]Updated comment {comment_id} on {issue_key}[/green]")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print("[red]Comment not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@comment_app.command("delete")
def delete_comment(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    comment_id: Annotated[
        int,
        typer.Argument(help="Comment ID"),
    ],
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Skip confirmation"),
    ] = False,
) -> None:
    """Delete a comment."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    if not force:
        confirm = typer.confirm(f"Delete comment {comment_id} on {issue_key}?")
        if not confirm:
            console.print("[yellow]Cancelled.[/yellow]")
            raise typer.Abort()

    try:
        with BacklogClient(settings=settings) as client:
            client.delete(f"/issues/{issue_key}/comments/{comment_id}")

        console.print(f"[green]Deleted comment {comment_id} on {issue_key}[/green]")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print("[red]Comment not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


# Attachment subcommands


@attachment_app.command("list")
def list_attachments(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """List attachments on an issue."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get(f"/issues/{issue_key}/attachments")
            attachments = [Attachment.model_validate(a) for a in data]  # type: ignore[union-attr]

        if json_output:
            import json

            out = [a.model_dump(by_alias=True, mode="json") for a in attachments]
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        if not attachments:
            console.print(f"[yellow]No attachments on {issue_key}.[/yellow]")
            return

        table = Table(title=f"Attachments: {issue_key}")
        table.add_column("ID", style="cyan")
        table.add_column("Name")
        table.add_column("Size", justify="right")
        table.add_column("Created By")

        for att in attachments:
            size_str = _format_size(att.size)
            created_by = att.created_user.name if att.created_user else "-"
            table.add_row(str(att.id), att.name, size_str, created_by)

        console.print(table)

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Issue '{issue_key}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


def _format_size(size: int) -> str:
    """Format file size in human readable format."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024  # type: ignore[assignment]
    return f"{size:.1f} TB"


@attachment_app.command("download")
def download_attachment(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    attachment_id: Annotated[
        int,
        typer.Argument(help="Attachment ID"),
    ],
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Output path (file or directory)"),
    ] = None,
) -> None:
    """Download an attachment."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    try:
        with BacklogClient(settings=settings) as client:
            output_path = output or Path(".")
            _, filename = client.download_file(
                f"/issues/{issue_key}/attachments/{attachment_id}",
                output_path=output_path,
            )

        if output_path.is_dir():
            saved_path = output_path / filename
        else:
            saved_path = output_path

        console.print(f"[green]Downloaded: {saved_path}[/green]")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print("[red]Attachment not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@attachment_app.command("upload")
def upload_attachment(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    file_path: Annotated[
        Path,
        typer.Argument(help="File to upload", exists=True),
    ],
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Upload an attachment to an issue."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    try:
        with BacklogClient(settings=settings) as client:
            # First upload the file
            upload_result = client.upload_file(file_path)
            attachment_id = upload_result["id"]

            # Then attach it to the issue using PATCH
            # The API requires attachmentId[] parameter
            result = client.patch(
                f"/issues/{issue_key}",
                data={"attachmentId[]": attachment_id},
            )
            issue = Issue.model_validate(result)

        if json_output:
            import json

            console.print_json(json.dumps(upload_result, ensure_ascii=False))
            return

        console.print(f"[green]Uploaded {file_path.name} to {issue.issue_key}[/green]")
        console.print(f"  Attachment ID: {attachment_id}")

    except FileNotFoundError as e:
        err_console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e
    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Issue '{issue_key}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@attachment_app.command("delete")
def delete_attachment(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    attachment_id: Annotated[
        int,
        typer.Argument(help="Attachment ID"),
    ],
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Skip confirmation"),
    ] = False,
) -> None:
    """Delete an attachment."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)

    if not force:
        confirm = typer.confirm(f"Delete attachment {attachment_id} from {issue_key}?")
        if not confirm:
            console.print("[yellow]Cancelled.[/yellow]")
            raise typer.Abort()

    try:
        with BacklogClient(settings=settings) as client:
            client.delete(f"/issues/{issue_key}/attachments/{attachment_id}")

        console.print(
            f"[green]Deleted attachment {attachment_id} from {issue_key}[/green]"
        )

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print("[red]Attachment not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


def _fetch_all_comments(client: BacklogClient, issue_key: str) -> list[Comment]:
    """コメントをページネーションで全件取得するヘルパー。

    100件ずつ昇順で取得し、100件返ってきた場合は次ページを取得する。
    """
    comments: list[Comment] = []
    min_id: int | None = None

    while True:
        params: dict[str, int | str] = {"count": 100, "order": "asc"}
        if min_id is not None:
            params["minId"] = min_id

        data = client.get(f"/issues/{issue_key}/comments", params=params)
        batch = [Comment.model_validate(c) for c in data]  # type: ignore[union-attr]
        comments.extend(batch)

        if len(batch) < 100:
            break

        # 次ページは最後のコメントIDの次から取得
        min_id = batch[-1].id + 1

    return comments


@app.command("export")
def export_issue(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    output_dir: Annotated[
        Path | None,
        typer.Option("--output-dir", "-o", help="Output directory (default: /tmp/bklg/<KEY>)"),
    ] = None,
    no_attachments: Annotated[
        bool,
        typer.Option("--no-attachments", help="Skip downloading attachments"),
    ] = False,
    no_comments: Annotated[
        bool,
        typer.Option("--no-comments", help="Skip fetching comments"),
    ] = False,
) -> None:
    """Export issue to local directory as Markdown."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        err_console.print("Run 'bklg auth login' to authenticate.")
        raise typer.Exit(1)

    issue_key = parse_issue_identifier(issue_id)
    target_dir = output_dir or Path("/tmp/bklg") / issue_key

    try:
        with BacklogClient(settings=settings) as client:
            # 課題取得（添付ファイル一覧も含まれる）
            data = client.get(f"/issues/{issue_key}")
            issue = Issue.model_validate(data)

            # コメント全件取得
            comments: list[Comment] = []
            if not no_comments:
                comments = _fetch_all_comments(client, issue_key)

            # 出力ディレクトリを作成
            target_dir.mkdir(parents=True, exist_ok=True)

            # 添付ファイルのダウンロード
            attachments = [Attachment.model_validate(a) for a in issue.attachments]
            attachments_downloaded = False
            if not no_attachments and attachments:
                attachment_dir = target_dir / "attachments"
                attachment_dir.mkdir(exist_ok=True)
                for att in attachments:
                    client.download_file(
                        f"/issues/{issue_key}/attachments/{att.id}",
                        output_path=attachment_dir,
                    )
                attachments_downloaded = True

        # issue.md を生成・書き出し
        exporter = IssueExporter(space_url=settings.space_url)
        exporter.export(
            issue=issue,
            comments=comments,
            attachments=attachments,
            output_dir=target_dir,
            attachments_downloaded=attachments_downloaded,
        )

        # 結果サマリを表示
        console.print(f"[green]Exported {issue_key} to {target_dir}[/green]")
        console.print(f"  issue.md: {target_dir / 'issue.md'}")
        if attachments:
            if attachments_downloaded:
                console.print(
                    f"  attachments: {len(attachments)} file(s) in {target_dir / 'attachments'}"
                )
            else:
                console.print(f"  attachments: skipped ({len(attachments)} file(s))")
        console.print(f"  comments: {len(comments)}")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Issue '{issue_key}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("bulk-update")
def bulk_update_issues(
    summary: Annotated[
        str | None,
        typer.Option("--summary", "-s", help="New summary/title"),
    ] = None,
    description: Annotated[
        str | None,
        typer.Option("--description", "-d", help="New description"),
    ] = None,
    status: Annotated[
        str | None,
        typer.Option("--status", help="New status name"),
    ] = None,
    priority: Annotated[
        str | None,
        typer.Option("--priority", help="New priority name"),
    ] = None,
    assignee: Annotated[
        str | None,
        typer.Option("--assignee", "-a", help="New assignee (@me for self)"),
    ] = None,
    due_date: Annotated[
        str | None,
        typer.Option("--due-date", help="New due date (YYYY-MM-DD)"),
    ] = None,
    start_date: Annotated[
        str | None,
        typer.Option("--start-date", help="New start date (YYYY-MM-DD)"),
    ] = None,
    estimated_hours: Annotated[
        float | None,
        typer.Option("--estimated-hours", help="Estimated hours"),
    ] = None,
    actual_hours: Annotated[
        float | None,
        typer.Option("--actual-hours", help="Actual hours"),
    ] = None,
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", help="Show what would be updated without making changes"),
    ] = False,
) -> None:
    """Update multiple issues from stdin (one issue key per line).

    Example:
        bklg issue list -p PROJ --overdue --json | jq -r '.[].issueKey' | bklg issue bulk-update --due-date 2024-02-15
    """
    import sys

    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        err_console.print("Run 'bklg auth login' to authenticate.")
        raise typer.Exit(1)

    # Check if any update field is provided
    if all(
        v is None
        for v in [
            summary,
            description,
            status,
            priority,
            assignee,
            due_date,
            start_date,
            estimated_hours,
            actual_hours,
        ]
    ):
        err_console.print("[yellow]No update options provided.[/yellow]")
        raise typer.Exit(1)

    # Read issue keys from stdin
    issue_keys = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            issue_keys.append(parse_issue_identifier(line))

    if not issue_keys:
        err_console.print("[yellow]No issue keys provided on stdin.[/yellow]")
        raise typer.Exit(1)

    console.print(f"[cyan]Found {len(issue_keys)} issue(s) to update.[/cyan]")

    if dry_run:
        console.print("\n[yellow]DRY RUN - No changes will be made[/yellow]\n")
        console.print("Issues to be updated:")
        for key in issue_keys:
            console.print(f"  - {key}")
        console.print("\nUpdate fields:")
        if summary:
            console.print(f"  - summary: {summary}")
        if description:
            console.print(f"  - description: {description}")
        if status:
            console.print(f"  - status: {status}")
        if priority:
            console.print(f"  - priority: {priority}")
        if assignee:
            console.print(f"  - assignee: {assignee}")
        if due_date:
            console.print(f"  - due_date: {due_date}")
        if start_date:
            console.print(f"  - start_date: {start_date}")
        if estimated_hours is not None:
            console.print(f"  - estimated_hours: {estimated_hours}")
        if actual_hours is not None:
            console.print(f"  - actual_hours: {actual_hours}")
        return

    # Perform bulk update
    try:
        with BacklogClient(settings=settings) as client:
            cache = ResolverCache()
            success_count = 0
            error_count = 0

            for issue_key in issue_keys:
                try:
                    # Build update data
                    data: dict[str, str | int | float] = {}

                    if summary:
                        data["summary"] = summary

                    if description:
                        data["description"] = description

                    # Resolve status if provided (needs project info from issue)
                    if status:
                        # First fetch the issue to get project info
                        issue_data = client.get(f"/issues/{issue_key}")
                        issue = Issue.model_validate(issue_data)
                        status_resolver = StatusResolver(
                            client,
                            cache,
                            issue.project_id,
                            issue.issue_key.rsplit("-", 1)[0],
                        )
                        status_id = status_resolver.resolve(status)
                        data["statusId"] = status_id

                    if priority:
                        priority_resolver = PriorityResolver(client, cache)
                        priority_id = priority_resolver.resolve(priority)
                        data["priorityId"] = priority_id

                    if assignee:
                        user_resolver = UserResolver(client, cache)
                        assignee_id = user_resolver.resolve(assignee)
                        data["assigneeId"] = assignee_id

                    if due_date:
                        data["dueDate"] = due_date

                    if start_date:
                        data["startDate"] = start_date

                    if estimated_hours is not None:
                        data["estimatedHours"] = estimated_hours

                    if actual_hours is not None:
                        data["actualHours"] = actual_hours

                    # Update issue
                    client.patch(f"/issues/{issue_key}", data=data)
                    console.print(f"[green]✓ Updated {issue_key}[/green]")
                    success_count += 1

                except (ResolverError, BacklogAPIError) as e:
                    err_console.print(f"[red]✗ Failed to update {issue_key}: {e}[/red]")
                    error_count += 1

            # Summary
            console.print(
                f"\n[cyan]Completed: {success_count} succeeded, {error_count} failed[/cyan]"
            )

    except Exception as e:
        err_console.print(f"[red]Unexpected error: {e}[/red]")
        raise typer.Exit(1) from e
