"""Logging configuration for bklg.

ログはファイルに出力され、ノーマルモードでは画面に表示されません。
--debug-api オプションを使用すると、APIログがstderrにも出力されます。
"""

from __future__ import annotations

import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

# bklg専用ロガー
logger = logging.getLogger("bklg")

# APIリクエスト専用サブロガー
api_logger = logging.getLogger("bklg.api")


def get_default_log_path() -> Path:
    """XDG_STATE_HOMEに基づくデフォルトログパスを取得."""
    xdg_state_home = os.environ.get("XDG_STATE_HOME")
    if xdg_state_home:
        base = Path(xdg_state_home)
    else:
        base = Path.home() / ".local" / "state"
    return base / "bklg" / "bklg.log"


def setup_logging(
    log_file: str | Path | None = None,
    level: str = "DEBUG",
    max_size_mb: int = 10,
    backup_count: int = 3,
    console_output: bool = False,
) -> None:
    """ロギングの初期化（ファイル出力）.

    Args:
        log_file: ログファイルパス。Noneの場合はXDG_STATE_HOMEのデフォルトを使用。
        level: ログレベル (DEBUG, INFO, WARNING, ERROR)。
        max_size_mb: ログファイルの最大サイズ（MB）。
        backup_count: ローテーションで保持するファイル数。
        console_output: Trueの場合、APIログをstderrにも出力（--debug-api用）。
    """
    # すでに初期化済みの場合はスキップ
    if logger.handlers:
        return

    # ログファイルパスの決定
    if log_file is None:
        log_path = get_default_log_path()
    else:
        log_path = Path(log_file).expanduser()

    # ログディレクトリの作成
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # フォーマッタの設定
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # ファイルハンドラ（ローテーション付き）
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=max_size_mb * 1024 * 1024,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    # ログレベルの設定
    log_level = getattr(logging, level.upper(), logging.DEBUG)

    # ルートロガーの設定
    logger.addHandler(file_handler)
    logger.setLevel(log_level)

    # APIロガーの設定（親ロガーの設定を継承）
    api_logger.setLevel(log_level)

    # デバッグ用: コンソール出力（--debug-api 使用時のみ）
    if console_output:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        api_logger.addHandler(console_handler)

    logger.debug(f"ログ初期化完了: {log_path}")
