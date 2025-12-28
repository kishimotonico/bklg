   
# プロジェクトの追加

新しいプロジェクトを追加します。

## 実行可能な権限

```
管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | プロジェクト名 |
| key (必須) | 文字列 | プロジェクトキー(半角英大文字と半角数字とアンダースコアが使用できます) |
| chartEnabled | 真偽値 | チャートを使用するかどうか |
| useResolvedForChart | 真偽値 | 「処理済み」以降を「完了」とみなすどうか |
| subtaskingEnabled | 真偽値 | 親子課題を使用するかどうか |
| projectLeaderCanEditProjectLeader | 真偽値 | プロジェクト管理者も他のプロジェクト管理者を指定可能にする |
| useWiki | 真偽値 | Wikiを使用するかどうか |
| useFileSharing | 真偽値 | 共有ファイルを使用するかどうか |
| useWikiTreeView | 真偽値 | Wikiツリー表示を有効にするかどうか |
| useSubversion | 真偽値 | Subversionを使用するかどうか |
| useGit | 真偽値 | Gitを使用するかどうか |
| useOriginalImageSizeAtWiki | 真偽値 | Wikiの画像をオリジナルのサイズで表示するかどうか |
| textFormattingRule | 文字列 | テキスト整形のルール backlog または markdown |
| useDevAttributes | 真偽値 | 優先度、マイルストーン、発生バージョンを使用するかどうか |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 201 CREATED
Content-Type:application/json;charset=utf-8
Location:https://xx.backlog.jp/projects/BLG

```
### レスポンスボディ

```
{
    "id": 1,
    "projectKey": "TEST",
    "name": "test",
    "chartEnabled": false,
    "useResolvedForChart": false,
    "subtaskingEnabled": false,
    "projectLeaderCanEditProjectLeader": false,
    "useWiki": true,
    "useFileSharing": true,
    "useWikiTreeView": true,
    "useOriginalImageSizeAtWiki": false,
    "useSubversion": true,
    "useGit": true,
    "textFormattingRule": "markdown",
    "archived":false,
    "displayOrder": 2147483646,
    "useDevAttributes": true
}

```
   