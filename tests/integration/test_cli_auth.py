"""Integration tests for CLI auth commands."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from bklg.cli.auth import app
from bklg.config.settings import Settings


@pytest.fixture
def runner() -> CliRunner:
    """Create CLI runner."""
    return CliRunner()


class TestLoginCommand:
    """Tests for auth login command."""

    def test_login_success(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
        sample_user: dict[str, Any],
    ) -> None:
        """Test successful login."""
        with patch("bklg.cli.auth.BacklogClient") as mock_client:
            mock_client.return_value.__enter__.return_value.get_myself.return_value = (
                sample_user
            )

            result = runner.invoke(
                app,
                ["login", "--space-url", "https://test.backlog.com", "--api-key", "test-key"],
            )

            assert result.exit_code == 0
            assert "Logged in as" in result.output
            assert "Test User" in result.output

    def test_login_auth_failure(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test login with invalid credentials."""
        from bklg.api.client import BacklogAPIError
        from bklg.models.common import ErrorCode

        with patch("bklg.cli.auth.BacklogClient") as mock_client:
            mock_client.return_value.__enter__.return_value.get_myself.side_effect = (
                BacklogAPIError("Auth failed", code=ErrorCode.AUTHENTICATION_ERROR)
            )

            result = runner.invoke(
                app,
                ["login", "--space-url", "https://test.backlog.com", "--api-key", "bad-key"],
            )

            assert result.exit_code == 1
            assert "Authentication failed" in result.output

    def test_login_url_normalization(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
        sample_user: dict[str, Any],
    ) -> None:
        """Test URL normalization (adding https://, removing trailing slash)."""
        with patch("bklg.cli.auth.BacklogClient") as mock_client:
            mock_client.return_value.__enter__.return_value.get_myself.return_value = (
                sample_user
            )

            # Test without https://
            result = runner.invoke(
                app,
                ["login", "--space-url", "test.backlog.com/", "--api-key", "test-key"],
            )

            assert result.exit_code == 0


class TestLogoutCommand:
    """Tests for auth logout command."""

    def test_logout_success(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test successful logout."""
        # First create config file
        settings = Settings(
            space_url="https://test.backlog.com",
            api_key="test-key",
        )
        settings.save()

        result = runner.invoke(app, ["logout"])

        assert result.exit_code == 0
        assert "Logged out successfully" in result.output

    def test_logout_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test logout when not logged in."""
        result = runner.invoke(app, ["logout"])

        assert result.exit_code == 0
        assert "Not logged in" in result.output


class TestStatusCommand:
    """Tests for auth status command."""

    def test_status_authenticated(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
        sample_user: dict[str, Any],
    ) -> None:
        """Test status when authenticated."""
        # First create config file
        settings = Settings(
            space_url="https://test.backlog.com",
            api_key="test-key",
        )
        settings.save()

        with patch("bklg.cli.auth.BacklogClient") as mock_client:
            mock_instance = mock_client.return_value.__enter__.return_value
            mock_instance.get_myself.return_value = sample_user
            mock_instance.rate_limit_handler.last_rate_limit = None

            result = runner.invoke(app, ["status"])

            assert result.exit_code == 0
            assert "Authenticated" in result.output
            assert "Test User" in result.output

    def test_status_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test status when not logged in."""
        result = runner.invoke(app, ["status"])

        assert result.exit_code == 1
        assert "Not logged in" in result.output

    def test_status_auth_expired(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test status when authentication has expired."""
        from bklg.api.client import BacklogAPIError
        from bklg.models.common import ErrorCode

        settings = Settings(
            space_url="https://test.backlog.com",
            api_key="expired-key",
        )
        settings.save()

        with patch("bklg.cli.auth.BacklogClient") as mock_client:
            mock_client.return_value.__enter__.return_value.get_myself.side_effect = (
                BacklogAPIError("Auth failed", code=ErrorCode.AUTHENTICATION_ERROR)
            )

            result = runner.invoke(app, ["status"])

            assert result.exit_code == 1
            assert "Authentication failed" in result.output
