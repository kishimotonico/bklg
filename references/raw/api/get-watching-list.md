   
# ウォッチ一覧の取得

ウォッチの一覧を取得します。

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
/api/v2/users/:userId/watchings

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | ユーザーのID |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| order | 文字列 | ”asc”または”desc” 指定が無い場合は”desc” |
| sort | 文字列 | ウォッチ一覧のソートに使用する属性名”created""updated""issueUpdated”指定が無い場合は”issueUpdated” |
| count | 数値 | 取得上限(1-100) 指定が無い場合は20 |
| offset | 数値 |  |
| resourceAlreadyRead | 真偽値 | ウォッチしている課題の詳細を既読かどうか。trueの場合は既読のウォッチ、falseの場合は未読のウォッチ、指定しない場合は両方のウォッチを返します。指定が無い場合は両方 |
| issueId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題のID |

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
        "resourceAlreadyRead": true,
        "note": "This is a note for the watching issue.",
        "type": "issue",
        "issue": {
            "id": 4531,
            "projectId": 2,
            "issueKey": "TEST2-17",
            "keyId": 17,
            "issueType": {
                "id": 7,
                "projectId": 2,
                "name": "Bug",
                "color": "#990000",
                "displayOrder": 0
            },
            "summary": "aaa",
            "description": "",
            "resolution": null,
            "priority": {
                "id": 3,
                "name": "Normal"
            },
            "status": {
                "id": 1,
                "projectId": 2,
                "name": "Open",
                "color": "#ed8077",
                "displayOrder": 1000
            },
            "assignee": {
                "id": 2,
                "userId": "eguchi",
                "name": "eguchi",
                "roleType": 2,
                "lang": null,
                "nulabAccount": {
                    "nulabId": "tSaVeJfRxLURSAkgfbNAfCbM7PqddYLJ3nG3BELjx6eSTbu8LD",
                    "name": "eguchi",
                    "uniqueId": "eguchi"
                },
                "mailAddress": "eguchi@nulab.example",
                "lastLoginTime": "2022-09-01T06:35:39Z"
            },
            "category": [],
            "versions": [],
            "milestone": [],
            "startDate": "2013-08-29T15:00:00Z",
            "dueDate": "2013-09-03T15:00:00Z",
            "estimatedHours": null,
            "actualHours": null,
            "parentIssueId": null,
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
            "created": "2013-04-23T07:38:59Z",
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
            "updated": "2013-09-06T09:25:41Z",
            "customFields": [],
            "attachments": [],
            "sharedFiles": [],
            "stars": []
        },
        "lastContentUpdated":"2013-10-31T06:58:59Z",
        "created": "2013-10-31T06:58:59Z",
        "updated": "2013-10-31T06:58:59Z"
    },
    // ...
]

```
   