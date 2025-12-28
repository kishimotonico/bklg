# CLI コマンドリファレンス

`bklg` コマンドの詳細な使い方を記載します。

## 共通オプション

すべてのコマンドで使用可能なオプション:

```bash
bklg [--quiet|-q] [--verbose|-v] <command>
```

- `--quiet, -q`: 最小限の出力（エラーのみ）
- `--verbose, -v`: 詳細な出力
- `--help, -h`: ヘルプを表示

## 認証 (auth)

```bash
# ログイン（APIキーを設定）
bklg auth login

# ログアウト（認証情報を削除）
bklg auth logout

# 認証状態を確認
bklg auth status
```

## プロジェクト (project)

```bash
# プロジェクト一覧
bklg project list

# プロジェクト詳細
bklg project info <project-id>

# 課題種別一覧
bklg project types <project-id>

# ステータス一覧
bklg project statuses <project-id>
```

- `<project-id>`: プロジェクトID または プロジェクトキー（例: `PROJ`）

## 課題 (issue)

### 基本操作

```bash
# 課題一覧
bklg issue list --project <project-id>
bklg issue list --project PROJ --status "処理中"
bklg issue list --project PROJ --assignee "@me"

# 課題詳細
bklg issue view <issue-id>
bklg issue view PROJ-123

# ブラウザで開く
bklg issue open <issue-id>
bklg issue open PROJ-123
```

### 課題の作成

```bash
bklg issue create --project <project-id> --type <type> --summary <summary> [flags]

# 例: 基本的な課題作成
bklg issue create --project PROJ --type "タスク" --summary "新機能の実装"

# 例: 詳細を指定して作成
bklg issue create --project PROJ --type "バグ" --summary "ログイン画面のエラー" \
  --description "ログイン時に500エラーが発生する" \
  --priority "高" \
  --assignee "@me" \
  --due-date 2024-12-31

# 例: マイルストーンとカテゴリを指定
bklg issue create --project PROJ --type "タスク" --summary "API設計" \
  --milestone "v1.0" \
  --category "バックエンド"
```

**主なオプション:**
- `--description, -d`: 課題の詳細
- `--priority`: 優先度
- `--assignee, -a`: 担当者（`@me` で自分）
- `--due-date`: 期限日（YYYY-MM-DD）
- `--start-date`: 開始日（YYYY-MM-DD）
- `--estimated-hours`: 予定時間
- `--milestone, -m`: マイルストーン名
- `--category`: カテゴリ名

### 課題の編集

```bash
bklg issue update <issue-id> [flags]

# 例: ステータスを変更
bklg issue update PROJ-123 --status "処理中"

# 例: 担当者と優先度を変更
bklg issue update PROJ-123 --assignee "yamada" --priority "高"

# 例: 期限を変更
bklg issue update PROJ-123 --due-date 2024-12-31
```

**主なオプション:**
- `--summary, -s`: 件名
- `--description, -d`: 詳細
- `--status`: ステータス名
- `--priority`: 優先度
- `--assignee, -a`: 担当者
- `--due-date`: 期限日
- `--actual-hours`: 実績時間
- `--resolution`: 完了理由

### 課題の削除

```bash
bklg issue delete <issue-id>
bklg issue delete PROJ-123 --force  # 確認なしで削除
```

### コメント

```bash
# コメント一覧
bklg issue comment list <issue-id>
bklg issue comment list PROJ-123

# コメント追加
bklg issue comment add <issue-id> <content>
bklg issue comment add PROJ-123 "対応完了しました"

# コメント編集
bklg issue comment update <issue-id> <comment-id> <content>
bklg issue comment update PROJ-123 456 "修正: 対応完了しました"

# コメント削除
bklg issue comment delete <issue-id> <comment-id>
bklg issue comment delete PROJ-123 456
```

### 添付ファイル

```bash
# 添付ファイル一覧
bklg issue attachment list <issue-id>

# ダウンロード
bklg issue attachment download <issue-id> <attachment-id> [--output <path>]

# アップロード
bklg issue attachment upload <issue-id> <file-path>

# 削除
bklg issue attachment delete <issue-id> <attachment-id>
```

## ウォッチ (watch)

```bash
# 自分のウォッチ一覧
bklg watch list

# ウォッチに追加
bklg watch add <issue-id>
bklg watch add PROJ-123

# ウォッチ情報の取得
bklg watch info <watch-id>

# ウォッチから削除
bklg watch remove <watch-id>

# 既読にする
bklg watch read <watch-id>
```

## Wiki

### 基本操作

```bash
# Wikiページ一覧
bklg wiki list --project <project-id>

# Wikiページの表示
bklg wiki view <wiki-id>

# Wikiページの作成
bklg wiki create --project <project-id> --name <name> [--content <content>]
bklg wiki create --project PROJ --name "設計ドキュメント" --content "# 概要\n..."

# Wikiページの編集
bklg wiki update <wiki-id> [--name <name>] [--content <content>]

# Wikiページの削除
bklg wiki delete <wiki-id>
```

### Wiki添付ファイル

```bash
bklg wiki attachment list <wiki-id>
bklg wiki attachment download <wiki-id> <attachment-id>
bklg wiki attachment upload <wiki-id> <file-path>
bklg wiki attachment delete <wiki-id> <attachment-id>
```

## ユーザー (user)

```bash
# ユーザー一覧
bklg user list

# ユーザー情報
bklg user info <user-id>
bklg user info @me  # 自分の情報

# ユーザーのアクティビティ
bklg user activity <user-id>
bklg user activity @me --limit 20
```

## 通知 (notification)

```bash
# 通知一覧
bklg notification list

# 通知数の取得
bklg notification count

# 通知を既読にする
bklg notification read <notification-id>

# 全て既読にする
bklg notification read --all
```

## スペース (space)

```bash
# スペース情報
bklg space info

# スペースのお知らせ
bklg space notice

# 最近の更新
bklg space activity

# 容量使用状況
bklg space disk
```

## 汎用APIアクセス (api)

細かい操作が必要なときは直接APIを叩くことができます。

```bash
bklg api call <endpoint> [--method <method>] [--data <data>] [--query <key=value>...]

# 例: GET リクエスト
bklg api call /users

# 例: クエリパラメータ付き
bklg api call /issues --query "projectId[]=1" --query "count=100"

# 例: POST リクエスト
bklg api call /issues --method POST --data '{"projectId":1,"summary":"test"}'

# 例: DELETE リクエスト
bklg api call /issues/123 --method DELETE
```

## 補足

- `<project-id>`: プロジェクトID または プロジェクトキー（例: `PROJ`）
- `<issue-id>`: 課題ID または 課題キー（例: `PROJ-123`）、URL（例: `https://hoge.backlog.jp/view/PROJ-123`）も可
- `@me`: 自分自身を表す特殊なキーワード
