"""Settings management for bklg.

Handles reading and writing configuration from ~/.config/bklg/config.toml
and environment variables.

Environment variables take precedence over config file values:
- BKLG_SPACE_URL: Backlog space URL
- BKLG_API_KEY: Backlog API key
- BKLG_DEFAULT_PROJECT: Default project key
"""

from __future__ import annotations

import os
import tomllib
from pathlib import Path
from typing import Self

import tomli_w
from pydantic import BaseModel, Field


class LoggingConfig(BaseModel):
    """ログ設定."""

    file: str | None = Field(
        default=None,
        description="ログファイルパス（省略時: $XDG_STATE_HOME/bklg/bklg.log）",
    )
    level: str = Field(
        default="DEBUG",
        description="ログレベル (DEBUG, INFO, WARNING, ERROR)",
    )
    max_size_mb: int = Field(
        default=10,
        description="ログファイルの最大サイズ（MB）",
    )
    backup_count: int = Field(
        default=3,
        description="ローテーションで保持するファイル数",
    )


def get_config_dir() -> Path:
    """Get the configuration directory path."""
    config_dir = Path.home() / ".config" / "bklg"
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
    logging: LoggingConfig = Field(
        default_factory=LoggingConfig,
        description="ログ設定",
    )

    @classmethod
    def load(cls) -> Self:
        """Load settings from environment variables and config file.

        Environment variables take precedence over config file values.
        Supported environment variables:
        - BKLG_SPACE_URL: Backlog space URL (domain or full URL)
        - BKLG_API_KEY: Backlog API key
        - BKLG_DEFAULT_PROJECT: Default project key
        """
        # Load from config file first
        config_file = get_config_file()
        if config_file.exists():
            with config_file.open("rb") as f:
                data = tomllib.load(f)
        else:
            data = {}

        # Override with environment variables (higher priority)
        if space_url := os.getenv("BKLG_SPACE_URL"):
            # Normalize URL: add https:// if not present, remove trailing slash
            space_url = space_url.rstrip("/")
            if not space_url.startswith("https://") and not space_url.startswith(
                "http://"
            ):
                space_url = f"https://{space_url}"
            data["space_url"] = space_url
        if api_key := os.getenv("BKLG_API_KEY"):
            data["api_key"] = api_key
        if default_project := os.getenv("BKLG_DEFAULT_PROJECT"):
            data["default_project"] = default_project

        return cls.model_validate(data) if data else cls()

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
