"""HTTP client for Backlog API."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import httpx

from bacli_py.api.auth import APIKeyAuth, get_auth
from bacli_py.api.rate_limit import RateLimitHandler
from bacli_py.config.settings import Settings, get_settings
from bacli_py.models.common import BacklogErrorResponse, ErrorCode


class BacklogAPIError(Exception):
    """Exception raised for Backlog API errors."""

    def __init__(
        self,
        message: str,
        code: int | None = None,
        status_code: int | None = None,
        more_info: str = "",
    ) -> None:
        """Initialize API error.

        Args:
            message: Error message.
            code: Backlog error code.
            status_code: HTTP status code.
            more_info: Additional error information.
        """
        super().__init__(message)
        self.code = code
        self.status_code = status_code
        self.more_info = more_info

    @classmethod
    def from_response(cls, response: httpx.Response) -> BacklogAPIError:
        """Create error from API response."""
        try:
            data = response.json()
            error_response = BacklogErrorResponse.model_validate(data)
            if error_response.first_error:
                return cls(
                    message=error_response.message,
                    code=error_response.first_error.code,
                    status_code=response.status_code,
                    more_info=error_response.first_error.more_info,
                )
        except Exception:
            pass

        return cls(
            message=f"HTTP {response.status_code}: {response.text}",
            status_code=response.status_code,
        )

    def is_auth_error(self) -> bool:
        """Check if this is an authentication error."""
        return self.code == ErrorCode.AUTHENTICATION_ERROR

    def is_rate_limit_error(self) -> bool:
        """Check if this is a rate limit error."""
        return self.code == ErrorCode.TOO_MANY_REQUESTS_ERROR

    def is_not_found(self) -> bool:
        """Check if this is a not found error."""
        return self.code == ErrorCode.NO_RESOURCE_ERROR


class BacklogClient:
    """HTTP client for Backlog API with rate limiting and error handling."""

    def __init__(
        self,
        settings: Settings | None = None,
        rate_limit_handler: RateLimitHandler | None = None,
    ) -> None:
        """Initialize client.

        Args:
            settings: Application settings. If None, loads from config file.
            rate_limit_handler: Rate limit handler. If None, creates default.
        """
        self.settings = settings or get_settings()
        self.rate_limit_handler = rate_limit_handler or RateLimitHandler()
        self._client: httpx.Client | None = None

    @property
    def base_url(self) -> str:
        """Get API base URL."""
        return self.settings.base_url

    @property
    def auth(self) -> APIKeyAuth:
        """Get authentication handler."""
        return get_auth(self.settings)

    @property
    def client(self) -> httpx.Client:
        """Get or create HTTP client."""
        if self._client is None:
            self._client = httpx.Client(
                base_url=self.base_url,
                auth=self.auth,
                timeout=30.0,
            )
        return self._client

    def close(self) -> None:
        """Close the HTTP client."""
        if self._client is not None:
            self._client.close()
            self._client = None

    def __enter__(self) -> BacklogClient:
        """Enter context manager."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Exit context manager."""
        self.close()

    def _request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """Make HTTP request with rate limiting and error handling.

        Args:
            method: HTTP method.
            endpoint: API endpoint (without base URL).
            params: Query parameters.
            data: Form data (will be sent as x-www-form-urlencoded).
            json_body: JSON body (for raw API access).

        Returns:
            HTTP response.

        Raises:
            BacklogAPIError: If API returns an error.
        """
        url = endpoint.lstrip("/")

        for attempt in range(self.rate_limit_handler.max_retries + 1):
            if json_body is not None:
                response = self.client.request(
                    method=method,
                    url=url,
                    params=params,
                    json=json_body,
                )
            else:
                response = self.client.request(
                    method=method,
                    url=url,
                    params=params,
                    data=data,
                )

            self.rate_limit_handler.update_from_response(response)

            if response.status_code == 429:
                if self.rate_limit_handler.should_retry(response, attempt):
                    delay = self.rate_limit_handler.get_retry_delay(response, attempt)
                    self.rate_limit_handler.wait_for_retry(delay)
                    continue
                raise BacklogAPIError.from_response(response)

            if response.status_code >= 400:
                raise BacklogAPIError.from_response(response)

            return response

        raise BacklogAPIError(
            message="Max retries exceeded",
            status_code=429,
            code=ErrorCode.TOO_MANY_REQUESTS_ERROR,
        )

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any] | list[Any]:
        """Make GET request.

        Args:
            endpoint: API endpoint.
            params: Query parameters.

        Returns:
            JSON response.
        """
        response = self._request("GET", endpoint, params=params)
        return response.json()  # type: ignore[no-any-return]

    def post(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make POST request with form data.

        Args:
            endpoint: API endpoint.
            data: Form data.
            params: Query parameters.

        Returns:
            JSON response.
        """
        response = self._request("POST", endpoint, params=params, data=data)
        return response.json()  # type: ignore[no-any-return]

    def patch(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make PATCH request with form data.

        Args:
            endpoint: API endpoint.
            data: Form data.
            params: Query parameters.

        Returns:
            JSON response.
        """
        response = self._request("PATCH", endpoint, params=params, data=data)
        return response.json()  # type: ignore[no-any-return]

    def delete(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make DELETE request.

        Args:
            endpoint: API endpoint.
            params: Query parameters.

        Returns:
            JSON response.
        """
        response = self._request("DELETE", endpoint, params=params)
        return response.json()  # type: ignore[no-any-return]

    def get_myself(self) -> dict[str, Any]:
        """Get current user information.

        This is useful for checking authentication status.

        Returns:
            User information.
        """
        return self.get("/users/myself")  # type: ignore[return-value]

    def upload_file(self, file_path: Path) -> dict[str, Any]:
        """Upload a file to Backlog.

        This uploads a file to /space/attachment endpoint.
        The returned attachment ID can be used when creating/updating issues.

        Args:
            file_path: Path to the file to upload.

        Returns:
            Upload response with attachment info.

        Raises:
            BacklogAPIError: If upload fails.
            FileNotFoundError: If file doesn't exist.
        """
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        url = "/space/attachment"

        with file_path.open("rb") as f:
            files = {"file": (file_path.name, f)}
            response = self.client.post(
                url,
                files=files,
            )

        if response.status_code >= 400:
            raise BacklogAPIError.from_response(response)

        return response.json()  # type: ignore[no-any-return]

    def download_file(
        self,
        endpoint: str,
        output_path: Path | None = None,
    ) -> tuple[bytes, str]:
        """Download a file from Backlog.

        Args:
            endpoint: API endpoint for the file.
            output_path: Optional path to save the file.

        Returns:
            Tuple of (file content, filename).

        Raises:
            BacklogAPIError: If download fails.
        """
        url = endpoint.lstrip("/")
        response = self.client.get(url)

        if response.status_code >= 400:
            raise BacklogAPIError.from_response(response)

        # Try to get filename from Content-Disposition header
        filename = "download"
        content_disposition = response.headers.get("content-disposition", "")
        if "filename=" in content_disposition:
            # Parse filename from header
            parts = content_disposition.split("filename=")
            if len(parts) > 1:
                filename = parts[1].strip('"').strip("'")

        content = response.content

        if output_path:
            if output_path.is_dir():
                output_path = output_path / filename
            output_path.write_bytes(content)

        return content, filename
