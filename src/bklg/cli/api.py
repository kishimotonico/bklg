"""Direct API access commands for bklg."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from bklg.api.client import BacklogAPIError, BacklogClient
from bklg.config.settings import get_settings

app = typer.Typer(help="Direct API access")
console = Console()
err_console = Console(stderr=True)


def _parse_query_params(params: list[str] | None) -> dict[str, str]:
    """Parse query parameters from key=value format."""
    if not params:
        return {}

    result: dict[str, str] = {}
    for param in params:
        if "=" in param:
            key, value = param.split("=", 1)
            result[key] = value
        else:
            err_console.print(f"[yellow]Invalid query param format: {param}[/yellow]")
    return result


def _parse_form_data(data: list[str] | None) -> dict[str, str]:
    """Parse form data from key=value format."""
    if not data:
        return {}

    result: dict[str, str] = {}
    for item in data:
        if "=" in item:
            key, value = item.split("=", 1)
            result[key] = value
        else:
            err_console.print(f"[yellow]Invalid data format: {item}[/yellow]")
    return result


def _load_json_data(json_str: str) -> dict:
    """Load JSON data from string or file."""
    # Check if it's a file reference
    if json_str.startswith("@"):
        file_path = Path(json_str[1:])
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        return json.loads(file_path.read_text(encoding="utf-8"))

    return json.loads(json_str)


@app.command(name="call")
def api_call(
    endpoint: Annotated[
        str,
        typer.Argument(help="API endpoint (e.g., /users, /issues)"),
    ],
    method: Annotated[
        str,
        typer.Option("--method", "-X", help="HTTP method"),
    ] = "GET",
    query: Annotated[
        list[str] | None,
        typer.Option("--query", "-q", help="Query parameters (key=value)"),
    ] = None,
    data: Annotated[
        list[str] | None,
        typer.Option("--data", "-d", help="Form data (key=value)"),
    ] = None,
    json_body: Annotated[
        str | None,
        typer.Option("--json", "-j", help="JSON body (or @file.json)"),
    ] = None,
) -> None:
    """Make a direct API call.

    Examples:
        bklg api /users
        bklg api /issues --query "projectId[]=1" --query "count=100"
        bklg api /issues --method POST --data "projectId=1" --data "summary=test"
        bklg api /issues --method POST --json '{"projectId":1,"summary":"test"}'
        bklg api /issues/123 --method DELETE
    """
    settings = get_settings()
    if not settings.is_configured:
        err_console.print("[red]Not logged in.[/red]")
        raise typer.Exit(1)

    method = method.upper()
    params = _parse_query_params(query)
    form_data = _parse_form_data(data)

    # Parse JSON body if provided
    json_data = None
    if json_body:
        try:
            json_data = _load_json_data(json_body)
        except FileNotFoundError as e:
            err_console.print(f"[red]{e}[/red]")
            raise typer.Exit(1) from e
        except json.JSONDecodeError as e:
            err_console.print(f"[red]Invalid JSON: {e}[/red]")
            raise typer.Exit(1) from e

    try:
        with BacklogClient(settings=settings) as client:
            if method == "GET":
                result = client.get(endpoint, params=params or None)
            elif method == "POST":
                if json_data:
                    result = client._request(
                        "POST", endpoint, params=params or None, json_body=json_data
                    ).json()
                else:
                    result = client.post(
                        endpoint, data=form_data or None, params=params or None
                    )
            elif method == "PATCH":
                if json_data:
                    result = client._request(
                        "PATCH", endpoint, params=params or None, json_body=json_data
                    ).json()
                else:
                    result = client.patch(
                        endpoint, data=form_data or None, params=params or None
                    )
            elif method == "DELETE":
                result = client.delete(endpoint, params=params or None)
            elif method == "PUT":
                if json_data:
                    result = client._request(
                        "PUT", endpoint, params=params or None, json_body=json_data
                    ).json()
                else:
                    result = client._request(
                        "PUT", endpoint, params=params or None, data=form_data or None
                    ).json()
            else:
                err_console.print(f"[red]Unsupported method: {method}[/red]")
                raise typer.Exit(1)

        # Output result as JSON
        console.print_json(json.dumps(result, ensure_ascii=False, indent=2, default=str))

    except BacklogAPIError as e:
        err_console.print(f"[red]API Error: {e}[/red]")
        if e.more_info:
            err_console.print(f"[dim]{e.more_info}[/dim]")
        raise typer.Exit(1) from e
