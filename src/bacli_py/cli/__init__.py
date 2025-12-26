"""CLI commands for bacli."""

from bacli_py.cli.auth import app as auth_app
from bacli_py.cli.project import app as project_app

__all__ = ["auth_app", "project_app"]
