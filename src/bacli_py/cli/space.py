"""Space commands for bacli."""

from __future__ import annotations

from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from bacli_py.api.client import BacklogAPIError, BacklogClient
from bacli_py.config.settings import get_settings
from bacli_py.models.space import DiskUsage, Space, SpaceNotification

app = typer.Typer(help="Space commands")
console = Console()
err_console = Console(stderr=True)


def _format_size(size: int) -> str:
    """Format file size in human readable format."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024  # type: ignore[assignment]
    return f"{size:.1f} TB"


@app.command("info")
def space_info(
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Show space information."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get("/space")
            space = Space.model_validate(data)

        if json_output:
            import json

            out = space.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        console.print(f"[bold]{space.name}[/bold]")
        console.print(f"  Space Key: {space.space_key}")
        console.print(f"  Language: {space.lang}")
        console.print(f"  Timezone: {space.timezone}")
        console.print(f"  Text Formatting: {space.text_formatting_rule}")
        console.print(f"  Created: {space.created.strftime('%Y-%m-%d')}")
        console.print(f"  Updated: {space.updated.strftime('%Y-%m-%d')}")

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("notice")
def space_notice(
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Show space notice/announcement."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get("/space/notification")
            notice = SpaceNotification.model_validate(data)

        if json_output:
            import json

            out = notice.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        if not notice.content:
            console.print("[yellow]No announcement set.[/yellow]")
            return

        console.print("[bold]Space Announcement[/bold]")
        if notice.updated:
            console.print(f"[dim]Updated: {notice.updated.strftime('%Y-%m-%d')}[/dim]")
        console.print()
        console.print(notice.content)

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("activity")
def space_activity(
    limit: Annotated[
        int,
        typer.Option("--limit", "-l", help="Number of activities to fetch"),
    ] = 20,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Show recent space activity."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get("/space/activities", params={"count": limit})

        if json_output:
            import json

            console.print_json(json.dumps(data, ensure_ascii=False, default=str))
            return

        if not data:
            console.print("[yellow]No activities found.[/yellow]")
            return

        activity_types = {
            1: "Issue Created",
            2: "Issue Updated",
            3: "Comment Added",
            4: "Issue Deleted",
            5: "Wiki Created",
            6: "Wiki Updated",
            7: "Wiki Deleted",
            8: "File Added",
            9: "File Updated",
            10: "File Deleted",
            11: "SVN Committed",
            12: "Git Pushed",
            13: "Git Repository Created",
            14: "Issue Multi-Updated",
            15: "Project Added",
            17: "PR Added",
            18: "PR Updated",
            19: "PR Comment",
            20: "PR Merged",
        }

        table = Table(title="Recent Space Activity")
        table.add_column("Type")
        table.add_column("Project")
        table.add_column("User")
        table.add_column("Content")
        table.add_column("Created")

        for act in data:  # type: ignore[union-attr]
            act_type = activity_types.get(act.get("type", 0), f"Type {act.get('type')}")
            project = act.get("project", {})
            project_key = project.get("projectKey", "-") if project else "-"

            created_user = act.get("createdUser", {})
            user_name = created_user.get("name", "-") if created_user else "-"

            content_obj = act.get("content", {})
            if isinstance(content_obj, dict):
                summary = content_obj.get("summary", content_obj.get("name", "-"))
            else:
                summary = "-"

            created = act.get("created", "-")
            if isinstance(created, str) and len(created) > 10:
                created = created[:10]

            table.add_row(
                act_type, project_key, user_name, str(summary)[:30], created
            )

        console.print(table)

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("disk")
def disk_usage(
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Show disk usage."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get("/space/diskUsage")
            usage = DiskUsage.model_validate(data)

        if json_output:
            import json

            out = usage.model_dump(by_alias=True)
            console.print_json(json.dumps(out, ensure_ascii=False))
            return

        total_used = (
            usage.issue
            + usage.wiki
            + usage.file
            + usage.subversion
            + usage.git
            + usage.git_lfs
            + usage.pull_request
        )
        percent = (total_used / usage.capacity * 100) if usage.capacity > 0 else 0

        console.print("[bold]Disk Usage[/bold]")
        console.print(
            f"  Total: {_format_size(total_used)} / {_format_size(usage.capacity)} "
            f"({percent:.1f}%)"
        )
        console.print()

        table = Table()
        table.add_column("Category")
        table.add_column("Size", justify="right")

        table.add_row("Issues", _format_size(usage.issue))
        table.add_row("Wiki", _format_size(usage.wiki))
        table.add_row("Files", _format_size(usage.file))
        table.add_row("Subversion", _format_size(usage.subversion))
        table.add_row("Git", _format_size(usage.git))
        table.add_row("Git LFS", _format_size(usage.git_lfs))
        if usage.pull_request > 0:
            table.add_row("Pull Requests", _format_size(usage.pull_request))

        console.print(table)

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e
