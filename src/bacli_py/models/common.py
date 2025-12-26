"""Common models for Backlog API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class BacklogError(BaseModel):
    """Single error from Backlog API."""

    message: str = Field(description="Error message")
    code: int = Field(description="Error code")
    more_info: str = Field(default="", alias="moreInfo", description="Additional info")


class BacklogErrorResponse(BaseModel):
    """Error response from Backlog API."""

    errors: list[BacklogError] = Field(default_factory=list)

    @property
    def first_error(self) -> BacklogError | None:
        """Get the first error if any."""
        return self.errors[0] if self.errors else None

    @property
    def message(self) -> str:
        """Get combined error message."""
        return "; ".join(e.message for e in self.errors)


class RateLimitInfo(BaseModel):
    """Rate limit information from response headers."""

    limit: int = Field(description="Maximum requests allowed")
    remaining: int = Field(description="Remaining requests")
    reset: int = Field(description="Unix timestamp when limit resets")

    @classmethod
    def from_headers(cls, headers: dict[str, str]) -> RateLimitInfo | None:
        """Parse rate limit info from response headers."""
        try:
            return cls(
                limit=int(headers.get("X-RateLimit-Limit", 0)),
                remaining=int(headers.get("X-RateLimit-Remaining", 0)),
                reset=int(headers.get("X-RateLimit-Reset", 0)),
            )
        except (ValueError, TypeError):
            return None

    @property
    def is_exhausted(self) -> bool:
        """Check if rate limit is exhausted."""
        return self.remaining <= 0


# Backlog API error codes
class ErrorCode:
    """Backlog API error codes."""

    INTERNAL_ERROR = 1
    LICENSE_ERROR = 2
    LICENSE_EXPIRED_ERROR = 3
    ACCESS_DENIED_ERROR = 4
    UNAUTHORIZED_OPERATION_ERROR = 5
    NO_RESOURCE_ERROR = 6
    INVALID_REQUEST_ERROR = 7
    SPACE_OVER_CAPACITY_ERROR = 8
    RESOURCE_OVERFLOW_ERROR = 9
    TOO_LARGE_FILE_ERROR = 10
    AUTHENTICATION_ERROR = 11
    REQUIRED_MFA_ERROR = 12
    TOO_MANY_REQUESTS_ERROR = 13
