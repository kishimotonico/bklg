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

#### 1.1 ログモジュールの追加

**新規ファイル**: `src/bklg/utils/logger.py`

```python
import logging
from typing import Optional
from contextlib import contextmanager

# bklg専用ロガー
logger = logging.getLogger("bklg")

# APIリクエスト専用サブロガー
api_logger = logging.getLogger("bklg.api")

def setup_logging(level: int = logging.WARNING, debug_api: bool = False) -> None:
    """ロギングの初期化"""
    # フォーマッタの設定
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    # stderr ハンドラ
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(level)

    if debug_api:
        api_logger.setLevel(logging.DEBUG)
```

#### 1.2 OutputContextとの連携

**変更ファイル**: `src/bklg/cli/context.py`

| OutputLevel | logging Level | 説明 |
|-------------|---------------|------|
| QUIET | WARNING | エラーと警告のみ |
| NORMAL | INFO | 標準的な情報 |
| VERBOSE | DEBUG | 詳細なデバッグ情報 |

#### 1.3 CLI引数の追加

**変更ファイル**: `src/bklg/main.py`

```python
@app.callback()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v"),
    quiet: bool = typer.Option(False, "--quiet", "-q"),
    debug_api: bool = typer.Option(False, "--debug-api", help="APIリクエストの詳細ログを出力"),
):
    ...
```

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

### 通常使用（変更なし）

```bash
$ bklg issue list --project PROJ
```

### デバッグモード

```bash
$ bklg --debug-api issue list --project PROJ
[12:34:56] DEBUG [bklg.api] → GET /api/v2/projects
[12:34:56] DEBUG [bklg.api] ← 200 (0.45s)
[12:34:56] DEBUG [bklg.api] キャッシュヒット: PROJ (statuses)
[12:34:56] DEBUG [bklg.api] → GET /api/v2/issues
[12:34:57] DEBUG [bklg.api] ← 200 (0.82s)

API呼び出し統計:
  総コール数: 2
  キャッシュヒット: 1
  エンドポイント別:
    /api/v2/projects: 1
    /api/v2/issues: 1
```

### 詳細モード

```bash
$ bklg --verbose issue list --project PROJ
# 通常の詳細出力に加え、コマンド終了時に統計を表示
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
