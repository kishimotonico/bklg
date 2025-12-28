"""Tests for models/*.py."""

from __future__ import annotations

from typing import Any

import pytest

from bklg.models.attachment import Attachment, UploadedFile
from bklg.models.common import (
    BacklogError,
    BacklogErrorResponse,
    ErrorCode,
    RateLimitInfo,
)
from bklg.models.issue import Comment, Issue, IssueUser
from bklg.models.notification import Notification, NotificationCount
from bklg.models.project import IssueType, Priority, Project, Status
from bklg.models.space import DiskUsage, Space, SpaceNotification
from bklg.models.user import User
from bklg.models.watch import Watching, WatchingCount
from bklg.models.wiki import Wiki, WikiTag


class TestBacklogError:
    """Tests for BacklogError model."""

    def test_basic_error(self) -> None:
        """Test basic error creation."""
        error = BacklogError(message="Test error", code=7)
        assert error.message == "Test error"
        assert error.code == 7
        assert error.more_info == ""

    def test_error_with_more_info(self) -> None:
        """Test error with moreInfo alias."""
        data = {"message": "Error", "code": 7, "moreInfo": "Additional details"}
        error = BacklogError.model_validate(data)
        assert error.more_info == "Additional details"


class TestBacklogErrorResponse:
    """Tests for BacklogErrorResponse model."""

    def test_empty_errors(self) -> None:
        """Test empty errors list."""
        response = BacklogErrorResponse()
        assert response.errors == []
        assert response.first_error is None
        assert response.message == ""

    def test_with_errors(self, sample_api_error: dict[str, Any]) -> None:
        """Test with error data."""
        response = BacklogErrorResponse.model_validate(sample_api_error)
        assert len(response.errors) == 1
        assert response.first_error is not None
        assert response.first_error.code == ErrorCode.AUTHENTICATION_ERROR
        assert "Authentication" in response.message


class TestRateLimitInfo:
    """Tests for RateLimitInfo model."""

    def test_from_headers(self) -> None:
        """Test creating from response headers."""
        headers = {
            "X-RateLimit-Limit": "100",
            "X-RateLimit-Remaining": "50",
            "X-RateLimit-Reset": "1700000000",
        }
        info = RateLimitInfo.from_headers(headers)
        assert info is not None
        assert info.limit == 100
        assert info.remaining == 50
        assert info.reset == 1700000000

    def test_from_headers_invalid(self) -> None:
        """Test with invalid headers."""
        headers = {"X-RateLimit-Limit": "invalid"}
        info = RateLimitInfo.from_headers(headers)
        assert info is None

    def test_is_exhausted(self) -> None:
        """Test is_exhausted property."""
        info = RateLimitInfo(limit=100, remaining=0, reset=0)
        assert info.is_exhausted is True

        info = RateLimitInfo(limit=100, remaining=50, reset=0)
        assert info.is_exhausted is False


class TestProject:
    """Tests for Project model."""

    def test_from_api_response(self, sample_project: dict[str, Any]) -> None:
        """Test creating from API response."""
        project = Project.model_validate(sample_project)
        assert project.id == 1
        assert project.project_key == "TEST"
        assert project.name == "Test Project"
        assert project.archived is False
        assert project.text_formatting_rule == "markdown"

    def test_alias_mapping(self) -> None:
        """Test camelCase to snake_case mapping."""
        data = {
            "id": 1,
            "projectKey": "TEST",
            "name": "Test",
            "chartEnabled": True,
            "subtaskingEnabled": True,
            "textFormattingRule": "backlog",
        }
        project = Project.model_validate(data)
        assert project.project_key == "TEST"
        assert project.chart_enabled is True
        assert project.subtasking_enabled is True
        assert project.text_formatting_rule == "backlog"


