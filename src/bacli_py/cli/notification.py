"""Notification commands for bacli."""

from __future__ import annotations

from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from bacli_py.api.client import BacklogAPIError, BacklogClient
from bacli_py.config.settings import get_settings
from bacli_py.models.notification import Notification

app = typer.Typer(help="Notification commands")
console = Console()
err_console = Console(stderr=True)


@app.command("list")
def list_notifications(
    limit: Annotated[
        int,
        typer.Option("--limit", "-l", help="Number of notifications to fetch"),
    ] = 20,
    unread_only: Annotated[
        bool,
        typer.Option("--unread", "-u", help="Show only unread notifications"),
    ] = False,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """List notifications."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            params: dict[str, int | bool] = {"count": limit}
            if unread_only:
                params["alreadyRead"] = False

            data = client.get("/notifications", params=params)
            notifications = [Notification.model_validate(n) for n in data]  # type: ignore[union-attr]

        if json_output:
            import json

            out = [n.model_dump(by_alias=True, mode="json") for n in notifications]
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        if not notifications:
            console.print("[yellow]No notifications.[/yellow]")
            return

        reason_map = {
            1: "Assigned",
            2: "Commented",
            3: "Added to Issue",
            4: "Updated",
            5: "File Added",
            6: "PR Assigned",
            7: "PR Commented",
            8: "PR Updated",
            9: "PR Added",
            10: "PR Merged",
            11: "Group Joined",
            12: "Other",
        }

        table = Table(title="Notifications")
        table.add_column("ID", style="cyan")
        table.add_column("Read")
        table.add_column("Reason")
        table.add_column("Project")
        table.add_column("Issue/Content")
        table.add_column("From")
        table.add_column("Created")

        for notif in notifications:
            read_mark = "✓" if notif.already_read else "[bold red]●[/bold red]"
            reason = reason_map.get(notif.reason, f"Reason {notif.reason}")

            project_key = "-"
            if notif.project:
                project_key = notif.project.get("projectKey", "-")

            content = "-"
            if notif.issue:
                issue_key = notif.issue.get("issueKey", "")
                summary = notif.issue.get("summary", "")[:20]
                content = f"{issue_key} {summary}"
            elif notif.pull_request:
                content = f"PR: {notif.pull_request.get('summary', '')[:20]}"

            sender_name = notif.sender.name if notif.sender else "-"
            created = notif.created.strftime("%Y-%m-%d %H:%M")

            table.add_row(
                str(notif.id),
                read_mark,
                reason,
                project_key,
                content,
                sender_name,
                created,
            )

        console.print(table)

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("count")
def notification_count(
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Show notification count."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get("/notifications/count")
            count = data.get("count", 0) if isinstance(data, dict) else 0

        if json_output:
            import json

            console.print_json(json.dumps({"count": count}))
            return

        if count == 0:
            console.print("No unread notifications.")
        else:
            console.print(f"[bold]{count}[/bold] unread notification(s)")

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("read")
def mark_as_read(
    notification_id: Annotated[
        int | None,
        typer.Argument(help="Notification ID (omit for all)"),
    ] = None,
    all_notifications: Annotated[
        bool,
        typer.Option("--all", "-a", help="Mark all as read"),
    ] = False,
) -> None:
    """Mark notification(s) as read."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    if notification_id is None and not all_notifications:
        err_console.print("[yellow]Specify notification ID or use --all.[/yellow]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            if all_notifications:
                client.post("/notifications/markAsRead")
                console.print("[green]Marked all notifications as read.[/green]")
            else:
                client.post(f"/notifications/{notification_id}/markAsRead")
                console.print(
                    f"[green]Marked notification {notification_id} as read.[/green]"
                )

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print("[red]Notification not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e
