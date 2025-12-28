   
# 課題情報の更新

課題の情報を更新します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/issues/:issueIdOrKey

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| summary | 文字列 | 課題の件名 |
| parentIssueId | 数値 | 課題の親課題のID |
| description | 文字列 | 課題の詳細 |
| statusId | 数値 | 状態のID |
| resolutionId | 数値 | 完了理由のID |
| startDate | 文字列 | 課題の開始日 (yyyy-MM-dd) |
| dueDate | 文字列 | 課題の期限日 (yyyy-MM-dd) |
| estimatedHours | 数値 | 課題の予定時間 |
| actualHours | 数値 | 課題の実績時間 |
| issueTypeId | 数値 | 課題の種別のID |
| categoryId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題のカテゴリーのID |
| versionId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題の発生バージョンのID |
| milestoneId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題のマイルストーンのID |
| priorityId | 数値 | 課題の優先度のID |
| assigneeId | 数値 | 課題の担当者のID |
| notifiedUserId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題の登録の通知を受け取るユーザーのID |
| attachmentId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 添付ファイルの送信APIが返すID |
| comment | 文字列 | コメント |

## カスタム属性

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| customField\_{id} | - | カスタム属性の値 |
| customField\_{id}\_otherValue | - | リスト属性のその他入力の値 |

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
    "projectId": 1,
    "issueKey": "BLG-1",
    "keyId": 1,
    "issueType": {
        "id": 2,
        "projectId" :1,
        "name": "タスク",
        "color": "#7ea800",
        "displayOrder": 0
    },
    "summary": "first issue",
    "description": "",
    "resolution": null,
    "priority": {
        "id": 3,
        "name": "中"
    },
    "status": {
        "id": 1,
        "projectId": 1,
        "name": "未対応",
        "color": "#ed8077",
        "displayOrder": 1000
    },
    "assignee": {
        "id": 2,
        "userId": "eguchi",
        "name": "eguchi",
        "roleType" :2,
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
    "milestone": [
        {
            "id": 30,
            "projectId": 1,
            "name": "wait for release",
            "description": "",
            "startDate": null,
            "releaseDueDate": null,
            "archived": false,
            "displayOrder": 0
        }
    ],
    "startDate": null,
    "dueDate": null,
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
    "created": "2012-07-23T06:10:15Z",
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
    "updated": "2013-02-07T08:09:49Z",
    "customFields": [],
    "attachments": [
        {
            "id": 1,
            "name": "IMGP0088.JPG",
            "size": 85079
        },
        // ...
    ],
    "sharedFiles": [],
    "stars": [
        {
            "id": 10,
            "comment": null,
            "url": "https://xx.backlog.jp/view/BLG-1",
            "title": "[BLG-1] first issue | 課題の表示 - Backlog",
            "presenter": {
                "id": 2,
                "userId": "eguchi",
                "name": "eguchi",
                "roleType": 2,
                "lang": "ja",
                "nulabAccount": {
                    "nulabId": "tSaVeJfRxLURSAkgfbNAfCbM7PqddYLJ3nG3BELjx6eSTbu8LD",
                    "name": "eguchi",
                    "uniqueId": "eguchi"
                },
                "mailAddress": "eguchi@nulab.example",
                "lastLoginTime": "2022-09-01T06:35:39Z"
            },
            "created":"2013-07-08T10:24:28Z"
        },
        // ...
    ]
}

```
   