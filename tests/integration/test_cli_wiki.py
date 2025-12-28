"""Integration tests for CLI wiki commands."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from bacli_py.cli.wiki import app
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


class TestListWikisCommand:
    """Tests for wiki list command."""

    def test_list_wikis(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_wiki: dict[str, Any],
        sample_project: dict[str, Any],
    ) -> None:
        """Test listing wiki pages."""
        with patch("bacli_py.cli.wiki.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.side_effect = [[sample_project], [sample_wiki]]

            result = runner.invoke(app, ["list", "-p", "TEST"])

            assert result.exit_code == 0
            assert "Wiki Pages" in result.output
            assert "Test Wiki Page" in result.output

    def test_list_wikis_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_wiki: dict[str, Any],
        sample_project: dict[str, Any],
    ) -> None:
        """Test listing wikis with JSON output."""
        with patch("bacli_py.cli.wiki.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.side_effect = [[sample_project], [sample_wiki]]

            result = runner.invoke(app, ["list", "-p", "TEST", "--json"])

            assert result.exit_code == 0
            assert '"projectId"' in result.output

    def test_list_wikis_empty(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_project: dict[str, Any],
    ) -> None:
        """Test listing wikis when none exist."""
        with patch("bacli_py.cli.wiki.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.side_effect = [[sample_project], []]

            result = runner.invoke(app, ["list", "-p", "TEST"])

            assert result.exit_code == 0
            assert "No wiki pages" in result.output

    def test_list_wikis_not_logged_in(
        self,
        runner: CliRunner,
        tmp_config_dir: Path,
    ) -> None:
        """Test listing wikis when not logged in."""
        result = runner.invoke(app, ["list", "-p", "TEST"])

        assert result.exit_code == 1
        assert "Not logged in" in result.output


class TestViewWikiCommand:
    """Tests for wiki view command."""

    def test_view_wiki(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_wiki: dict[str, Any],
    ) -> None:
        """Test viewing a wiki page."""
        with patch("bacli_py.cli.wiki.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_wiki

            result = runner.invoke(app, ["view", "1"])

            assert result.exit_code == 0
            assert "Test Wiki Page" in result.output

    def test_view_wiki_json(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_wiki: dict[str, Any],
    ) -> None:
        """Test viewing wiki with JSON output."""
        with patch("bacli_py.cli.wiki.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_wiki

            result = runner.invoke(app, ["view", "1", "--json"])

            assert result.exit_code == 0
            assert '"projectId"' in result.output


class TestCreateWikiCommand:
    """Tests for wiki create command."""

    def test_create_wiki(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_wiki: dict[str, Any],
        sample_project: dict[str, Any],
    ) -> None:
        """Test creating a wiki page."""
        with patch("bacli_py.cli.wiki.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = [sample_project]
            mock_instance.post.return_value = sample_wiki

            result = runner.invoke(
                app, ["create", "-p", "TEST", "-n", "New Wiki", "-c", "Content"]
            )

            assert result.exit_code == 0
            assert "Created wiki page" in result.output


class TestUpdateWikiCommand:
    """Tests for wiki update command."""

    def test_update_wiki(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_wiki: dict[str, Any],
    ) -> None:
        """Test updating a wiki page."""
        with patch("bacli_py.cli.wiki.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.patch.return_value = sample_wiki

            result = runner.invoke(app, ["update", "1", "-n", "Updated Name"])

            assert result.exit_code == 0
            assert "Updated wiki page" in result.output

    def test_update_wiki_no_options(
        self,
        runner: CliRunner,
        configured_settings: Settings,
    ) -> None:
        """Test updating wiki without options."""
        result = runner.invoke(app, ["update", "1"])

        assert result.exit_code == 1
        assert "No update options provided" in result.output


class TestDeleteWikiCommand:
    """Tests for wiki delete command."""

    def test_delete_wiki(
        self,
        runner: CliRunner,
        configured_settings: Settings,
        sample_wiki: dict[str, Any],
    ) -> None:
        """Test deleting a wiki page."""
        with patch("bacli_py.cli.wiki.BacklogClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            mock_instance.__enter__.return_value = mock_instance
            mock_instance.__exit__.return_value = None
            mock_instance.get.return_value = sample_wiki
            mock_instance.delete.return_value = {}

            result = runner.invoke(app, ["delete", "1", "--force"])

            assert result.exit_code == 0
            assert "Deleted wiki page" in result.output
