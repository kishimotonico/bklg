"""CLI commands for bklg."""

from bklg.cli.auth import app as auth_app
from bklg.cli.project import app as project_app

__all__ = ["auth_app", "project_app"]
