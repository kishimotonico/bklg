# 新規実装予定のCLIコマンド

このファイルには、今後実装予定のコマンドの使い方を記載しています。

## 課題 (Issue)

### 課題の作成

```bash
bacli issue create --project <project-id> --type <type> --summary <summary> [flags]

# 例: 基本的な課題作成
bacli issue create --project PROJ --type "タスク" --summary "新機能の実装"

# 例: 詳細を指定して作成
bacli issue create --project PROJ --type "バグ" --summary "ログイン画面のエラー" \
  --description "ログイン時に500エラーが発生する" \
  --priority "高" \
  --assignee "@me" \
  --due-date 2024-12-31

# 例: マイルストーンとカテゴリを指定
bacli issue create --project PROJ --type "タスク" --summary "API設計" \
  --milestone "v1.0" \
  --category "バックエンド"
```

**flags:**
- `--description, -d`: 課題の詳細
- `--priority`: 優先度 (低/中/高)
- `--assignee, -a`: 担当者 (@meで自分)
- `--due-date`: 期限日 (YYYY-MM-DD)
- `--start-date`: 開始日 (YYYY-MM-DD)
- `--estimated-hours`: 予定時間
- `--milestone, -m`: マイルストーン名
- `--category`: カテゴリ名

### 課題の編集

```bash
bacli issue update <issue-id> [flags]

# 例: ステータスを変更
bacli issue update PROJ-123 --status "処理中"

# 例: 担当者と優先度を変更
bacli issue update PROJ-123 --assignee "yamada" --priority "高"

# 例: 期限を変更
bacli issue update PROJ-123 --due-date 2024-12-31

# 例: 説明を追記
bacli issue update PROJ-123 --description "追加情報: テスト環境で再現確認済み"
```

**flags:**
- `--summary, -s`: 件名
- `--description, -d`: 詳細
- `--status`: ステータス名
- `--priority`: 優先度
- `--assignee, -a`: 担当者
- `--due-date`: 期限日
- `--start-date`: 開始日
- `--estimated-hours`: 予定時間
- `--actual-hours`: 実績時間
- `--milestone, -m`: マイルストーン名
- `--resolution`: 完了理由

### 課題の削除

```bash
bacli issue delete <issue-id>

# 例
bacli issue delete PROJ-123
bacli issue delete PROJ-123 --force  # 確認なしで削除
```

### 課題のコメント

```bash
# コメント一覧
bacli issue comment list <issue-id>
bacli issue comment list PROJ-123
bacli issue comment list PROJ-123 --limit 50

# コメント追加
bacli issue comment add <issue-id> <content>
bacli issue comment add PROJ-123 "対応完了しました"
bacli issue comment add PROJ-123 --file comment.txt  # ファイルから読み込み

# コメント編集
bacli issue comment update <issue-id> <comment-id> <content>
bacli issue comment update PROJ-123 456 "修正: 対応完了しました"

# コメント削除
bacli issue comment delete <issue-id> <comment-id>
bacli issue comment delete PROJ-123 456
```

### 添付ファイル

```bash
# 添付ファイル一覧
bacli issue attachment list <issue-id>
bacli issue attachment list PROJ-123

# 添付ファイルのダウンロード
bacli issue attachment download <issue-id> <attachment-id> [--output <path>]
bacli issue attachment download PROJ-123 789
bacli issue attachment download PROJ-123 789 --output ./downloads/

# 全添付ファイルをダウンロード
bacli issue attachment download PROJ-123 --all --output ./downloads/

# 添付ファイルのアップロード
bacli issue attachment upload <issue-id> <file-path>
bacli issue attachment upload PROJ-123 ./screenshot.png
bacli issue attachment upload PROJ-123 ./doc1.pdf ./doc2.pdf  # 複数ファイル

# 添付ファイルの削除
bacli issue attachment delete <issue-id> <attachment-id>
bacli issue attachment delete PROJ-123 789
```

## プロジェクト (Project)

### プロジェクトの作成

```bash
bacli project create <project-key> --name <name> [flags]

# 例: 基本的なプロジェクト作成
bacli project create NEWPROJ --name "新規プロジェクト"

# 例: オプションを指定して作成
bacli project create NEWPROJ --name "新規プロジェクト" \
  --text-format markdown \
  --use-git \
  --use-wiki
```

**flags:**
- `--name, -n`: プロジェクト名
- `--text-format`: テキスト形式 (markdown/backlog)
- `--use-git`: Gitリポジトリを有効化
- `--use-wiki`: Wikiを有効化
- `--use-subtasking`: サブタスクを有効化

### プロジェクトの編集

