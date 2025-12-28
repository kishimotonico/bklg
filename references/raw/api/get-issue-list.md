   
# 課題一覧の取得

課題の一覧を取得します。

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
/api/v2/issues

```
## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | プロジェクトのID |
| issueTypeId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 種別のID |
| categoryId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | カテゴリーのID |
| versionId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 発生バージョンのID |
| milestoneId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | マイルストーンのID |
| statusId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 状態のID[プロジェクト毎の状態一覧のAPI](/ja/docs/backlog/api/2/get-status-list-of-project) |
| priorityId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 優先度のID |
| assigneeId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 担当者のID |
| createdUserId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 登録者のID |
| resolutionId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 完了理由のID |
| parentChild | 数値 | 親子課題の条件0: すべて1: 子課題以外2: 子課題3: 親課題でも子課題でもない課題4: 親課題 |
| attachment | 真偽値 | 添付ファイルを含む場合はtrue |
| sharedFile | 真偽値 | 共有ファイルを含む場合はtrue |
| sort | 文字列 | 課題一覧のソートに使用する属性名”issueType""category""version""milestone""summary""status""priority""attachment""sharedFile""created""createdUser""updated""updatedUser""assignee""startDate""dueDate""estimatedHours""actualHours""childIssue""customField\_${id}“ |
| order | 文字列 | ”asc”または”desc” 指定が無い場合は”desc” |
| offset | 数値 |  |
| count | 数値 | 取得上限(1-100) 指定が無い場合は20 |
| createdSince | 文字列 | 登録日 (yyyy-MM-dd) |
| createdUntil | 文字列 | 登録日 (yyyy-MM-dd) |
| updatedSince | 文字列 | 更新日 (yyyy-MM-dd) |
| updatedUntil | 文字列 | 更新日 (yyyy-MM-dd) |
| startDateSince | 文字列 | 開始日 (yyyy-MM-dd) |
| startDateUntil | 文字列 | 開始日 (yyyy-MM-dd) |
| dueDateSince | 文字列 | 期限日 (yyyy-MM-dd) |
| dueDateUntil | 文字列 | 期限日 (yyyy-MM-dd) |
| id[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題のID |
| parentIssueId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 親課題のID |
| keyword | 文字列 | 検索キーワード |

## カスタム属性を指定した検索 (テキスト属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| customField\_${id} | 文字列 | 検索キーワード |

## カスタム属性を指定した検索 (数値属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| customField\_${id}\_min | 数値 | 最小値 |
| customField\_${id}\_max | 数値 | 最大値 |

## カスタム属性を指定した検索 (日付属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| customField\_${id}\_min | 文字列 | 最小値 |
| customField\_${id}\_max | 文字列 | 最大値 |

## カスタム属性を指定した検索 (リスト属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| customField\_${id}[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 値のID |

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
    }
]

```
   