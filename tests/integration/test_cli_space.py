"""Integration tests for CLI space commands."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from bacli_py.cli.space import app
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


class TestSpaceInfoCommand:
    """Tests for space info command."""

    def test_space_info(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_space: dict[str, Any],
    ) -> None:
        """Test showing space info."""
        with patch("bacli_py.cli.space.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_space

            result = runner.invoke(app, ["info"])

            assert result.exit_code == 0
            assert "Demo Space" in result.output
            assert "demo" in result.output

    def test_space_info_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_space: dict[str, Any],
    ) -> None:
        """Test showing space info with JSON output."""
        with patch("bacli_py.cli.space.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_space

            result = runner.invoke(app, ["info", "--json"])

            assert result.exit_code == 0
            assert '"spaceKey"' in result.output

    def test_space_info_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test showing space info when not logged in."""
        result = runner.invoke(app, ["info"])

        assert result.exit_code == 1
        assert "Not logged in" in result.output


class TestSpaceNoticeCommand:
    """Tests for space notice command."""

    def test_space_notice(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_space_notification: dict[str, Any],
    ) -> None:
        """Test showing space notice."""
        with patch("bacli_py.cli.space.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_space_notification

            result = runner.invoke(app, ["notice"])

            assert result.exit_code == 0
            assert "This is a space announcement" in result.output

    def test_space_notice_empty(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test showing space notice when none set."""
        with patch("bacli_py.cli.space.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = {"content": None}

            result = runner.invoke(app, ["notice"])

            assert result.exit_code == 0
            assert "No announcement set" in result.output


class TestDiskUsageCommand:
    """Tests for disk usage command."""

    def test_disk_usage(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_disk_usage: dict[str, Any],
    ) -> None:
        """Test showing disk usage."""
        with patch("bacli_py.cli.space.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_disk_usage

            result = runner.invoke(app, ["disk"])

            assert result.exit_code == 0
            assert "Disk Usage" in result.output
            assert "Issues" in result.output
            assert "Wiki" in result.output
            assert "Git" in result.output

    def test_disk_usage_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_disk_usage: dict[str, Any],
    ) -> None:
        """Test showing disk usage with JSON output."""
        with patch("bacli_py.cli.space.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_disk_usage

            result = runner.invoke(app, ["disk", "--json"])

            assert result.exit_code == 0
            assert '"capacity"' in result.output