class TestUser:
    """Tests for User model."""

    def test_from_api_response(self, sample_user: dict[str, Any]) -> None:
        """Test creating from API response."""
        user = User.model_validate(sample_user)
        assert user.id == 1
        assert user.user_id == "test_user"
        assert user.name == "Test User"
        assert user.mail_address == "test@example.com"


class TestIssueType:
    """Tests for IssueType model."""

    def test_from_api_response(self, sample_issue_type: dict[str, Any]) -> None:
        """Test creating from API response."""
        issue_type = IssueType.model_validate(sample_issue_type)
        assert issue_type.id == 1
        assert issue_type.project_id == 1
        assert issue_type.name == "Task"
        assert issue_type.color == "#7ea800"


class TestPriority:
    """Tests for Priority model."""

    def test_from_api_response(self, sample_priority: dict[str, Any]) -> None:
        """Test creating from API response."""
        priority = Priority.model_validate(sample_priority)
        assert priority.id == 3
        assert priority.name == "Normal"


class TestStatus:
    """Tests for Status model."""

    def test_from_api_response(self, sample_status: dict[str, Any]) -> None:
        """Test creating from API response."""
        status = Status.model_validate(sample_status)
        assert status.id == 1
        assert status.project_id == 1
        assert status.name == "Open"
        assert status.color == "#ed8077"


class TestIssue:
    """Tests for Issue model."""

    def test_from_api_response(self, sample_issue: dict[str, Any]) -> None:
        """Test creating from API response."""
        issue = Issue.model_validate(sample_issue)
        assert issue.id == 100
        assert issue.project_id == 1
        assert issue.issue_key == "TEST-1"
        assert issue.summary == "Test Issue"
        assert issue.issue_type.name == "Task"
        assert issue.priority.name == "Normal"
        assert issue.status.name == "Open"
        assert issue.assignee is not None
        assert issue.assignee.name == "Test User"

    def test_optional_assignee(self, sample_issue: dict[str, Any]) -> None:
        """Test issue with no assignee."""
        sample_issue["assignee"] = None
        issue = Issue.model_validate(sample_issue)
        assert issue.assignee is None

    def test_url_property(self, sample_issue: dict[str, Any]) -> None:
        """Test url property."""
        issue = Issue.model_validate(sample_issue)
        assert issue.url == "view/TEST-1"


class TestIssueUser:
    """Tests for IssueUser model."""

    def test_nullable_user_id(self) -> None:
        """Test IssueUser with null userId."""
        data = {
            "id": 1,
            "userId": None,
            "name": "Test User",
            "roleType": 1,
        }
        user = IssueUser.model_validate(data)
        assert user.id == 1
        assert user.user_id is None
        assert user.name == "Test User"


class TestComment:
    """Tests for Comment model."""

    def test_from_api_response(self, sample_comment: dict[str, Any]) -> None:
        """Test creating from API response."""
        comment = Comment.model_validate(sample_comment)
        assert comment.id == 1
        assert comment.content == "This is a test comment."
        assert comment.created_user.name == "Test User"

    def test_empty_content(self, sample_comment: dict[str, Any]) -> None:
        """Test comment with no content."""
        sample_comment["content"] = None
        comment = Comment.model_validate(sample_comment)
        assert comment.content is None


class TestSpace:
    """Tests for Space model."""

    def test_from_api_response(self, sample_space: dict[str, Any]) -> None:
        """Test creating from API response."""
        space = Space.model_validate(sample_space)
        assert space.space_key == "demo"
        assert space.name == "Demo Space"
        assert space.owner_id == 1
        assert space.lang == "ja"
        assert space.timezone == "Asia/Tokyo"
        assert space.text_formatting_rule == "markdown"


class TestDiskUsage:
    """Tests for DiskUsage model."""

    def test_from_api_response(self, sample_disk_usage: dict[str, Any]) -> None:
        """Test creating from API response."""
        disk = DiskUsage.model_validate(sample_disk_usage)
        assert disk.capacity == 1073741824
        assert disk.issue == 104857600
        assert disk.wiki == 52428800
        assert disk.git == 524288000
        assert disk.git_lfs == 209715200
        assert disk.pull_request == 10485760


