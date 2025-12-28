"""Issue-related models for Backlog API."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class IssueUser(BaseModel):
    """User reference in issue."""

    id: int
    user_id: str | None = Field(alias="userId", default=None)
    name: str = Field(default="")
    role_type: int = Field(alias="roleType", default=0)
    lang: str | None = None
    mail_address: str | None = Field(alias="mailAddress", default=None)


class IssueType(BaseModel):
    """Issue type reference."""

    id: int
    project_id: int = Field(alias="projectId")
    name: str
    color: str
    display_order: int = Field(alias="displayOrder", default=0)


class IssueStatus(BaseModel):
    """Issue status reference."""

    id: int
    project_id: int = Field(alias="projectId")
    name: str
    color: str
    display_order: int = Field(alias="displayOrder", default=0)


class IssuePriority(BaseModel):
    """Issue priority reference."""

    id: int
    name: str


class IssueCategory(BaseModel):
    """Issue category reference."""

    id: int
    name: str
    display_order: int = Field(alias="displayOrder", default=0)


class IssueVersion(BaseModel):
    """Issue version/milestone reference."""

    id: int
    project_id: int = Field(alias="projectId")
    name: str
    description: str | None = None
    start_date: str | None = Field(alias="startDate", default=None)
    release_due_date: str | None = Field(alias="releaseDueDate", default=None)
    archived: bool = False
    display_order: int = Field(alias="displayOrder", default=0)


class IssueProject(BaseModel):
    """Project reference in issue."""

    id: int
    project_key: str = Field(alias="projectKey")
    name: str
    chart_enabled: bool = Field(alias="chartEnabled", default=False)
    subtasking_enabled: bool = Field(alias="subtaskingEnabled", default=False)
    text_formatting_rule: str = Field(alias="textFormattingRule", default="markdown")
    archived: bool = False
    display_order: int | None = Field(alias="displayOrder", default=None)


class Issue(BaseModel):
    """Issue model."""

    id: int = Field(description="Issue ID")
    project_id: int = Field(alias="projectId", description="Project ID")
    issue_key: str = Field(alias="issueKey", description="Issue key (e.g., PROJ-123)")
    key_id: int = Field(alias="keyId", description="Key numeric part")
    issue_type: IssueType = Field(alias="issueType")
    summary: str = Field(description="Issue title/summary")
    description: str | None = Field(default=None, description="Issue description")
    resolution: dict | None = Field(default=None)
    priority: IssuePriority
    status: IssueStatus
    assignee: IssueUser | None = None
    category: list[IssueCategory] = Field(default_factory=list)
    versions: list[IssueVersion] = Field(default_factory=list)
    milestone: list[IssueVersion] = Field(default_factory=list)
    start_date: str | None = Field(alias="startDate", default=None)
    due_date: str | None = Field(alias="dueDate", default=None)
    estimated_hours: float | None = Field(alias="estimatedHours", default=None)
    actual_hours: float | None = Field(alias="actualHours", default=None)
    parent_issue_id: int | None = Field(alias="parentIssueId", default=None)
    created_user: IssueUser = Field(alias="createdUser")
    created: datetime
    updated_user: IssueUser = Field(alias="updatedUser")
    updated: datetime
    custom_fields: list[dict] = Field(alias="customFields", default_factory=list)
    attachments: list[dict] = Field(default_factory=list)
    shared_files: list[dict] = Field(alias="sharedFiles", default_factory=list)
    stars: list[dict] = Field(default_factory=list)

    @property
    def url(self) -> str:
        """Get issue URL (requires project info)."""
        # This is a placeholder - actual URL construction needs space URL
        return f"view/{self.issue_key}"


class Comment(BaseModel):
    """Issue comment model."""

    id: int
    content: str | None = None
    change_log: list[dict] = Field(alias="changeLog", default_factory=list)
    created_user: IssueUser = Field(alias="createdUser")
    created: datetime
    updated: datetime | None = None
    stars: list[dict] = Field(default_factory=list)
    notifications: list[dict] = Field(default_factory=list)
