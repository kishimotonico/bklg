# APIログ改修計画

## 概要

本ドキュメントは、`bklg` CLIツールにおけるAPIリクエストのログ機能を改善し、以下の目的を達成するための改修計画を記載します。

- 意図しないAPIリクエストの発生を検知
- APIコール効率性の可視化・改善
- デバッグ時の問題追跡を容易化

## 現状分析

### 現在のログ出力方式

| 項目 | 現状 |
|------|------|
| ログライブラリ | Rich Console（標準loggingは未使用） |
| 出力レベル制御 | `OutputContext` で QUIET/NORMAL/VERBOSE の3段階 |
| APIリクエストログ | **なし** |
| パフォーマンスメトリクス | **なし** |
| API呼び出し数記録 | **なし** |

### 現在の出力レベル

```python
class OutputLevel(IntEnum):
    QUIET = 0      # エラーのみ
    NORMAL = 1     # 標準出力
    VERBOSE = 2    # 詳細出力
```

### 既存のキャッシュ・最適化機能

- **ResolverCache**: プロジェクトメタデータのファイルキャッシュ（24時間TTL）
- **RateLimitHandler**: 429エラー時の指数バックオフリトライ

## 課題

1. **APIリクエストの不可視性**
   - どのエンドポイントにいつリクエストが発生したか追跡できない
   - 意図しない重複リクエストの検知が困難

2. **効率性の測定手段がない**
   - キャッシュヒット率が不明
   - 1コマンドあたりのAPI呼び出し数が把握できない

3. **デバッグの困難さ**
   - レート制限発生時の原因特定が難しい
   - パフォーマンス問題の切り分けができない

---

## 改修計画

### フェーズ1: ログ基盤の構築

#### 1.1 設計方針

- **ノーマルモード**: 画面（stderr）にはログを出力しない
- **ファイル出力**: すべてのログはファイルに記録
- **設定ファイル**: ログファイルパスは設定ファイルで指定
- **XDG準拠**: デフォルトパスは `XDG_STATE_HOME` を使用

#### 1.2 XDG Base Directory 仕様

| 環境変数 | デフォルト | 用途 |
|----------|-----------|------|
| `XDG_CONFIG_HOME` | `~/.config` | 設定ファイル |
| `XDG_STATE_HOME` | `~/.local/state` | 状態データ（ログ等） |
| `XDG_CACHE_HOME` | `~/.cache` | キャッシュデータ |

**ログファイルのデフォルトパス**:
```
$XDG_STATE_HOME/bklg/bklg.log
→ ~/.local/state/bklg/bklg.log
```

#### 1.3 設定ファイルの拡張

**変更ファイル**: `src/bklg/config/settings.py`

```toml
# ~/.config/bklg/config.toml
[logging]
# ログファイルのパス（省略時: $XDG_STATE_HOME/bklg/bklg.log）
file = "~/.local/state/bklg/bklg.log"

# ログレベル: DEBUG, INFO, WARNING, ERROR
level = "DEBUG"

# ログファイルの最大サイズ（MB）、超過時にローテーション
max_size_mb = 10

# 保持するローテーションファイル数
backup_count = 3
```

#### 1.4 ログモジュールの追加

**新規ファイル**: `src/bklg/utils/logger.py`

