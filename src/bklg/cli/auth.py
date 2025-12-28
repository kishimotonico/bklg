"""Authentication commands for bklg."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

from bklg.api.client import BacklogAPIError, BacklogClient
from bklg.config.settings import Settings, get_config_file, get_settings

app = typer.Typer(help="Authentication commands")
console = Console()
err_console = Console(stderr=True)


@app.command("login")
def login(
    space_url: str = typer.Option(
        None,
        "--space-url",
        "-s",
        prompt="Backlog Space URL (e.g., https://example.backlog.com)",
        help="Backlog space URL",
    ),
    api_key: str = typer.Option(
        None,
        "--api-key",
        "-k",
        prompt="API Key",
        hide_input=True,
        help="Backlog API key",
    ),
) -> None:
    """Login to Backlog with API key."""
    space_url = space_url.rstrip("/")
    if not space_url.startswith("https://"):
        space_url = f"https://{space_url}"

    settings = Settings(space_url=space_url, api_key=api_key)

    console.print("Verifying credentials...", style="dim")

    try:
        with BacklogClient(settings=settings) as client:
            user = client.get_myself()

        settings.save()

        console.print(f"[green]Logged in as {user['name']} ({user['userId']})[/green]")
        console.print(f"Config saved to: {get_config_file()}")

    except BacklogAPIError as e:
        if e.is_auth_error():
            err_console.print("[red]Authentication failed. Check your API key.[/red]")
        else:
            err_console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e
    except Exception as e:
        err_console.print(f"[red]Connection error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("logout")
def logout() -> None:
    """Logout from Backlog (remove stored credentials)."""
    config_file = get_config_file()

    if not config_file.exists():
        console.print("Not logged in.")
        return

    config_file.unlink()
    console.print("[green]Logged out successfully.[/green]")


@app.command("status")
def status() -> None:
    """Show authentication status."""
    settings = get_settings()

    if not settings.is_configured:
        console.print("[yellow]Not logged in.[/yellow]")
        console.print("Run 'bklg auth login' to authenticate.")
        raise typer.Exit(1)

    console.print("Checking authentication...", style="dim")

    try:
        with BacklogClient(settings=settings) as client:
            user = client.get_myself()

        table = Table(title="Authentication Status", show_header=False)
        table.add_column("Key", style="cyan")
        table.add_column("Value")

        table.add_row("Status", "[green]Authenticated[/green]")
        table.add_row("Space", settings.space_url or "")
        table.add_row("User", user.get("name", "Unknown"))
        table.add_row("User ID", user.get("userId", "Unknown"))
        table.add_row("Email", user.get("mailAddress", "N/A"))

        rate_limit = client.rate_limit_handler.last_rate_limit
        if rate_limit:
            table.add_row(
                "Rate Limit",
                f"{rate_limit.remaining}/{rate_limit.limit} remaining",
            )

        console.print(table)

    except BacklogAPIError as e:
        if e.is_auth_error():
            err_console.print("[red]Authentication failed.[/red]")
            err_console.print("Your API key may have expired or been revoked.")
            err_console.print("Run 'bklg auth login' to re-authenticate.")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e
    except Exception as e:
        err_console.print(f"[red]Connection error: {e}[/red]")
        raise typer.Exit(1) from e
