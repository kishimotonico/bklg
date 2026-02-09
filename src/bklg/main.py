"""Main CLI entry point for bklg."""

from __future__ import annotations

from typing import Annotated

import typer

from bklg.cli.api import app as api_app
from bklg.cli.auth import app as auth_app
from bklg.cli.context import OutputContext
from bklg.cli.issue import app as issue_app
from bklg.cli.notification import app as notification_app
from bklg.cli.project import app as project_app
from bklg.cli.space import app as space_app
from bklg.cli.user import app as user_app
from bklg.cli.watch import app as watch_app
from bklg.cli.wiki import app as wiki_app
from bklg.config.settings import get_settings
from bklg.utils.logger import setup_logging

app = typer.Typer(
    name="bklg",
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
    debug_api: Annotated[
        bool,
        typer.Option("--debug-api", help="APIリクエストログをstderrにも出力"),
    ] = False,
) -> None:
    """Backlog CLI - A command-line interface for Backlog."""
    # ログ初期化
    settings = get_settings()
    setup_logging(
        log_file=settings.logging.file,
        level=settings.logging.level,
        max_size_mb=settings.logging.max_size_mb,
        backup_count=settings.logging.backup_count,
        console_output=debug_api,
    )

    OutputContext.set_level(quiet=quiet, verbose=verbose)


if __name__ == "__main__":
    app()
