"""Main CLI entry point for bacli."""

from __future__ import annotations

from typing import Annotated

import typer

from bacli_py.cli.auth import app as auth_app
from bacli_py.cli.context import OutputContext
from bacli_py.cli.issue import app as issue_app
from bacli_py.cli.project import app as project_app

app = typer.Typer(
    name="bacli",
    help="Backlog CLI - A command-line interface for Backlog",
    no_args_is_help=True,
)

app.add_typer(auth_app, name="auth")
app.add_typer(project_app, name="project")
app.add_typer(issue_app, name="issue")


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
