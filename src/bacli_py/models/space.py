"""Space-related models for Backlog API."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class Space(BaseModel):
    """Space model."""

    space_key: str = Field(alias="spaceKey")
    name: str
    owner_id: int = Field(alias="ownerId")
    lang: str
    timezone: str
    report_send_time: str = Field(alias="reportSendTime")
    text_formatting_rule: str = Field(alias="textFormattingRule")
    created: datetime
    updated: datetime


class DiskUsage(BaseModel):
    """Disk usage model."""

    capacity: int = Field(description="Total capacity in bytes")
    issue: int = Field(description="Issue attachments in bytes")
    wiki: int = Field(description="Wiki attachments in bytes")
    file: int = Field(description="Shared files in bytes")
    subversion: int = Field(description="Subversion in bytes")
    git: int = Field(description="Git in bytes")
    git_lfs: int = Field(alias="gitLFS", description="Git LFS in bytes")
    pull_request: int = Field(
        alias="pullRequest", default=0, description="Pull request in bytes"
    )


class SpaceNotification(BaseModel):
    """Space notification/announcement model."""

    content: str | None = None
    updated: datetime | None = None
