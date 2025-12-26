"""Tests for resolver/cache.py."""

from __future__ import annotations

import time
from pathlib import Path

import pytest

from bacli_py.resolver.cache import (
    CACHE_TTL_SECONDS,
    CacheData,
    ProjectCache,
    ResolverCache,
)


class TestProjectCache:
    """Tests for ProjectCache model."""

    def test_default_values(self) -> None:
        """Test default values."""
        cache = ProjectCache(id=1)
        assert cache.id == 1
        assert cache.issue_types == {}
        assert cache.statuses == {}
        assert cache.categories == {}
        assert cache.versions == {}
        assert cache.users == {}
        assert cache.last_updated > 0

    def test_with_data(self) -> None:
        """Test with populated data."""
        cache = ProjectCache(
            id=1,
            issue_types={"Task": 1, "Bug": 2},
            statuses={"Open": 1, "Done": 2},
        )
        assert cache.issue_types == {"Task": 1, "Bug": 2}
        assert cache.statuses == {"Open": 1, "Done": 2}


class TestCacheData:
    """Tests for CacheData model."""

    def test_default_values(self) -> None:
        """Test default values."""
        data = CacheData()
        assert data.projects == {}
        assert data.priorities == {}
        assert data.global_users == {}
        assert data.last_updated > 0


class TestResolverCache:
    """Tests for ResolverCache class."""

    def test_init_creates_cache_file_path(self, tmp_cache_dir: Path) -> None:
        """Test initialization sets cache file path."""
        cache_file = tmp_cache_dir / "test_cache.json"
        cache = ResolverCache(cache_file=cache_file)
        assert cache.cache_file == cache_file

    def test_load_empty_cache(self, mock_cache: ResolverCache) -> None:
        """Test loading from non-existent file returns empty cache."""
        data = mock_cache.data
        assert data.projects == {}
        assert data.priorities == {}

    def test_save_and_load(self, mock_cache: ResolverCache) -> None:
        """Test saving and loading cache data."""
        mock_cache.set_priorities({"High": 1, "Normal": 2, "Low": 3})
        mock_cache.save()

        # Create new cache instance to load from file
        new_cache = ResolverCache(cache_file=mock_cache.cache_file)
        priorities = new_cache.get_priorities()
        assert priorities == {"High": 1, "Normal": 2, "Low": 3}

    def test_clear(self, mock_cache: ResolverCache) -> None:
        """Test clearing cache."""
        mock_cache.set_priorities({"High": 1})
        mock_cache.save()
        assert mock_cache.cache_file.exists()

        mock_cache.clear()
        assert not mock_cache.cache_file.exists()
        assert mock_cache.data.priorities == {}

    def test_is_expired_false(self, mock_cache: ResolverCache) -> None:
        """Test is_expired returns False for fresh data."""
        current_time = time.time()
        assert mock_cache.is_expired(current_time) is False

    def test_is_expired_true(self, mock_cache: ResolverCache) -> None:
        """Test is_expired returns True for old data."""
        old_time = time.time() - CACHE_TTL_SECONDS - 1
        assert mock_cache.is_expired(old_time) is True

    def test_is_expired_custom_ttl(self, mock_cache: ResolverCache) -> None:
        """Test is_expired with custom TTL."""
        recent_time = time.time() - 10
        assert mock_cache.is_expired(recent_time, ttl=5) is True
        assert mock_cache.is_expired(recent_time, ttl=20) is False


class TestResolverCacheProjectMethods:
    """Tests for project-related cache methods."""

    def test_get_project_none_when_not_exists(
        self, mock_cache: ResolverCache
    ) -> None:
        """Test get_project returns None for non-existent project."""
        result = mock_cache.get_project("NONEXISTENT")
        assert result is None

    def test_set_and_get_project(self, mock_cache: ResolverCache) -> None:
        """Test setting and getting project cache."""
        project_cache = ProjectCache(
            id=1,
            issue_types={"Task": 1},
            statuses={"Open": 1},
        )
        mock_cache.set_project("TEST", project_cache)

        result = mock_cache.get_project("TEST")
        assert result is not None
        assert result.id == 1
        assert result.issue_types == {"Task": 1}

    def test_get_project_id(self, mock_cache: ResolverCache) -> None:
        """Test get_project_id method."""
        project_cache = ProjectCache(id=42)
        mock_cache.set_project("TEST", project_cache)

        assert mock_cache.get_project_id("TEST") == 42
        assert mock_cache.get_project_id("NONEXISTENT") is None

    def test_get_project_returns_none_when_expired(
        self, mock_cache: ResolverCache
    ) -> None:
        """Test get_project returns None for expired cache."""
        project_cache = ProjectCache(id=1)
        project_cache.last_updated = time.time() - CACHE_TTL_SECONDS - 1
        mock_cache.data.projects["TEST"] = project_cache

        result = mock_cache.get_project("TEST")
        assert result is None


class TestResolverCachePriorityMethods:
    """Tests for priority-related cache methods."""

    def test_get_priorities_empty_when_not_set(
        self, mock_cache: ResolverCache
    ) -> None:
        """Test get_priorities returns empty dict when not set."""
        result = mock_cache.get_priorities()
        assert result == {}

    def test_set_and_get_priorities(self, mock_cache: ResolverCache) -> None:
        """Test setting and getting priorities."""
        priorities = {"High": 1, "Normal": 2, "Low": 3}
        mock_cache.set_priorities(priorities)

        result = mock_cache.get_priorities()
        assert result == priorities

    def test_get_priorities_empty_when_expired(
        self, mock_cache: ResolverCache
    ) -> None:
        """Test get_priorities returns empty dict when expired."""
        mock_cache.set_priorities({"High": 1})
        mock_cache.data.last_updated = time.time() - CACHE_TTL_SECONDS - 1

        result = mock_cache.get_priorities()
        assert result == {}


class TestResolverCacheIssueTypeMethods:
    """Tests for issue type cache methods."""

    def test_get_issue_types_empty_when_not_set(
        self, mock_cache: ResolverCache
    ) -> None:
        """Test get_issue_types returns empty dict."""
        result = mock_cache.get_issue_types("TEST")
        assert result == {}

    def test_set_and_get_issue_types(self, mock_cache: ResolverCache) -> None:
        """Test setting and getting issue types."""
        issue_types = {"Task": 1, "Bug": 2}
        mock_cache.set_issue_types("TEST", 1, issue_types)

        result = mock_cache.get_issue_types("TEST")
        assert result == issue_types

    def test_set_issue_types_creates_project_cache(
        self, mock_cache: ResolverCache
    ) -> None:
        """Test set_issue_types creates project cache if not exists."""
        mock_cache.set_issue_types("NEW_PROJECT", 99, {"Task": 1})

        project_cache = mock_cache.get_project("NEW_PROJECT")
        assert project_cache is not None
        assert project_cache.id == 99
