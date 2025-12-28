# bklg-py

## 予定している使い方

### CLIの基本機能

```bash
# 認証機能: 最初はOAuth未対応で設定ファイルのアクセストークンを参照するためlogin/logoutは未実装
bklg auth login
bklg auth logout
bklg auth status

# 基本機能
bklg project list
bklg project create <project-name>
bklg project delete <project-id>
bklg project info <project-id>

bklg issue list --project <project-id>
bklg issue create --project <project-id> [flags]
bklg issue update <issue-id> [flags]

bklg issue comment add
```

- `<project-id>`: プロジェクトID。APIで利用する内部IDの他、ワークスペースで一意のプロジェクトキー(例: PROJ)でもOK
- `<issue-id>`: 課題のID。APIで利用する内部IDの他、課題キー(例: PROJ-123)や、URL(例: `https://hoge.backlog.co.jp/view/PROJ-123`)でもOK
- `[flags]`: 各種オプション。APIドキュメントを参照

上のコマンドはある程度使いやすいようにラップしているため、細かい操作が必要なときはAPIを使います

```bash
bklg api <endpoint> [--method <method>] [--data <data>] [--hearder <key:value> ...]
```

### TUI機能

必要なパラメータを省略した場合、必要な情報を対話的に入力できるTUIモードに入ります

```bash
bklg issue create --project <project-id>
```

他にも最初からTUIモードに入ることもできます

```bash
bklg
```

