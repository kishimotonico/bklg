"""Cache management for resolver data."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from bklg.config.settings import get_cache_dir

CACHE_TTL_SECONDS = 24 * 60 * 60  # 24 hours


class ProjectCache(BaseModel):
    """Cached data for a single project."""

    id: int = Field(description="Project ID")
    issue_types: dict[str, int] = Field(
        default_factory=dict, description="Issue type name -> ID mapping"
    )
    statuses: dict[str, int] = Field(
        default_factory=dict, description="Status name -> ID mapping"
    )
    categories: dict[str, int] = Field(
        default_factory=dict, description="Category name -> ID mapping"
    )
    versions: dict[str, int] = Field(
        default_factory=dict, description="Version name -> ID mapping"
    )
    users: dict[str, int] = Field(
        default_factory=dict, description="User ID -> numeric ID mapping"
    )
    last_updated: float = Field(
        default_factory=time.time, description="Last update timestamp"
    )


class CacheData(BaseModel):
    """Root cache data structure."""

    projects: dict[str, ProjectCache] = Field(
        default_factory=dict, description="Project key -> cache mapping"
    )
    priorities: dict[str, int] = Field(
        default_factory=dict, description="Priority name -> ID mapping"
    )
    global_users: dict[str, int] = Field(
        default_factory=dict, description="Global user ID -> numeric ID mapping"
    )
    last_updated: float = Field(
        default_factory=time.time, description="Last update timestamp"
    )


class ResolverCache:
    """Cache manager for resolver data."""

    def __init__(self, cache_file: Path | None = None) -> None:
        """Initialize cache manager.

        Args:
            cache_file: Path to cache file. If None, uses default location.
        """
        self.cache_file = cache_file or (get_cache_dir() / "metadata.json")
        self._data: CacheData | None = None

    @property
    def data(self) -> CacheData:
        """Get cache data, loading from file if needed."""
        if self._data is None:
            self._data = self._load()
        return self._data

    def _load(self) -> CacheData:
        """Load cache from file."""
        if not self.cache_file.exists():
            return CacheData()

        try:
            with self.cache_file.open("r", encoding="utf-8") as f:
                raw = json.load(f)
            return CacheData.model_validate(raw)
        except Exception:
            return CacheData()

    def save(self) -> None:
        """Save cache to file."""
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        with self.cache_file.open("w", encoding="utf-8") as f:
            json.dump(self.data.model_dump(), f, ensure_ascii=False, indent=2)

    def clear(self) -> None:
        """Clear all cached data."""
        self._data = CacheData()
        if self.cache_file.exists():
            self.cache_file.unlink()

    def is_expired(self, last_updated: float, ttl: float = CACHE_TTL_SECONDS) -> bool:
        """Check if cache entry is expired.

        Args:
            last_updated: Timestamp when entry was last updated.
            ttl: Time-to-live in seconds.

        Returns:
            True if expired, False otherwise.
        """
        return (time.time() - last_updated) > ttl

    # Project cache methods
    def get_project(self, project_key: str) -> ProjectCache | None:
        """Get cached project data.

        Args:
            project_key: Project key.

        Returns:
            Project cache or None if not found/expired.
        """
        cache = self.data.projects.get(project_key)
        if cache and not self.is_expired(cache.last_updated):
            return cache
        return None

    def set_project(self, project_key: str, cache: ProjectCache) -> None:
        """Set cached project data.

        Args:
            project_key: Project key.
            cache: Project cache data.
        """
        cache.last_updated = time.time()
        self.data.projects[project_key] = cache
        self.save()

    def get_project_id(self, project_key: str) -> int | None:
        """Get project ID from cache.

        Args:
            project_key: Project key.

        Returns:
            Project ID or None if not found.
        """
        cache = self.get_project(project_key)
        return cache.id if cache else None

    # Priority cache methods
    def get_priorities(self) -> dict[str, int]:
        """Get cached priorities.

        Returns:
            Priority name -> ID mapping, or empty dict if expired.
        """
        if self.is_expired(self.data.last_updated):
            return {}
        return self.data.priorities

    def set_priorities(self, priorities: dict[str, int]) -> None:
        """Set cached priorities.

        Args:
            priorities: Priority name -> ID mapping.
        """
        self.data.priorities = priorities
        self.data.last_updated = time.time()
        self.save()

    # Global user cache methods
    def get_global_users(self) -> dict[str, int]:
        """Get cached global users.

        Returns:
            User ID -> numeric ID mapping, or empty dict if expired.
        """
        if self.is_expired(self.data.last_updated):
            return {}
        return self.data.global_users

    def set_global_users(self, users: dict[str, int]) -> None:
        """Set cached global users.

        Args:
            users: User ID -> numeric ID mapping.
        """
        self.data.global_users = users
        self.data.last_updated = time.time()
        self.save()

    # Issue type cache methods
    def get_issue_types(self, project_key: str) -> dict[str, int]:
        """Get cached issue types for a project.

        Args:
            project_key: Project key.

        Returns:
            Issue type name -> ID mapping, or empty dict if not found.
        """
        cache = self.get_project(project_key)
        return cache.issue_types if cache else {}

    def set_issue_types(
        self, project_key: str, project_id: int, issue_types: dict[str, int]
    ) -> None:
        """Set cached issue types for a project.

        Args:
            project_key: Project key.
            project_id: Project ID.
            issue_types: Issue type name -> ID mapping.
        """
        cache = self.get_project(project_key) or ProjectCache(id=project_id)
        cache.issue_types = issue_types
        self.set_project(project_key, cache)

    # Status cache methods
    def get_statuses(self, project_key: str) -> dict[str, int]:
        """Get cached statuses for a project.

        Args:
            project_key: Project key.

        Returns:
            Status name -> ID mapping, or empty dict if not found.
        """
        cache = self.get_project(project_key)
        return cache.statuses if cache else {}

    def set_statuses(
        self, project_key: str, project_id: int, statuses: dict[str, int]
    ) -> None:
        """Set cached statuses for a project.

        Args:
            project_key: Project key.
            project_id: Project ID.
            statuses: Status name -> ID mapping.
        """
        cache = self.get_project(project_key) or ProjectCache(id=project_id)
        cache.statuses = statuses
        self.set_project(project_key, cache)
