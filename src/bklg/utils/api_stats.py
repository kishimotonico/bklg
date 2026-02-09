"""API call statistics tracking.

APIコール数やキャッシュヒット率を追跡し、
過剰なAPIコールを検知するための機能を提供します。
"""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Generator

from bklg.utils.logger import api_logger

# 警告を出すAPIコール数の閾値
MAX_CALLS_WARNING = 10


@dataclass
class APIStats:
    """APIコール統計を管理."""

    calls: int = 0
    cache_hits: int = 0
    endpoints: dict[str, int] = field(default_factory=dict)
    _last_endpoint: str = ""
    _consecutive_same: int = 0

    def record_call(self, endpoint: str) -> None:
        """APIコールを記録.

        Args:
            endpoint: APIエンドポイント。
        """
        self.calls += 1
        self.endpoints[endpoint] = self.endpoints.get(endpoint, 0) + 1

        # 過剰APIコール警告
        if self.calls == MAX_CALLS_WARNING:
            api_logger.warning(
                f"API呼び出しが{MAX_CALLS_WARNING}回を超えました。"
                "意図しない過剰なリクエストが発生している可能性があります。"
            )

        # 重複リクエスト検知
        if endpoint == self._last_endpoint:
            self._consecutive_same += 1
            if self._consecutive_same >= 3:
                api_logger.warning(f"同一エンドポイントへの連続リクエスト検知: {endpoint}")
        else:
            self._consecutive_same = 1
            self._last_endpoint = endpoint

    def record_cache_hit(self, cache_type: str = "") -> None:
        """キャッシュヒットを記録.

        Args:
            cache_type: キャッシュの種類（ログ用）。
        """
        self.cache_hits += 1
        if cache_type:
            api_logger.debug(f"キャッシュヒット: {cache_type}")

    def summary(self) -> str:
        """統計サマリーを文字列で返す."""
        lines = [
            "API呼び出し統計:",
            f"  総コール数: {self.calls}",
            f"  キャッシュヒット: {self.cache_hits}",
        ]
        if self.endpoints:
            lines.append("  エンドポイント別:")
            for endpoint, count in sorted(self.endpoints.items()):
                lines.append(f"    {endpoint}: {count}")
        return "\n".join(lines)


# グローバルインスタンス
_stats: APIStats | None = None


@contextmanager
def track_api_calls() -> Generator[APIStats, None, None]:
    """APIコール追跡のコンテキストマネージャ.

    Usage:
        with track_api_calls() as stats:
            # APIコールを実行
            ...
        print(stats.summary())
    """
    global _stats
    _stats = APIStats()
    try:
        yield _stats
    finally:
        # 統計をログに記録
        if _stats.calls > 0:
            api_logger.info(_stats.summary())
        _stats = None


def get_stats() -> APIStats | None:
    """現在のAPIStats インスタンスを取得.

    Returns:
        追跡中の場合はAPIStatsインスタンス、そうでなければNone。
    """
    return _stats


def record_api_call(endpoint: str) -> None:
    """APIコールを記録（グローバル統計へ）.

    Args:
        endpoint: APIエンドポイント。
    """
    if stats := get_stats():
        stats.record_call(endpoint)


def record_cache_hit(cache_type: str = "") -> None:
    """キャッシュヒットを記録（グローバル統計へ）.

    Args:
        cache_type: キャッシュの種類。
    """
    if stats := get_stats():
        stats.record_cache_hit(cache_type)
