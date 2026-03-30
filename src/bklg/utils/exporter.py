"""IssueExporter - 課題情報をMarkdownにエクスポートするユーティリティ。"""

from __future__ import annotations

from pathlib import Path

from bklg.models.attachment import Attachment
from bklg.models.issue import Comment, Issue


class IssueExporter:
    """課題情報をMarkdownファイルにエクスポートするクラス。"""

    def __init__(self, space_url: str) -> None:
        self.space_url = space_url.rstrip("/")

    def export(
        self,
        issue: Issue,
        comments: list[Comment],
        attachments: list[Attachment],
        output_dir: Path,
        attachments_downloaded: bool = True,
    ) -> Path:
        """課題情報をMarkdownファイルに書き出す。

        Args:
            issue: 課題データ。
            comments: コメントのリスト。
            attachments: 添付ファイルのリスト。
            output_dir: 出力ディレクトリ。
            attachments_downloaded: 添付ファイルがダウンロード済みかどうか。

        Returns:
            書き出した issue.md のパス。
        """
        md = self._build_markdown(issue, comments, attachments, attachments_downloaded)
        output_path = output_dir / "issue.md"
        output_path.write_text(md, encoding="utf-8")
        return output_path

    def _build_markdown(
        self,
        issue: Issue,
        comments: list[Comment],
        attachments: list[Attachment],
        attachments_downloaded: bool,
    ) -> str:
        parts = [
            self._build_header(issue),
            self._build_metadata_table(issue),
            self._build_description(issue),
        ]
        if attachments:
            parts.append(self._build_attachments_section(attachments, attachments_downloaded))
        parts.append(self._build_comments_section(comments))
        return "\n\n".join(parts) + "\n"

    def _build_header(self, issue: Issue) -> str:
        return f"# {issue.issue_key}: {issue.summary}"

    def _build_metadata_table(self, issue: Issue) -> str:
        url = f"{self.space_url}/view/{issue.issue_key}"
        assignee = issue.assignee.name if issue.assignee else "-"
        due_date = issue.due_date[:10] if issue.due_date else "-"
        created = issue.created.strftime("%Y-%m-%d %H:%M")
        updated = issue.updated.strftime("%Y-%m-%d %H:%M")

        rows = [
            ("Status", issue.status.name),
            ("Type", issue.issue_type.name),
            ("Priority", issue.priority.name),
            ("Assignee", assignee),
            ("Created by", issue.created_user.name),
            ("Created", created),
            ("Updated", updated),
            ("Due Date", due_date),
            ("URL", url),
        ]
        lines = ["| Field | Value |", "|---|---|"]
        for field, value in rows:
            lines.append(f"| {field} | {value} |")
        return "\n".join(lines)

    def _build_description(self, issue: Issue) -> str:
        description = issue.description or ""
        return f"## Description\n\n{description}"

    def _build_attachments_section(
        self,
        attachments: list[Attachment],
        downloaded: bool,
    ) -> str:
        lines = ["## Attachments", "", "| Name | Size |", "|---|---|"]
        for att in attachments:
            size_str = _format_size(att.size)
            lines.append(f"| {att.name} | {size_str} |")
        if downloaded:
            lines.extend(["", "Files saved to: ./attachments/"])
        return "\n".join(lines)

    def _build_comments_section(self, comments: list[Comment]) -> str:
        header = f"## Comments ({len(comments)})"
        if not comments:
            return header

        comment_parts = []
        for i, comment in enumerate(comments, 1):
            created = comment.created.strftime("%Y-%m-%d %H:%M")
            author = comment.created_user.name
            content = comment.content or ""
            comment_parts.append(f"### Comment #{i} - {author} ({created})\n\n{content}")

        return header + "\n\n" + "\n\n".join(comment_parts)


def _format_size(size: int) -> str:
    """ファイルサイズを人が読みやすい形式に変換する。"""
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024  # type: ignore[assignment]
    return f"{size:.1f} TB"
