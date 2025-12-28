"""Tests for config/settings.py."""

from __future__ import annotations

from pathlib import Path

import pytest

from bklg.config.settings import Settings, get_config_file, get_settings


class TestSettings:
    """Tests for Settings class."""

    def test_default_values(self) -> None:
        """Test default values when no config provided."""
        settings = Settings()
        assert settings.space_url is None
        assert settings.api_key is None
        assert settings.default_project is None

    def test_with_values(self) -> None:
        """Test settings with provided values."""
        settings = Settings(
            space_url="https://test.backlog.com",
            api_key="test-key",
            default_project="TEST",
        )
        assert settings.space_url == "https://test.backlog.com"
        assert settings.api_key == "test-key"
        assert settings.default_project == "TEST"

    def test_is_configured_false(self) -> None:
        """Test is_configured returns False when not configured."""
        settings = Settings()
        assert settings.is_configured is False

        settings = Settings(space_url="https://test.backlog.com")
        assert settings.is_configured is False

        settings = Settings(api_key="test-key")
        assert settings.is_configured is False

    def test_is_configured_true(self) -> None:
        """Test is_configured returns True when configured."""
        settings = Settings(
            space_url="https://test.backlog.com",
            api_key="test-key",
        )
        assert settings.is_configured is True

    def test_base_url(self) -> None:
        """Test base_url property."""
        settings = Settings(
            space_url="https://test.backlog.com",
            api_key="test-key",
        )
        assert settings.base_url == "https://test.backlog.com/api/v2"

    def test_base_url_strips_trailing_slash(self) -> None:
        """Test base_url strips trailing slash from space_url."""
        settings = Settings(
            space_url="https://test.backlog.com/",
            api_key="test-key",
        )
        assert settings.base_url == "https://test.backlog.com/api/v2"

    def test_base_url_raises_when_not_configured(self) -> None:
        """Test base_url raises ValueError when space_url not set."""
        settings = Settings()
        with pytest.raises(ValueError, match="space_url is not configured"):
            _ = settings.base_url


class TestSettingsPersistence:
    """Tests for settings save/load functionality."""

    def test_save_and_load(self, tmp_config_dir: Path) -> None:
        """Test saving and loading settings."""
        settings = Settings(
            space_url="https://test.backlog.com",
            api_key="test-key",
            default_project="TEST",
        )
        settings.save()

        loaded = Settings.load()
        assert loaded.space_url == settings.space_url
        assert loaded.api_key == settings.api_key
        assert loaded.default_project == settings.default_project

    def test_load_nonexistent_file(self, tmp_config_dir: Path) -> None:
        """Test loading returns empty settings when file doesn't exist."""
        settings = Settings.load()
        assert settings.space_url is None
        assert settings.api_key is None

    def test_save_excludes_none_values(self, tmp_config_dir: Path) -> None:
        """Test save excludes None values from TOML."""
        settings = Settings(
            space_url="https://test.backlog.com",
            api_key="test-key",
        )
        settings.save()

        config_file = get_config_file()
        content = config_file.read_text()
        assert "default_project" not in content

    def test_get_settings_helper(self, tmp_config_dir: Path) -> None:
        """Test get_settings helper function."""
        settings = Settings(
            space_url="https://test.backlog.com",
            api_key="test-key",
        )
        settings.save()

        loaded = get_settings()
        assert loaded.space_url == settings.space_url
