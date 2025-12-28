"""Notification models for Backlog API."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from bklg.models.issue import IssueUser


class Notification(BaseModel):
    """Notification model."""

    id: int
    already_read: bool = Field(alias="alreadyRead")
    reason: int
    resource_already_read: bool = Field(alias="resourceAlreadyRead")
    project: dict | None = None
    issue: dict | None = None
    comment: dict | None = None
    pull_request: dict | None = Field(alias="pullRequest", default=None)
    pull_request_comment: dict | None = Field(alias="pullRequestComment", default=None)
    sender: IssueUser | None = None
    created: datetime


class NotificationCount(BaseModel):
    """Notification count model."""

    count: int
