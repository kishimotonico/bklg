   
# プロジェクトの削除

プロジェクトを削除します。

## 実行可能な権限

```
管理者

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

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
    "textFormattingRule": "markdown",
    "archived":false,
    "displayOrder": 2147483646,
    "useDevAttributes": true
}

```
   