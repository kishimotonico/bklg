"""Authentication handler for Backlog API."""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from bklg.config.settings import Settings


class APIKeyAuth(httpx.Auth):
    """Authentication using API key as query parameter."""

    def __init__(self, api_key: str) -> None:
        """Initialize with API key.

        Args:
            api_key: Backlog API key.
        """
        self.api_key = api_key

    def auth_flow(
        self, request: httpx.Request
    ) -> httpx.Request | httpx.Response:  # type: ignore[misc]
        """Add API key to request query parameters."""
        url = request.url.copy_merge_params({"apiKey": self.api_key})
        request = httpx.Request(
            method=request.method,
            url=url,
            headers=request.headers,
            content=request.content,
        )
        yield request


def get_auth(settings: Settings) -> APIKeyAuth:
    """Get authentication handler from settings.

    Args:
        settings: Application settings.

    Returns:
        Authentication handler.

    Raises:
        ValueError: If API key is not configured.
    """
    if not settings.api_key:
        raise ValueError("API key is not configured. Run 'bklg auth login' first.")

    return APIKeyAuth(settings.api_key)
