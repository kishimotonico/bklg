"""User commands for bacli."""

from __future__ import annotations

from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from bacli_py.api.client import BacklogAPIError, BacklogClient
from bacli_py.config.settings import get_settings
from bacli_py.models.user import User

app = typer.Typer(help="User commands")
console = Console()
err_console = Console(stderr=True)


@app.command("list")
def list_users(
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """List all users."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get("/users")
            users = [User.model_validate(u) for u in data]  # type: ignore[union-attr]

        if json_output:
            import json

            out = [u.model_dump(by_alias=True, mode="json") for u in users]
            console.print_json(json.dumps(out, ensure_ascii=False))
            return

        if not users:
            console.print("[yellow]No users found.[/yellow]")
            return

        table = Table(title="Users")
        table.add_column("ID", style="cyan")
        table.add_column("User ID")
        table.add_column("Name")
        table.add_column("Email")
        table.add_column("Role")

        role_map = {
            1: "Admin",
            2: "Normal",
            3: "Reporter",
            4: "Viewer",
            5: "Guest Reporter",
            6: "Guest Viewer",
        }

        for user in users:
            role = role_map.get(user.role_type, str(user.role_type))
            table.add_row(
                str(user.id),
                user.user_id or "-",
                user.name,
                user.mail_address or "-",
                role,
            )

        console.print(table)

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("info")
def user_info(
    user_id: Annotated[
        str,
        typer.Argument(help="User ID or @me for self"),
    ] = "@me",
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Show user details."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            if user_id == "@me":
                data = client.get("/users/myself")
            else:
                data = client.get(f"/users/{user_id}")
            user = User.model_validate(data)

        if json_output:
            import json

            out = user.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False))
            return

        role_map = {
            1: "Admin",
            2: "Normal",
            3: "Reporter",
            4: "Viewer",
            5: "Guest Reporter",
            6: "Guest Viewer",
        }

        console.print(f"[bold]{user.name}[/bold]")
        console.print(f"  ID: {user.id}")
        console.print(f"  User ID: {user.user_id or '-'}")
        console.print(f"  Email: {user.mail_address or '-'}")
        console.print(f"  Role: {role_map.get(user.role_type, str(user.role_type))}")
        if user.lang:
            console.print(f"  Language: {user.lang}")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]User '{user_id}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("activity")
def user_activity(
    user_id: Annotated[
        str,
        typer.Argument(help="User ID or @me for self"),
    ] = "@me",
    limit: Annotated[
        int,
        typer.Option("--limit", "-l", help="Number of activities to fetch"),
    ] = 20,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Show user activity."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            # Resolve @me to actual user ID
            if user_id == "@me":
                myself = client.get("/users/myself")
                numeric_id = myself["id"]  # type: ignore[index]
            else:
                numeric_id = user_id

            data = client.get(
                f"/users/{numeric_id}/activities",
                params={"count": limit},
            )

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

        table = Table(title="Recent Activity")
        table.add_column("Type")
        table.add_column("Project")
        table.add_column("Content")
        table.add_column("Created")

        for act in data:  # type: ignore[union-attr]
            act_type = activity_types.get(act.get("type", 0), f"Type {act.get('type')}")
            project = act.get("project", {})
            project_key = project.get("projectKey", "-") if project else "-"

            content_obj = act.get("content", {})
            if isinstance(content_obj, dict):
                summary = content_obj.get("summary", content_obj.get("name", "-"))
            else:
                summary = "-"

            created = act.get("created", "-")
            if isinstance(created, str) and len(created) > 10:
                created = created[:10]

            table.add_row(act_type, project_key, str(summary)[:40], created)

        console.print(table)

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]User '{user_id}' not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e
