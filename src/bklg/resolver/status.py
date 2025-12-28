"""Status resolver for name to ID resolution."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bklg.models import Status
from bklg.resolver.base import BaseResolver, ResolverError

if TYPE_CHECKING:
    from bklg.api.client import BacklogClient
    from bklg.resolver.cache import ResolverCache


class StatusResolver(BaseResolver[Status]):
    """Resolver for status name to ID within a project."""

    def __init__(
        self,
        client: BacklogClient,
        cache: ResolverCache,
        project_id: int,
        project_key: str,
    ) -> None:
        """Initialize status resolver.

        Args:
            client: Backlog API client.
            cache: Resolver cache.
            project_id: Project numeric ID.
            project_key: Project key for cache lookup.
        """
        super().__init__(client, cache)
        self.project_id = project_id
        self.project_key = project_key
        self._statuses: dict[str, Status] | None = None

    def _fetch_statuses(self) -> list[Status]:
        """Fetch statuses from API."""
        data = self.client.get(f"/projects/{self.project_id}/statuses")
        return [Status.model_validate(s) for s in data]  # type: ignore[union-attr]

    def _ensure_loaded(self) -> dict[str, Status]:
        """Ensure statuses are loaded."""
        if self._statuses is None:
            # Try cache first
            cached = self.cache.get_statuses(self.project_key)
            if cached:
                # We need to fetch to get full IssueStatus objects
                self.refresh()
            else:
                self.refresh()
        return self._statuses  # type: ignore[return-value]

    def resolve(self, name: str) -> int:
        """Resolve status name to ID.

        Args:
            name: Status name (e.g., "未対応", "処理中", "完了").

        Returns:
            Status numeric ID.

        Raises:
            ResolverError: If status not found.
        """
        # Check cache first
        cached = self.cache.get_statuses(self.project_key)
        if name in cached:
            return cached[name]

        # Load and search
        statuses = self._ensure_loaded()
        status = statuses.get(name)

        if status is None:
            raise ResolverError(name, "status")

        return status.id

    def get_all(self) -> dict[str, int]:
        """Get all status name to ID mappings.

        Returns:
            Dictionary mapping status names to IDs.
        """
        statuses = self._ensure_loaded()
        return {name: s.id for name, s in statuses.items()}

    def list_statuses(self) -> list[Status]:
        """List all statuses.

        Returns:
            List of statuses.
        """
        statuses = self._ensure_loaded()
        return list(statuses.values())

    def refresh(self) -> None:
        """Refresh cached data from API."""
        statuses = self._fetch_statuses()
        self._statuses = {s.name: s for s in statuses}

        # Update cache
        mapping = {s.name: s.id for s in statuses}
        self.cache.set_statuses(self.project_key, self.project_id, mapping)
