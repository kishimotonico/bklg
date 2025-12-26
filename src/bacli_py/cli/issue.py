"""Issue commands for bacli."""

from __future__ import annotations

import re
from typing import Annotated

import typer
from rich.console import Console

from bacli_py.api.client import BacklogAPIError, BacklogClient
from bacli_py.config.settings import get_settings
from bacli_py.models.issue import Comment, Issue
from bacli_py.resolver.base import ResolverError
from bacli_py.resolver.cache import ResolverCache
from bacli_py.resolver.project import ProjectResolver
from bacli_py.resolver.user import UserResolver
from bacli_py.utils.formatter import IssueFormatter

app = typer.Typer(help="Issue commands")
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
        err_console.print("Run 'bacli auth login' to authenticate.")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            cache = ResolverCache()
            params: dict[str, str | int | list[int]] = {
                "count": limit,
                "offset": offset,
                "sort": sort,
                "order": order,
            }

            # Resolve project
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

            # Resolve status (requires project)
            if status and project:
                project_resolver = ProjectResolver(client, cache)
                proj = project_resolver.get_project(project)
                # Fetch statuses for this project
                status_data = client.get(f"/projects/{proj.id}/statuses")
                status_map = {s["name"]: s["id"] for s in status_data}  # type: ignore[union-attr]
                if status in status_map:
                    params["statusId[]"] = [status_map[status]]

            # Fetch issues
            data = client.get("/issues", params=params)
            issues = [Issue.model_validate(i) for i in data]  # type: ignore[union-attr]

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
        err_console.print("Run 'bacli auth login' to authenticate.")
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
