# bacli-py

## 予定している使い方

### CLIの基本機能

```bash
# 認証機能: 最初はOAuth未対応で設定ファイルのアクセストークンを参照するためlogin/logoutは未実装
bacli auth login
bacli auth logout
bacli auth status

# 基本機能
bacli project list
bacli project create <project-name>
bacli project delete <project-id>
bacli project info <project-id>

bacli issue list --project <project-id>
bacli issue create --project <project-id> [flags]
bacli issue update <issue-id> [flags]

bacli issue comment add
```

- `<project-id>`: プロジェクトID。APIで利用する内部IDの他、ワークスペースで一意のプロジェクトキー(例: PROJ)でもOK
- `<issue-id>`: 課題のID。APIで利用する内部IDの他、課題キー(例: PROJ-123)や、URL(例: `https://hoge.backlog.co.jp/view/PROJ-123`)でもOK
- `[flags]`: 各種オプション。APIドキュメントを参照

上のコマンドはある程度使いやすいようにラップしているため、細かい操作が必要なときはAPIを使います

```bash
bacli api <endpoint> [--method <method>] [--data <data>] [--hearder <key:value> ...]
```

### TUI機能

必要なパラメータを省略した場合、必要な情報を対話的に入力できるTUIモードに入ります

```bash
bacli issue create --project <project-id>
```

他にも最初からTUIモードに入ることもできます

```bash
bacli
```

