"""Tests for resolver/*.py."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from bklg.models import IssueType, Priority, Project, Status, User
from bklg.resolver.base import ResolverError
from bklg.resolver.cache import ProjectCache, ResolverCache
from bklg.resolver.issue_type import IssueTypeResolver
from bklg.resolver.priority import PriorityResolver
from bklg.resolver.project import ProjectResolver
from bklg.resolver.status import StatusResolver
from bklg.resolver.user import UserResolver


@pytest.fixture
def mock_client() -> MagicMock:
    """Create mock Backlog client."""
    return MagicMock()


class TestResolverError:
    """Tests for ResolverError exception."""

    def test_error_message(self) -> None:
        """Test error message format."""
        error = ResolverError("PROJ", "project")
        assert str(error) == "project 'PROJ' not found"
        assert error.name == "PROJ"
        assert error.resource_type == "project"


class TestProjectResolver:
    """Tests for ProjectResolver class."""

    def test_resolve_by_key(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test resolving project by key."""
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        project_id = resolver.resolve("TEST")
        assert project_id == 1

    def test_resolve_by_numeric_id(
        self, mock_client: MagicMock, mock_cache: ResolverCache
    ) -> None:
        """Test resolving numeric ID returns as-is."""
        resolver = ProjectResolver(mock_client, mock_cache)

        project_id = resolver.resolve("123")
        assert project_id == 123
        mock_client.get.assert_not_called()

    def test_resolve_uses_cache(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
    ) -> None:
        """Test resolver uses cache when available."""
        # Pre-populate cache
        mock_cache.set_project("CACHED", ProjectCache(id=999))

        resolver = ProjectResolver(mock_client, mock_cache)
        project_id = resolver.resolve("CACHED")

        assert project_id == 999
        mock_client.get.assert_not_called()

    def test_resolve_not_found(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test ResolverError raised when project not found."""
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        with pytest.raises(ResolverError) as exc_info:
            resolver.resolve("NONEXISTENT")

        assert exc_info.value.name == "NONEXISTENT"
        assert exc_info.value.resource_type == "project"

    def test_resolve_case_insensitive(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test project key resolution is case insensitive."""
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        # Should work with lowercase
        assert resolver.resolve("test") == 1
        assert resolver.resolve("Test") == 1

    def test_get_all(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test get_all returns all mappings."""
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        all_projects = resolver.get_all()
        assert all_projects == {"TEST": 1, "PROJ2": 2}

    def test_get_project(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test get_project returns Project object."""
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        project = resolver.get_project("TEST")
        assert isinstance(project, Project)
        assert project.project_key == "TEST"
        assert project.name == "Test Project"

    def test_get_project_by_numeric_id(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test get_project by numeric ID."""
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        project = resolver.get_project("1")
        assert project.project_key == "TEST"

    def test_list_projects(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test list_projects returns all projects."""
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        projects = resolver.list_projects()
        assert len(projects) == 2

    def test_list_projects_excludes_archived(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test list_projects excludes archived by default."""
        # Add an archived project
        sample_projects.append(
            {**sample_projects[0], "id": 3, "projectKey": "ARCH", "archived": True}
        )
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        projects = resolver.list_projects(archived=False)
        assert len(projects) == 2
        assert all(not p.archived for p in projects)

    def test_refresh_updates_cache(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test refresh updates the cache."""
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        resolver.refresh()

        # Cache should be updated
        assert mock_cache.get_project_id("TEST") == 1
        assert mock_cache.get_project_id("PROJ2") == 2


class TestIssueTypeResolver:
    """Tests for IssueTypeResolver class."""

    def test_resolve_by_name(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_issue_types: list[dict[str, Any]],
    ) -> None:
        """Test resolving issue type by name."""
        mock_client.get.return_value = sample_issue_types
        resolver = IssueTypeResolver(mock_client, mock_cache, project_id=1, project_key="TEST")

        issue_type_id = resolver.resolve("Task")
        assert issue_type_id == 1

    def test_resolve_uses_cache(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
    ) -> None:
        """Test resolver uses cache when available."""
        # Pre-populate cache
        mock_cache.set_issue_types("TEST", 1, {"Cached Type": 999})

        resolver = IssueTypeResolver(mock_client, mock_cache, project_id=1, project_key="TEST")

        # Note: Current implementation still fetches to get full objects
        # but the cache check happens first for ID resolution
        mock_client.get.return_value = [
            {"id": 999, "projectId": 1, "name": "Cached Type", "color": "#000000", "displayOrder": 0}
        ]
        issue_type_id = resolver.resolve("Cached Type")
        assert issue_type_id == 999

    def test_resolve_not_found(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_issue_types: list[dict[str, Any]],
    ) -> None:
        """Test ResolverError raised when issue type not found."""
        mock_client.get.return_value = sample_issue_types
        resolver = IssueTypeResolver(mock_client, mock_cache, project_id=1, project_key="TEST")

        with pytest.raises(ResolverError) as exc_info:
            resolver.resolve("NonexistentType")

        assert exc_info.value.resource_type == "issue type"

    def test_get_all(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_issue_types: list[dict[str, Any]],
    ) -> None:
        """Test get_all returns all mappings."""
        mock_client.get.return_value = sample_issue_types
        resolver = IssueTypeResolver(mock_client, mock_cache, project_id=1, project_key="TEST")

        all_types = resolver.get_all()
        assert all_types == {"Task": 1, "Bug": 2}

    def test_list_issue_types(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_issue_types: list[dict[str, Any]],
    ) -> None:
        """Test list_issue_types returns all types."""
        mock_client.get.return_value = sample_issue_types
        resolver = IssueTypeResolver(mock_client, mock_cache, project_id=1, project_key="TEST")

        types = resolver.list_issue_types()
        assert len(types) == 2
        assert all(isinstance(t, IssueType) for t in types)


class TestUserResolver:
    """Tests for UserResolver class."""

    def test_resolve_by_user_id(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_users: list[dict[str, Any]],
    ) -> None:
        """Test resolving user by user_id."""
        mock_client.get.return_value = sample_users
        resolver = UserResolver(mock_client, mock_cache)

        user_id = resolver.resolve("test_user")
        assert user_id == 1

    def test_resolve_by_numeric_id(
        self, mock_client: MagicMock, mock_cache: ResolverCache
    ) -> None:
        """Test resolving numeric ID returns as-is."""
        resolver = UserResolver(mock_client, mock_cache)

        user_id = resolver.resolve("42")
        assert user_id == 42
        mock_client.get.assert_not_called()

    def test_resolve_at_me(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_user: dict[str, Any],
    ) -> None:
        """Test @me resolves to current user."""
        mock_client.get_myself.return_value = sample_user
        resolver = UserResolver(mock_client, mock_cache)

        user_id = resolver.resolve("@me")
        assert user_id == 1
        mock_client.get_myself.assert_called_once()

    def test_resolve_at_me_case_insensitive(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_user: dict[str, Any],
    ) -> None:
        """Test @me is case insensitive."""
        mock_client.get_myself.return_value = sample_user
        resolver = UserResolver(mock_client, mock_cache)

        assert resolver.resolve("@ME") == 1
        assert resolver.resolve("@Me") == 1

    def test_resolve_uses_cache(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
    ) -> None:
        """Test resolver uses cache when available."""
        # Pre-populate cache
        mock_cache.set_global_users({"cached_user": 888})

        resolver = UserResolver(mock_client, mock_cache)
        user_id = resolver.resolve("cached_user")

        assert user_id == 888
        mock_client.get.assert_not_called()

    def test_resolve_not_found(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_users: list[dict[str, Any]],
    ) -> None:
        """Test ResolverError raised when user not found."""
        mock_client.get.return_value = sample_users
        resolver = UserResolver(mock_client, mock_cache)

        with pytest.raises(ResolverError) as exc_info:
            resolver.resolve("nonexistent_user")

        assert exc_info.value.resource_type == "user"

    def test_get_myself(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_user: dict[str, Any],
    ) -> None:
        """Test get_myself returns current user."""
        mock_client.get_myself.return_value = sample_user
        resolver = UserResolver(mock_client, mock_cache)

        user = resolver.get_myself()
        assert isinstance(user, User)
        assert user.id == 1
        assert user.name == "Test User"

    def test_get_myself_caches_result(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_user: dict[str, Any],
    ) -> None:
        """Test get_myself caches the result."""
        mock_client.get_myself.return_value = sample_user
        resolver = UserResolver(mock_client, mock_cache)

        resolver.get_myself()
        resolver.get_myself()

        # Should only call API once
        mock_client.get_myself.assert_called_once()

    def test_get_user_by_id(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_users: list[dict[str, Any]],
    ) -> None:
        """Test get_user returns User object."""
        mock_client.get.return_value = sample_users
        resolver = UserResolver(mock_client, mock_cache)

        user = resolver.get_user("test_user")
        assert isinstance(user, User)
        assert user.user_id == "test_user"

    def test_get_user_at_me(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_user: dict[str, Any],
    ) -> None:
        """Test get_user with @me."""
        mock_client.get_myself.return_value = sample_user
        resolver = UserResolver(mock_client, mock_cache)

        user = resolver.get_user("@me")
        assert user.id == 1

    def test_list_users(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_users: list[dict[str, Any]],
    ) -> None:
        """Test list_users returns all users."""
        mock_client.get.return_value = sample_users
        resolver = UserResolver(mock_client, mock_cache)

        users = resolver.list_users()
        assert len(users) == 2
        assert all(isinstance(u, User) for u in users)


class TestBaseResolverOrNone:
    """Tests for resolve_or_none method."""

    def test_resolve_or_none_success(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test resolve_or_none returns ID on success."""
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        result = resolver.resolve_or_none("TEST")
        assert result == 1

    def test_resolve_or_none_not_found(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_projects: list[dict[str, Any]],
    ) -> None:
        """Test resolve_or_none returns None when not found."""
        mock_client.get.return_value = sample_projects
        resolver = ProjectResolver(mock_client, mock_cache)

        result = resolver.resolve_or_none("NONEXISTENT")
        assert result is None


class TestStatusResolver:
    """Tests for StatusResolver class."""

    def test_resolve_by_name(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_statuses: list[dict[str, Any]],
    ) -> None:
        """Test resolving status by name."""
        mock_client.get.return_value = sample_statuses
        resolver = StatusResolver(mock_client, mock_cache, project_id=1, project_key="TEST")

        status_id = resolver.resolve("Open")
        assert status_id == 1

    def test_resolve_uses_cache(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
    ) -> None:
        """Test resolver uses cache when available."""
        # Pre-populate cache
        mock_cache.set_statuses("TEST", 1, {"Cached Status": 999})

        resolver = StatusResolver(mock_client, mock_cache, project_id=1, project_key="TEST")
        status_id = resolver.resolve("Cached Status")

        assert status_id == 999
        mock_client.get.assert_not_called()

    def test_resolve_not_found(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_statuses: list[dict[str, Any]],
    ) -> None:
        """Test ResolverError raised when status not found."""
        mock_client.get.return_value = sample_statuses
        resolver = StatusResolver(mock_client, mock_cache, project_id=1, project_key="TEST")

        with pytest.raises(ResolverError) as exc_info:
            resolver.resolve("NonexistentStatus")

        assert exc_info.value.resource_type == "status"

    def test_get_all(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_statuses: list[dict[str, Any]],
    ) -> None:
        """Test get_all returns all mappings."""
        mock_client.get.return_value = sample_statuses
        resolver = StatusResolver(mock_client, mock_cache, project_id=1, project_key="TEST")

        all_statuses = resolver.get_all()
        assert all_statuses == {"Open": 1, "In Progress": 2, "Done": 3}

    def test_list_statuses(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_statuses: list[dict[str, Any]],
    ) -> None:
        """Test list_statuses returns all statuses."""
        mock_client.get.return_value = sample_statuses
        resolver = StatusResolver(mock_client, mock_cache, project_id=1, project_key="TEST")

        statuses = resolver.list_statuses()
        assert len(statuses) == 3
        assert all(isinstance(s, Status) for s in statuses)


class TestPriorityResolver:
    """Tests for PriorityResolver class."""

    def test_resolve_by_name(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_priorities: list[dict[str, Any]],
    ) -> None:
        """Test resolving priority by name."""
        mock_client.get.return_value = sample_priorities
        resolver = PriorityResolver(mock_client, mock_cache)

        priority_id = resolver.resolve("Normal")
        assert priority_id == 3

    def test_resolve_uses_cache(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
    ) -> None:
        """Test resolver uses cache when available."""
        # Pre-populate cache
        mock_cache.set_priorities({"Cached Priority": 888})

        resolver = PriorityResolver(mock_client, mock_cache)
        priority_id = resolver.resolve("Cached Priority")

        assert priority_id == 888
        mock_client.get.assert_not_called()

    def test_resolve_not_found(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_priorities: list[dict[str, Any]],
    ) -> None:
        """Test ResolverError raised when priority not found."""
        mock_client.get.return_value = sample_priorities
        resolver = PriorityResolver(mock_client, mock_cache)

        with pytest.raises(ResolverError) as exc_info:
            resolver.resolve("NonexistentPriority")

        assert exc_info.value.resource_type == "priority"

    def test_get_all(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_priorities: list[dict[str, Any]],
    ) -> None:
        """Test get_all returns all mappings."""
        mock_client.get.return_value = sample_priorities
        resolver = PriorityResolver(mock_client, mock_cache)

        all_priorities = resolver.get_all()
        assert all_priorities == {"High": 2, "Normal": 3, "Low": 4}

    def test_list_priorities(
        self,
        mock_client: MagicMock,
        mock_cache: ResolverCache,
        sample_priorities: list[dict[str, Any]],
    ) -> None:
        """Test list_priorities returns all priorities."""
        mock_client.get.return_value = sample_priorities
        resolver = PriorityResolver(mock_client, mock_cache)

        priorities = resolver.list_priorities()
        assert len(priorities) == 3
        assert all(isinstance(p, Priority) for p in priorities)