class TestSpaceNotification:
    """Tests for SpaceNotification model."""

    def test_from_api_response(self, sample_space_notification: dict[str, Any]) -> None:
        """Test creating from API response."""
        notification = SpaceNotification.model_validate(sample_space_notification)
        assert notification.content == "This is a space announcement."
        assert notification.updated is not None

    def test_empty_notification(self) -> None:
        """Test empty notification."""
        notification = SpaceNotification.model_validate({})
        assert notification.content is None
        assert notification.updated is None


class TestWiki:
    """Tests for Wiki model."""

    def test_from_api_response(self, sample_wiki: dict[str, Any]) -> None:
        """Test creating from API response."""
        wiki = Wiki.model_validate(sample_wiki)
        assert wiki.id == 1
        assert wiki.project_id == 1
        assert wiki.name == "Test Wiki Page"
        assert wiki.content == "# Test\n\nThis is a test wiki page."
        assert len(wiki.tags) == 1
        assert wiki.created_user is not None
        assert wiki.created_user.name == "Test User"

    def test_minimal_wiki(self) -> None:
        """Test wiki with minimal data."""
        data = {"id": 1, "projectId": 1, "name": "Minimal"}
        wiki = Wiki.model_validate(data)
        assert wiki.id == 1
        assert wiki.content is None
        assert wiki.tags == []


class TestWikiTag:
    """Tests for WikiTag model."""

    def test_from_api_response(self) -> None:
        """Test creating from API response."""
        data = {"id": 1, "name": "documentation"}
        tag = WikiTag.model_validate(data)
        assert tag.id == 1
        assert tag.name == "documentation"


class TestNotification:
    """Tests for Notification model."""

    def test_from_api_response(self, sample_notification: dict[str, Any]) -> None:
        """Test creating from API response."""
        notification = Notification.model_validate(sample_notification)
        assert notification.id == 1
        assert notification.already_read is False
        assert notification.reason == 1
        assert notification.resource_already_read is False
        assert notification.project is not None
        assert notification.issue is not None
        assert notification.sender is not None
        assert notification.sender.name == "Test User"


class TestNotificationCount:
    """Tests for NotificationCount model."""

    def test_from_api_response(self) -> None:
        """Test creating from API response."""
        data = {"count": 5}
        count = NotificationCount.model_validate(data)
        assert count.count == 5


class TestWatching:
    """Tests for Watching model."""

    def test_from_api_response(self, sample_watching: dict[str, Any]) -> None:
        """Test creating from API response."""
        watching = Watching.model_validate(sample_watching)
        assert watching.id == 1
        assert watching.resource_already_read is True
        assert watching.note == "Important issue"
        assert watching.type == "issue"
        assert watching.issue is not None
        assert watching.last_content_updated is not None


class TestWatchingCount:
    """Tests for WatchingCount model."""

    def test_from_api_response(self) -> None:
        """Test creating from API response."""
        data = {"count": 10}
        count = WatchingCount.model_validate(data)
        assert count.count == 10


class TestAttachment:
    """Tests for Attachment model."""

    def test_from_api_response(self, sample_attachment: dict[str, Any]) -> None:
        """Test creating from API response."""
        attachment = Attachment.model_validate(sample_attachment)
        assert attachment.id == 1
        assert attachment.name == "test_file.pdf"
        assert attachment.size == 1048576
        assert attachment.created_user is not None
        assert attachment.created_user.name == "Test User"


class TestUploadedFile:
    """Tests for UploadedFile model."""

    def test_from_api_response(self, sample_uploaded_file: dict[str, Any]) -> None:
        """Test creating from API response."""
        uploaded = UploadedFile.model_validate(sample_uploaded_file)
        assert uploaded.id == 1
        assert uploaded.name == "uploaded_file.txt"
        assert uploaded.size == 2048
