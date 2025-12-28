"""Watch commands for bklg."""

from __future__ import annotations

import re
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from bklg.api.client import BacklogAPIError, BacklogClient
from bklg.config.settings import get_settings
from bklg.models.watch import Watching

app = typer.Typer(help="Watch commands")
console = Console()
err_console = Console(stderr=True)


def _parse_issue_identifier(identifier: str) -> str:
    """Parse issue identifier from various formats."""
    url_match = re.search(r"/view/([A-Z0-9_]+-\d+)", identifier, re.IGNORECASE)
    if url_match:
        return url_match.group(1)
    return identifier


@app.command("list")
def list_watchings(
    limit: Annotated[
        int,
        typer.Option("--limit", "-l", help="Number of watchings to fetch"),
    ] = 20,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """List watched items."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            # First get my user ID
            myself = client.get("/users/myself")
            user_id = myself["id"]  # type: ignore[index]

            data = client.get(
                f"/users/{user_id}/watchings",
                params={"count": limit},
            )
            watchings = [Watching.model_validate(w) for w in data]  # type: ignore[union-attr]

        if json_output:
            import json

            out = [w.model_dump(by_alias=True, mode="json") for w in watchings]
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        if not watchings:
            console.print("[yellow]No watched items.[/yellow]")
            return

        table = Table(title="Watched Items")
        table.add_column("Watch ID", style="cyan")
        table.add_column("Read")
        table.add_column("Issue")
        table.add_column("Summary")
        table.add_column("Note")
        table.add_column("Updated")

        for watch in watchings:
            read_mark = "✓" if watch.resource_already_read else "[bold red]●[/bold red]"

            issue_key = "-"
            summary = "-"
            if watch.issue:
                issue_key = watch.issue.get("issueKey", "-")
                summary = watch.issue.get("summary", "-")[:30]

            note = watch.note[:20] if watch.note else "-"
            updated = watch.updated.strftime("%Y-%m-%d")

            table.add_row(
                str(watch.id),
                read_mark,
                issue_key,
                summary,
                note,
                updated,
            )

        console.print(table)

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("add")
def add_watching(
    issue_id: Annotated[
        str,
        typer.Argument(help="Issue key, ID, or URL"),
    ],
    note: Annotated[
        str | None,
        typer.Option("--note", "-n", help="Note for this watch"),
    ] = None,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Watch an issue."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    issue_key = _parse_issue_identifier(issue_id)

    try:
        with BacklogClient(settings=settings) as client:
            data: dict[str, str] = {"issueIdOrKey": issue_key}
            if note:
                data["note"] = note

            result = client.post("/watchings", data=data)
            watching = Watching.model_validate(result)

        if json_output:
            import json

            out = watching.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        console.print(f"[green]Now watching {issue_key}[/green]")
        console.print(f"  Watch ID: {watching.id}")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Issue '{issue_key}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("info")
def watching_info(
    watch_id: Annotated[
        int,
        typer.Argument(help="Watch ID"),
    ],
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Show watch details."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get(f"/watchings/{watch_id}")
            watching = Watching.model_validate(data)

        if json_output:
            import json

            out = watching.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        console.print(f"[bold]Watch ID: {watching.id}[/bold]")
        console.print(
            f"  Read: {'Yes' if watching.resource_already_read else 'No'}"
        )
        if watching.issue:
            console.print(f"  Issue: {watching.issue.get('issueKey', '-')}")
            console.print(f"  Summary: {watching.issue.get('summary', '-')}")
        if watching.note:
            console.print(f"  Note: {watching.note}")
        console.print(f"  Created: {watching.created.strftime('%Y-%m-%d %H:%M')}")
        console.print(f"  Updated: {watching.updated.strftime('%Y-%m-%d %H:%M')}")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print("[red]Watch not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("remove")
def remove_watching(
    watch_id: Annotated[
        int,
        typer.Argument(help="Watch ID"),
    ],
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Skip confirmation"),
    ] = False,
) -> None:
    """Stop watching."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    if not force:
        confirm = typer.confirm(f"Remove watch {watch_id}?")
        if not confirm:
            console.print("[yellow]Cancelled.[/yellow]")
            raise typer.Abort()

    try:
        with BacklogClient(settings=settings) as client:
            client.delete(f"/watchings/{watch_id}")

        console.print(f"[green]Removed watch {watch_id}[/green]")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print("[red]Watch not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("read")
def mark_watching_read(
    watch_id: Annotated[
        int,
        typer.Argument(help="Watch ID"),
    ],
) -> None:
    """Mark watch as read."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            client.post(f"/watchings/{watch_id}/markAsRead")

        console.print(f"[green]Marked watch {watch_id} as read.[/green]")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print("[red]Watch not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e
