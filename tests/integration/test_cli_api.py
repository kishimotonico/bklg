"""Integration tests for CLI api commands."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from bacli_py.cli.api import app
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


class TestApiCallCommand:
    """Tests for api call command."""

    def test_api_get(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_users: list[dict[str, Any]],
    ) -> None:
        """Test GET request."""
        with patch("bacli_py.cli.api.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_users

            result = runner.invoke(app, ["/users"])

            assert result.exit_code == 0
            assert '"userId"' in result.output

    def test_api_get_with_query_params(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_issues: list[dict[str, Any]],
    ) -> None:
        """Test GET request with query parameters."""
        with patch("bacli_py.cli.api.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_issues

            result = runner.invoke(
                app, ["/issues", "-q", "projectId[]=1", "-q", "count=10"]
            )

            assert result.exit_code == 0
            mock_instance.get.assert_called_once()

    def test_api_post(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_issue: dict[str, Any],
    ) -> None:
        """Test POST request."""
        with patch("bacli_py.cli.api.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.post.return_value = sample_issue

            result = runner.invoke(
                app,
                ["/issues", "-X", "POST", "-d", "projectId=1", "-d", "summary=test"],
            )

            assert result.exit_code == 0

    def test_api_delete(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test DELETE request."""
        with patch("bacli_py.cli.api.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.delete.return_value = {}

            result = runner.invoke(app, ["/issues/123", "-X", "DELETE"])

            assert result.exit_code == 0

    def test_api_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test API call when not logged in."""
        result = runner.invoke(app, ["/users"])

        assert result.exit_code == 1
        assert "Not logged in" in result.output
