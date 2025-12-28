"""Tests for api/rate_limit.py."""

from __future__ import annotations

import time
from unittest.mock import patch

import httpx
import pytest

from bklg.api.rate_limit import RateLimitHandler


@pytest.fixture
def handler() -> RateLimitHandler:
    """Create test rate limit handler."""
    return RateLimitHandler(max_retries=3, base_delay=1.0, max_delay=60.0)


class TestRateLimitHandler:
    """Tests for RateLimitHandler class."""

    def test_default_values(self) -> None:
        """Test default initialization values."""
        handler = RateLimitHandler()
        assert handler.max_retries == 3
        assert handler.base_delay == 1.0
        assert handler.max_delay == 60.0
        assert handler.last_rate_limit is None

    def test_custom_values(self) -> None:
        """Test custom initialization values."""
        handler = RateLimitHandler(max_retries=5, base_delay=2.0, max_delay=120.0)
        assert handler.max_retries == 5
        assert handler.base_delay == 2.0
        assert handler.max_delay == 120.0


class TestUpdateFromResponse:
    """Tests for update_from_response method."""

    def test_update_with_rate_limit_headers(self, handler: RateLimitHandler) -> None:
        """Test updating from response with rate limit headers."""
        response = httpx.Response(
            status_code=200,
            headers={
                "x-ratelimit-limit": "100",
                "x-ratelimit-remaining": "50",
                "x-ratelimit-reset": "1700000000",
            },
        )
        handler.update_from_response(response)

        assert handler.last_rate_limit is not None
        assert handler.last_rate_limit.limit == 100
        assert handler.last_rate_limit.remaining == 50
        assert handler.last_rate_limit.reset == 1700000000

    def test_update_without_rate_limit_headers(
        self, handler: RateLimitHandler
    ) -> None:
        """Test updating from response without rate limit headers."""
        response = httpx.Response(status_code=200)
        handler.update_from_response(response)

        # Without rate limit headers, returns None
        assert handler.last_rate_limit is None


class TestShouldRetry:
    """Tests for should_retry method."""

    def test_should_retry_on_429(self, handler: RateLimitHandler) -> None:
        """Test should_retry returns True on 429."""
        response = httpx.Response(status_code=429)
        assert handler.should_retry(response, 0) is True
        assert handler.should_retry(response, 1) is True
        assert handler.should_retry(response, 2) is True

    def test_should_not_retry_on_max_attempts(
        self, handler: RateLimitHandler
    ) -> None:
        """Test should_retry returns False when max attempts reached."""
        response = httpx.Response(status_code=429)
        assert handler.should_retry(response, handler.max_retries) is False

    def test_should_not_retry_on_other_status(
        self, handler: RateLimitHandler
    ) -> None:
        """Test should_retry returns False for non-429 status codes."""
        assert handler.should_retry(httpx.Response(status_code=200), 0) is False
        assert handler.should_retry(httpx.Response(status_code=400), 0) is False
        assert handler.should_retry(httpx.Response(status_code=500), 0) is False


class TestGetRetryDelay:
    """Tests for get_retry_delay method."""

    def test_retry_after_header(self, handler: RateLimitHandler) -> None:
        """Test using Retry-After header value."""
        response = httpx.Response(
            status_code=429,
            headers={"Retry-After": "30"},
        )
        delay = handler.get_retry_delay(response, 0)
        assert delay == 30.0

    def test_retry_after_header_capped_by_max_delay(
        self, handler: RateLimitHandler
    ) -> None:
        """Test Retry-After value is capped by max_delay."""
        response = httpx.Response(
            status_code=429,
            headers={"Retry-After": "120"},
        )
        delay = handler.get_retry_delay(response, 0)
        assert delay == handler.max_delay

    def test_retry_after_invalid_value(self, handler: RateLimitHandler) -> None:
        """Test handling of invalid Retry-After header."""
        response = httpx.Response(
            status_code=429,
            headers={"Retry-After": "invalid"},
        )
        delay = handler.get_retry_delay(response, 0)
        # Falls back to exponential backoff
        assert delay == handler.base_delay

    def test_exponential_backoff(self, handler: RateLimitHandler) -> None:
        """Test exponential backoff calculation."""
        response = httpx.Response(status_code=429)

        # attempt 0: base_delay * 2^0 = 1.0
        assert handler.get_retry_delay(response, 0) == 1.0

        # attempt 1: base_delay * 2^1 = 2.0
        assert handler.get_retry_delay(response, 1) == 2.0

        # attempt 2: base_delay * 2^2 = 4.0
        assert handler.get_retry_delay(response, 2) == 4.0

    def test_exponential_backoff_capped_by_max_delay(
        self, handler: RateLimitHandler
    ) -> None:
        """Test exponential backoff is capped by max_delay."""
        response = httpx.Response(status_code=429)

        # attempt 10: base_delay * 2^10 = 1024, capped at 60
        delay = handler.get_retry_delay(response, 10)
        assert delay == handler.max_delay

    def test_uses_reset_time_from_headers(self, handler: RateLimitHandler) -> None:
        """Test using reset time from rate limit headers."""
        # Set up rate limit info with a future reset time
        reset_time = time.time() + 10  # 10 seconds from now
        response = httpx.Response(
            status_code=200,
            headers={
                "x-ratelimit-limit": "100",
                "x-ratelimit-remaining": "0",
                "x-ratelimit-reset": str(int(reset_time)),
            },
        )
        handler.update_from_response(response)

        # Now get retry delay for a 429
        retry_response = httpx.Response(status_code=429)
        delay = handler.get_retry_delay(retry_response, 0)

        # Should use the reset time
        assert 9 < delay < 11  # Around 10 seconds


class TestWaitForRetry:
    """Tests for wait_for_retry method."""

    def test_wait_for_short_delay(self, handler: RateLimitHandler) -> None:
        """Test waiting for a short delay."""
        with patch("time.sleep") as mock_sleep:
            handler.wait_for_retry(0.5)
            mock_sleep.assert_called_once_with(0.5)

    def test_wait_for_long_delay_shows_message(
        self, handler: RateLimitHandler
    ) -> None:
        """Test that long delays show a message."""
        with patch("time.sleep") as mock_sleep:
            with patch("bklg.api.rate_limit.console.print") as mock_print:
                handler.wait_for_retry(15)
                mock_sleep.assert_called_once_with(15)
                mock_print.assert_called_once()
                # Check that the message contains the delay
                call_args = mock_print.call_args[0][0]
                assert "15" in call_args
