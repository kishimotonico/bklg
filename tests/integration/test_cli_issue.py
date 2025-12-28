"""Integration tests for CLI issue commands."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from bacli_py.cli.issue import app, parse_issue_identifier
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


class TestParseIssueIdentifier:
    """Tests for parse_issue_identifier function."""

    def test_parse_issue_key(self) -> None:
        """Test parsing issue key."""
        assert parse_issue_identifier("PROJ-123") == "PROJ-123"
        assert parse_issue_identifier("TEST-1") == "TEST-1"

    def test_parse_numeric_id(self) -> None:
        """Test parsing numeric ID."""
        assert parse_issue_identifier("12345") == "12345"

    def test_parse_url(self) -> None:
        """Test parsing URL."""
        url = "https://example.backlog.com/view/PROJ-123"
        assert parse_issue_identifier(url) == "PROJ-123"

    def test_parse_url_with_query(self) -> None:
        """Test parsing URL with query parameters."""
        url = "https://example.backlog.com/view/PROJ-456?tab=comments"
        assert parse_issue_identifier(url) == "PROJ-456"

    def test_parse_url_case_insensitive(self) -> None:
        """Test URL parsing is case insensitive for project key."""
        url = "https://example.backlog.com/view/proj-123"
        assert parse_issue_identifier(url) == "proj-123"


class TestListIssuesCommand:
    """Tests for issue list command."""

    def test_list_issues(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
        sample_issues: list[dict[str, Any]],
    ) -> None:
        """Test listing issues."""
        with patch("bacli_py.cli.issue.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None

            mock_instance.get.side_effect = [
                [sample_project],  # Projects
                sample_issues,  # Issues
            ]

            result = runner.invoke(app, ["list", "--project", "TEST"])

            assert result.exit_code == 0
            assert "TEST-1" in result.output

    def test_list_issues_with_project(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
        sample_issues: list[dict[str, Any]],
    ) -> None:
        """Test listing issues with project filter."""
        with patch("bacli_py.cli.issue.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None

            mock_instance.get.side_effect = [
                [sample_project],  # Projects
                sample_issues,  # Issues
            ]

            result = runner.invoke(app, ["list", "--project", "TEST"])

            assert result.exit_code == 0
            assert "TEST-1" in result.output

    def test_list_issues_with_assignee_me(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
        sample_user: dict[str, Any],
        sample_issues: list[dict[str, Any]],
    ) -> None:
        """Test listing issues assigned to @me."""
        with patch("bacli_py.cli.issue.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get_myself.return_value = sample_user

            mock_instance.get.side_effect = [
                [sample_project],  # Projects
                sample_issues,  # Issues
            ]

            result = runner.invoke(app, ["list", "--project", "TEST", "--assignee", "@me"])

            assert result.exit_code == 0
            mock_instance.get_myself.assert_called()

    def test_list_issues_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
        sample_issues: list[dict[str, Any]],
    ) -> None:
        """Test listing issues with JSON output."""
        with patch("bacli_py.cli.issue.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None

            mock_instance.get.side_effect = [
                [sample_project],  # Projects
                sample_issues,  # Issues
            ]

            result = runner.invoke(app, ["list", "--project", "TEST", "--json"])

            assert result.exit_code == 0
            assert '"issueKey"' in result.output

    def test_list_issues_empty(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
    ) -> None:
        """Test listing issues when none exist."""
        with patch("bacli_py.cli.issue.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None

            mock_instance.get.side_effect = [
                [sample_project],  # Projects
                [],  # Issues (empty)
            ]

            result = runner.invoke(app, ["list", "--project", "TEST"])

            assert result.exit_code == 0
            assert "No issues found" in result.output

    def test_list_issues_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test listing issues when not logged in."""
        result = runner.invoke(app, ["list", "--project", "TEST"])

        assert result.exit_code == 1
        assert "Not logged in" in result.output


class TestViewIssueCommand:
    """Tests for issue view command."""

    def test_view_issue(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_issue: dict[str, Any],
    ) -> None:
        """Test viewing issue details."""
        with patch("bacli_py.cli.issue.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_issue

            result = runner.invoke(app, ["view", "TEST-1"])

            assert result.exit_code == 0
            assert "TEST-1" in result.output
            assert "Test Issue" in result.output

    def test_view_issue_with_comments(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_issue: dict[str, Any],
        sample_comment: dict[str, Any],
    ) -> None:
        """Test viewing issue with comments."""
        with patch("bacli_py.cli.issue.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None

            mock_instance.get.side_effect = [
                sample_issue,  # Issue
                [sample_comment],  # Comments
            ]

            result = runner.invoke(app, ["view", "TEST-1", "--comments"])

            assert result.exit_code == 0
            assert "Test Issue" in result.output
            assert "test comment" in result.output

    def test_view_issue_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_issue: dict[str, Any],
    ) -> None:
        """Test viewing issue with JSON output."""
        with patch("bacli_py.cli.issue.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_issue

            result = runner.invoke(app, ["view", "TEST-1", "--json"])

            assert result.exit_code == 0
            assert '"issueKey"' in result.output

    def test_view_issue_from_url(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_issue: dict[str, Any],
    ) -> None:
        """Test viewing issue from URL."""
        with patch("bacli_py.cli.issue.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_issue

            result = runner.invoke(
                app,
                ["view", "https://example.backlog.com/view/TEST-1"],
            )

            assert result.exit_code == 0
            assert "TEST-1" in result.output

    def test_view_issue_not_found(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test viewing non-existent issue."""
        from bacli_py.api.client import BacklogAPIError
        from bacli_py.models.common import ErrorCode

        with patch("bacli_py.cli.issue.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.side_effect = BacklogAPIError(
                "Not found", code=ErrorCode.NO_RESOURCE_ERROR
            )

            result = runner.invoke(app, ["view", "NONEXISTENT-999"])

            assert result.exit_code == 1
            assert "not found" in result.output

    def test_view_issue_web(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test opening issue in browser."""
        with patch("webbrowser.open") as mock_open:
            result = runner.invoke(app, ["view", "TEST-1", "--web"])

            assert result.exit_code == 0
            assert "Opening" in result.output
            mock_open.assert_called_once()
            call_url = mock_open.call_args[0][0]
            assert "TEST-1" in call_url


class TestOpenIssueCommand:
    """Tests for issue open command."""

    def test_open_issue(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test opening issue in browser."""
        with patch("webbrowser.open") as mock_open:
            result = runner.invoke(app, ["open", "TEST-1"])

            assert result.exit_code == 0
            assert "Opening" in result.output
            mock_open.assert_called_once_with(
                "https://test.backlog.com/view/TEST-1"
            )

    def test_open_issue_from_url(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test opening issue from URL."""
        with patch("webbrowser.open") as mock_open:
            result = runner.invoke(
                app,
                ["open", "https://other.backlog.com/view/PROJ-456"],
            )

            assert result.exit_code == 0
            mock_open.assert_called_once()
            call_url = mock_open.call_args[0][0]
            assert "PROJ-456" in call_url

    def test_open_issue_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test opening issue when not logged in."""
        result = runner.invoke(app, ["open", "TEST-1"])

        assert result.exit_code == 1
        assert "Not logged in" in result.output
