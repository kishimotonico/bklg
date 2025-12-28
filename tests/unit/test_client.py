"""Tests for api/client.py."""

from __future__ import annotations

from typing import Any

import httpx
import pytest
from pytest_httpx import HTTPXMock

from bklg.api.client import BacklogAPIError, BacklogClient
from bklg.config.settings import Settings
from bklg.models.common import ErrorCode


@pytest.fixture
def settings() -> Settings:
    """Create test settings."""
    return Settings(
        space_url="https://test.backlog.com",
        api_key="test-api-key",
    )


@pytest.fixture
def client(settings: Settings) -> BacklogClient:
    """Create test client."""
    return BacklogClient(settings=settings)


class TestBacklogAPIError:
    """Tests for BacklogAPIError class."""

    def test_basic_error(self) -> None:
        """Test basic error creation."""
        error = BacklogAPIError(
            message="Test error",
            code=ErrorCode.AUTHENTICATION_ERROR,
            status_code=401,
        )
        assert str(error) == "Test error"
        assert error.code == ErrorCode.AUTHENTICATION_ERROR
        assert error.status_code == 401

    def test_from_response_with_json_error(self) -> None:
        """Test creating error from API response with JSON body."""
        response = httpx.Response(
            status_code=401,
            json={
                "errors": [
                    {
                        "message": "Authentication failure.",
                        "code": 11,
                        "moreInfo": "Invalid API key",
                    }
                ]
            },
        )
        error = BacklogAPIError.from_response(response)
        assert "Authentication failure" in str(error)
        assert error.code == ErrorCode.AUTHENTICATION_ERROR
        assert error.status_code == 401
        assert error.more_info == "Invalid API key"

    def test_from_response_with_invalid_json(self) -> None:
        """Test creating error from response with invalid JSON."""
        response = httpx.Response(
            status_code=500,
            text="Internal Server Error",
        )
        error = BacklogAPIError.from_response(response)
        assert "500" in str(error)
        assert error.status_code == 500

    def test_is_auth_error(self) -> None:
        """Test is_auth_error method."""
        auth_error = BacklogAPIError("Auth failed", code=ErrorCode.AUTHENTICATION_ERROR)
        assert auth_error.is_auth_error() is True

        other_error = BacklogAPIError("Other error", code=ErrorCode.NO_RESOURCE_ERROR)
        assert other_error.is_auth_error() is False

    def test_is_rate_limit_error(self) -> None:
        """Test is_rate_limit_error method."""
        rate_error = BacklogAPIError(
            "Rate limited", code=ErrorCode.TOO_MANY_REQUESTS_ERROR
        )
        assert rate_error.is_rate_limit_error() is True

        other_error = BacklogAPIError("Other error", code=ErrorCode.NO_RESOURCE_ERROR)
        assert other_error.is_rate_limit_error() is False

    def test_is_not_found(self) -> None:
        """Test is_not_found method."""
        not_found = BacklogAPIError("Not found", code=ErrorCode.NO_RESOURCE_ERROR)
        assert not_found.is_not_found() is True

        other_error = BacklogAPIError(
            "Other error", code=ErrorCode.AUTHENTICATION_ERROR
        )
        assert other_error.is_not_found() is False


