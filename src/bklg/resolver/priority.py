"""Priority resolver for name to ID resolution."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bklg.models import Priority
from bklg.resolver.base import BaseResolver, ResolverError

if TYPE_CHECKING:
    from bklg.api.client import BacklogClient
    from bklg.resolver.cache import ResolverCache


class PriorityResolver(BaseResolver[Priority]):
    """Resolver for priority name to ID."""

    def __init__(self, client: BacklogClient, cache: ResolverCache) -> None:
        """Initialize priority resolver."""
        super().__init__(client, cache)
        self._priorities: dict[str, Priority] | None = None

    def _fetch_priorities(self) -> list[Priority]:
        """Fetch priorities from API."""
        data = self.client.get("/priorities")
        return [Priority.model_validate(p) for p in data]  # type: ignore[union-attr]

    def _ensure_loaded(self) -> dict[str, Priority]:
        """Ensure priorities are loaded."""
        if self._priorities is None:
            # Try cache first
            cached = self.cache.get_priorities()
            if cached:
                self.refresh()
            else:
                self.refresh()
        return self._priorities  # type: ignore[return-value]

    def resolve(self, name: str) -> int:
        """Resolve priority name to ID.

        Args:
            name: Priority name (e.g., "高", "中", "低").

        Returns:
            Priority numeric ID.

        Raises:
            ResolverError: If priority not found.
        """
        # Check cache first
        cached = self.cache.get_priorities()
        if name in cached:
            return cached[name]

        # Load and search
        priorities = self._ensure_loaded()
        priority = priorities.get(name)

        if priority is None:
            raise ResolverError(name, "priority")

        return priority.id

    def get_all(self) -> dict[str, int]:
        """Get all priority name to ID mappings.

        Returns:
            Dictionary mapping priority names to IDs.
        """
        priorities = self._ensure_loaded()
        return {name: p.id for name, p in priorities.items()}

    def list_priorities(self) -> list[Priority]:
        """List all priorities.

        Returns:
            List of priorities.
        """
        priorities = self._ensure_loaded()
        return list(priorities.values())

    def refresh(self) -> None:
        """Refresh cached data from API."""
        priorities = self._fetch_priorities()
        self._priorities = {p.name: p for p in priorities}

        # Update cache
        mapping = {p.name: p.id for p in priorities}
        self.cache.set_priorities(mapping)
