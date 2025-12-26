"""Integration tests for CLI project commands."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from bacli_py.cli.project import app
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


class TestListProjectsCommand:
    """Tests for project list command."""

    def test_list_projects(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test listing projects."""
        with patch("bacli_py.cli.project.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_projects

            result = runner.invoke(app, ["list"])

            assert result.exit_code == 0
            assert "TEST" in result.output
            assert "Test Project" in result.output

    def test_list_projects_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test listing projects with JSON output."""
        with patch("bacli_py.cli.project.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_projects

            result = runner.invoke(app, ["list", "--json"])

            assert result.exit_code == 0
            assert '"projectKey"' in result.output

    def test_list_projects_empty(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test listing projects when none exist."""
        with patch("bacli_py.cli.project.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = []

            result = runner.invoke(app, ["list"])

            assert result.exit_code == 0
            assert "No projects found" in result.output

    def test_list_projects_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test listing projects when not logged in."""
        result = runner.invoke(app, ["list"])

        assert result.exit_code == 1
        assert "Not logged in" in result.output


class TestProjectInfoCommand:
    """Tests for project info command."""

    def test_project_info(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
    ) -> None:
        """Test showing project info."""
        with patch("bacli_py.cli.project.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = [sample_project]

            result = runner.invoke(app, ["info", "TEST"])

            assert result.exit_code == 0
            assert "Test Project" in result.output
            assert "TEST" in result.output

    def test_project_info_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
    ) -> None:
        """Test showing project info with JSON output."""
        with patch("bacli_py.cli.project.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = [sample_project]

            result = runner.invoke(app, ["info", "TEST", "--json"])

            assert result.exit_code == 0
            assert '"projectKey"' in result.output

    def test_project_info_not_found(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test showing info for non-existent project."""
        with patch("bacli_py.cli.project.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_projects

            result = runner.invoke(app, ["info", "NONEXISTENT"])

            assert result.exit_code == 1
            assert "not found" in result.output


class TestListIssueTypesCommand:
    """Tests for project types command."""

    def test_list_issue_types(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
        sample_issue_types: list[dict[str, Any]],
    ) -> None:
        """Test listing issue types."""
        with patch("bacli_py.cli.project.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None

            # First call for project, second for issue types
            mock_instance.get.side_effect = [
                [sample_project],  # Projects
                sample_issue_types,  # Issue types
            ]

            result = runner.invoke(app, ["types", "TEST"])

            assert result.exit_code == 0
            assert "Task" in result.output
            assert "Bug" in result.output

    def test_list_issue_types_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
        sample_issue_types: list[dict[str, Any]],
    ) -> None:
        """Test listing issue types with JSON output."""
        with patch("bacli_py.cli.project.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None

            mock_instance.get.side_effect = [
                [sample_project],
                sample_issue_types,
            ]

            result = runner.invoke(app, ["types", "TEST", "--json"])

            assert result.exit_code == 0
            assert '"name"' in result.output


class TestListStatusesCommand:
    """Tests for project statuses command."""

    def test_list_statuses(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
        sample_statuses: list[dict[str, Any]],
    ) -> None:
        """Test listing statuses."""
        with patch("bacli_py.cli.project.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None

            mock_instance.get.side_effect = [
                [sample_project],  # Projects
                sample_statuses,  # Statuses
            ]

            result = runner.invoke(app, ["statuses", "TEST"])

            assert result.exit_code == 0
            assert "Open" in result.output
            assert "In Progress" in result.output
            assert "Done" in result.output