```python
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional
import os

# bklg専用ロガー
logger = logging.getLogger("bklg")

# APIリクエスト専用サブロガー
api_logger = logging.getLogger("bklg.api")

def get_default_log_path() -> Path:
    """XDG_STATE_HOMEに基づくデフォルトログパスを取得"""
    xdg_state_home = os.environ.get("XDG_STATE_HOME")
    if xdg_state_home:
        base = Path(xdg_state_home)
    else:
        base = Path.home() / ".local" / "state"
    return base / "bklg" / "bklg.log"

def setup_logging(
    log_file: Optional[Path] = None,
    level: str = "DEBUG",
    max_size_mb: int = 10,
    backup_count: int = 3,
    console_output: bool = False,  # デバッグ用: stderrにも出力
) -> None:
    """ロギングの初期化（ファイル出力）"""

    # ログファイルパスの決定
    if log_file is None:
        log_file = get_default_log_path()
    else:
        log_file = Path(log_file).expanduser()

    # ログディレクトリの作成
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # フォーマッタの設定
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # ファイルハンドラ（ローテーション付き）
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_size_mb * 1024 * 1024,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    # ルートロガーの設定
    logger.addHandler(file_handler)
    logger.setLevel(getattr(logging, level.upper(), logging.DEBUG))

    # APIロガーはルートロガーの設定を継承
    api_logger.setLevel(getattr(logging, level.upper(), logging.DEBUG))

    # デバッグ用: コンソール出力（--debug-api 使用時のみ）
    if console_output:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        api_logger.addHandler(console_handler)

    logger.debug(f"ログ初期化完了: {log_file}")
```

#### 1.5 設定モデルの拡張

**変更ファイル**: `src/bklg/config/settings.py`

```python
from pydantic import BaseModel

class LoggingConfig(BaseModel):
    """ログ設定"""
    file: str | None = None  # None時はXDG_STATE_HOMEのデフォルトを使用
    level: str = "DEBUG"
    max_size_mb: int = 10
    backup_count: int = 3

class Settings(BaseModel):
    # 既存の設定...
    logging: LoggingConfig = LoggingConfig()
```

#### 1.6 CLI引数の追加（オプション）

**変更ファイル**: `src/bklg/main.py`

```python
@app.callback()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v"),
    quiet: bool = typer.Option(False, "--quiet", "-q"),
    debug_api: bool = typer.Option(False, "--debug-api", help="APIリクエストログをstderrにも出力"),
):
    # ログ初期化
    from bklg.utils.logger import setup_logging
    from bklg.config.settings import get_settings

    settings = get_settings()
    setup_logging(
        log_file=settings.logging.file,
        level=settings.logging.level,
        max_size_mb=settings.logging.max_size_mb,
        backup_count=settings.logging.backup_count,
        console_output=debug_api,  # --debug-api の場合のみstderrにも出力
    )
    ...
```

#### 1.7 出力の使い分け

| モード | 画面出力 | ファイル出力 |
|--------|----------|-------------|
| ノーマル (`bklg issue list`) | なし | すべてのログ |
| デバッグ (`--debug-api`) | APIログのみ | すべてのログ |
| 詳細 (`--verbose`) | Rich出力 | すべてのログ |

**ポイント**:
- 通常使用時、ユーザーの画面にはログが表示されない
- 問題発生時は `~/.local/state/bklg/bklg.log` を確認
- `--debug-api` でリアルタイムにAPIコールを確認可能

---

### フェーズ2: APIリクエストのログ実装

#### 2.1 APIクライアントへのログ埋め込み

**変更ファイル**: `src/bklg/api/client.py`

##### リクエスト開始時

```python
from bklg.utils.logger import api_logger

def _request(self, method: str, path: str, **kwargs):
    api_logger.debug(f"→ {method} {path}")
    start_time = time.time()

    response = self._client.request(method, path, **kwargs)

    elapsed = time.time() - start_time
    api_logger.debug(f"← {response.status_code} ({elapsed:.2f}s)")

    return response
```

##### 出力例

```
[12:34:56] DEBUG [bklg.api] → GET /api/v2/projects
[12:34:57] DEBUG [bklg.api] ← 200 (0.45s)
[12:34:57] DEBUG [bklg.api] → GET /api/v2/projects/PROJ/issueTypes
[12:34:57] DEBUG [bklg.api] ← 200 (0.32s)
```

#### 2.2 レート制限ログの強化

**変更ファイル**: `src/bklg/api/rate_limit.py`

```python
api_logger.warning(
    f"レート制限検知: {response.headers.get('X-RateLimit-Remaining')}/{response.headers.get('X-RateLimit-Limit')} "
    f"(リセット: {reset_seconds}秒後)"
)
```

