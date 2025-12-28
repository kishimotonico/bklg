"""User resolver for user ID to numeric ID resolution."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bklg.models import User
from bklg.resolver.base import BaseResolver, ResolverError

if TYPE_CHECKING:
    from bklg.api.client import BacklogClient
    from bklg.resolver.cache import ResolverCache


class UserResolver(BaseResolver[User]):
    """Resolver for user ID (string) to numeric ID."""

    def __init__(self, client: BacklogClient, cache: ResolverCache) -> None:
        """Initialize user resolver."""
        super().__init__(client, cache)
        self._users: dict[str, User] | None = None
        self._myself: User | None = None

    def _fetch_users(self) -> list[User]:
        """Fetch all users from API."""
        data = self.client.get("/users")
        return [User.model_validate(u) for u in data]  # type: ignore[union-attr]

    def _fetch_myself(self) -> User:
        """Fetch current user from API."""
        data = self.client.get_myself()
        return User.model_validate(data)

    def _ensure_loaded(self) -> dict[str, User]:
        """Ensure users are loaded."""
        if self._users is None:
            self.refresh()
        return self._users  # type: ignore[return-value]

    def get_myself(self) -> User:
        """Get current authenticated user.

        Returns:
            Current user.
        """
        if self._myself is None:
            self._myself = self._fetch_myself()
        return self._myself

    def resolve(self, user_id: str) -> int:
        """Resolve user ID to numeric ID.

        Args:
            user_id: User ID string (e.g., "h_tanaka") or "@me" for current user.

        Returns:
            User numeric ID.

        Raises:
            ResolverError: If user not found.
        """
        # Handle @me
        if user_id.lower() == "@me":
            return self.get_myself().id

        # If it's already a numeric ID, return it
        if user_id.isdigit():
            return int(user_id)

        # Check cache first
        cached = self.cache.get_global_users()
        if user_id in cached:
            return cached[user_id]

        # Load and search
        users = self._ensure_loaded()
        user = users.get(user_id)

        if user is None:
            raise ResolverError(user_id, "user")

        return user.id

    def get_all(self) -> dict[str, int]:
        """Get all user ID to numeric ID mappings.

        Returns:
            Dictionary mapping user IDs to numeric IDs.
        """
        users = self._ensure_loaded()
        return {uid: u.id for uid, u in users.items()}

    def get_user(self, user_id: str) -> User:
        """Get user by ID.

        Args:
            user_id: User ID string or "@me".

        Returns:
            User object.

        Raises:
            ResolverError: If user not found.
        """
        if user_id.lower() == "@me":
            return self.get_myself()

        users = self._ensure_loaded()

        if user_id.isdigit():
            numeric_id = int(user_id)
            for user in users.values():
                if user.id == numeric_id:
                    return user
            raise ResolverError(user_id, "user")

        user = users.get(user_id)
        if user is None:
            raise ResolverError(user_id, "user")

        return user

    def list_users(self) -> list[User]:
        """List all users.

        Returns:
            List of users.
        """
        users = self._ensure_loaded()
        return list(users.values())

    def refresh(self) -> None:
        """Refresh cached data from API."""
        users = self._fetch_users()
        self._users = {u.user_id: u for u in users}

        # Update cache
        mapping = {u.user_id: u.id for u in users}
        self.cache.set_global_users(mapping)