```bash
bacli project update <project-id> [flags]

# 例: プロジェクト名を変更
bacli project update PROJ --name "新しいプロジェクト名"

# 例: アーカイブ
bacli project update PROJ --archived
```

### プロジェクトの削除

```bash
bacli project delete <project-id>

# 例
bacli project delete PROJ
bacli project delete PROJ --force  # 確認なしで削除
```

## ウォッチ (Watch)

```bash
# 自分のウォッチ一覧
bacli watch list
bacli watch list --limit 50

# ウォッチに追加
bacli watch add <issue-id>
bacli watch add PROJ-123

# ウォッチ情報の取得
bacli watch info <watch-id>

# ウォッチから削除
bacli watch remove <watch-id>

# 既読にする
bacli watch read <watch-id>
```

## Wiki

```bash
# Wikiページ一覧
bacli wiki list --project <project-id>
bacli wiki list --project PROJ

# Wikiページの表示
bacli wiki view <wiki-id>
bacli wiki view 123
bacli wiki view 123 --web  # ブラウザで開く

# Wikiページの作成
bacli wiki create --project <project-id> --name <name> [--content <content>]
bacli wiki create --project PROJ --name "設計ドキュメント" --content "# 概要\n..."
bacli wiki create --project PROJ --name "設計ドキュメント" --file ./design.md

# Wikiページの編集
bacli wiki update <wiki-id> [--name <name>] [--content <content>]
bacli wiki update 123 --content "更新された内容"
bacli wiki update 123 --file ./updated.md

# Wikiページの削除
bacli wiki delete <wiki-id>

# Wiki添付ファイル
bacli wiki attachment list <wiki-id>
bacli wiki attachment download <wiki-id> <attachment-id>
bacli wiki attachment upload <wiki-id> <file-path>
bacli wiki attachment delete <wiki-id> <attachment-id>
```

## プルリクエスト (PR)

```bash
# プルリクエスト一覧
bacli pr list --project <project-id> --repo <repo-name>
bacli pr list --project PROJ --repo myrepo

# プルリクエストの表示
bacli pr view <project-id> <repo-name> <pr-number>
bacli pr view PROJ myrepo 42
bacli pr view PROJ myrepo 42 --web  # ブラウザで開く

# プルリクエストの作成
bacli pr create --project <project-id> --repo <repo-name> \
  --summary <summary> --base <base-branch> --branch <feature-branch>
bacli pr create --project PROJ --repo myrepo \
  --summary "新機能追加" --base main --branch feature/new-feature

# プルリクエストの編集
bacli pr update <project-id> <repo-name> <pr-number> [flags]

# プルリクエストのコメント
bacli pr comment list <project-id> <repo-name> <pr-number>
bacli pr comment add <project-id> <repo-name> <pr-number> <content>
```

## Gitリポジトリ

```bash
# リポジトリ一覧
bacli git list --project <project-id>
bacli git list --project PROJ

# リポジトリ情報
bacli git info <project-id> <repo-name>
bacli git info PROJ myrepo
```

## ユーザー (User)

```bash
# ユーザー一覧
bacli user list

# ユーザー情報
bacli user info <user-id>
bacli user info @me  # 自分の情報

# ユーザーのアクティビティ
bacli user activity <user-id>
bacli user activity @me --limit 20
```

## 通知 (Notification)

```bash
# 通知一覧
bacli notification list
bacli notification list --limit 50

# 通知数の取得
bacli notification count

# 通知を既読にする
bacli notification read <notification-id>

# 全て既読にする
bacli notification read --all
```

## スペース (Space)

```bash
# スペース情報
bacli space info

# スペースのお知らせ
bacli space notice

# 最近の更新
bacli space activity
bacli space activity --limit 50

# 容量使用状況
bacli space disk
```

## 汎用APIアクセス

細かい操作が必要なときは直接APIを叩くことができます。

```bash
bacli api <endpoint> [--method <method>] [--data <data>] [--query <key=value>...]

# 例: GET リクエスト
bacli api /users

# 例: クエリパラメータ付き
bacli api /issues --query "projectId[]=1" --query "count=100"

# 例: POST リクエスト
bacli api /issues --method POST --data '{"projectId":1,"summary":"test","issueTypeId":2,"priorityId":3}'

# 例: ファイルからデータを読み込み
bacli api /issues --method POST --data @issue.json

# 例: DELETE リクエスト
bacli api /issues/123 --method DELETE
```

## 共通オプション

すべてのコマンドで使用可能なオプション:

- `--json, -j`: JSON形式で出力
- `--quiet, -q`: 最小限の出力
- `--verbose, -v`: 詳細な出力
- `--help, -h`: ヘルプを表示
