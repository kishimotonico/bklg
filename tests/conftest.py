"""Shared fixtures for bacli-py tests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from bacli_py.config.settings import Settings
from bacli_py.resolver.cache import ResolverCache


@pytest.fixture
def tmp_config_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Create temporary config directory and patch get_config_dir."""
    config_dir = tmp_path / ".config" / "bacli"
    config_dir.mkdir(parents=True)

    def mock_get_config_dir() -> Path:
        return config_dir

    monkeypatch.setattr("bacli_py.config.settings.get_config_dir", mock_get_config_dir)
    return config_dir


@pytest.fixture
def tmp_cache_dir(tmp_path: Path) -> Path:
    """Create temporary cache directory."""
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir(parents=True)
    return cache_dir


@pytest.fixture
def mock_settings() -> Settings:
    """Create test settings."""
    return Settings(
        space_url="https://test.backlog.com",
        api_key="test-api-key-12345",
    )


@pytest.fixture
def mock_cache(tmp_cache_dir: Path) -> ResolverCache:
    """Create test cache with temporary file."""
    cache_file = tmp_cache_dir / "metadata.json"
    return ResolverCache(cache_file=cache_file)


# Sample API response fixtures


@pytest.fixture
def sample_project() -> dict[str, Any]:
    """Sample project data."""
    return {
        "id": 1,
        "projectKey": "TEST",
        "name": "Test Project",
        "chartEnabled": False,
        "useResolvedForChart": False,
        "subtaskingEnabled": True,
        "projectLeaderCanEditProjectLeader": False,
        "useWiki": True,
        "useFileSharing": True,
        "useWikiTreeView": False,
        "useSubversion": False,
        "useGit": True,
        "useOriginalImageSizeAtWiki": False,
        "textFormattingRule": "markdown",
        "archived": False,
        "displayOrder": 0,
        "useDevAttributes": False,
    }


@pytest.fixture
def sample_projects(sample_project: dict[str, Any]) -> list[dict[str, Any]]:
    """Sample projects list."""
    return [
        sample_project,
        {
            **sample_project,
            "id": 2,
            "projectKey": "PROJ2",
            "name": "Second Project",
        },
    ]


@pytest.fixture
def sample_user() -> dict[str, Any]:
    """Sample user data."""
    return {
        "id": 1,
        "userId": "test_user",
        "name": "Test User",
        "roleType": 1,
        "lang": "ja",
        "mailAddress": "test@example.com",
        "nulabAccount": None,
        "keyword": None,
        "lastLoginTime": "2024-01-01T00:00:00Z",
    }


@pytest.fixture
def sample_users(sample_user: dict[str, Any]) -> list[dict[str, Any]]:
    """Sample users list."""
    return [
        sample_user,
        {
            **sample_user,
            "id": 2,
            "userId": "another_user",
            "name": "Another User",
        },
    ]


@pytest.fixture
def sample_issue_type() -> dict[str, Any]:
    """Sample issue type data."""
    return {
        "id": 1,
        "projectId": 1,
        "name": "Task",
        "color": "#7ea800",
        "displayOrder": 0,
    }


@pytest.fixture
def sample_issue_types(sample_issue_type: dict[str, Any]) -> list[dict[str, Any]]:
    """Sample issue types list."""
    return [
        sample_issue_type,
        {
            **sample_issue_type,
            "id": 2,
            "name": "Bug",
            "color": "#e30000",
            "displayOrder": 1,
        },
    ]


@pytest.fixture
def sample_priority() -> dict[str, Any]:
    """Sample priority data."""
    return {"id": 3, "name": "Normal"}


@pytest.fixture
def sample_priorities() -> list[dict[str, Any]]:
    """Sample priorities list."""
    return [
        {"id": 2, "name": "High"},
        {"id": 3, "name": "Normal"},
        {"id": 4, "name": "Low"},
    ]


@pytest.fixture
def sample_status() -> dict[str, Any]:
    """Sample status data."""
    return {
        "id": 1,
        "projectId": 1,
        "name": "Open",
        "color": "#ed8077",
        "displayOrder": 0,
    }


@pytest.fixture
def sample_statuses(sample_status: dict[str, Any]) -> list[dict[str, Any]]:
    """Sample statuses list."""
    return [
        sample_status,
        {
            **sample_status,
            "id": 2,
            "name": "In Progress",
            "color": "#4488c5",
            "displayOrder": 1,
        },
        {
            **sample_status,
            "id": 3,
            "name": "Done",
            "color": "#5eb5a6",
            "displayOrder": 2,
        },
    ]


@pytest.fixture
def sample_issue(
    sample_issue_type: dict[str, Any],
    sample_priority: dict[str, Any],
    sample_status: dict[str, Any],
    sample_user: dict[str, Any],
) -> dict[str, Any]:
    """Sample issue data."""
    return {
        "id": 100,
        "projectId": 1,
        "issueKey": "TEST-1",
        "keyId": 1,
        "issueType": sample_issue_type,
        "summary": "Test Issue",
        "description": "This is a test issue.\n\n## Details\n- Item 1\n- Item 2",
        "resolution": None,
        "priority": sample_priority,
        "status": sample_status,
        "assignee": sample_user,
        "category": [],
        "versions": [],
        "milestone": [],
        "startDate": None,
        "dueDate": "2024-12-31T00:00:00Z",
        "estimatedHours": 8.0,
        "actualHours": 4.0,
        "parentIssueId": None,
        "createdUser": sample_user,
        "created": "2024-01-01T00:00:00Z",
        "updatedUser": sample_user,
        "updated": "2024-01-15T00:00:00Z",
        "customFields": [],
        "attachments": [],
        "sharedFiles": [],
        "stars": [],
    }


@pytest.fixture
def sample_issues(sample_issue: dict[str, Any]) -> list[dict[str, Any]]:
    """Sample issues list."""
    return [
        sample_issue,
        {
            **sample_issue,
            "id": 101,
            "issueKey": "TEST-2",
            "keyId": 2,
            "summary": "Another Test Issue",
        },
    ]


@pytest.fixture
def sample_comment(sample_user: dict[str, Any]) -> dict[str, Any]:
    """Sample comment data."""
    return {
        "id": 1,
        "content": "This is a test comment.",
        "changeLog": [],
        "createdUser": sample_user,
        "created": "2024-01-02T00:00:00Z",
        "updated": "2024-01-02T00:00:00Z",
        "stars": [],
        "notifications": [],
    }


@pytest.fixture
def sample_api_error() -> dict[str, Any]:
    """Sample API error response."""
    return {
        "errors": [
            {
                "message": "Authentication failure.",
                "code": 11,
                "moreInfo": "",
            }
        ]
    }


# Helper to write JSON fixtures to files


@pytest.fixture
def write_fixture(tmp_path: Path):
    """Helper to write fixture data to JSON file."""

    def _write(filename: str, data: Any) -> Path:
        filepath = tmp_path / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with filepath.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return filepath

    return _write