---

### フェーズ3: API呼び出し統計の実装

#### 3.1 APIコールカウンターの追加

**新規ファイル**: `src/bklg/utils/api_stats.py`

```python
from dataclasses import dataclass, field
from typing import Dict
from contextlib import contextmanager

@dataclass
class APIStats:
    """APIコール統計を管理"""
    calls: int = 0
    cache_hits: int = 0
    endpoints: Dict[str, int] = field(default_factory=dict)

    def record_call(self, endpoint: str) -> None:
        self.calls += 1
        self.endpoints[endpoint] = self.endpoints.get(endpoint, 0) + 1

    def record_cache_hit(self) -> None:
        self.cache_hits += 1

    def summary(self) -> str:
        lines = [
            f"API呼び出し統計:",
            f"  総コール数: {self.calls}",
            f"  キャッシュヒット: {self.cache_hits}",
            f"  エンドポイント別:",
        ]
        for endpoint, count in sorted(self.endpoints.items()):
            lines.append(f"    {endpoint}: {count}")
        return "\n".join(lines)

# グローバルインスタンス
_stats: APIStats | None = None

@contextmanager
def track_api_calls():
    """APIコール追跡のコンテキストマネージャ"""
    global _stats
    _stats = APIStats()
    try:
        yield _stats
    finally:
        _stats = None

def get_stats() -> APIStats | None:
    return _stats
```

#### 3.2 統計の出力

`--verbose` 時にコマンド終了時に統計を出力:

```
API呼び出し統計:
  総コール数: 3
  キャッシュヒット: 2
  エンドポイント別:
    /api/v2/issues: 1
    /api/v2/projects: 1
    /api/v2/projects/PROJ/statuses: 1
```

---

### フェーズ4: キャッシュログの実装

#### 4.1 キャッシュヒット/ミスのログ

**変更ファイル**: `src/bklg/resolver/cache.py`

```python
from bklg.utils.logger import api_logger
from bklg.utils.api_stats import get_stats

def get_project_cache(self, project_key: str) -> ProjectCache | None:
    cache = self._load_cache()
    if project_key in cache and not self._is_expired(cache[project_key]):
        api_logger.debug(f"キャッシュヒット: {project_key}")
        if stats := get_stats():
            stats.record_cache_hit()
        return cache[project_key]

    api_logger.debug(f"キャッシュミス: {project_key}")
    return None
```

#### 4.2 各Resolverへのログ追加

**変更ファイル**: `src/bklg/resolver/` 以下の各ファイル

```python
# 例: status.py
def resolve(self, name: str, project_key: str) -> int:
    # キャッシュチェック
    if cached := self.cache.get_statuses(project_key):
        api_logger.debug(f"ステータス '{name}' をキャッシュから解決")
        return cached[name]

    # API呼び出し
    api_logger.debug(f"ステータス一覧をAPIから取得: {project_key}")
    ...
```

---

### フェーズ5: 警告・異常検知

#### 5.1 過剰APIコール警告

同一コマンド内で閾値（例: 10回）を超えるAPIコールが発生した場合に警告:

```python
MAX_CALLS_WARNING = 10

def record_call(self, endpoint: str) -> None:
    self.calls += 1
    if self.calls == MAX_CALLS_WARNING:
        api_logger.warning(
            f"API呼び出しが{MAX_CALLS_WARNING}回を超えました。"
            "意図しない過剰なリクエストが発生している可能性があります。"
        )
```

#### 5.2 重複リクエスト検知

同一エンドポイントへの連続リクエストを検知:

```python
def record_call(self, endpoint: str) -> None:
    if endpoint == self._last_endpoint:
        self._consecutive_same += 1
        if self._consecutive_same >= 3:
            api_logger.warning(f"同一エンドポイントへの連続リクエスト検知: {endpoint}")
    else:
        self._consecutive_same = 1
        self._last_endpoint = endpoint
```

---

## 実装優先度

