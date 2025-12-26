"""Project commands for bacli."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

from bacli_py.api.client import BacklogAPIError, BacklogClient
from bacli_py.config.settings import get_settings
from bacli_py.resolver.base import ResolverError
from bacli_py.resolver.cache import ResolverCache
from bacli_py.resolver.project import ProjectResolver

app = typer.Typer(help="Project commands")
console = Console()
err_console = Console(stderr=True)


def get_project_resolver() -> tuple[BacklogClient, ProjectResolver]:
    """Get project resolver with client."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        err_console.print("Run 'bacli auth login' to authenticate.")
        raise typer.Exit(1)

    client = BacklogClient(settings=settings)
    cache = ResolverCache()
    resolver = ProjectResolver(client, cache)
    return client, resolver


@app.command("list")
def list_projects(
    archived: bool = typer.Option(False, "--archived", "-a", help="Include archived"),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
) -> None:
    """List all projects."""
    try:
        client, resolver = get_project_resolver()
        with client:
            projects = resolver.list_projects(archived=archived)

        if json_output:
            import json

            data = [p.model_dump(by_alias=True) for p in projects]
            console.print_json(json.dumps(data, ensure_ascii=False))
            return

        if not projects:
            console.print("[yellow]No projects found.[/yellow]")
            return

        table = Table(title="Projects")
        table.add_column("Key", style="cyan", no_wrap=True)
        table.add_column("Name")
        table.add_column("ID", style="dim")
        table.add_column("Archived", style="dim")

        for project in projects:
            archived_mark = "[yellow]Yes[/yellow]" if project.archived else ""
            table.add_row(
                project.project_key,
                project.name,
                str(project.id),
                archived_mark,
            )

        console.print(table)

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e
    except Exception as e:
        err_console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("info")
def project_info(
    project: str = typer.Argument(..., help="Project key or ID"),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
) -> None:
    """Show project details."""
    try:
        client, resolver = get_project_resolver()
        with client:
            proj = resolver.get_project(project)

        if json_output:
            import json

            console.print_json(json.dumps(proj.model_dump(by_alias=True), ensure_ascii=False))
            return

        table = Table(title=f"Project: {proj.name}", show_header=False)
        table.add_column("Key", style="cyan")
        table.add_column("Value")

        table.add_row("Project Key", proj.project_key)
        table.add_row("Name", proj.name)
        table.add_row("ID", str(proj.id))
        table.add_row("Archived", "Yes" if proj.archived else "No")
        table.add_row("Text Format", proj.text_formatting_rule)
        table.add_row("Subtasking", "Enabled" if proj.subtasking_enabled else "Disabled")
        table.add_row("Wiki", "Enabled" if proj.use_wiki else "Disabled")
        table.add_row("Git", "Enabled" if proj.use_git else "Disabled")

        console.print(table)

    except ResolverError as e:
        err_console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e
    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e
    except Exception as e:
        err_console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("types")
def list_issue_types(
    project: str = typer.Argument(..., help="Project key or ID"),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
) -> None:
    """List issue types for a project."""
    from bacli_py.resolver.issue_type import IssueTypeResolver

    try:
        client, project_resolver = get_project_resolver()
        with client:
            proj = project_resolver.get_project(project)
            cache = ResolverCache()
            issue_type_resolver = IssueTypeResolver(
                client, cache, proj.id, proj.project_key
            )
            issue_types = issue_type_resolver.list_issue_types()

        if json_output:
            import json

            data = [it.model_dump(by_alias=True) for it in issue_types]
            console.print_json(json.dumps(data, ensure_ascii=False))
            return

        if not issue_types:
            console.print("[yellow]No issue types found.[/yellow]")
            return

        table = Table(title=f"Issue Types: {proj.project_key}")
        table.add_column("Name", style="cyan")
        table.add_column("ID", style="dim")
        table.add_column("Color")

        for it in issue_types:
            table.add_row(it.name, str(it.id), it.color)

        console.print(table)

    except ResolverError as e:
        err_console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e
    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("statuses")
def list_statuses(
    project: str = typer.Argument(..., help="Project key or ID"),
    json_output: bool = typer.Option(False, "--json", "-j", help="Output as JSON"),
) -> None:
    """List statuses for a project."""
    from bacli_py.models import Status

    try:
        client, project_resolver = get_project_resolver()
        with client:
            proj = project_resolver.get_project(project)
            data = client.get(f"/projects/{proj.id}/statuses")
            statuses = [Status.model_validate(s) for s in data]  # type: ignore[union-attr]

        if json_output:
            import json

            out = [s.model_dump(by_alias=True) for s in statuses]
            console.print_json(json.dumps(out, ensure_ascii=False))
            return

        if not statuses:
            console.print("[yellow]No statuses found.[/yellow]")
            return

        table = Table(title=f"Statuses: {proj.project_key}")
        table.add_column("Name", style="cyan")
        table.add_column("ID", style="dim")
        table.add_column("Color")

        for s in statuses:
            table.add_row(s.name, str(s.id), s.color)

        console.print(table)

    except ResolverError as e:
        err_console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e
    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e
