"""Tests for utils/formatter.py."""

from __future__ import annotations

from io import StringIO
from typing import Any
from unittest.mock import MagicMock

import pytest
from rich.console import Console

from bacli_py.models.issue import Comment, Issue
from bacli_py.utils.formatter import IssueFormatter


@pytest.fixture
def formatter() -> IssueFormatter:
    """Create a formatter with captured output."""
    console = Console(file=StringIO(), force_terminal=False, no_color=True)
    return IssueFormatter(console=console)


@pytest.fixture
def sample_issue_obj(sample_issue: dict[str, Any]) -> Issue:
    """Create Issue object from sample data."""
    return Issue.model_validate(sample_issue)


@pytest.fixture
def sample_issues_obj(sample_issues: list[dict[str, Any]]) -> list[Issue]:
    """Create Issue objects from sample data."""
    return [Issue.model_validate(i) for i in sample_issues]


@pytest.fixture
def sample_comment_obj(sample_comment: dict[str, Any]) -> Comment:
    """Create Comment object from sample data."""
    return Comment.model_validate(sample_comment)


class TestIssueFormatter:
    """Tests for IssueFormatter class."""

    def test_format_issue_table_basic(
        self,
        formatter: IssueFormatter,
        sample_issues_obj: list[Issue],
    ) -> None:
        """Test basic table formatting."""
        table = formatter.format_issue_table(sample_issues_obj)

        assert table.title == "Issues"
        assert len(table.columns) == 6
        assert table.row_count == 2

    def test_format_issue_table_with_title(
        self,
        formatter: IssueFormatter,
        sample_issues_obj: list[Issue],
    ) -> None:
        """Test table with custom title."""
        table = formatter.format_issue_table(sample_issues_obj, title="My Issues")
        assert table.title == "My Issues"

    def test_format_issue_table_empty(
        self,
        formatter: IssueFormatter,
    ) -> None:
        """Test table with no issues."""
        table = formatter.format_issue_table([])
        assert table.row_count == 0

    def test_format_issue_detail(
        self,
        formatter: IssueFormatter,
        sample_issue_obj: Issue,
    ) -> None:
        """Test detailed issue formatting."""
        formatter.format_issue_detail(sample_issue_obj)

        output = formatter.console.file.getvalue()
        assert "TEST-1" in output
        assert "Test Issue" in output

    def test_format_issue_detail_with_space_url(
        self,
        formatter: IssueFormatter,
        sample_issue_obj: Issue,
    ) -> None:
        """Test detailed issue with space URL."""
        formatter.format_issue_detail(sample_issue_obj, space_url="https://test.backlog.com")

        output = formatter.console.file.getvalue()
        assert "https://test.backlog.com/view/TEST-1" in output

    def test_format_comments(
        self,
        formatter: IssueFormatter,
        sample_comment_obj: Comment,
    ) -> None:
        """Test comment formatting."""
        formatter.format_comments([sample_comment_obj])

        output = formatter.console.file.getvalue()
        assert "Comments (1)" in output
        assert "This is a test comment." in output

    def test_format_comments_empty(
        self,
        formatter: IssueFormatter,
    ) -> None:
        """Test empty comments."""
        formatter.format_comments([])

        output = formatter.console.file.getvalue()
        assert "No comments" in output


class TestStatusStyle:
    """Tests for status style mapping."""

    def test_status_done(self, formatter: IssueFormatter) -> None:
        """Test done status style."""
        assert formatter._get_status_style("Done") == "green"
        assert formatter._get_status_style("完了") == "green"
        assert formatter._get_status_style("Closed") == "green"
        assert formatter._get_status_style("Resolved") == "green"

    def test_status_in_progress(self, formatter: IssueFormatter) -> None:
        """Test in progress status style."""
        assert formatter._get_status_style("In Progress") == "yellow"
        assert formatter._get_status_style("処理中") == "yellow"
        assert formatter._get_status_style("Doing") == "yellow"

    def test_status_open(self, formatter: IssueFormatter) -> None:
        """Test open status style."""
        assert formatter._get_status_style("Open") == "blue"
        assert formatter._get_status_style("未対応") == "blue"
        assert formatter._get_status_style("TODO") == "blue"
        assert formatter._get_status_style("New") == "blue"

    def test_status_pending(self, formatter: IssueFormatter) -> None:
        """Test pending status style."""
        assert formatter._get_status_style("Pending") == "magenta"
        assert formatter._get_status_style("保留") == "magenta"
        assert formatter._get_status_style("On Hold") == "magenta"

    def test_status_unknown(self, formatter: IssueFormatter) -> None:
        """Test unknown status style."""
        assert formatter._get_status_style("Custom Status") == ""


class TestPriorityStyle:
    """Tests for priority style mapping."""

    def test_priority_high(self, formatter: IssueFormatter) -> None:
        """Test high priority style."""
        assert formatter._get_priority_style("High") == "red"
        assert formatter._get_priority_style("高") == "red"
        assert formatter._get_priority_style("Urgent") == "red"

    def test_priority_medium(self, formatter: IssueFormatter) -> None:
        """Test medium priority style."""
        assert formatter._get_priority_style("Medium") == "yellow"
        assert formatter._get_priority_style("中") == "yellow"
        assert formatter._get_priority_style("Normal") == "yellow"

    def test_priority_low(self, formatter: IssueFormatter) -> None:
        """Test low priority style."""
        assert formatter._get_priority_style("Low") == "dim"
        assert formatter._get_priority_style("低") == "dim"

    def test_priority_unknown(self, formatter: IssueFormatter) -> None:
        """Test unknown priority style."""
        assert formatter._get_priority_style("Custom Priority") == ""
