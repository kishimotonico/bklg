"""IssueExporter のユニットテスト。"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pytest

from bklg.models.attachment import Attachment
from bklg.models.issue import Comment, Issue
from bklg.utils.exporter import IssueExporter, _format_size


@pytest.fixture
def sample_issue(
    sample_issue_type: dict[str, Any],
    sample_priority: dict[str, Any],
    sample_status: dict[str, Any],
    sample_user: dict[str, Any],
) -> Issue:
    """テスト用 Issue オブジェクト。"""
    return Issue.model_validate(
        {
            "id": 100,
            "projectId": 1,
            "issueKey": "TEST-1",
            "keyId": 1,
            "issueType": sample_issue_type,
            "summary": "テスト課題タイトル",
            "description": "課題の説明文がここに入る。",
            "resolution": None,
            "priority": sample_priority,
            "status": sample_status,
            "assignee": sample_user,
            "category": [],
            "versions": [],
            "milestone": [],
            "startDate": None,
            "dueDate": "2024-12-31T00:00:00Z",
            "estimatedHours": None,
            "actualHours": None,
            "parentIssueId": None,
            "createdUser": sample_user,
            "created": "2024-01-01T00:00:00Z",
            "updatedUser": sample_user,
            "updated": "2024-01-15T10:30:00Z",
            "customFields": [],
            "attachments": [],
            "sharedFiles": [],
            "stars": [],
        }
    )


@pytest.fixture
def sample_comment(sample_user: dict[str, Any]) -> Comment:
    """テスト用 Comment オブジェクト。"""
    return Comment.model_validate(
        {
            "id": 1,
            "content": "これはテストコメントです。",
            "changeLog": [],
            "createdUser": sample_user,
            "created": "2024-01-02T10:00:00Z",
            "updated": "2024-01-02T10:00:00Z",
            "stars": [],
            "notifications": [],
        }
    )


@pytest.fixture
def sample_attachment() -> Attachment:
    """テスト用 Attachment オブジェクト。"""
    return Attachment.model_validate(
        {
            "id": 1,
            "name": "report.pdf",
            "size": 1048576,
        }
    )


@pytest.fixture
def exporter() -> IssueExporter:
    """テスト用 IssueExporter インスタンス。"""
    return IssueExporter(space_url="https://example.backlog.com")


class TestFormatSize:
    """_format_size 関数のテスト。"""

    def test_bytes(self) -> None:
        assert _format_size(512) == "512.0 B"

    def test_kilobytes(self) -> None:
        assert _format_size(1024) == "1.0 KB"

    def test_megabytes(self) -> None:
        assert _format_size(1048576) == "1.0 MB"

    def test_gigabytes(self) -> None:
        assert _format_size(1073741824) == "1.0 GB"

    def test_fractional(self) -> None:
        assert _format_size(262144) == "256.0 KB"


class TestBuildHeader:
    """_build_header のテスト。"""

    def test_header_format(self, exporter: IssueExporter, sample_issue: Issue) -> None:
        result = exporter._build_header(sample_issue)
        assert result == "# TEST-1: テスト課題タイトル"


class TestBuildMetadataTable:
    """_build_metadata_table のテスト。"""

    def test_table_contains_fields(
        self, exporter: IssueExporter, sample_issue: Issue
    ) -> None:
        result = exporter._build_metadata_table(sample_issue)
        assert "| Status | Open |" in result
        assert "| Type | Task |" in result
        assert "| Priority | Normal |" in result
        assert "| Assignee | Test User |" in result
        assert "| Created by | Test User |" in result
        assert "| Created | 2024-01-01 00:00 |" in result
        assert "| Updated | 2024-01-15 10:30 |" in result
        assert "| Due Date | 2024-12-31 |" in result
        assert "| URL | https://example.backlog.com/view/TEST-1 |" in result

    def test_table_no_assignee(
        self,
        exporter: IssueExporter,
        sample_issue: Issue,
    ) -> None:
        sample_issue.assignee = None
        result = exporter._build_metadata_table(sample_issue)
        assert "| Assignee | - |" in result

    def test_table_no_due_date(
        self,
        exporter: IssueExporter,
        sample_issue: Issue,
    ) -> None:
        sample_issue.due_date = None
        result = exporter._build_metadata_table(sample_issue)
        assert "| Due Date | - |" in result

    def test_space_url_trailing_slash(
        self,
        sample_issue: Issue,
    ) -> None:
        # trailing slash が除去されて URL が正しく生成されること
        exp = IssueExporter(space_url="https://example.backlog.com/")
        result = exp._build_metadata_table(sample_issue)
        assert "https://example.backlog.com/view/TEST-1" in result


class TestBuildDescription:
    """_build_description のテスト。"""

    def test_description_with_content(
        self, exporter: IssueExporter, sample_issue: Issue
    ) -> None:
        result = exporter._build_description(sample_issue)
        assert result == "## Description\n\n課題の説明文がここに入る。"

    def test_description_empty(
        self, exporter: IssueExporter, sample_issue: Issue
    ) -> None:
        sample_issue.description = None
        result = exporter._build_description(sample_issue)
        assert result == "## Description\n\n"


class TestBuildAttachmentsSection:
    """_build_attachments_section のテスト。"""

    def test_with_download(
        self, exporter: IssueExporter, sample_attachment: Attachment
    ) -> None:
        result = exporter._build_attachments_section([sample_attachment], downloaded=True)
        assert "## Attachments" in result
        assert "| report.pdf | 1.0 MB |" in result
        assert "Files saved to: ./attachments/" in result

    def test_without_download(
        self, exporter: IssueExporter, sample_attachment: Attachment
    ) -> None:
        result = exporter._build_attachments_section([sample_attachment], downloaded=False)
        assert "## Attachments" in result
        assert "| report.pdf | 1.0 MB |" in result
        assert "Files saved to: ./attachments/" not in result

    def test_multiple_attachments(self, exporter: IssueExporter) -> None:
        attachments = [
            Attachment.model_validate({"id": 1, "name": "report.pdf", "size": 1048576}),
            Attachment.model_validate({"id": 2, "name": "screenshot.png", "size": 262144}),
        ]
        result = exporter._build_attachments_section(attachments, downloaded=True)
        assert "| report.pdf | 1.0 MB |" in result
        assert "| screenshot.png | 256.0 KB |" in result


class TestBuildCommentsSection:
    """_build_comments_section のテスト。"""

    def test_no_comments(self, exporter: IssueExporter) -> None:
        result = exporter._build_comments_section([])
        assert result == "## Comments (0)"

    def test_single_comment(
        self, exporter: IssueExporter, sample_comment: Comment
    ) -> None:
        result = exporter._build_comments_section([sample_comment])
        assert "## Comments (1)" in result
        assert "### Comment #1 - Test User (2024-01-02 10:00)" in result
        assert "これはテストコメントです。" in result

    def test_multiple_comments(
        self, exporter: IssueExporter, sample_comment: Comment
    ) -> None:
        from bklg.models.issue import IssueUser

        second_comment = Comment.model_validate(
            {
                "id": 2,
                "content": "2番目のコメント。",
                "changeLog": [],
                "createdUser": {
                    "id": 2,
                    "userId": "another_user",
                    "name": "Another User",
                    "roleType": 1,
                },
                "created": "2024-01-03T14:30:00Z",
                "updated": "2024-01-03T14:30:00Z",
                "stars": [],
                "notifications": [],
            }
        )
        result = exporter._build_comments_section([sample_comment, second_comment])
        assert "## Comments (2)" in result
        assert "### Comment #1 - Test User (2024-01-02 10:00)" in result
        assert "### Comment #2 - Another User (2024-01-03 14:30)" in result

    def test_comment_no_content(
        self, exporter: IssueExporter, sample_comment: Comment
    ) -> None:
        sample_comment.content = None
        result = exporter._build_comments_section([sample_comment])
        assert "## Comments (1)" in result
        # content が None でもクラッシュしないこと


class TestExport:
    """export メソッドのテスト。"""

    def test_creates_issue_md(
        self,
        exporter: IssueExporter,
        sample_issue: Issue,
        tmp_path: Path,
    ) -> None:
        output_path = exporter.export(
            issue=sample_issue,
            comments=[],
            attachments=[],
            output_dir=tmp_path,
        )
        assert output_path == tmp_path / "issue.md"
        assert output_path.exists()

    def test_markdown_content(
        self,
        exporter: IssueExporter,
        sample_issue: Issue,
        sample_comment: Comment,
        sample_attachment: Attachment,
        tmp_path: Path,
    ) -> None:
        output_path = exporter.export(
            issue=sample_issue,
            comments=[sample_comment],
            attachments=[sample_attachment],
            output_dir=tmp_path,
            attachments_downloaded=True,
        )
        content = output_path.read_text(encoding="utf-8")
        assert "# TEST-1: テスト課題タイトル" in content
        assert "## Description" in content
        assert "## Attachments" in content
        assert "## Comments (1)" in content

    def test_no_attachments_section_when_empty(
        self,
        exporter: IssueExporter,
        sample_issue: Issue,
        tmp_path: Path,
    ) -> None:
        output_path = exporter.export(
            issue=sample_issue,
            comments=[],
            attachments=[],
            output_dir=tmp_path,
        )
        content = output_path.read_text(encoding="utf-8")
        assert "## Attachments" not in content

    def test_ends_with_newline(
        self,
        exporter: IssueExporter,
        sample_issue: Issue,
        tmp_path: Path,
    ) -> None:
        output_path = exporter.export(
            issue=sample_issue,
            comments=[],
            attachments=[],
            output_dir=tmp_path,
        )
        content = output_path.read_text(encoding="utf-8")
        assert content.endswith("\n")
