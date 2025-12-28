"""Rate limiting handler with exponential backoff."""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from rich.console import Console

from bklg.models.common import RateLimitInfo

if TYPE_CHECKING:
    import httpx

console = Console(stderr=True)


class RateLimitHandler:
    """Handles rate limiting with exponential backoff."""

    def __init__(
        self,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
    ) -> None:
        """Initialize rate limit handler.

        Args:
            max_retries: Maximum number of retry attempts.
            base_delay: Base delay in seconds for exponential backoff.
            max_delay: Maximum delay in seconds.
        """
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self._last_rate_limit: RateLimitInfo | None = None

    @property
    def last_rate_limit(self) -> RateLimitInfo | None:
        """Get the last rate limit info."""
        return self._last_rate_limit

    def update_from_response(self, response: httpx.Response) -> None:
        """Update rate limit info from response headers."""
        headers = dict(response.headers)
        self._last_rate_limit = RateLimitInfo.from_headers(headers)

    def should_retry(self, response: httpx.Response, attempt: int) -> bool:
        """Check if request should be retried."""
        if attempt >= self.max_retries:
            return False

        return response.status_code == 429

    def get_retry_delay(self, response: httpx.Response, attempt: int) -> float:
        """Calculate delay before next retry.

        Uses Retry-After header if available, otherwise exponential backoff.
        """
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                return min(float(retry_after), self.max_delay)
            except ValueError:
                pass

        if self._last_rate_limit and self._last_rate_limit.reset:
            reset_delay = self._last_rate_limit.reset - time.time()
            if reset_delay > 0:
                return min(reset_delay, self.max_delay)

        delay = self.base_delay * (2**attempt)
        return min(delay, self.max_delay)

    def wait_for_retry(self, delay: float) -> None:
        """Wait before retrying with user feedback."""
        if delay > 10:
            console.print(
                f"[yellow]Rate limit reached. Waiting {delay:.0f} seconds...[/yellow]"
            )
        time.sleep(delay)
