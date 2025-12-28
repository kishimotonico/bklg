   
# プロジェクト一覧の取得

プロジェクトの一覧を取得します。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
GET

```
## URL

```
/api/v2/projects

```
## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| archived | 真偽値 | 省略された場合は全てのプロジェクト、falseの場合はアーカイブされていないプロジェクト、trueの場合はアーカイブされたプロジェクトを返します。 |
| all | 真偽値 | ユーザが管理者権限の場合のみ有効なパラメータです。trueの場合はすべてのプロジェクト、falseの場合は参加しているプロジェクトのみを返します。初期値はfalse。 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
[
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
        "useSubversion": true,
        "useGit": true,
        "useOriginalImageSizeAtWiki": false,
        "textFormattingRule": "markdown",
        "archived":false,
        "displayOrder": 2147483646,
        "useDevAttributes": true
    },
    // ...
]

```
   