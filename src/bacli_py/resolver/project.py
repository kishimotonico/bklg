"""Project resolver for project key to ID resolution."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bacli_py.models import Project
from bacli_py.resolver.base import BaseResolver, ResolverError
from bacli_py.resolver.cache import ProjectCache

if TYPE_CHECKING:
    from bacli_py.api.client import BacklogClient
    from bacli_py.resolver.cache import ResolverCache


class ProjectResolver(BaseResolver[Project]):
    """Resolver for project key to ID."""

    def __init__(self, client: BacklogClient, cache: ResolverCache) -> None:
        """Initialize project resolver."""
        super().__init__(client, cache)
        self._projects: dict[str, Project] | None = None

    def _fetch_projects(self) -> list[Project]:
        """Fetch all projects from API."""
        data = self.client.get("/projects")
        return [Project.model_validate(p) for p in data]  # type: ignore[union-attr]

    def _ensure_loaded(self) -> dict[str, Project]:
        """Ensure projects are loaded."""
        if self._projects is None:
            self.refresh()
        return self._projects  # type: ignore[return-value]

    def resolve(self, key_or_id: str) -> int:
        """Resolve project key or ID to numeric ID.

        Args:
            key_or_id: Project key (e.g., "PROJ") or numeric ID.

        Returns:
            Project numeric ID.

        Raises:
            ResolverError: If project not found.
        """
        # If it's already a numeric ID, return it
        if key_or_id.isdigit():
            return int(key_or_id)

        # Check cache first
        cached_id = self.cache.get_project_id(key_or_id)
        if cached_id is not None:
            return cached_id

        # Load and search
        projects = self._ensure_loaded()
        project = projects.get(key_or_id.upper())

        if project is None:
            raise ResolverError(key_or_id, "project")

        return project.id

    def get_all(self) -> dict[str, int]:
        """Get all project key to ID mappings.

        Returns:
            Dictionary mapping project keys to IDs.
        """
        projects = self._ensure_loaded()
        return {key: p.id for key, p in projects.items()}

    def get_project(self, key_or_id: str) -> Project:
        """Get project by key or ID.

        Args:
            key_or_id: Project key or numeric ID.

        Returns:
            Project object.

        Raises:
            ResolverError: If project not found.
        """
        projects = self._ensure_loaded()

        if key_or_id.isdigit():
            project_id = int(key_or_id)
            for project in projects.values():
                if project.id == project_id:
                    return project
            raise ResolverError(key_or_id, "project")

        project = projects.get(key_or_id.upper())
        if project is None:
            raise ResolverError(key_or_id, "project")

        return project

    def list_projects(self, archived: bool = False) -> list[Project]:
        """List all projects.

        Args:
            archived: Include archived projects.

        Returns:
            List of projects.
        """
        projects = self._ensure_loaded()
        if archived:
            return list(projects.values())
        return [p for p in projects.values() if not p.archived]

    def refresh(self) -> None:
        """Refresh cached data from API."""
        projects = self._fetch_projects()
        self._projects = {p.project_key: p for p in projects}

        # Update cache
        for project in projects:
            existing = self.cache.get_project(project.project_key)
            if existing is None:
                self.cache.set_project(
                    project.project_key,
                    ProjectCache(id=project.id),
                )
            else:
                # Keep existing metadata, just update project ID
                existing.id = project.id
                self.cache.set_project(project.project_key, existing)
