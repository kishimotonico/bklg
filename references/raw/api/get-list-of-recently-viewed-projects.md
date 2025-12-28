   
# 自分が最近見たプロジェクト一覧の取得

APIとの認証に使用しているユーザーが最近見たプロジェクトの一覧を取得します。

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
/api/v2/users/myself/recentlyViewedProjects

```
## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| order | 文字列 | ”asc”または”desc” 指定が無い場合は”desc” |
| offset | 数値 |  |
| count | 数値 | 取得上限(1-100) 指定が無い場合は20 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "project": {
        "id": 1,
        "projectKey": "TEST",
        "name": "test",
        "chartEnabled": true,
        "useResolvedForChart": true,
        "subtaskingEnabled": true,
        "projectLeaderCanEditProjectLeader": false,
        "useWiki": true,
        "useFileSharing": true,
        "useWikiTreeView": true,
        "useSubversion": false,
        "useGit": false,
        "useOriginalImageSizeAtWiki": false,
        "textFormattingRule": "backlog",
        "archived": false,
        "displayOrder": 3,
        "useDevAttributes": true
    },
    "updated": "2014-07-11T01:59:07Z"
}

```
   