"""Base resolver class."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from bklg.api.client import BacklogClient
    from bklg.resolver.cache import ResolverCache

T = TypeVar("T")


class ResolverError(Exception):
    """Exception raised when resolution fails."""

    def __init__(self, name: str, resource_type: str) -> None:
        """Initialize resolver error.

        Args:
            name: The name that couldn't be resolved.
            resource_type: Type of resource (e.g., "project", "issue type").
        """
        super().__init__(f"{resource_type} '{name}' not found")
        self.name = name
        self.resource_type = resource_type


class BaseResolver(ABC, Generic[T]):
    """Base class for name-to-ID resolvers."""

    def __init__(self, client: BacklogClient, cache: ResolverCache) -> None:
        """Initialize resolver.

        Args:
            client: Backlog API client.
            cache: Resolver cache.
        """
        self.client = client
        self.cache = cache

    @abstractmethod
    def resolve(self, name: str) -> int:
        """Resolve name to ID.

        Args:
            name: Name to resolve.

        Returns:
            Resolved ID.

        Raises:
            ResolverError: If name cannot be resolved.
        """

    @abstractmethod
    def get_all(self) -> dict[str, int]:
        """Get all name-to-ID mappings.

        Returns:
            Dictionary mapping names to IDs.
        """

    @abstractmethod
    def refresh(self) -> None:
        """Refresh cached data from API."""

    def resolve_or_none(self, name: str) -> int | None:
        """Resolve name to ID, returning None if not found.

        Args:
            name: Name to resolve.

        Returns:
            Resolved ID or None.
        """
        try:
            return self.resolve(name)
        except ResolverError:
            return None
