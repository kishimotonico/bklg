"""Integration tests for CLI notification commands."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from bacli_py.cli.notification import app
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


class TestListNotificationsCommand:
    """Tests for notification list command."""

    def test_list_notifications(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_notification: dict[str, Any],
    ) -> None:
        """Test listing notifications."""
        with patch("bacli_py.cli.notification.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = [sample_notification]

            result = runner.invoke(app, ["list"])

            assert result.exit_code == 0
            assert "Notifications" in result.output
            assert "TEST" in result.output

    def test_list_notifications_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_notification: dict[str, Any],
    ) -> None:
        """Test listing notifications with JSON output."""
        with patch("bacli_py.cli.notification.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = [sample_notification]

            result = runner.invoke(app, ["list", "--json"])

            assert result.exit_code == 0
            assert '"alreadyRead"' in result.output

    def test_list_notifications_empty(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test listing notifications when none exist."""
        with patch("bacli_py.cli.notification.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = []

            result = runner.invoke(app, ["list"])

            assert result.exit_code == 0
            assert "No notifications" in result.output

    def test_list_notifications_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test listing notifications when not logged in."""
        result = runner.invoke(app, ["list"])

        assert result.exit_code == 1
        assert "Not logged in" in result.output


class TestNotificationCountCommand:
    """Tests for notification count command."""

    def test_notification_count(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test getting notification count."""
        with patch("bacli_py.cli.notification.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = {"count": 5}

            result = runner.invoke(app, ["count"])

            assert result.exit_code == 0
            assert "5" in result.output
            assert "unread" in result.output

    def test_notification_count_zero(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test getting notification count when zero."""
        with patch("bacli_py.cli.notification.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = {"count": 0}

            result = runner.invoke(app, ["count"])

            assert result.exit_code == 0
            assert "No unread notifications" in result.output

    def test_notification_count_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test getting notification count with JSON output."""
        with patch("bacli_py.cli.notification.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = {"count": 3}

            result = runner.invoke(app, ["count", "--json"])

            assert result.exit_code == 0
            assert '"count"' in result.output


class TestMarkAsReadCommand:
    """Tests for notification mark as read command."""

    def test_mark_as_read_single(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test marking single notification as read."""
        with patch("bacli_py.cli.notification.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.post.return_value = {}

            result = runner.invoke(app, ["read", "123"])

            assert result.exit_code == 0
            assert "Marked notification 123 as read" in result.output

    def test_mark_as_read_all(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test marking all notifications as read."""
        with patch("bacli_py.cli.notification.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.post.return_value = {}

            result = runner.invoke(app, ["read", "--all"])

            assert result.exit_code == 0
            assert "Marked all notifications as read" in result.output

    def test_mark_as_read_no_id(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test marking as read without ID or --all."""
        result = runner.invoke(app, ["read"])

        assert result.exit_code == 1
        assert "Specify notification ID or use --all" in result.output
