"""Main CLI entry point for bacli."""

from __future__ import annotations

from typing import Annotated

import typer

from bacli_py.cli.api import app as api_app
from bacli_py.cli.auth import app as auth_app
from bacli_py.cli.context import OutputContext
from bacli_py.cli.issue import app as issue_app
from bacli_py.cli.notification import app as notification_app
from bacli_py.cli.project import app as project_app
from bacli_py.cli.space import app as space_app
from bacli_py.cli.user import app as user_app
from bacli_py.cli.watch import app as watch_app
from bacli_py.cli.wiki import app as wiki_app

app = typer.Typer(
    name="bacli",
    help="Backlog CLI - A command-line interface for Backlog",
    no_args_is_help=True,
)

app.add_typer(auth_app, name="auth")
app.add_typer(project_app, name="project")
app.add_typer(issue_app, name="issue")
app.add_typer(user_app, name="user")
app.add_typer(space_app, name="space")
app.add_typer(notification_app, name="notification")
app.add_typer(watch_app, name="watch")
app.add_typer(wiki_app, name="wiki")
app.add_typer(api_app, name="api")


@app.callback()
def callback(
    quiet: Annotated[
        bool,
        typer.Option("--quiet", "-q", help="Minimal output (errors only)"),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Verbose output"),
    ] = False,
) -> None:
    """Backlog CLI - A command-line interface for Backlog."""
    OutputContext.set_level(quiet=quiet, verbose=verbose)


if __name__ == "__main__":
    app()
