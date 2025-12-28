"""Attachment models for Backlog API."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from bklg.models.issue import IssueUser


class Attachment(BaseModel):
    """Attachment model."""

    id: int = Field(description="Attachment ID")
    name: str = Field(description="File name")
    size: int = Field(description="File size in bytes")
    created_user: IssueUser | None = Field(alias="createdUser", default=None)
    created: datetime | None = None


class UploadedFile(BaseModel):
    """Uploaded file response model."""

    id: int = Field(description="Uploaded file ID")
    name: str = Field(description="File name")
    size: int = Field(description="File size in bytes")
