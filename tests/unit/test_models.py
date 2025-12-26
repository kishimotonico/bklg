"""Tests for models/*.py."""

from __future__ import annotations

from typing import Any

import pytest

from bacli_py.models.common import (
    BacklogError,
    BacklogErrorResponse,
    ErrorCode,
    RateLimitInfo,
)
from bacli_py.models.issue import Comment, Issue, IssueUser
from bacli_py.models.project import IssueType, Priority, Project, Status
from bacli_py.models.user import User


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
