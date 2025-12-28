"""Integration tests for CLI user commands."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from bacli_py.cli.user import app
from bacli_py.config.settings import Settings


@pytest.fixture
def runner() -> CliRunner:
    """Create CLI runner."""
    return CliRunner()


@pytest.fixture
def configured_settings(tmp_config_dir: Path) -> Settings:
    """Create and save configured settings."""
    settings = Settings(
        space_url="https://test.backlog.com",
        api_key="test-key",
    )
    settings.save()
    return settings


class TestListUsersCommand:
    """Tests for user list command."""

    def test_list_users(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_users: list[dict[str, Any]],
    ) -> None:
        """Test listing users."""
        with patch("bacli_py.cli.user.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_users

            result = runner.invoke(app, ["list"])

            assert result.exit_code == 0
            assert "Test User" in result.output
            assert "test_user" in result.output

    def test_list_users_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_users: list[dict[str, Any]],
    ) -> None:
        """Test listing users with JSON output."""
        with patch("bacli_py.cli.user.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_users

            result = runner.invoke(app, ["list", "--json"])

            assert result.exit_code == 0
            assert '"userId"' in result.output

    def test_list_users_empty(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test listing users when none exist."""
        with patch("bacli_py.cli.user.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = []

            result = runner.invoke(app, ["list"])

            assert result.exit_code == 0
            assert "No users found" in result.output

    def test_list_users_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test listing users when not logged in."""
        result = runner.invoke(app, ["list"])

        assert result.exit_code == 1
        assert "Not logged in" in result.output


class TestUserInfoCommand:
    """Tests for user info command."""

    def test_user_info_me(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_user: dict[str, Any],
    ) -> None:
        """Test showing current user info."""
        with patch("bacli_py.cli.user.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_user

            result = runner.invoke(app, ["info"])

            assert result.exit_code == 0
            assert "Test User" in result.output

    def test_user_info_by_id(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_user: dict[str, Any],
    ) -> None:
        """Test showing user info by ID."""
        with patch("bacli_py.cli.user.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_user

            result = runner.invoke(app, ["info", "test_user"])

            assert result.exit_code == 0
            assert "Test User" in result.output

    def test_user_info_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_user: dict[str, Any],
    ) -> None:
        """Test showing user info with JSON output."""
        with patch("bacli_py.cli.user.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_user

            result = runner.invoke(app, ["info", "--json"])

            assert result.exit_code == 0
            assert '"userId"' in result.output


class TestUserActivityCommand:
    """Tests for user activity command."""

    def test_user_activity(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_user: dict[str, Any],
    ) -> None:
        """Test showing user activity."""
        sample_activity = [
            {
                "type": 1,
                "content": {"summary": "Test Issue"},
                "project": {"projectKey": "TEST"},
                "created": "2024-01-01T00:00:00Z",
            }
        ]

        with patch("bacli_py.cli.user.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.side_effect = [sample_user, sample_activity]

            result = runner.invoke(app, ["activity"])

            assert result.exit_code == 0
            assert "Issue Created" in result.output
            assert "TEST" in result.output
