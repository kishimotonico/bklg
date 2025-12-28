   
# プルリクエスト一覧の取得

プルリクエストの一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| statusId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 状態のID |
| assigneeId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 担当者のID |
| issueId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 関連課題のID |
| createdUserId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 登録者のID |
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
[
    {
        "id": 2,
        "projectId": 3,
        "repositoryId": 5,
        "number": 1,
        "summary": "test",
        "description": "test data",
        "base": "master",
        "branch": "develop",
        "status": {
            "id": 1,
            "name": "Open"
        },
        "assignee": {
            "id": 5,
            "userId": "testuser2",
            "name": "testuser2",
            "roleType": 1,
            "lang": null,
            "nulabAccount": {
                "nulabId": "J884YBYbiDBZcN4tj7rzcKcv8EYhekYcGfGtZ5oo7fCiGPnCjM",
                "name": "testuser2",
                "uniqueId": "testuser2"
            },
            "mailAddress": "testuser2@nulab.test",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        },
        "issue": {
            "id": 31
        },
        "baseCommit": null,
        "branchCommit": null,
        "mergeCommit": null,
        "closeAt": null,
        "mergeAt": null,
        "createdUser":{
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
        "created": "2015-04-23T03:04:14Z",
        "updatedUser": {
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
        "updated":"2015-04-23T03:04:14Z"
    },
    // ...
]

```
   