| フェーズ | 優先度 | 工数目安 | 効果 |
|---------|--------|----------|------|
| 1: ログ基盤 | **高** | 小 | 必須の基盤 |
| 2: APIリクエストログ | **高** | 小 | 即座にデバッグ可能に |
| 3: API統計 | **中** | 中 | 効率性の可視化 |
| 4: キャッシュログ | **中** | 小 | キャッシュ効果の確認 |
| 5: 警告・異常検知 | **低** | 小 | 問題の早期発見 |

---

## 変更対象ファイル一覧

### 新規作成

| ファイル | 概要 |
|----------|------|
| `src/bklg/utils/logger.py` | ログ設定モジュール |
| `src/bklg/utils/api_stats.py` | API統計モジュール |

### 変更

| ファイル | 変更内容 |
|----------|----------|
| `src/bklg/main.py` | `--debug-api` オプション追加、ログ初期化 |
| `src/bklg/cli/context.py` | OutputLevelとlogging連携 |
| `src/bklg/api/client.py` | リクエスト/レスポンスログ追加 |
| `src/bklg/api/rate_limit.py` | レート制限ログ強化 |
| `src/bklg/resolver/cache.py` | キャッシュヒット/ミスログ |
| `src/bklg/resolver/*.py` | 各Resolverにログ追加 |

---

## 使用例

### 通常使用（画面にログ出力なし）

```bash
$ bklg issue list --project PROJ
# 通常の出力のみ（ログは画面に表示されない）
# ログは ~/.local/state/bklg/bklg.log に記録される
```

### ログファイルの確認

```bash
$ tail -f ~/.local/state/bklg/bklg.log
[2024-01-15 12:34:56] DEBUG [bklg.api] → GET /api/v2/projects
[2024-01-15 12:34:56] DEBUG [bklg.api] ← 200 (0.45s)
[2024-01-15 12:34:56] DEBUG [bklg.api] キャッシュヒット: PROJ (statuses)
[2024-01-15 12:34:56] DEBUG [bklg.api] → GET /api/v2/issues
[2024-01-15 12:34:57] DEBUG [bklg.api] ← 200 (0.82s)
```

### デバッグモード（リアルタイム確認）

```bash
$ bklg --debug-api issue list --project PROJ
# 通常の出力に加え、APIログがstderrにも出力される
[2024-01-15 12:34:56] DEBUG [bklg.api] → GET /api/v2/projects
[2024-01-15 12:34:56] DEBUG [bklg.api] ← 200 (0.45s)
...
```

### 設定ファイル例

```toml
# ~/.config/bklg/config.toml
[backlog]
space = "example"
api_key = "your-api-key"

[logging]
# カスタムログファイルパス（省略可）
file = "~/logs/bklg.log"
# ログレベル: DEBUG, INFO, WARNING, ERROR
level = "DEBUG"
# ログローテーション設定
max_size_mb = 10
backup_count = 3
```

---

## テスト計画

### 単体テスト

1. `logger.py`: ログレベル設定のテスト
2. `api_stats.py`: 統計カウントのテスト
3. 各Resolverのキャッシュログ出力テスト

### 統合テスト

1. `--debug-api` フラグが正しく機能するか
2. 実際のAPIコールが正しくログ出力されるか
3. キャッシュヒット時にAPIコールがスキップされるか

### 手動テスト

1. `bklg issue list` を複数回実行し、キャッシュ効果を確認
2. レート制限発生時のログ出力を確認
3. 大量課題取得時のAPI呼び出し数を確認

---

## 補足: AGENTS.md の要件への対応

> SHOULD: 実装はAPIコール数を適切に抑えることを意識ください
> SHOULD: ユーザーは `bklg issue list` などを軽率に実行します。そういった場合でも過剰なAPIコールを発生させないように注意してください

本改修により、以下が可能になります：

- **可視化**: `--debug-api` でAPIコール数を即座に確認
- **検知**: 過剰APIコールの警告機能
- **効率化**: キャッシュヒット率の把握による改善ポイントの特定
