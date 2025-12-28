# 新規実装予定のCLIコマンド

このファイルには、今後実装予定のコマンドの使い方を記載しています。

## 課題 (Issue)

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
bklg issue update <issue-id> [flags]

# 例: ステータスを変更
bklg issue update PROJ-123 --status "処理中"

# 例: 担当者と優先度を変更
bklg issue update PROJ-123 --assignee "yamada" --priority "高"

# 例: 期限を変更
bklg issue update PROJ-123 --due-date 2024-12-31

# 例: 説明を追記
bklg issue update PROJ-123 --description "追加情報: テスト環境で再現確認済み"
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
bklg issue delete <issue-id>

# 例
bklg issue delete PROJ-123
bklg issue delete PROJ-123 --force  # 確認なしで削除
```

### 課題のコメント

```bash
# コメント一覧
bklg issue comment list <issue-id>
bklg issue comment list PROJ-123
bklg issue comment list PROJ-123 --limit 50

# コメント追加
bklg issue comment add <issue-id> <content>
bklg issue comment add PROJ-123 "対応完了しました"
bklg issue comment add PROJ-123 --file comment.txt  # ファイルから読み込み

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
bklg issue attachment list PROJ-123

# 添付ファイルのダウンロード
bklg issue attachment download <issue-id> <attachment-id> [--output <path>]
bklg issue attachment download PROJ-123 789
bklg issue attachment download PROJ-123 789 --output ./downloads/

# 全添付ファイルをダウンロード
bklg issue attachment download PROJ-123 --all --output ./downloads/

# 添付ファイルのアップロード
bklg issue attachment upload <issue-id> <file-path>
bklg issue attachment upload PROJ-123 ./screenshot.png
bklg issue attachment upload PROJ-123 ./doc1.pdf ./doc2.pdf  # 複数ファイル

# 添付ファイルの削除
bklg issue attachment delete <issue-id> <attachment-id>
bklg issue attachment delete PROJ-123 789
```

## ウォッチ (Watch)

```bash
# 自分のウォッチ一覧
bklg watch list
bklg watch list --limit 50

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

```bash
# Wikiページ一覧
bklg wiki list --project <project-id>
bklg wiki list --project PROJ

# Wikiページの表示
bklg wiki view <wiki-id>
bklg wiki view 123
bklg wiki view 123 --web  # ブラウザで開く

# Wikiページの作成
bklg wiki create --project <project-id> --name <name> [--content <content>]
bklg wiki create --project PROJ --name "設計ドキュメント" --content "# 概要\n..."
bklg wiki create --project PROJ --name "設計ドキュメント" --file ./design.md

# Wikiページの編集
bklg wiki update <wiki-id> [--name <name>] [--content <content>]
bklg wiki update 123 --content "更新された内容"
bklg wiki update 123 --file ./updated.md

# Wikiページの削除
bklg wiki delete <wiki-id>

# Wiki添付ファイル
bklg wiki attachment list <wiki-id>
bklg wiki attachment download <wiki-id> <attachment-id>
bklg wiki attachment upload <wiki-id> <file-path>
bklg wiki attachment delete <wiki-id> <attachment-id>
```

## ユーザー (User)

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

## 通知 (Notification)

```bash
# 通知一覧
bklg notification list
bklg notification list --limit 50

# 通知数の取得
bklg notification count

# 通知を既読にする
bklg notification read <notification-id>

# 全て既読にする
bklg notification read --all
```

## スペース (Space)

```bash
# スペース情報
bklg space info

# スペースのお知らせ
bklg space notice

# 最近の更新
bklg space activity
bklg space activity --limit 50

# 容量使用状況
bklg space disk
```

## 汎用APIアクセス

細かい操作が必要なときは直接APIを叩くことができます。

```bash
bklg api <endpoint> [--method <method>] [--data <data>] [--query <key=value>...]

# 例: GET リクエスト
bklg api /users

# 例: クエリパラメータ付き
bklg api /issues --query "projectId[]=1" --query "count=100"

# 例: POST リクエスト
bklg api /issues --method POST --data '{"projectId":1,"summary":"test","issueTypeId":2,"priorityId":3}'

# 例: ファイルからデータを読み込み
bklg api /issues --method POST --data @issue.json

# 例: DELETE リクエスト
bklg api /issues/123 --method DELETE
```

## 共通オプション

すべてのコマンドで使用可能なオプション:

- `--json, -j`: JSON形式で出力
- `--quiet, -q`: 最小限の出力
- `--verbose, -v`: 詳細な出力
- `--help, -h`: ヘルプを表示
