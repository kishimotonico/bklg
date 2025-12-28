"""Wiki models for Backlog API."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from bacli_py.models.issue import IssueUser


class Wiki(BaseModel):
    """Wiki page model."""

    id: int
    project_id: int = Field(alias="projectId")
    name: str
    content: str | None = None
    tags: list[dict] = Field(default_factory=list)
    attachments: list[dict] = Field(default_factory=list)
    shared_files: list[dict] = Field(alias="sharedFiles", default_factory=list)
    stars: list[dict] = Field(default_factory=list)
    created_user: IssueUser | None = Field(alias="createdUser", default=None)
    created: datetime | None = None
    updated_user: IssueUser | None = Field(alias="updatedUser", default=None)
    updated: datetime | None = None


class WikiTag(BaseModel):
    """Wiki tag model."""

    id: int
    name: str
