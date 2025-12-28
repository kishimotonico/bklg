"""Watch/Watching models for Backlog API."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class Watching(BaseModel):
    """Watching model."""

    id: int
    resource_already_read: bool = Field(alias="resourceAlreadyRead")
    note: str | None = None
    type: str | None = None
    issue: dict | None = None
    last_content_updated: datetime | None = Field(alias="lastContentUpdated", default=None)
    created: datetime
    updated: datetime


class WatchingCount(BaseModel):
    """Watching count model."""

    count: int
