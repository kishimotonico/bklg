   
# プルリクエストコメントの取得

プルリクエストのコメントの一覧を取得します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
GET

```
## URL

```
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/:number/comments

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |
| number | 数値 | プルリクエストの番号 |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| minId | 数値 | 最小ID |
| maxId | 数値 | 最大ID |
| count | 数値 | 取得上限(1-100) 指定が無い場合は20 |
| order | 文字列 | ”asc”または”desc” 指定が無い場合は”desc” |

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
        "id": 35,
        "content": "from api",
        "changeLog": [
            {
                "field": "dependentIssue",
                "newValue": "GIT-3",
                "originalValue": null
            }
        ],
        "createdUser": {
            "id": 1,
            "userId": "admin",
            "name": "admin",
            "roleType": 1,
            "lang": "ja",
            "nulabAccount": {
                "nulabId": "Prm9ZD9DQD5snNWcSYSwZiQoA9WFBUEa2ySznrSnSQRhdC2X8G",
                "name": "admin",
                "uniqueId": "admin"
            },
            "mailAddress": "eguchi@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        },
        "created":"2015-05-14T01:53:38Z",
        "updated":"2015-05-14T01:53:38Z",
        "stars":[],
        "notifications":[]
    },
    // ...
]

```
   