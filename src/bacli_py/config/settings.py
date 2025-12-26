"""Settings management for bacli.

Handles reading and writing configuration from ~/.config/bacli/config.toml
"""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Self

import tomli_w
from pydantic import BaseModel, Field


def get_config_dir() -> Path:
    """Get the configuration directory path."""
    config_dir = Path.home() / ".config" / "bacli"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


def get_config_file() -> Path:
    """Get the configuration file path."""
    return get_config_dir() / "config.toml"


def get_cache_dir() -> Path:
    """Get the cache directory path."""
    cache_dir = get_config_dir() / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


class Settings(BaseModel):
    """Application settings."""

    space_url: str | None = Field(
        default=None,
        description="Backlog space URL (e.g., https://example.backlog.com)",
    )
    api_key: str | None = Field(
        default=None,
        description="Backlog API key",
    )
    default_project: str | None = Field(
        default=None,
        description="Default project key",
    )

    @classmethod
    def load(cls) -> Self:
        """Load settings from config file."""
        config_file = get_config_file()
        if not config_file.exists():
            return cls()

        with config_file.open("rb") as f:
            data = tomllib.load(f)

        return cls.model_validate(data)

    def save(self) -> None:
        """Save settings to config file."""
        config_file = get_config_file()
        data = self.model_dump(exclude_none=True)

        with config_file.open("wb") as f:
            tomli_w.dump(data, f)

    @property
    def is_configured(self) -> bool:
        """Check if essential settings are configured."""
        return self.space_url is not None and self.api_key is not None

    @property
    def base_url(self) -> str:
        """Get the API base URL."""
        if not self.space_url:
            raise ValueError("space_url is not configured")

        url = self.space_url.rstrip("/")
        return f"{url}/api/v2"


def get_settings() -> Settings:
    """Get application settings."""
    return Settings.load()


def save_settings(settings: Settings) -> None:
    """Save application settings."""
    settings.save()
