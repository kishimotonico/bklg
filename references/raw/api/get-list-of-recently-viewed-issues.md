   
# 自分が最近見た課題一覧の取得

APIとの認証に使用しているユーザーが最近見た課題の一覧を取得します。

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
/api/v2/users/myself/recentlyViewedIssues

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
    "issue":{
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
                "archived": false
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
        "sharedFiles": [
            {
                "id": 454403,
                "projectId": 5,
                "type": "file",
                "dir": "/ユーザアイコン/",
                "name": "01_サラリーマン.png",
                "size": 2735,
                "createdUser": {
                    "id": 5686,
                    "userId": "takada",
                    "name": "takada",
                    "roleType":2,
                    "lang":"ja",
                    "nulabAccount": {
                        "nulabId": "r4iGCWu4mU64aGUJykJH4GhBwdAXMTAtVRQ5RwZTDpeaECoBs2",
                        "name": "takada",
                        "uniqueId": "takada"
                    },
                    "mailAddress":"takada@nulab.example",
                    "lastLoginTime": "2022-09-01T06:35:39Z"
                },
                "created": "2009-02-27T03:26:15Z",
                "updatedUser": {
                    "id": 5686,
                    "userId": "takada",
                    "name": "takada",
                    "roleType": 2,
                    "lang": "ja",
                    "nulabAccount": {
                        "nulabId": "r4iGCWu4mU64aGUJykJH4GhBwdAXMTAtVRQ5RwZTDpeaECoBs2",
                        "name": "takada",
                        "uniqueId": "takada"
                    },
                    "mailAddress": "takada@nulab.example",
                    "lastLoginTime": "2022-09-01T06:35:39Z"
                },
                "updated":"2009-03-03T16:57:47Z"
            },
            // ...
        ],
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
    },
    "updated": "2014-07-11T02:00:00Z"
}

```
   