"""User-related models for Backlog API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class User(BaseModel):
    """User model."""

    id: int = Field(description="User ID")
    user_id: str = Field(alias="userId", description="User ID string")
    name: str = Field(description="User name")
    role_type: int = Field(alias="roleType", description="Role type")
    lang: str | None = Field(default=None, description="Language")
    mail_address: str | None = Field(alias="mailAddress", default=None)
    nulabAccount: dict | None = Field(alias="nulabAccount", default=None)
    keyword: str | None = Field(default=None)
    last_login_time: str | None = Field(alias="lastLoginTime", default=None)


class NulabAccount(BaseModel):
    """Nulab account model."""

    nulab_id: str = Field(alias="nulabId")
    name: str
    unique_id: str = Field(alias="uniqueId")
