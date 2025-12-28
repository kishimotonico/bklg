"""Formatters for CLI output."""

from __future__ import annotations

from typing import TYPE_CHECKING

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

if TYPE_CHECKING:
    from bklg.models.issue import Comment, Issue


class IssueFormatter:
    """Formatter for issue output."""

    def __init__(self, console: Console | None = None) -> None:
        """Initialize formatter.

        Args:
            console: Rich console for output.
        """
        self.console = console or Console()

    def format_issue_table(
        self,
        issues: list[Issue],
        title: str = "Issues",
    ) -> Table:
        """Format issues as a table.

        Args:
            issues: List of issues.
            title: Table title.

        Returns:
            Rich table.
        """
        table = Table(title=title)
        table.add_column("Key", style="cyan", no_wrap=True)
        table.add_column("Type", style="dim", no_wrap=True)
        table.add_column("Status", no_wrap=True)
        table.add_column("Priority", no_wrap=True)
        table.add_column("Summary", overflow="ellipsis", max_width=50)
        table.add_column("Assignee", style="dim")

        for issue in issues:
            status_style = self._get_status_style(issue.status.name)
            priority_style = self._get_priority_style(issue.priority.name)

            assignee = issue.assignee.name if issue.assignee else "-"

            table.add_row(
                issue.issue_key,
                issue.issue_type.name,
                Text(issue.status.name, style=status_style),
                Text(issue.priority.name, style=priority_style),
                issue.summary,
                assignee,
            )

        return table

    def format_issue_detail(
        self,
        issue: Issue,
        space_url: str | None = None,
    ) -> None:
        """Print detailed issue view.

        Args:
            issue: Issue to display.
            space_url: Space URL for link generation.
        """
        # Header
        title = f"[bold cyan]{issue.issue_key}[/bold cyan] {issue.summary}"
        self.console.print(title)
        self.console.print()

        # Metadata table
        meta_table = Table(show_header=False, box=None, padding=(0, 2))
        meta_table.add_column("Key", style="dim")
        meta_table.add_column("Value")

        status_style = self._get_status_style(issue.status.name)
        priority_style = self._get_priority_style(issue.priority.name)

        meta_table.add_row("Type", issue.issue_type.name)
        meta_table.add_row("Status", Text(issue.status.name, style=status_style))
        meta_table.add_row("Priority", Text(issue.priority.name, style=priority_style))
        meta_table.add_row(
            "Assignee", issue.assignee.name if issue.assignee else "Unassigned"
        )
        meta_table.add_row("Created by", issue.created_user.name)
        meta_table.add_row("Created", issue.created.strftime("%Y-%m-%d %H:%M"))
        meta_table.add_row("Updated", issue.updated.strftime("%Y-%m-%d %H:%M"))

        if issue.due_date:
            meta_table.add_row("Due Date", issue.due_date)

        if issue.start_date:
            meta_table.add_row("Start Date", issue.start_date)

        if issue.estimated_hours:
            meta_table.add_row("Estimated", f"{issue.estimated_hours}h")

        if issue.actual_hours:
            meta_table.add_row("Actual", f"{issue.actual_hours}h")

        if issue.category:
            categories = ", ".join(c.name for c in issue.category)
            meta_table.add_row("Categories", categories)

        if issue.milestone:
            milestones = ", ".join(m.name for m in issue.milestone)
            meta_table.add_row("Milestone", milestones)

        if space_url:
            url = f"{space_url}/view/{issue.issue_key}"
            meta_table.add_row("URL", f"[link={url}]{url}[/link]")

        self.console.print(meta_table)
        self.console.print()

        # Description
        if issue.description:
            self.console.print("[bold]Description[/bold]")
            self.console.print()
            self._render_markdown(issue.description)
        else:
            self.console.print("[dim]No description[/dim]")

    def format_comments(self, comments: list[Comment]) -> None:
        """Print issue comments.

        Args:
            comments: List of comments.
        """
        if not comments:
            self.console.print("[dim]No comments[/dim]")
            return

        self.console.print()
        self.console.print(f"[bold]Comments ({len(comments)})[/bold]")
        self.console.print()

        for comment in comments:
            if not comment.content:
                continue

            header = (
                f"[bold]{comment.created_user.name}[/bold] "
                f"[dim]{comment.created.strftime('%Y-%m-%d %H:%M')}[/dim]"
            )
            panel = Panel(
                Markdown(comment.content),
                title=header,
                title_align="left",
                border_style="dim",
            )
            self.console.print(panel)

    def _render_markdown(self, text: str) -> None:
        """Render markdown text.

        Args:
            text: Markdown text.
        """
        md = Markdown(text)
        self.console.print(md)

    def _get_status_style(self, status_name: str) -> str:
        """Get style for status name.

        Args:
            status_name: Status name.

        Returns:
            Rich style string.
        """
        status_lower = status_name.lower()

        # Common status patterns
        if any(word in status_lower for word in ["完了", "done", "closed", "resolved"]):
            return "green"
        if any(word in status_lower for word in ["処理中", "進行", "progress", "doing"]):
            return "yellow"
        if any(word in status_lower for word in ["未対応", "open", "todo", "new"]):
            return "blue"
        if any(word in status_lower for word in ["保留", "pending", "hold"]):
            return "magenta"

        return ""

    def _get_priority_style(self, priority_name: str) -> str:
        """Get style for priority name.

        Args:
            priority_name: Priority name.

        Returns:
            Rich style string.
        """
        priority_lower = priority_name.lower()

        if any(word in priority_lower for word in ["高", "high", "urgent"]):
            return "red"
        if any(word in priority_lower for word in ["中", "medium", "normal"]):
            return "yellow"
        if any(word in priority_lower for word in ["低", "low"]):
            return "dim"

        return ""