class TestBacklogClient:
    """Tests for BacklogClient class."""

    def test_base_url(self, client: BacklogClient) -> None:
        """Test base_url property."""
        assert client.base_url == "https://test.backlog.com/api/v2"

    def test_context_manager(self, settings: Settings) -> None:
        """Test context manager usage."""
        with BacklogClient(settings=settings) as client:
            assert client._client is None  # Client not created until first request
        # Client should be closed after exiting context

    def test_get_request(
        self, httpx_mock: HTTPXMock, client: BacklogClient, sample_project: dict[str, Any]
    ) -> None:
        """Test GET request."""
        httpx_mock.add_response(
            method="GET",
            url="https://test.backlog.com/api/v2/projects/TEST?apiKey=test-api-key",
            json=sample_project,
        )

        result = client.get("/projects/TEST")
        assert result["id"] == 1
        assert result["projectKey"] == "TEST"

    def test_get_request_with_params(
        self, httpx_mock: HTTPXMock, client: BacklogClient
    ) -> None:
        """Test GET request with query parameters."""
        httpx_mock.add_response(
            method="GET",
            url="https://test.backlog.com/api/v2/issues?apiKey=test-api-key&projectId%5B%5D=1&count=10",
            json=[],
        )

        result = client.get("/issues", params={"projectId[]": 1, "count": 10})
        assert result == []

    def test_post_request(self, httpx_mock: HTTPXMock, client: BacklogClient) -> None:
        """Test POST request with form data."""
        httpx_mock.add_response(
            method="POST",
            url="https://test.backlog.com/api/v2/issues?apiKey=test-api-key",
            json={"id": 1, "issueKey": "TEST-1"},
        )

        result = client.post("/issues", data={"projectId": 1, "summary": "Test"})
        assert result["issueKey"] == "TEST-1"

    def test_patch_request(self, httpx_mock: HTTPXMock, client: BacklogClient) -> None:
        """Test PATCH request."""
        httpx_mock.add_response(
            method="PATCH",
            url="https://test.backlog.com/api/v2/issues/TEST-1?apiKey=test-api-key",
            json={"id": 1, "issueKey": "TEST-1", "summary": "Updated"},
        )

        result = client.patch("/issues/TEST-1", data={"summary": "Updated"})
        assert result["summary"] == "Updated"

    def test_delete_request(self, httpx_mock: HTTPXMock, client: BacklogClient) -> None:
        """Test DELETE request."""
        httpx_mock.add_response(
            method="DELETE",
            url="https://test.backlog.com/api/v2/issues/TEST-1?apiKey=test-api-key",
            json={"id": 1, "issueKey": "TEST-1"},
        )

        result = client.delete("/issues/TEST-1")
        assert result["issueKey"] == "TEST-1"

    def test_api_error_response(
        self, httpx_mock: HTTPXMock, client: BacklogClient
    ) -> None:
        """Test handling of API error responses."""
        httpx_mock.add_response(
            method="GET",
            url="https://test.backlog.com/api/v2/projects/INVALID?apiKey=test-api-key",
            status_code=404,
            json={
                "errors": [
                    {
                        "message": "No resource.",
                        "code": 6,
                        "moreInfo": "",
                    }
                ]
            },
        )

        with pytest.raises(BacklogAPIError) as exc_info:
            client.get("/projects/INVALID")

        assert exc_info.value.code == ErrorCode.NO_RESOURCE_ERROR
        assert exc_info.value.status_code == 404

    def test_get_myself(
        self, httpx_mock: HTTPXMock, client: BacklogClient, sample_user: dict[str, Any]
    ) -> None:
        """Test get_myself method."""
        httpx_mock.add_response(
            method="GET",
            url="https://test.backlog.com/api/v2/users/myself?apiKey=test-api-key",
            json=sample_user,
        )

        result = client.get_myself()
        assert result["id"] == 1
        assert result["name"] == "Test User"


class TestBacklogClientRateLimit:
    """Tests for rate limiting in BacklogClient."""

    def test_rate_limit_retry(
        self, httpx_mock: HTTPXMock, client: BacklogClient, sample_project: dict[str, Any]
    ) -> None:
        """Test automatic retry on rate limit."""
        # First request returns 429
        httpx_mock.add_response(
            method="GET",
            url="https://test.backlog.com/api/v2/projects/TEST?apiKey=test-api-key",
            status_code=429,
            headers={"Retry-After": "0"},
            json={"errors": [{"message": "Rate limited", "code": 8, "moreInfo": ""}]},
        )
        # Second request succeeds
        httpx_mock.add_response(
            method="GET",
            url="https://test.backlog.com/api/v2/projects/TEST?apiKey=test-api-key",
            json=sample_project,
        )

        # Override rate limit handler for faster tests
        client.rate_limit_handler.base_delay = 0.01
        client.rate_limit_handler.max_delay = 0.01

        result = client.get("/projects/TEST")
        assert result["projectKey"] == "TEST"

    def test_rate_limit_max_retries_exceeded(
        self, httpx_mock: HTTPXMock, client: BacklogClient
    ) -> None:
        """Test max retries exceeded on rate limit."""
        # All requests return 429
        for _ in range(client.rate_limit_handler.max_retries + 1):
            httpx_mock.add_response(
                method="GET",
                url="https://test.backlog.com/api/v2/projects/TEST?apiKey=test-api-key",
                status_code=429,
                headers={"Retry-After": "0"},
                json={
                    "errors": [{"message": "Rate limited", "code": 13, "moreInfo": ""}]
                },
            )

        client.rate_limit_handler.base_delay = 0.01
        client.rate_limit_handler.max_delay = 0.01

        with pytest.raises(BacklogAPIError) as exc_info:
            client.get("/projects/TEST")

        # Error is raised from the last response
        assert exc_info.value.code == ErrorCode.TOO_MANY_REQUESTS_ERROR
        assert exc_info.value.status_code == 429
