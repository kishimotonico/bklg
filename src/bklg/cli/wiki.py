"""Wiki commands for bklg."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table

from bklg.api.client import BacklogAPIError, BacklogClient
from bklg.config.settings import get_settings
from bklg.models.attachment import Attachment
from bklg.models.wiki import Wiki
from bklg.resolver.cache import ResolverCache
from bklg.resolver.project import ProjectResolver

app = typer.Typer(help="Wiki commands")
attachment_app = typer.Typer(help="Wiki attachment commands")
app.add_typer(attachment_app, name="attachment")

console = Console()
err_console = Console(stderr=True)


def _format_size(size: int) -> str:
    """Format file size in human readable format."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024  # type: ignore[assignment]
    return f"{size:.1f} TB"


@app.command("list")
def list_wikis(
    project: Annotated[
        str,
        typer.Option("--project", "-p", help="Project key or ID"),
    ],
    keyword: Annotated[
        str | None,
        typer.Option("--keyword", "-k", help="Search keyword"),
    ] = None,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """List wiki pages in a project."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            cache = ResolverCache()
            project_resolver = ProjectResolver(client, cache)
            project_id = project_resolver.resolve(project)

            params: dict[str, str | int] = {"projectIdOrKey": project_id}
            if keyword:
                params["keyword"] = keyword

            data = client.get("/wikis", params=params)
            wikis = [Wiki.model_validate(w) for w in data]  # type: ignore[union-attr]

        if json_output:
            import json

            out = [w.model_dump(by_alias=True, mode="json") for w in wikis]
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        if not wikis:
            console.print(f"[yellow]No wiki pages in {project}.[/yellow]")
            return

        table = Table(title=f"Wiki Pages: {project}")
        table.add_column("ID", style="cyan")
        table.add_column("Name")
        table.add_column("Tags")
        table.add_column("Updated")

        for wiki in wikis:
            tags = ", ".join(t.get("name", "") for t in wiki.tags[:3])
            if len(wiki.tags) > 3:
                tags += "..."
            updated = wiki.updated.strftime("%Y-%m-%d") if wiki.updated else "-"
            table.add_row(str(wiki.id), wiki.name, tags or "-", updated)

        console.print(table)

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("view")
def view_wiki(
    wiki_id: Annotated[
        int,
        typer.Argument(help="Wiki page ID"),
    ],
    web: Annotated[
        bool,
        typer.Option("--web", "-w", help="Open in browser"),
    ] = False,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """View a wiki page."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    if web:
        import webbrowser

        url = f"{settings.space_url}/wiki/{wiki_id}"
        webbrowser.open(url)
        console.print(f"Opening {url} in browser...")
        return

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get(f"/wikis/{wiki_id}")
            wiki = Wiki.model_validate(data)

        if json_output:
            import json

            out = wiki.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        # Header
        console.print(Panel(f"[bold]{wiki.name}[/bold]", expand=False))

        # Meta info
        if wiki.tags:
            tags = ", ".join(t.get("name", "") for t in wiki.tags)
            console.print(f"Tags: {tags}")
        if wiki.updated:
            console.print(f"Updated: {wiki.updated.strftime('%Y-%m-%d %H:%M')}")
        if wiki.updated_user:
            console.print(f"Updated by: {wiki.updated_user.name}")
        console.print()

        # Content
        if wiki.content:
            md = Markdown(wiki.content)
            console.print(md)
        else:
            console.print("[dim]No content.[/dim]")

        # Attachments
        if wiki.attachments:
            console.print()
            console.print(f"[dim]Attachments: {len(wiki.attachments)}[/dim]")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Wiki page {wiki_id} not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("create")
def create_wiki(
    project: Annotated[
        str,
        typer.Option("--project", "-p", help="Project key or ID"),
    ],
    name: Annotated[
        str,
        typer.Option("--name", "-n", help="Wiki page name"),
    ],
    content: Annotated[
        str | None,
        typer.Option("--content", "-c", help="Wiki content"),
    ] = None,
    file: Annotated[
        Path | None,
        typer.Option("--file", "-f", help="Read content from file"),
    ] = None,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Create a wiki page."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    # Get content from file if specified
    wiki_content = content
    if file:
        if not file.exists():
            err_console.print(f"[red]File not found: {file}[/red]")
            raise typer.Exit(1)
        wiki_content = file.read_text(encoding="utf-8")

    try:
        with BacklogClient(settings=settings) as client:
            cache = ResolverCache()
            project_resolver = ProjectResolver(client, cache)
            project_id = project_resolver.resolve(project)

            data: dict[str, str | int] = {
                "projectId": project_id,
                "name": name,
            }
            if wiki_content:
                data["content"] = wiki_content

            result = client.post("/wikis", data=data)
            wiki = Wiki.model_validate(result)

        if json_output:
            import json

            out = wiki.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        console.print(f"[green]Created wiki page: {wiki.name}[/green]")
        console.print(f"  ID: {wiki.id}")
        console.print(f"  URL: {settings.space_url}/wiki/{wiki.id}")

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("update")
def update_wiki(
    wiki_id: Annotated[
        int,
        typer.Argument(help="Wiki page ID"),
    ],
    name: Annotated[
        str | None,
        typer.Option("--name", "-n", help="New page name"),
    ] = None,
    content: Annotated[
        str | None,
        typer.Option("--content", "-c", help="New content"),
    ] = None,
    file: Annotated[
        Path | None,
        typer.Option("--file", "-f", help="Read content from file"),
    ] = None,
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """Update a wiki page."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    # Get content from file if specified
    wiki_content = content
    if file:
        if not file.exists():
            err_console.print(f"[red]File not found: {file}[/red]")
            raise typer.Exit(1)
        wiki_content = file.read_text(encoding="utf-8")

    if not name and not wiki_content:
        err_console.print("[yellow]No update options provided.[/yellow]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            data: dict[str, str] = {}
            if name:
                data["name"] = name
            if wiki_content:
                data["content"] = wiki_content

            result = client.patch(f"/wikis/{wiki_id}", data=data)
            wiki = Wiki.model_validate(result)

        if json_output:
            import json

            out = wiki.model_dump(by_alias=True, mode="json")
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        console.print(f"[green]Updated wiki page: {wiki.name}[/green]")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Wiki page {wiki_id} not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@app.command("delete")
def delete_wiki(
    wiki_id: Annotated[
        int,
        typer.Argument(help="Wiki page ID"),
    ],
    force: Annotated[
        bool,
        typer.Option("--force", "-f", help="Skip confirmation"),
    ] = False,
) -> None:
    """Delete a wiki page."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            # Fetch wiki first to show info
            data = client.get(f"/wikis/{wiki_id}")
            wiki = Wiki.model_validate(data)

            if not force:
                confirm = typer.confirm(f"Delete wiki page '{wiki.name}'?")
                if not confirm:
                    console.print("[yellow]Cancelled.[/yellow]")
                    raise typer.Abort()

            client.delete(f"/wikis/{wiki_id}")

        console.print(f"[green]Deleted wiki page: {wiki.name}[/green]")

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Wiki page {wiki_id} not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


# Wiki attachment subcommands


@attachment_app.command("list")
def list_wiki_attachments(
    wiki_id: Annotated[
        int,
        typer.Argument(help="Wiki page ID"),
    ],
    json_output: Annotated[
        bool,
        typer.Option("--json", "-j", help="Output as JSON"),
    ] = False,
) -> None:
    """List attachments on a wiki page."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            data = client.get(f"/wikis/{wiki_id}/attachments")
            attachments = [Attachment.model_validate(a) for a in data]  # type: ignore[union-attr]

        if json_output:
            import json

            out = [a.model_dump(by_alias=True, mode="json") for a in attachments]
            console.print_json(json.dumps(out, ensure_ascii=False, default=str))
            return

        if not attachments:
            console.print(f"[yellow]No attachments on wiki {wiki_id}.[/yellow]")
            return

        table = Table(title=f"Wiki Attachments: {wiki_id}")
        table.add_column("ID", style="cyan")
        table.add_column("Name")
        table.add_column("Size", justify="right")

        for att in attachments:
            table.add_row(str(att.id), att.name, _format_size(att.size))

        console.print(table)

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Wiki page {wiki_id} not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@attachment_app.command("download")
def download_wiki_attachment(
    wiki_id: Annotated[
        int,
        typer.Argument(help="Wiki page ID"),
    ],
    attachment_id: Annotated[
        int,
        typer.Argument(help="Attachment ID"),
    ],
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Output path"),
    ] = None,
) -> None:
    """Download a wiki attachment."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            output_path = output or Path(".")
            _, filename = client.download_file(
                f"/wikis/{wiki_id}/attachments/{attachment_id}",
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
def upload_wiki_attachment(
    wiki_id: Annotated[
        int,
        typer.Argument(help="Wiki page ID"),
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
    """Upload an attachment to a wiki page."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    try:
        with BacklogClient(settings=settings) as client:
            # Upload file to space first
            upload_result = client.upload_file(file_path)
            attachment_id = upload_result["id"]

            # Attach to wiki
            result = client.post(
                f"/wikis/{wiki_id}/attachments",
                data={"attachmentId[]": attachment_id},
            )

        if json_output:
            import json

            console.print_json(json.dumps(result, ensure_ascii=False))
            return

        console.print(f"[green]Uploaded {file_path.name} to wiki {wiki_id}[/green]")

    except FileNotFoundError as e:
        err_console.print(f"[red]{e}[/red]")
        raise typer.Exit(1) from e
    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print(f"[red]Wiki page {wiki_id} not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e


@attachment_app.command("delete")
def delete_wiki_attachment(
    wiki_id: Annotated[
        int,
        typer.Argument(help="Wiki page ID"),
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
    """Delete a wiki attachment."""
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    if not force:
        confirm = typer.confirm(
            f"Delete attachment {attachment_id} from wiki {wiki_id}?"
        )
        if not confirm:
            console.print("[yellow]Cancelled.[/yellow]")
            raise typer.Abort()

    try:
        with BacklogClient(settings=settings) as client:
            client.delete(f"/wikis/{wiki_id}/attachments/{attachment_id}")

        console.print(
            f"[green]Deleted attachment {attachment_id} from wiki {wiki_id}[/green]"
        )

    except BacklogAPIError as e:
        if e.is_not_found():
            err_console.print("[red]Attachment not found.[/red]")
        else:
            err_console.print(f"[red]API Error: {e}[/red]")
        raise typer.Exit(1) from e
