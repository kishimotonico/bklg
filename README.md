# bklg

Backlog API の非公式コマンドラインツール。

## インストール

```bash
# uv を使用
uv pip install .

# または pip を使用
pip install .
```

開発用:

```bash
uv pip install -e ".[test]"
```

## 設定

### 初期設定

```bash
bklg auth login
```

対話的にスペースURLとAPIキーを設定します。

設定は `~/.config/bklg/config.toml` に保存されます:

```toml
space_url = "https://example.backlog.com"
api_key = "your-api-key"
default_project = "PROJ"  # オプション
```

### APIキーの取得

Backlog の個人設定 > API から API キーを発行できます。

## 基本的な使い方

```bash
# プロジェクト一覧
bklg project list

# 課題一覧
bklg issue list --project PROJ

# 課題の詳細を表示
bklg issue view PROJ-123

# 課題をブラウザで開く
bklg issue open PROJ-123

# 課題を作成
bklg issue create --project PROJ --type "タスク" --summary "新しいタスク"

# 課題にコメント
bklg issue comment add PROJ-123 "対応しました"

# 通知を確認
bklg notification list
```

### サブコマンド一覧

| コマンド | 説明 |
|---------|------|
| `auth` | 認証設定 |
| `project` | プロジェクト操作 |
| `issue` | 課題操作 |
| `user` | ユーザー情報 |
| `space` | スペース情報 |
| `notification` | 通知 |
| `watch` | ウォッチ |
| `wiki` | Wiki操作 |
| `api` | 汎用APIアクセス |

各コマンドの詳細は `bklg <command> --help` で確認できます。

詳しい使い方は [cli-usage.md](./cli-usage.md) を参照してください。

## ライセンス

MIT
