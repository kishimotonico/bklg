"""Integration tests for CLI watch commands."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from bacli_py.cli.watch import app
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


class TestListWatchingsCommand:
    """Tests for watch list command."""

    def test_list_watchings(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_watching: dict[str, Any],
        sample_user: dict[str, Any],
    ) -> None:
        """Test listing watched items."""
        with patch("bacli_py.cli.watch.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.side_effect = [sample_user, [sample_watching]]

            result = runner.invoke(app, ["list"])

            assert result.exit_code == 0
            assert "Watched Items" in result.output
            assert "TEST-1" in result.output

    def test_list_watchings_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_watching: dict[str, Any],
        sample_user: dict[str, Any],
    ) -> None:
        """Test listing watchings with JSON output."""
        with patch("bacli_py.cli.watch.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.side_effect = [sample_user, [sample_watching]]

            result = runner.invoke(app, ["list", "--json"])

            assert result.exit_code == 0
            assert '"resourceAlreadyRead"' in result.output

    def test_list_watchings_empty(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_user: dict[str, Any],
    ) -> None:
        """Test listing watchings when none exist."""
        with patch("bacli_py.cli.watch.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.side_effect = [sample_user, []]

            result = runner.invoke(app, ["list"])

            assert result.exit_code == 0
            assert "No watched items" in result.output

    def test_list_watchings_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test listing watchings when not logged in."""
        result = runner.invoke(app, ["list"])

        assert result.exit_code == 1
        assert "Not logged in" in result.output


class TestAddWatchingCommand:
    """Tests for watch add command."""

    def test_add_watching(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_watching: dict[str, Any],
    ) -> None:
        """Test adding a watch."""
        with patch("bacli_py.cli.watch.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.post.return_value = sample_watching

            result = runner.invoke(app, ["add", "TEST-1"])

            assert result.exit_code == 0
            assert "Now watching TEST-1" in result.output

    def test_add_watching_with_note(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_watching: dict[str, Any],
    ) -> None:
        """Test adding a watch with note."""
        with patch("bacli_py.cli.watch.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.post.return_value = sample_watching

            result = runner.invoke(app, ["add", "TEST-1", "--note", "Important"])

            assert result.exit_code == 0
            assert "Now watching TEST-1" in result.output


class TestRemoveWatchingCommand:
    """Tests for watch remove command."""

    def test_remove_watching(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test removing a watch."""
        with patch("bacli_py.cli.watch.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.delete.return_value = {}

            result = runner.invoke(app, ["remove", "1", "--force"])

            assert result.exit_code == 0
            assert "Removed watch 1" in result.output


class TestWatchingInfoCommand:
    """Tests for watch info command."""

    def test_watching_info(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_watching: dict[str, Any],
    ) -> None:
        """Test showing watch info."""
        with patch("bacli_py.cli.watch.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_watching

            result = runner.invoke(app, ["info", "1"])

            assert result.exit_code == 0
            assert "Watch ID: 1" in result.output
            assert "TEST-1" in result.output


class TestMarkWatchingReadCommand:
    """Tests for watch read command."""

    def test_mark_watching_read(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test marking watch as read."""
        with patch("bacli_py.cli.watch.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.post.return_value = {}

            result = runner.invoke(app, ["read", "1"])

            assert result.exit_code == 0
            assert "Marked watch 1 as read" in result.output
