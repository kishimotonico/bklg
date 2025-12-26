"""Main CLI entry point for bacli."""

from __future__ import annotations

import typer

from bacli_py.cli.auth import app as auth_app
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
def callback() -> None:
    """Backlog CLI - A command-line interface for Backlog."""


if __name__ == "__main__":
    app()
