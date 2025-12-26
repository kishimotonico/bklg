"""Issue type resolver for name to ID resolution."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bacli_py.models import IssueType
from bacli_py.resolver.base import BaseResolver, ResolverError

if TYPE_CHECKING:
    from bacli_py.api.client import BacklogClient
    from bacli_py.resolver.cache import ResolverCache


class IssueTypeResolver(BaseResolver[IssueType]):
    """Resolver for issue type name to ID within a project."""

    def __init__(
        self,
        client: BacklogClient,
        cache: ResolverCache,
        project_id: int,
        project_key: str,
    ) -> None:
        """Initialize issue type resolver.

        Args:
            client: Backlog API client.
            cache: Resolver cache.
            project_id: Project numeric ID.
            project_key: Project key for cache lookup.
        """
        super().__init__(client, cache)
        self.project_id = project_id
        self.project_key = project_key
        self._issue_types: dict[str, IssueType] | None = None

    def _fetch_issue_types(self) -> list[IssueType]:
        """Fetch issue types from API."""
        data = self.client.get(f"/projects/{self.project_id}/issueTypes")
        return [IssueType.model_validate(it) for it in data]  # type: ignore[union-attr]

    def _ensure_loaded(self) -> dict[str, IssueType]:
        """Ensure issue types are loaded."""
        if self._issue_types is None:
            # Try cache first
            cached = self.cache.get_issue_types(self.project_key)
            if cached:
                # We need to fetch to get full IssueType objects
                self.refresh()
            else:
                self.refresh()
        return self._issue_types  # type: ignore[return-value]

    def resolve(self, name: str) -> int:
        """Resolve issue type name to ID.

        Args:
            name: Issue type name (e.g., "バグ", "タスク").

        Returns:
            Issue type numeric ID.

        Raises:
            ResolverError: If issue type not found.
        """
        # Check cache first
        cached = self.cache.get_issue_types(self.project_key)
        if name in cached:
            return cached[name]

        # Load and search
        issue_types = self._ensure_loaded()
        issue_type = issue_types.get(name)

        if issue_type is None:
            raise ResolverError(name, "issue type")

        return issue_type.id

    def get_all(self) -> dict[str, int]:
        """Get all issue type name to ID mappings.

        Returns:
            Dictionary mapping issue type names to IDs.
        """
        issue_types = self._ensure_loaded()
        return {name: it.id for name, it in issue_types.items()}

    def list_issue_types(self) -> list[IssueType]:
        """List all issue types.

        Returns:
            List of issue types.
        """
        issue_types = self._ensure_loaded()
        return list(issue_types.values())

    def refresh(self) -> None:
        """Refresh cached data from API."""
        issue_types = self._fetch_issue_types()
        self._issue_types = {it.name: it for it in issue_types}

        # Update cache
        mapping = {it.name: it.id for it in issue_types}
        self.cache.set_issue_types(self.project_key, self.project_id, mapping)
