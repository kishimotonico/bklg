   
# プルリクエストコメントの追加

プルリクエストにコメントを追加します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
POST

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

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| content (必須) | 文字列 | コメントの本文 |
| attachmentId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 添付ファイルの送信APIが返すID |
| notifiedUserId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | コメント登録の通知を受け取るユーザーID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
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
}

```
   