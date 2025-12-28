"""Project-related models for Backlog API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Project(BaseModel):
    """Project model."""

    id: int = Field(description="Project ID")
    project_key: str = Field(alias="projectKey", description="Project key")
    name: str = Field(description="Project name")
    chart_enabled: bool = Field(alias="chartEnabled", default=False)
    use_resolved_for_chart: bool = Field(alias="useResolvedForChart", default=False)
    subtasking_enabled: bool = Field(alias="subtaskingEnabled", default=False)
    project_leader_can_edit_project_leader: bool = Field(
        alias="projectLeaderCanEditProjectLeader", default=False
    )
    use_wiki: bool = Field(alias="useWiki", default=True)
    use_file_sharing: bool = Field(alias="useFileSharing", default=True)
    use_wiki_tree_view: bool = Field(alias="useWikiTreeView", default=False)
    use_sub_version: bool = Field(alias="useSubversion", default=False)
    use_git: bool = Field(alias="useGit", default=False)
    use_original_image_size_at_wiki: bool = Field(
        alias="useOriginalImageSizeAtWiki", default=False
    )
    text_formatting_rule: str = Field(alias="textFormattingRule", default="markdown")
    archived: bool = Field(default=False)
    display_order: int | None = Field(alias="displayOrder", default=None)
    use_dev_attributes: bool = Field(alias="useDevAttributes", default=False)


class IssueType(BaseModel):
    """Issue type model."""

    id: int = Field(description="Issue type ID")
    project_id: int = Field(alias="projectId", description="Project ID")
    name: str = Field(description="Issue type name")
    color: str = Field(description="Color code")
    display_order: int = Field(alias="displayOrder", default=0)
    template_summary: str | None = Field(alias="templateSummary", default=None)
    template_description: str | None = Field(alias="templateDescription", default=None)


class Priority(BaseModel):
    """Priority model."""

    id: int = Field(description="Priority ID")
    name: str = Field(description="Priority name")


class Status(BaseModel):
    """Status model."""

    id: int = Field(description="Status ID")
    project_id: int = Field(alias="projectId", description="Project ID")
    name: str = Field(description="Status name")
    color: str = Field(description="Color code")
    display_order: int = Field(alias="displayOrder", default=0)


class Category(BaseModel):
    """Category model."""

    id: int = Field(description="Category ID")
    name: str = Field(description="Category name")
    display_order: int = Field(alias="displayOrder", default=0)


class Version(BaseModel):
    """Version/Milestone model."""

    id: int = Field(description="Version ID")
    project_id: int = Field(alias="projectId", description="Project ID")
    name: str = Field(description="Version name")
    description: str | None = Field(default=None)
    start_date: str | None = Field(alias="startDate", default=None)
    release_due_date: str | None = Field(alias="releaseDueDate", default=None)
    archived: bool = Field(default=False)
    display_order: int = Field(alias="displayOrder", default=0)
