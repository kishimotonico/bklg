   
# プロジェクトグループの追加 (add-project-group)

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[プロジェクトチームの追加](/ja/docs/backlog/api/2/add-project-team)をご利用ください。

プロジェクトにグループを追加します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/groups

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| groupId | 数値 | 追加するグループのID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# Wiki添付ファイルの削除 (remove-wiki-attachment)

Wikiの添付ファイルを削除します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/wikis/:wikiId/attachments/:attachmentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |
| attachmentId | 数値 | 添付ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 2,
    "name": "Duke.png",
    "size": 196186,
    "createdUser": {
        "id": 1,
        "userId": "admin",
        "name": "admin",
        "roleType": 1,
        "lang": null,
        "nulabAccount": {
            "nulabId": "Prm9ZD9DQD5snNWcSYSwZiQoA9WFBUEa2ySznrSnSQRhdC2X8G",
            "name": "admin",
            "uniqueId": "admin"
        },
        "mailAddress": "eguchi@nulab.example",
        "lastLoginTime": "2022-09-01T06:35:39Z"
    },
    "created": "2014-07-11T06:26:05Z"
}

```
   

   
# 課題添付ファイルのダウンロード (get-issue-attachment)

課題の添付ファイルをダウンロードします。

## 実行可能な権限

```
管理者
一般ユーザー
レポーター
ゲストレポーター

```
## メソッド

```
GET

```
## URL

```
/api/v2/issues/:issueIdOrKey/attachments/:attachmentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |
| attachmentId | 数値 | 添付ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="attachment.doc"

```
   

   
# 課題に共有ファイルをリンク (link-shared-files-to-issue)

課題に共有ファイルをリンクします。

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
/api/v2/issues/:issueIdOrKey/sharedFiles

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
| fileId[] (必須) | 数値 | 共有ファイルのID |

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
        "id": 4056,
        "projectId": 5,
        "type": "file",
        "dir": "/design/",
        "name": "site.png",
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
        "updated":"2010-05-02T17:37:10Z"
    },
    // ...
]

```
   

   
# Wikiページの追加 (add-wiki-page)

WIkiの新しいページを追加します。

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
/api/v2/wikis

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectId (必須) | 数値 | プロジェクトのID |
| name (必須) | 文字列 | ページ名 |
| content (必須) | 文字列 | ページの内容 |
| mailNotify | 真偽値 | ページの追加をメールで通知する場合はtrue |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 201 CREATED
Content-Type:application/json;charset=utf-8
Location:https://xx.backlog.jp/alias/wiki/1

```
### レスポンスボディ

```
{
    "id": 1,
    "projectId": 1,
    "name": "Home",
    "content": "test",
    "tags": [
        {
            "id": 12,
            "name": "議事録"
        }
    ],
    "attachments": [],
    "sharedFiles": [],
    "stars": [],
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
    "created": "2012-07-23T06:09:48Z",
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
    "updated": "2012-07-23T06:09:48Z"
}

```
   

   
# 自分が最近見たプロジェクト一覧の取得 (get-list-of-recently-viewed-projects)

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
   

   
# Wikiページ更新履歴一覧の取得 (get-wiki-page-history)

Wikiページの更新履歴の一覧を取得します。

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
/api/v2/wikis/:wikiId/history

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |

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
        "pageId": 1,
        "version": 1,
        "name": "test",
        "content": "hello world",
        "createdUser": {
            "id": 1,
            "userId": "admin",
            "name": "admin",
            "roleType": 1,
            "lang": null,
            "nulabAccount": {
                "nulabId": "Prm9ZD9DQD5snNWcSYSwZiQoA9WFBUEa2ySznrSnSQRhdC2X8G",
                "name": "admin",
                "uniqueId": "admin"
            },
            "mailAddress": "eguchi@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        },
        "created":"2014-06-24T05:04:48Z"
    },
    // ...
]

```
   

   
# プルリクエスト添付ファイルの削除 (delete-pull-request-attachments)

プルリクエストの添付ファイルを削除します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/:number/attachments/:attachmentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |
| number | 数値 | プルリクエストの番号 |
| attachmentId | 数値 | 添付ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
        "id": 8,
        "name": "IMG0088.png",
        "size": 5563,
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
        "created": "2014-10-28T09:24:43Z"
    }

```
   

   
# プロジェクトの最近の活動の取得 (get-project-recent-updates)

プロジェクト上の最近の活動の一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/activities

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| activityTypeId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | type(1-26) |
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

2022年2月9日にレスポンスボディからnotificationsのコンテンツが削除され空の配列になります。
詳しくは[こちら](https://backlog.com/ja/product-updates/announcement/backlog-will-changes-to-the-get-recent-updates-apis/)をご確認下さい。

```
[
    {
        "id": 3153,
        "project": {
            "id": 92,
            "projectKey": "SUB",
            "name": "サブタスク",
            "chartEnabled": true,
            "useResolvedForChart": true,
            "subtaskingEnabled": true,
            "projectLeaderCanEditProjectLeader": false,
            "useWiki": true,
            "useFileSharing": true,
            "useWikiTreeView": true,
            "useOriginalImageSizeAtWiki": false,
            "textFormattingRule": "backlog",
            "archived": false,
            "displayOrder": 3,
            "useDevAttributes": true
        },
        "type": 2,
        "content": {
            "id": 4809,
            "key_id": 121,
            "summary": "コメント",
            "description": "",
            "comment": {
                "id": 7237,
                "content": ""
            },
            "changes": [
                {
                    "field": "milestone",
                    "new_value": " R2014-07-23",
                    "old_value": "",
                    "type": "standard"
                },
                {
                    "field": "status",
                    "new_value": "4",
                    "old_value": "1",
                    "type": "standard"
                }
            ]
        },
        "notifications": [],
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
        "created": "2013-12-27T07:50:44Z"
    },
    // ...
]

```
## レスポンス説明

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| type | 数値 | 最近の更新の種別：1:課題の追加2”課題の更新3:課題にコメント4:課題の削除5:Wikiを追加6:Wikiを更新7:Wikiを削除8:共有ファイルを追加9:共有ファイルを更新10:共有ファイルを削除11:Subversionコミット12:GITプッシュ13:GITリポジトリ作成14:課題をまとめて更新15:プロジェクトに参加16:プロジェクトから脱退17:コメントにお知らせを追加18:プルリクエストの追加19:プルリクエストの更新20:プルリクエストにコメント21:プルリクエストの削除22:マイルストーンの追加23:マイルストーンの更新24:マイルストーンの削除25:グループがプロジェクトに参加26:グループがプロジェクトから脱退 |
| reason | 数値 | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 |

   

   
# プロジェクトチームの追加 (add-project-team)

プロジェクトにチームを追加します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/teams

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| teamId | 数値 | 追加するチームのID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# スペースアイコン画像の取得 (get-space-logo)

スペースのアイコン画像を取得します。

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
/api/v2/space/image

```
## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="logo_mark.png"

```
   

   
# 課題情報の取得 (get-issue)

課題の情報を取得します。

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
/api/v2/issues/:issueIdOrKey

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |

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
   

   
# Webhookの取得 (get-webhook)

Webhookの情報を取得します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
GET

```
## URL

```
/api/v2/projects/:projectIdOrKey/webhooks/:webhookId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| webhookId | 文字列 | WebhookのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 3,
    "name": "webhook",
    "description": "",
    "hookUrl": "http://nulab.test/",
    "allEvent": false,
    "activityTypeIds": [1, 2, 3, 4, 5],
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
    "created": "2014-11-30T01:22:21Z",
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
    "updated": "2014-11-30T01:22:21Z"
}

```
   

   
# Wikiページ情報の更新 (update-wiki-page)

Wikiページの情報を更新します。

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
/api/v2/wikis/:wikiId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | ページ名 |
| content | 文字列 | ページの内容 |
| mailNotify | 真偽値 | ページの更新をメールで通知する場合はtrue |

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
    "name": "Home",
    "content": "test",
    "tags": [
        {
            "id": 12,
            "name": "議事録"
        }
    ],
    "attachments": [
        {
            "id": 1,
            "name": "test.json",
            "size": 8857,
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
            "created": "2014-01-06T11:10:45Z"
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
    "stars": [],
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
    "created": "2012-07-23T06:09:48Z",
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
    "updated": "2012-07-23T06:09:48Z"
}

```
   

   
# Wikiページの削除 (delete-wiki-page)

WIkiページを削除します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/wikis/:wikiId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| mailNotify | 真偽値 | ページの削除をメールで通知する場合はtrue |

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
    "name": "Home",
    "content": "test",
    "tags": [
        {
            "id": 12,
            "name": "議事録"
        }
    ],
    "attachments": [
        {
            "id": 1,
            "name": "test.json",
            "size": 8857,
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
            "created": "2014-01-06T11:10:45Z"
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
    "stars": [],
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
    "created": "2012-07-23T06:09:48Z",
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
    "updated": "2012-07-23T06:09:48Z"
}

```
   

   
# プロジェクトユーザー一覧の取得 (get-project-user-list)

プロジェクトのユーザーの一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/users

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| excludeGroupMembers | 真偽値 | グループを介してプロジェクトに参加しているメンバーを除く |

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
    // ...
]

```
   

   
# Wiki添付ファイルの追加 (attach-file-to-wiki)

Wikiに添付ファイルを追加します。

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
/api/v2/wikis/:wikiId/attachments

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| attachmentId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 添付ファイルの送信APIが返すID |

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
        "name": "Duke.png",
        "size": 196186,
        "createdUser": {
            "id": 1,
            "userId": "admin",
            "name": "admin",
            "roleType": 1,
            "lang": null,
            "nulabAccount": {
                "nulabId": "Prm9ZD9DQD5snNWcSYSwZiQoA9WFBUEa2ySznrSnSQRhdC2X8G",
                "name": "admin",
                "uniqueId": "admin"
            },
            "mailAddress": "eguchi@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        },
        "created": "2014-07-11T06:26:05Z"
    },
    // ...
]

```
   

   
# グループ情報の取得 (get-group)

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[チーム情報の取得](/ja/docs/backlog/api/2/get-team)をご利用ください。

グループの情報を取得します。

## 実行可能な権限

```
管理者

```
## メソッド

```
GET

```
## URL

```
/api/v2/groups/:groupId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| groupId | 数値 | グループのID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# 課題コメントの追加 (add-comment)

課題に新しいコメントを追加します。

## 実行可能な権限

```
管理者
一般ユーザー
レポーター
ゲストレポーター

```
## メソッド

```
POST

```
## URL

```
/api/v2/issues/:issueIdOrKey/comments

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
| content (必須) | 文字列 | コメントの本文 |
| notifiedUserId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | コメント登録の通知を受け取るユーザーID |
| attachmentId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 添付ファイルの送信APIが返すID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 201 CREATED
Content-Type:application/json;charset=utf-8
Location:https://xx.backlog.jp/view/BLG-5742#comment-6586

```
### レスポンスボディ

```
{
    "id": 6586,
    "projectId": 5,
    "issueId": 50,
    "content": "テスト",
    "changeLog": null,
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
    "created": "2013-08-05T06:15:06Z",
    "updated": "2013-08-05T06:15:06Z",
    "stars": [],
    "notifications": []
}

```
   

   
# カテゴリー情報の更新 (update-category)

カテゴリーの情報を更新します。

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
/api/v2/projects/:projectIdOrKey/categories/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カテゴリーのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | カテゴリーの名前 |

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
    "projectId": 5,
    "name": "開発",
    "displayOrder": 0
}

```
   

   
# Wikiの共有ファイルのリンクを解除 (remove-link-to-shared-file-from-wiki)

Wikiにリンクされた共有ファイルのリンクを解除します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/wikis/:wikiId/sharedFiles/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |
| id | 数値 | 共有ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 4056,
    "projectId": 5,
    "type": "file",
    "dir": "/design/",
    "name": "site.png",
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
    "updated":"2010-05-02T17:37:10Z"
}

```
   

   
# グループ一覧の取得 (get-list-of-groups)

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[チーム一覧の取得](/ja/docs/backlog/api/2/get-list-of-teams)をご利用ください。

グループの一覧を取得します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
GET

```
## URL

```
/api/v2/groups

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
[
    {
        "id": 1,
        "name": "test",
        "members": [
            {
                "id": 2,
                "userId": "developer",
                "name": "developer",
                "roleType": 2,
                "lang": null,
                "nulabAccount": {
                    "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                    "name": "developer",
                    "uniqueId": "developer"
                },
                "mailAddress": "developer@nulab.example",
                "lastLoginTime": "2022-09-01T06:35:39Z"
            }
        ],
        "displayOrder": null,
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
        "created": "2013-05-30T09:11:36Z",
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
        "updated": "2013-05-30T09:11:36Z"
    },
    // ...
]

```
   

   
# プルリクエストコメントの取得 (get-pull-request-comment)

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
   

   
# スペースのお知らせの取得 (get-space-notification)

スペースのお知らせの情報を取得します。

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
/api/v2/space/notification

```
## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "content": "Notification",
    "updated": "2013-06-18T07:55:37Z"
}

```
   

   
# 完了理由一覧の取得 (get-resolution-list)

課題に設定できる完了理由の一覧を取得します。

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
/api/v2/resolutions

```
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
        "id": 0,
        "name": "対応済み"
    },
    {
        "id": 1,
        "name": "対応しない"
    },
    {
        "id": 2,
        "name": "無効"
    },
    {
        "id": 3,
        "name": "重複"
    },
    {
        "id": 4,
        "name": "再現しない"
    }
]

```
   

   
# Wikiページのスター一覧の取得 (get-wiki-page-star)

Wikiページが受け取ったスターの一覧を取得します。

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
/api/v2/wikis/:wikiId/stars

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |

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
        "id":75,
        "comment":null,
        "url": "https://xx.backlog.jp/alias/wiki/1",
        "title": "[TEST1] Home | Wiki - Backlog",
        "presenter":{
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
        "created":"2014-01-23T10:55:19Z"
    },
    // ...
]

```
   

   
# スペース情報の取得 (get-space)

スペースの情報を取得します。

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
/api/v2/space

```
## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "spaceKey": "nulab",
    "name": "Nulab Inc.",
    "ownerId": 1,
    "lang": "ja",
    "timezone": "Asia/Tokyo",
    "reportSendTime": "08:00:00",
    "textFormattingRule": "markdown",
    "created": "2008-07-06T15:00:00Z",
    "updated": "2013-06-18T07:55:37Z"
}

```
   

   
# 課題の追加 (add-issue)

新しい課題を追加します。

## 実行可能な権限

```
管理者
一般ユーザー
レポーター
ゲストレポーター

```
## メソッド

```
POST

```
## URL

```
/api/v2/issues

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectId (必須) | 数値 | 課題を登録するプロジェクトのID |
| summary (必須) | 文字列 | 課題の件名 |
| parentIssueId | 数値 | 課題の親課題のID |
| description | 文字列 | 課題の詳細 |
| startDate | 文字列 | 課題の開始日 (yyyy-MM-dd) |
| dueDate | 文字列 | 課題の期限日 (yyyy-MM-dd) |
| estimatedHours | 数値 | 課題の予定時間 |
| actualHours | 数値 | 課題の実績時間 |
| issueTypeId (必須) | 数値 | 課題の種別のID |
| categoryId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題のカテゴリーのID |
| versionId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題の発生バージョンのID |
| milestoneId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題のマイルストーンのID |
| priorityId (必須) | 数値 | 課題の優先度のID |
| assigneeId | 数値 | 課題の担当者のID |
| notifiedUserId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題の登録の通知を受け取るユーザーのID |
| attachmentId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 添付ファイルの送信APIが返すID |

## カスタム属性

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| customField\_{id} | - | カスタム属性の値 |
| customField\_{id}\_otherValue | - | リスト属性のその他入力の値 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 201 CREATED
Content-Type:application/json;charset=utf-8
Location:https://xx.backlog.jp/view/BLG-5742

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
    "updated": "2012-07-23T06:10:15Z",
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
    "stars": []
}

```
   

   
# 課題コメントのお知らせ一覧の取得 (get-list-of-comment-notifications)

課題コメントのお知らせ一覧を取得します。

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
/api/v2/issues/:issueIdOrKey/comments/:commentId/notifications

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |
| commentId | 数値 | コメントのID |

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
        "id":22,
        "alreadyRead":false,
        "reason":2,
        "user":{
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
    "resourceAlreadyRead":false
    },
    // ...
]

```
## レスポンス説明

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| reason | 数値 | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 |

   

   
# 課題添付ファイル一覧の取得 (get-list-of-issue-attachments)

課題の添付ファイルの一覧を取得します。

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
/api/v2/issues/:issueIdOrKey/attachments

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |

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
        "id": 8,
        "name": "IMG0088.png",
        "size": 5563,
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
        "created":"2014-10-28T09:24:43Z"
    },
    // ...
]

```
   

   
# プロジェクトチームの削除 (delete-project-team)

プロジェクトからチームを削除します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/teams

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| teamId | 数値 | 削除するチームのID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# グループの追加 (add-group)

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[チームの追加](/ja/docs/backlog/api/2/add-team) をご利用ください。

グループを追加します。
[新プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)のスペースではこのAPIを利用できません。

## 実行可能な権限

```
管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/groups

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | グループ名 |
| members[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | グループに含めるユーザーID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# プロジェクト管理者の削除 (delete-project-administrator)

プロジェクトユーザーからプロジェクト管理者権限を削除します。

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
/api/v2/projects/:projectIdOrKey/administrators

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | 削除するユーザーのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
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
}

```
   

   
# プルリクエストコメント数の取得 (get-number-of-pull-request-comments)

プルリクエストに登録されているコメントの数を取得します。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/:number/comments/count

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |
| number | 数値 | プルリクエストの番号 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "count": 10
}

```
   

   
# チーム情報の更新 (update-team)

チームの情報を更新します。
[新プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)のスペースではこのAPIを利用できません。

## 実行可能な権限

```
管理者

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/teams/:teamId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| teamId | 数値 | チームのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | チーム名 |
| members[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | チームに含めるユーザーID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
## 課題の参加者一覧の取得

課題の参加者一覧を取得します。

### メソッド

```
GET

```
### URL

```
/api/v2/issues/:issueIdOrKey/participants

```
### URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |

### レスポンス例

#### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
#### レスポンスボディ

```
[
    {
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
    // ...
]

```
   

   
# バージョン(マイルストーン)の削除 (delete-version)

バージョン(マイルストーン)を削除します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/versions/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | バージョンのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 3,
    "projectId": 1,
    "name": "いますぐ",
    "description": "",
    "startDate": null,
    "releaseDueDate": null,
    "archived": false,
    "displayOrder": 0
}

```
   

   
# ウォッチの削除 (delete-watching)

ウォッチを削除します。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/watchings/:watchingId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| watchingId | 数値 | ウォッチのID |

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
    "note": "This is an updated note for the watching.",
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
}

```
   

   
# ユーザーの受け取ったスター一覧の取得 (get-received-star-list)

ユーザーの受け取ったスターの一覧を取得します。

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
/api/v2/users/:userId/stars

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | ユーザーのID |

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
        "id":75,
        "comment":null,
        "url": "https://xx.backlog.jp/view/BLG-1",
        "title": "[BLG-1] first issue | 課題の表示 - Backlog",
        "presenter":{
            "id":1,
            "userId": "admin",
            "name":"admin",
            "roleType":1,
            "lang":"ja",
            "nulabAccount": {
                "nulabId": "Prm9ZD9DQD5snNWcSYSwZiQoA9WFBUEa2ySznrSnSQRhdC2X8G",
                "name": "admin",
                "uniqueId": "admin"
            },
            "mailAddress":"eguchi@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        },
        "created":"2014-01-23T10:55:19Z"
    },
    // ...
]

```
   

   
# グループ情報の更新 (update-group)

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[チーム情報の更新](/ja/docs/backlog/api/2/update-team)をご利用ください。

グループの情報を更新します。
[新プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)のスペースではこのAPIを利用できません。

## 実行可能な権限

```
管理者

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/groups/:groupId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| groupId | 数値 | グループのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | グループ名 |
| members[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | グループに含めるユーザーID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# プルリクエストの取得 (get-pull-request)

プルリクエストを取得します。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/:number

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |
| number | 数値 | プルリクエストの番号 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
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
            "name": "未対応"
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
            "mailAddress": "eguchi@nulab.example"
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
    "updated":"2015-04-23T03:04:14Z",
    "attachments": [],
    "stars": []
}

```
   

   
# Wikiページ数の取得 (count-wiki-page)

Wikiページの数を取得します。

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
/api/v2/wikis/count

```
## クエリパラメーター

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
    "count": 5
}

```
   

   
# お知らせ数のリセット (reset-unread-notification-count)

自分の受け取ったお知らせの未読数をリセットします。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
POST

```
## URL

```
/api/v2/notifications/markAsRead

```
## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "count": 4
}

```
   

   
# Webhookの更新 (update-webhook)

Webhookの情報を更新します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/projects/:projectIdOrKey/webhooks/:webhookId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| webhookId | 文字列 | WebhookのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | 名前 |
| description | 文字列 | 詳細 |
| hookUrl | 文字列 | hook URL |
| allEvent | 真偽値 | 全てのイベントを通知 |
| activityTypeIds[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 通知するイベントのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 3,
    "name": "webhook",
    "description": "",
    "hookUrl": "http://nulab.test/",
    "allEvent": false,
    "activityTypeIds": [1, 2, 3, 4, 5],
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
    "created": "2014-11-30T01:22:21Z",
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
    "updated": "2014-11-30T01:22:21Z"
}

```
   

   
# Webhook一覧の取得 (get-list-of-webhooks)

Webhookの一覧を取得します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
GET

```
## URL

```
/api/v2/projects/:projectIdOrKey/webhooks

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
[
    {
        "id": 3,
        "name": "webhook",
        "description": "",
        "hookUrl": "http://nulab.test/",
        "allEvent": false,
        "activityTypeIds": [1, 2, 3, 4, 5],
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
        "created": "2014-11-30T01:22:21Z",
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
        "updated": "2014-11-30T01:22:21Z"
    },
    // ...
]

```
   

   
# チームアイコンの取得 (get-team-icon)

チームアイコン画像を取得します。

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
/api/v2/teams/:teamId/icon

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| teamId | 数値 | チームのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="team_168.gif"

```
   

   
# プルリクエストの更新 (update-pull-request)

プルリクエストを更新します。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/:number

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
| summary | 文字列 | プルリクエストの件名 |
| description | 文字列 | プルリクエストの詳細 |
| issueId | 数値 | 関連課題のID |
| assigneeId | 数値 | プルリクエストの担当者のID |
| notifiedUserId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | プルリクエストの登録の通知を受け取るユーザーのID |
| comment | 文字列 | コメント |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
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
            "name": "未対応"
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
    "updated":"2015-04-23T03:04:14Z",
    "attachments": [],
    "stars": []
}

```
   

   
# 課題一覧の取得 (get-issue-list)

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
   

   
# 状態一覧の取得 (get-status-list)

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[プロジェクトの状態一覧の取得](/ja/docs/backlog/api/2/get-status-list-of-project)をご利用ください。

課題に設定できる状態の一覧を取得します。

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
/api/v2/statuses

```
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
        "name": "未対応"
    },
    {
        "id": 2,
        "name": "処理中"
    },
    {
        "id": 3,
        "name": "処理済み"
    },
    {
        "id": 4,
        "name": "完了"
    }
]

```
   

   
# カスタム属性の削除 (delete-custom-field)

カスタム属性を削除します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/customFields/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カスタム属性のID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 2,
    "projectId": 5,
    "typeId": 1,
    "name": "バグ専用属性",
    "description": "",
    "required": false,
    "applicableIssueTypes": [1]
}

```
   

   
# 自分が最近見た課題一覧の取得 (get-list-of-recently-viewed-issues)

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
   

   
# ウォッチの追加 (add-watching)

ウォッチを追加します。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
POST

```
## URL

```
/api/v2/watchings

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey (必須) | 文字列 | 課題のID または 課題キー |
| note | 文字列 | メモ |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 201 CREATED
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 1,
    "note": "This is a note for the watching.",
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
}

```
   

   
# 課題の共有ファイルのリンクを解除 (remove-link-to-shared-file-from-issue)

課題にリンクされた共有ファイルのリンクを解除します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/issues/:issueIdOrKey/sharedFiles/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |
| id | 数値 | 共有ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 4056,
    "projectId": 5,
    "type": "file",
    "dir": "/design/",
    "name": "site.png",
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
    "updated":"2010-05-02T17:37:10Z"
}

```
   

   
# 種別一覧の取得 (get-issue-type-list)

プロジェクトに登録されている種別の一覧を返します。

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
/api/v2/projects/:projectIdOrKey/issueTypes

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
[
    {
        "id": 1,
        "projectId": 1,
        "name": "バグ",
        "color": "#990000",
        "displayOrder": 0,
        "templateSummary": "件名",
        "templateDescription": "詳細"
    },
    // ...
]

```
   

   
# 状態の追加 (add-status)

プロジェクトに状態を追加します。
1プロジェクトにつき8個まで状態を追加できます。 標準の4つの状態と合わせると、合計12個の状態を設定できます。

## 実行可能な権限

```
管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/statuses

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | 状態の名前 |
| color (必須) | 文字列 | 状態の背景色：以下から指定”#ea2c00""#e87758""#e07b9a""#868cb7""#3b9dbd""#4caf93""#b0be3c""#eda62a""#f42858""#393939” |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 101,
    "projectId": 1,
    "name": "レビュー待ち",
    "color": "#e87758",
    "displayOrder": 3999
}

```
   

   
# プロジェクトの状態一覧の取得 (get-status-list-of-project)

プロジェクト固有の課題に設定できる状態一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/statuses

```
## URL パラメーター

| Parameter Name | Type | Description |
| --- | --- | --- |
| projectIdOrKey | String | Project ID or Project Key |

## レスポンス名

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
        "name": "未対応",
        "color": "#ed8077",
        "displayOrder": 1000
    },
    // ...
]

```
   

   
# 状態情報の更新 (update-status)

追加した状態の情報を更新します。

## 実行可能な権限

```
管理者

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/projects/:projectIdOrKey/statuses/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | 状態のID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | 状態の名前 |
| color | 文字列 | 状態の背景色；以下から指定”#ea2c00""#e87758""#e07b9a""#868cb7""#3b9dbd""#4caf93""#b0be3c""#eda62a""#f42858""#393939” |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 101,
    "projectId": 1,
    "name": "レビュー待ち",
    "color": "#e87758",
    "displayOrder": 3999
}

```
   

   
# グループの削除 (delete-group)

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[チームの削除](/ja/docs/backlog/api/2/delete-team) をご利用ください。

グループを削除します。
[新プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)のスペースではこのAPIを利用できません。

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
/api/v2/groups/:groupId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| groupId | 数値 | グループのID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# 種別情報の更新 (update-issue-type)

種別の情報を更新します。

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
/api/v2/projects/:projectIdOrKey/issueTypes/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | 種別のID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | 種別の名前 |
| color | 文字列 | 種別の背景色 |
| templateSummary | 文字列 | 課題テンプレートの件名 |
| templateDescription | 文字列 | 課題テンプレートの詳細 |

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
    "name": "バグ",
    "color": "#990000",
    "displayOrder": 0,
    "templateSummary": "件名",
    "templateDescription": "詳細"
}

```
   

   
# レート制限情報の取得 (get-rate-limit)

使用中のAPIキーに対応するユーザーに対して、現在設定されているレート制限に関する情報を取得します。

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
/api/v2/rateLimit

```
## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
  "rateLimit": {
    "read": {
      "limit": 600,
      "remaining": 600,
      "reset": 1603881873
    },
    "update": {
      "limit": 150,
      "remaining": 150,
      "reset": 1603881873
    },
    "search": {
      "limit": 150,
      "remaining": 150,
      "reset": 1603881873
    },
    "icon": {
      "limit": 60,
      "remaining": 60,
      "reset": 1603881873
    }
  }
}

```
   

   
# カスタム属性一覧の取得 (get-custom-field-list)

プロジェクトに登録されているカスタム属性の一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/customFields

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
[
    {
        "id": 1,
        "projectId": 5,
        "typeId": 6,
        "name": "custom",
        "description": "",
        "required": false,
        "applicableIssueTypes": [],
        "allowAddItem": false,
        "items": [
            {
                "id": 1,
                "name": "Windows 8",
                "displayOrder": 0
            },
            // ...
        ]
    },
    {
        "id": 2,
        "typeId": 1,
        "name": "バグ専用属性",
        "description": "",
        "required": false,
        "applicableIssueTypes": [1]
    },
    // ...
]

```
   

   
# 課題コメントの取得 (get-comment-list)

課題に登録されているコメントの一覧を取得します。

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
/api/v2/issues/:issueIdOrKey/comments

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |

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
        "id": 6586,
        "projectId": 5,
        "issueId": 50,
        "content": "テスト",
        "changeLog": null,
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
        "created": "2013-08-05T06:15:06Z",
        "updated": "2013-08-05T06:15:06Z",
        "stars": [],
        "notifications": []
    },
    // ...
]

```
   

   
# プロジェクトアイコンの取得 (get-project-icon)

プロジェクトのアイコン画像を取得します。

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
/api/v2/projects/:projectIdOrKey/image

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="logo_mark.png"

```
   

   
# プルリクエスト添付ファイルのダウンロード (download-pull-request-attachment)

プルリクエストの添付ファイルをダウンロードします。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/:number/attachments/:attachmentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |
| number | 数値 | プルリクエストの番号 |
| attachmentId | 数値 | 添付ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="attachment.doc"

```
   

   
# ユーザー一覧の取得 (get-user-list)

スペースのユーザーの一覧を取得します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
GET

```
## URL

```
/api/v2/users

```
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
    // ...
]

```
## レスポンス説明

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| lang | 文字列 | ユーザーの言語設定。`"en"` 英語`"ja"` 日本語`null` 未指定 |
| roleType | 数値 | ユーザーの権限。利用する[スペースの契約プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)により値の意味が異なります。クラシックプランの場合:`1` 管理者`2` 一般ユーザー`3` レポーター`4` ビューワー`5` ゲストレポーター`6` ゲストビューワー新プランの場合:`1` 管理者`2` 一般ユーザー、ゲスト（制限：制限なし）`3` 一般ユーザー、ゲスト（制限：課題の登録のみ）`4` 一般ユーザー、ゲスト（制限：課題の閲覧のみ） |

   

   
# 選択リストカスタム属性のリスト項目の追加 (add-list-item-for-list-type-custom-field)

選択リスト形式のカスタム属性のリスト項目を追加します。
「課題の追加/編集時に選択肢を追加できる」の設定が無効な場合は管理者権限のユーザーのみ呼び出せます。
指定されたカスタム属性が選択リスト形式でない場合はエラーになります。

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
/api/v2/projects/:projectIdOrKey/customFields/:id/items

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カスタム属性のID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | リスト項目の名前 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 8,
    "projectId": 5,
    "typeId": 5,
    "name": "language",
    "description": "",
    "required": false,
    "applicableIssueTypes": [ ],
    "allowAddItem": true,
    "items": [
        {
            "id": 1,
            "name": "java",
            "displayOrder": 0
        },
        // ...
    ]
}

```
   

   
# スペースの容量使用状況の取得 (get-space-disk-usage)

スペースの容量使用状況の情報を取得します。

## 実行可能な権限

```
管理者

```
## メソッド

```
GET

```
## URL

```
/api/v2/space/diskUsage

```
## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "capacity": 1073741824,
    "issue": 119511,
    "wiki": 48575,
    "file": 0,
    "subversion": 0,
    "git": 0,
    "gitLFS": 0,
    "details":[
        {
            "projectId": 1,
            "issue": 11931,
            "wiki": 0,
            "file": 0,
            "subversion": 0,
            "git": 0,
            "gitLFS": 0
        },
        // ...
    ]
}

```
   

   
# 最近の更新の取得 (get-recent-updates)

スペース上で行われた最近の更新の一覧を取得します。

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
/api/v2/space/activities

```
## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| activityTypeId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | type(1-26) |
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

2022年2月9日にレスポンスボディからnotificationsのコンテンツが削除され空の配列になります。
詳しくは[こちら](https://backlog.com/ja/product-updates/announcement/backlog-will-changes-to-the-get-recent-updates-apis/)をご確認下さい。

```
[
    {
        "id": 3153,
        "project": {
            "id": 92,
            "projectKey": "SUB",
            "name": "サブタスク",
            "chartEnabled": true,
            "useResolvedForChart": true,
            "subtaskingEnabled": true,
            "projectLeaderCanEditProjectLeader": false,
            "useWiki": true,
            "useFileSharing": true,
            "useWikiTreeView": true,
            "useOriginalImageSizeAtWiki": false,
            "textFormattingRule": "backlog",
            "archived": false,
            "displayOrder": 3,
            "useDevAttributes": true
        },
        "type": 2,
        "content": {
            "id": 4809,
            "key_id": 121,
            "summary": "コメント",
            "description": "",
            "comment": {
                "id": 7237,
                "content": ""
            },
            "changes": [
                {
                    "field": "milestone",
                    "new_value": "R2014-07-23",
                    "old_value": "",
                    "type": "standard"
                },
                {
                    "field": "status",
                    "new_value": "4",
                    "old_value": "1",
                    "type": "standard"
                }
            ]
        },
        "notifications": [],
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
        "created": "2013-12-27T07:50:44Z"
    },
    // ...
]

```
## レスポンス説明

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| type | 数値 | 最近の更新の種別：1:課題の追加2:課題の更新3:課題にコメント4:課題の削除5:Wikiを追加6:Wikiを更新7:Wikiを削除8:共有ファイルを追加9:共有ファイルを更新10:共有ファイルを削除11:Subversionコミット12:GITプッシュ13:GITリポジトリ作成14:課題をまとめて更新15:ユーザーがプロジェクトに参加16:ユーザーがプロジェクトから脱退17:コメントにお知らせを追加18:プルリクエストの追加19:プルリクエストの更新20:プルリクエストにコメント21:プルリクエストの削除22:マイルストーンの追加23:マイルストーンの更新24:マイルストーンの削除25:グループがプロジェクトに参加26:グループがプロジェクトから脱退 |
| reason | 数値 | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 |

   

   
# Wiki添付ファイルのダウンロード (get-wiki-page-attachment)

Wikiの添付ファイルをダウンロードします。

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
/api/v2/wikis/:wikiId/attachments/:attachmentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |
| attachmentId | 数値 | 添付ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="attachment.doc"

```
### レスポンスボディ

   

   
# 課題コメント情報の取得 (get-comment)

課題コメントの詳細を取得します。

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
/api/v2/issues/:issueIdOrKey/comments/:commentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |
| commentId | 数値 | コメントのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 6586,
    "projectId": 5,
    "issueId": 50,
    "content": "テスト",
    "changeLog": null,
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
    "created": "2013-08-05T06:15:06Z",
    "updated": "2013-08-05T06:15:06Z",
    "stars": [],
    "notifications": []
}

```
   

   
# 添付ファイルの送信 (post-attachment-file)

課題、コメントまたはWikiに添付するファイルを送信し、添付ファイルに発行されたIDを取得します。

送信されたファイルは添付された後に削除されます。また添付されなかった場合は1時間後に削除されます。

## 実行可能な権限

```
管理者
一般ユーザー
レポーター
ゲストレポーター

```
## メソッド

```
POST

```
## URL

```
/api/v2/space/attachment

```
## リクエストパラメーター

```
// 全体
--- Content-Type:multipart/form-data
// ファイル部のパート
--- Content-Disposition: form-data; name="file"; filename="ファイル名"
--- Content-Type: application/octet-stream 等

```
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
    "name": "test.txt",
    "size": 8857
}

```
   

   
# アクティビティの取得 (get-activity)

アクティビティの詳細を返します。

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
/api/v2/activities/:activityId

```
## URL parameters

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| activityId | 数値 | アクティビティのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
  "id": 3153,
  "project": {
    "id": 92,
    "projectKey": "SUB",
    "name": "Subtasking",
    "chartEnabled": true,
    "useResolvedForChart": true,
    "subtaskingEnabled": true,
    "projectLeaderCanEditProjectLeader": false,
    "useWiki": true,
    "useFileSharing": true,
    "useWikiTreeView": true,
    "useOriginalImageSizeAtWiki": false,
    "textFormattingRule": "backlog",
    "archived": false,
    "displayOrder": 3,
    "useDevAttributes": true
  },
  "type": 0,
  "content": {
    "id": 92,
    "key_id": 121,
    "summary": "Comment",
    "description": "string",
    "comment": {
      "id": 7237,
      "content": "Comment"
    },
    "changes": [
      {
        "field": "milestone",
        "new_value": "R2014-07-23",
        "old_value": null,
        "type": "standard"
      }
    ]
  },
  "notifications": [
    {
      "id": 25,
      "alreadyRead": false,
      "reason": 2,
      "user": {
        "id": 25,
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
      }
    }
  ],
  "createdUser": {
    "id": 25,
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
  "created": "2013-12-27T07:50:44Z"
}

```
## レスポンス説明

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| type | 数値 | 最近の更新の種別：1:課題の追加2:課題の更新3:課題にコメント4:課題の削除5:Wikiを追加6:Wikiを更新7:Wikiを削除8:共有ファイルを追加9:共有ファイルを更新10:共有ファイルを削除11:Subversionコミット12:GITプッシュ13:GITリポジトリ作成14:課題をまとめて更新15:ユーザーがプロジェクトに参加16:ユーザーがプロジェクトから脱退17:コメントにお知らせを追加18:プルリクエストの追加19:プルリクエストの更新20:プルリクエストにコメント21:プルリクエストの削除22:マイルストーンの追加23:マイルストーンの更新24:マイルストーンの削除25:グループがプロジェクトに参加26:グループがプロジェクトから脱退 |
| reason | 数値 | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 |

   

   
# プルリクエスト一覧の取得 (get-pull-request-list)

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
   

   
# 課題数の取得 (count-issue)

課題の数を取得します。

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
/api/v2/issues/count

```
## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | プロジェクトのID |
| issueTypeId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 種別のID |
| categoryId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | カテゴリーのID |
| versionId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 発生バージョンのID |
| milestoneId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | マイルストーンのID |
| statusId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 状態のID |
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
{
    "count": 43
}

```
   

   
# Webhookの追加 (add-webhook)

Webhookを追加します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/webhooks

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | 名前 |
| description | 文字列 | 詳細 |
| hookUrl | 文字列 | hook URL |
| allEvent | 真偽値 | 全てのイベントを通知 |
| activityTypeIds[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 通知するイベントのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 3,
    "name": "webhook",
    "description": "",
    "hookUrl": "http://nulab.test/",
    "allEvent": false,
    "activityTypeIds": [1, 2, 3, 4, 5],
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
    "created": "2014-11-30T01:22:21Z",
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
    "updated": "2014-11-30T01:22:21Z"
}

```
   

   
# Gitリポジトリの取得 (get-git-repository)

Gitリポジトリを取得します。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id":1,
    "projectId":151,
    "name":"app",
    "description":"",
    "hookUrl":null,
    "httpUrl":"https://xx.backlog.jp/git/BLG/app.git",
    "sshUrl":"xx@xx.git.backlog.jp:/BLG/app.git",
    "displayOrder":0,
    "pushedAt":null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# ユーザーの追加 (add-user)

スペースに新しいユーザーを追加します。
プロジェクト管理者は管理者権限のユーザを追加することは出来ません。
[新プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)のスペースではこのAPIを利用できません。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/users

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId (必須) | 文字列 | ユーザID |
| password (必須) | 文字列 | パスワード |
| name (必須) | 文字列 | ハンドルネーム |
| mailAddress (必須) | 文字列 | メールアドレス |
| roleType (必須) | 数値 | 管理者(1) 一般ユーザー(2) レポーター(3) ビューワー(4) ゲストレポーター(5) ゲストビューワー(6) |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 201 CREATED
Content-Type:application/json;charset=utf-8
Location:https://xx.backlog.jp/user/eguchi

```
### レスポンスボディ

```
{
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
}

```
   

   
# ウォッチ一覧の取得 (get-watching-list)

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
   

   
# ウォッチ情報の取得 (get-watching)

ウォッチの情報を追加します。

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
/api/v2/watchings/:watchingId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| watchingId | 数値 | ウォッチのID |

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
    "alreadyRead": true,
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
}

```
   

   
# プロジェクトユーザーの削除 (delete-project-user)

プロジェクトからユーザーを削除します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/users

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | 削除するユーザーのID |

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
}

```
   

   
# バージョン(マイルストーン)の追加 (add-version-milestone)

プロジェクトにバージョン(マイルストーン)を追加します。

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
/api/v2/projects/:projectIdOrKey/versions

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | バージョンの名前 |
| description | 文字列 | バージョンの説明 |
| startDate | 文字列 | バージョンの開始日 (yyyy-MM-dd) |
| releaseDueDate | 文字列 | バージョンのリリース予定日 (yyyy-MM-dd) |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 3,
    "projectId": 1,
    "name": "いますぐ",
    "description": "",
    "startDate": null,
    "releaseDueDate": null,
    "archived": false,
    "displayOrder": 0
}

```
   

   
# プロジェクト一覧の取得 (get-project-list)

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
   

   
# 課題コメントにお知らせを追加 (add-comment-notification)

コメントにお知らせを追加します

認証ユーザー自身が登録したコメントのみお知らせを追加することが出来ます。

## 実行可能な権限

```
管理者
一般ユーザー
レポーター
ゲストレポーター

```
## メソッド

```
POST

```
## URL

```
/api/v2/issues/:issueIdOrKey/comments/:commentId/notifications

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |
| commentId | 数値 | コメントのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| notifiedUserId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 課題の登録の通知を受け取るユーザーのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 6586,
    "projectId": 5,
    "issueId": 50,
    "content": "テスト",
    "changeLog": null,
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
    "created": "2013-08-05T06:15:06Z",
    "updated": "2013-08-05T06:15:06Z",
    "stars": [],
    "notifications": [
        {
            "id":22,
            "alreadyRead":false,
            "reason":2,
            "user":{
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
        "resourceAlreadyRead":false
        },
        // ...
    ]
}

```
## レスポンス説明

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| reason | 数値 | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 |

   

   
# ウォッチの更新 (update-watching)

ウォッチを更新します。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/watchings/:watchingId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| watchingId | 数値 | ウォッチのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| note | 文字列 | メモ |

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
    "note": "This is an updated note for the watching.",
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
}

```
   

   
# 課題の削除 (delete-issue)

課題を削除します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/issues/:issueIdOrKey

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |

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
   

   
# 状態の削除 (delete-status)

プロジェクトから状態を削除します。

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
/api/v2/projects/:projectIdOrKey/statuses/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | 状態のID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| substituteStatusId (必須) | 数値 | 紐づく課題を付け替える先の状態のID。削除対象の状態が設定されている課題がある場合、このパラメーターで指定した状態へ一括変更します。 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 101,
    "projectId": 1,
    "name": "レビュー待ち",
    "color": "#e87758",
    "displayOrder": 3999
}

```
   

   
# バージョン(マイルストーン)一覧の取得 (get-version-milestone-list)

プロジェクトに登録されているバージョン(マイルストーン)の一覧を返します。

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
/api/v2/projects/:projectIdOrKey/versions

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
[
    {
        "id": 3,
        "projectId": 1,
        "name": "いますぐ",
        "description": "",
        "startDate": null,
        "releaseDueDate": null,
        "archived": false,
        "displayOrder": 0
    },
    // ...
]

```
   

   
# チームの追加 (add-team)

チームを追加します。
[新プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)のスペースではこのAPIを利用できません。

## 実行可能な権限

```
管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/teams

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | グループ名 |
| members[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | グループに含めるユーザーID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# 選択リストカスタム属性のリスト項目の更新 (update-list-item-for-list-type-custom-field)

選択リスト形式のカスタム属性のリスト項目を更新します。
指定されたカスタム属性が選択リスト形式でない場合はエラーになります。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/projects/:projectIdOrKey/customFields/:id/items/:itemId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カスタム属性のID |
| itemId | 数値 | リスト項目のID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | リスト項目の名前 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 8,
    "projectId": 5,
    "typeId": 5,
    "name": "language",
    "description": "",
    "required": false,
    "applicableIssueTypes": [ ],
    "allowAddItem": true,
    "items": [
        {
            "id": 1,
            "name": "java",
            "displayOrder": 0
        },
        // ...
    ]
}

```
   

   
# プルリクエスト添付ファイル一覧の取得 (get-list-of-pull-request-attachment)

プルリクエストの添付ファイルの一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/:number/attachments

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |
| number | 数値 | プルリクエストの番号 |

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
        "id": 8,
        "name": "IMG0088.png",
        "size": 5563,
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
        "created": "2014-10-28T09:24:43Z"
    },
    // ...
]

```
   

   
# カスタム属性の追加 (add-custom-field)

プロジェクトに新しいカスタム属性を追加します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/customFields

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| typeId (必須) | 数値 | カスタム属性の形式1: 文字列2: 文章3: 数値4: 日付5: 単一リスト6: 複数リスト7: チェックボックス8: ラジオ |
| name (必須) | 文字列 | カスタム属性の名前 |
| applicableIssueTypes[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | カスタム属性を有効にする種別ID空の場合、すべての課題種別で有効 |
| description | 文字列 | カスタム属性の説明 |
| required | 真偽値 | 必須な属性とする場合はtrue |

## 追加パラメーター (数値属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| min | 数値 | 最小値 |
| max | 数値 | 最大値 |
| initialValue | 数値 | 初期値 |
| unit | 文字列 | 単位 |

## 追加パラメーター (日付属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| min | 文字列 | 最小値 (yyyy-MM-dd) |
| max | 文字列 | 最大値 (yyyy-MM-dd) |
| initialValueType | 数値 | 1:当日 2: 当日 + initialShift 3:指定日 |
| initialDate | 文字列 | 初期値 (yyyy-MM-dd) |
| initialShift | 数値 | 差分日数 |

## 追加パラメーター (リスト属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| items[][(複数指定可)](/ja/docs/backlog/tips) | 文字列 | リスト項目 |
| allowInput | 真偽値 | その他直接入力を許可 |
| allowAddItem | 真偽値 | 項目の追加を許可 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 2,
    "projectId": 5,
    "typeId": 1,
    "name": "バグ専用属性",
    "description": "",
    "required": false,
    "applicableIssueTypes": [1]
}

```
   

   
# プロジェクト情報の更新 (update-project)

プロジェクトの情報を更新します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/projects/:projectIdOrKey

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | プロジェクト名 |
| key | 文字列 | プロジェクトキー |
| chartEnabled | 真偽値 | チャートを使用するかどうか |
| useResolvedForChart | 真偽値 | 「処理済み」以降を「完了」とみなすどうか |
| subtaskingEnabled | 真偽値 | 親子課題を使用するかどうか |
| projectLeaderCanEditProjectLeader | 真偽値 | プロジェクト管理者も他のプロジェクト管理者を指定可能にする |
| useWiki | 真偽値 | Wikiを使用するかどうか |
| useFileSharing | 真偽値 | 共有ファイルを使用するかどうか |
| useWikiTreeView | 真偽値 | Wikiツリー表示を有効にするかどうか |
| useSubversion | 真偽値 | Subversionを使用するかどうか |
| useGit | 真偽値 | Gitを使用するかどうか |
| useOriginalImageSizeAtWiki | 真偽値 | Wikiの画像をオリジナルのサイズで表示するかどうか |
| textFormattingRule | 文字列 | テキスト整形のルール backlog または markdown |
| archived | 真偽値 | プロジェクトの一覧に表示するかどうか |
| useDevAttributes | 真偽値 | 優先度、マイルストーン、発生バージョンを使用するかどうか |

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
    "useSubversion": true,
    "useGit": true,
    "textFormattingRule": "markdown",
    "archived":false,
    "displayOrder": 2147483646,
    "useDevAttributes": true
}

```
   

   
# ウォッチ数の取得 (count-watching)

ウォッチの数を取得します。

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
/api/v2/users/:userId/watchings/count

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | ユーザーのID |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| resourceAlreadyRead | 真偽値 | 既読かどうか。trueの場合は既読のウォッチ、falseの場合は未読のウォッチ、指定しない場合は両方のウォッチを返します。指定が無い場合は両方 |
| alreadyRead | 真偽値 | ウォッチメニューの一覧表示後に更新されたウォッチの件数を返します。trueの場合はウォッチメニューを表示した後に更新されていない(既読状態の)件数を返します。falseの場合はウォッチメニューを表示した後に更新された(未読状態の)ウォッチの件数を返します。指定が無い場合は両方を合わせた件数を返します。resourceAlreadyReadが指定してある場合、alreadyReadは使用されません。 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "count": 138
}

```
   

   
# 自分が最近見たWikiの追加 (add-recently-viewed-wiki)

APIとの認証に使用しているユーザーが最近見たWikiを追加します。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
POST

```
## URL

```
/api/v2/users/myself/recentlyViewedWikis

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId (必須) | 数値 | WikiページのId |

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
    "name": "Home",
    "content": "test",
    "tags": [
        {
            "id": 12,
            "name": "議事録"
        }
    ],
    "attachments": [
        {
            "id": 1,
            "name": "test.json",
            "size": 8857,
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
            "created": "2014-01-06T11:10:45Z"
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
    "stars": [],
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
    "created": "2012-07-23T06:09:48Z",
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
    "updated": "2012-07-23T06:09:48Z"
}


```
   

   
# プルリクエストの追加 (add-pull-request)

プルリクエストを追加します。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| summary (必須) | 文字列 | プルリクエストの件名 |
| description (必須) | 文字列 | プルリクエストの詳細 |
| base (必須) | 文字列 | マージ先のブランチ名 |
| branch (必須) | 文字列 | マージされるブランチ名 |
| issueId | 数値 | 関連課題のID |
| assigneeId | 数値 | プルリクエストの担当者のID |
| notifiedUserId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | プルリクエストの登録の通知を受け取るユーザーのID |
| attachmentId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 添付ファイルの送信APIが返すID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
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
            "name": "未対応"
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
    "baseCommit": null,
    "branchCommit": null,
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
}

```
   

   
# グループアイコンの取得 (get-group-icon)

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[チームアイコンの取得](/ja/docs/backlog/api/2/get-team-icon)をご利用ください。

グループのアイコン画像を取得します。

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
/api/v2/groups/:groupId/icon

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| groupId | 数値 | グループのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="group_168.gif"

```
   

   
# 選択リストカスタム属性のリスト項目の削除 (delete-list-item-for-list-type-custom-field)

選択リスト形式のカスタム属性のリスト項目を削除します。
指定されたカスタム属性が選択リスト形式でない場合はエラーになります。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/customFields/:id/items/:itemId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カスタム属性のID |
| itemId | 数値 | リスト項目のID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 8,
    "projectId": 5,
    "typeId": 5,
    "name": "language",
    "description": "",
    "required": false,
    "applicableIssueTypes": [ ],
    "allowAddItem": true,
    "items": [
        {
            "id": 1,
            "name": "java",
            "displayOrder": 0
        },
        // ...
    ]
}

```
   

   
# 課題添付ファイルの削除 (delete-issue-attachment)

課題の添付ファイルを削除します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/issues/:issueIdOrKey/attachments/:attachmentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |
| attachmentId | 数値 | 添付ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
        "id": 8,
        "name": "IMG0088.png",
        "size": 5563,
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
        "created":"2014-10-28T09:24:43Z"
}

```
   

   
# ユーザーアイコンの取得 (get-user-icon)

ユーザーのアイコン画像を取得します。

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
/api/v2/users/:userId/icon

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | ユーザーのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="person_168.gif"

```
   

   
# 種別の削除 (delete-issue-type)

プロジェクトから種別を削除します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/issueTypes/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | 種別のID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| substituteIssueTypeId (必須) | 数値 | 紐づく課題を付け替える先の種別のID |

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
    "name": "バグ",
    "color": "#990000",
    "displayOrder": 0,
    "templateSummary": "件名",
    "templateDescription": "詳細"
}

```
   

   
# チーム一覧の取得 (get-list-of-teams)

チームの一覧を取得します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
GET

```
## URL

```
/api/v2/teams

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
[
    {
        "id": 1,
        "name": "test",
        "members": [
            {
                "id": 2,
                "userId": "developer",
                "name": "developer",
                "roleType": 2,
                "lang": null,
                "nulabAccount": {
                    "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                    "name": "developer",
                    "uniqueId": "developer"
                },
                "mailAddress": "developer@nulab.example",
                "lastLoginTime": "2022-09-01T06:35:39Z"
            }
        ],
        "displayOrder": null,
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
        "created": "2013-05-30T09:11:36Z",
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
        "updated": "2013-05-30T09:11:36Z"
    },
    // ...
]

```
   

   
# お知らせの既読化 (read-notification)

お知らせを既読にします。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
POST

```
## URL

```
/api/v2/notifications/:id/markAsRead

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| id | 数値 | お知らせのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 204 NO_CONTENT

```
   

   
# 共有ファイル一覧の取得 (get-list-of-shared-files)

共有ファイルの一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/files/metadata/:path

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| path | 文字列 | ディレクトリのパス |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| order | 文字列 | ”asc”または”desc” 指定が無い場合は”desc” |
| offset | 数値 |  |
| count | 数値 | 取得上限(1-1000) 指定が無い場合は1000 |

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
        "id": 825952,
        "projectId": 5,
        "type": "file",
        "dir": "/プレスリリース/20091130/",
        "name": "20091130.txt",
        "size": 4836,
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
        "created": "2009-11-30T01:22:21Z",
        "updatedUser": null,
        "updated": "2009-11-30T01:22:21Z"
    },
    // ...
]

```
   

   
# カテゴリーの追加 (add-category)

プロジェクトにカテゴリーを追加します。

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
/api/v2/projects/:projectIdOrKey/categories

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | カテゴリーの名前 |

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
    "projectId": 5,
    "name": "開発",
    "displayOrder": 0
}

```
   

   
# プロジェクトの追加 (add-project)

新しいプロジェクトを追加します。

## 実行可能な権限

```
管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | プロジェクト名 |
| key (必須) | 文字列 | プロジェクトキー(半角英大文字と半角数字とアンダースコアが使用できます) |
| chartEnabled | 真偽値 | チャートを使用するかどうか |
| useResolvedForChart | 真偽値 | 「処理済み」以降を「完了」とみなすどうか |
| subtaskingEnabled | 真偽値 | 親子課題を使用するかどうか |
| projectLeaderCanEditProjectLeader | 真偽値 | プロジェクト管理者も他のプロジェクト管理者を指定可能にする |
| useWiki | 真偽値 | Wikiを使用するかどうか |
| useFileSharing | 真偽値 | 共有ファイルを使用するかどうか |
| useWikiTreeView | 真偽値 | Wikiツリー表示を有効にするかどうか |
| useSubversion | 真偽値 | Subversionを使用するかどうか |
| useGit | 真偽値 | Gitを使用するかどうか |
| useOriginalImageSizeAtWiki | 真偽値 | Wikiの画像をオリジナルのサイズで表示するかどうか |
| textFormattingRule | 文字列 | テキスト整形のルール backlog または markdown |
| useDevAttributes | 真偽値 | 優先度、マイルストーン、発生バージョンを使用するかどうか |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 201 CREATED
Content-Type:application/json;charset=utf-8
Location:https://xx.backlog.jp/projects/BLG

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
    "useSubversion": true,
    "useGit": true,
    "textFormattingRule": "markdown",
    "archived":false,
    "displayOrder": 2147483646,
    "useDevAttributes": true
}

```
   

   
# Wikiページ情報の取得 (get-wiki-page)

Wikiページの情報を取得します。

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
/api/v2/wikis/:wikiId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |

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
    "name": "Home",
    "content": "test",
    "tags": [
        {
            "id": 12,
            "name": "議事録"
        }
    ],
    "attachments": [
        {
            "id": 1,
            "name": "test.json",
            "size": 8857,
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
            "created": "2014-01-06T11:10:45Z"
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
    "stars": [],
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
    "created": "2012-07-23T06:09:48Z",
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
    "updated": "2012-07-23T06:09:48Z"
}

```
   

   
# お知らせ数の取得 (count-notification)

自分の受け取ったお知らせの数を取得します。

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
/api/v2/notifications/count

```
## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| alreadyRead | 真偽値 |  |
| resourceAlreadyRead | 真偽値 |  |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "count": 138
}

```
   

   
# プロジェクトの容量使用状況の取得 (get-project-disk-usage)

プロジェクトの容量使用状況の情報を取得します。

## 実行可能な権限

```
管理者

```
## メソッド

```
GET

```
## URL

```
/api/v2/projects/:projectIdOrKey/diskUsage

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
    "projectId": 1,
    "issue": 11931,
    "wiki": 0,
    "file": 0,
    "subversion": 0,
    "git": 0,
    "gitLFS": 0
}

```
   

   
# ユーザーの受け取ったスターの数の取得 (count-user-received-stars)

ユーザーの受け取ったスターの数を取得します。

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
/api/v2/users/:userId/stars/count

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | ユーザーのID |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| since | 文字列 | 指定した日付以降のスターをカウント (yyyy-MM-dd) |
| until | 文字列 | 指定した日付以前のスターをカウント (yyyy-MM-dd) |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "count":54
}

```
   

   
# プロジェクトグループの削除 (delete-project-group)

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[プロジェクトチームの削除](/ja/docs/backlog/api/2/delete-project-team)をご利用ください。

プロジェクトからグループを削除します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/groups

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| groupId | 数値 | 削除するグループのID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# カスタム属性の更新 (update-custom-field)

カスタム属性を更新します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/projects/:projectIdOrKey/customFields/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カスタム属性のID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | カスタム属性の名前 |
| applicableIssueTypes[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | カスタム属性を有効にする種別ID空の場合、すべての課題種別で有効 |
| description | 文字列 | カスタム属性の説明 |
| required | 真偽値 | 必須な属性とする場合はtrue |

## 追加パラメーター (数値属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| min | 数値 | 最小値 |
| max | 数値 | 最大値 |
| initialValue | 数値 | 初期値 |
| unit | 文字列 | 単位 |

## 追加パラメーター (日付属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| min | 文字列 | 最小値 (yyyy-MM-dd) |
| max | 文字列 | 最大値 (yyyy-MM-dd) |
| initialValueType | 数値 | 1:当日 2: 当日 + initialShift 3:指定日 |
| initialDate | 文字列 | 初期値 (yyyy-MM-dd) |
| initialShift | 数値 | 差分日数 |

## 追加パラメーター (リスト属性)

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| items[][(複数指定可)](/ja/docs/backlog/tips) | 文字列 | リスト項目 |
| allowInput | 真偽値 | その他直接入力を許可 |
| allowAddItem | 真偽値 | 項目の追加を許可 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 2,
    "projectId": 5,
    "typeId": 1,
    "name": "バグ専用属性",
    "description": "",
    "required": false,
    "applicableIssueTypes": [1]
}

```
   

   
# 種別の追加 (add-issue-type)

プロジェクトに種別を追加します。

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
/api/v2/projects/:projectIdOrKey/issueTypes

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | 種別の名前 |
| color (必須) | 文字列 | 種別の背景色：以下から指定”#e30000""#990000""#934981""#814fbc""#2779ca""#007e9a""#7ea800""#ff9200""#ff3265""#666665” |
| templateSummary | 文字列 | 課題テンプレートの件名 |
| templateDescription | 文字列 | 課題テンプレートの詳細 |

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
    "name": "バグ",
    "color": "#990000",
    "displayOrder": 0,
    "templateSummary": "件名",
    "templateDescription": "詳細"
}

```
   

   
# Wiki共有ファイル一覧の取得 (get-list-of-shared-files-on-wiki)

Wikiの共有ファイルの一覧を取得します。

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
/api/v2/wikis/:wikiId/sharedFiles

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |

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
        "id": 825952,
        "projectId": 5,
        "type": "file",
        "dir": "/プレスリリース/20091130/",
        "name": "20091130.txt",
        "size": 4836,
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
        "created": "2009-11-30T01:22:21Z",
        "updatedUser": null,
        "updated": "2009-11-30T01:22:21Z"
    },
    // ...
]

```
   

   
# プロジェクトチーム一覧の取得 (get-project-team-list)

プロジェクトのチームの一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/teams

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
[
    {
        "id": 1,
        "name": "test",
        "members": [
            {
                "id": 2,
                "userId": "developer",
                "name": "developer",
                "roleType": 2,
                "lang": null,
                "nulabAccount": {
                    "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                    "name": "developer",
                    "uniqueId": "developer"
                },
                "mailAddress": "developer@nulab.example",
                "lastLoginTime": "2022-09-01T06:35:39Z"
            }
        ],
        "displayOrder": null,
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
        "created": "2013-05-30T09:11:36Z",
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
        "updated": "2013-05-30T09:11:36Z"
    },
    // ...
]

```
   

   
# 課題コメント情報の更新 (update-comment)

課題コメントの情報を更新します。

認証ユーザー自身が登録したコメントのみ更新することが出来ます。

## 実行可能な権限

```
管理者
一般ユーザー
レポーター
ゲストレポーター

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/issues/:issueIdOrKey/comments/:commentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |
| commentId | 数値 | コメントのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| content | 文字列 | コメントの本文 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 6586,
    "projectId": 5,
    "issueId": 50,
    "content": "テスト",
    "changeLog": null,
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
    "created": "2013-08-05T06:15:06Z",
    "updated": "2013-08-05T06:15:06Z",
    "stars": [],
    "notifications": []
}

```
   

   
# Wikiに共有ファイルをリンク (link-shared-files-to-wiki)

Wikiに共有ファイルをリンクします。

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
/api/v2/wikis/:wikiId/sharedFiles

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| fileId[] (必須) | 数値 | 共有ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 4056,
    "projectId": 5,
    "type": "file",
    "dir": "/design/",
    "name": "site.png",
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
    "updated":"2010-05-02T17:37:10Z"
}

```
   

   
# 自分が最近見たWiki一覧の取得 (get-list-of-recently-viewed-wikis)

APIとの認証に使用しているユーザーが最近見たWikiの一覧を取得します。

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
/api/v2/users/myself/recentlyViewedWikis

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
    "page": {
        "id": 112,
        "projectId": 103,
        "name": "Home",
        "tags": [
            {
                "id": 12,
                "name": "議事録"
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
        "created": "2013-05-30T09:11:36Z",
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
        "updated": "2013-05-30T09:11:36Z"
    },
    "updated": "2014-07-16T07:18:16Z"
}

```
   

   
# プロジェクトユーザーの追加 (add-project-user)

プロジェクトにユーザーを追加します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/users

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | 追加するユーザーのID |

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
}

```
   

   
# ユーザーの削除 (delete-user)

ユーザーをスペースから削除します。
[新プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)のスペースではこのAPIを利用できません。

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
/api/v2/users/:userId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | 削除するユーザーのID |

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
}

```
   

   
# 共有ファイルのダウンロード (get-file)

共有ファイルを取得します。

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
/api/v2/projects/:projectIdOrKey/files/:sharedFileId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | 共有ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="sharedFile.doc"

```
   

   
# カテゴリー一覧の取得 (get-category-list)

プロジェクトに登録されているカテゴリーの一覧を返します。

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
/api/v2/projects/:projectIdOrKey/categories

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
[
    {
        "id": 12,
        "projectId": 5,
        "name": "開発",
        "displayOrder": 0
    },
    // ...
]

```
   

   
# ユーザーの更新 (update-user)

ユーザーの情報を更新します。
[新プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)のスペースではこのAPIを利用できません。

## 実行可能な権限

```
管理者

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/users/:userId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | 更新するユーザーのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| password | 文字列 | パスワード |
| name | 文字列 | ハンドルネーム |
| mailAddress | 文字列 | メールアドレス |
| roleType | 数値 | 管理者(1) 一般ユーザー(2) レポーター(3) ビューワー(4) ゲストレポーター(5) ゲストビューワー(6) |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8
Location:https://xx.backlog.jp/user/eguchi

```
### レスポンスボディ

```
{
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
}

```
   

   
# プルリクエストコメントの追加 (add-pull-request-comment)

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
   

   
# スペースのお知らせの更新 (update-space-notification)

スペースのお知らせの情報を更新します。

## 実行可能な権限

```
管理者

```
## メソッド

```
PUT

```
## URL

```
/api/v2/space/notification

```
## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "content": "Notification",
    "updated": "2013-06-18T07:55:37Z"
}

```
   

   
# プロジェクトの削除 (delete-project)

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
   

   
# Wikiページ一覧の取得 (get-wiki-page-list)

Wikiページの一覧を取得します。

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
/api/v2/wikis

```
## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| keyword | 文字列 | 検索キーワード |

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
        "id": 112,
        "projectId": 103,
        "name": "Home",
        "tags": [
            {
                "id": 12,
                "name": "議事録"
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
        "created": "2013-05-30T09:11:36Z",
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
        "updated": "2013-05-30T09:11:36Z"
    },
    // ...

]

```
   

   
# プロジェクト管理者の追加 (add-project-administrator)

プロジェクトユーザーにプロジェクト管理者権限を追加します。

## 実行可能な権限

```
管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/administrators

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | 追加するユーザーのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
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
}

```
   

   
# プルリクエスト数の取得 (get-number-of-pull-requests)

プルリクエストの数を取得します。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/count

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
{
    "count": 10
}

```
   

   
# 自分が最近見た課題の追加 (add-recently-viewed-issue)

APIとの認証に使用しているユーザーが最近見た課題を追加します。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
POST

```
## URL

```
/api/v2/users/myself/recentlyViewedIssues

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey (必須) | 文字列 | 課題のID または 課題キー |

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
   

   
# プロジェクトグループ一覧の取得 (get-project-group-list)

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[プロジェクトチーム一覧の取得](/ja/docs/backlog/api/2/get-project-team-list)をご利用ください。

プロジェクトのグループの一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/groups

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
[
    {
        "id": 1,
        "name": "test",
        "members": [
            {
                "id": 2,
                "userId": "developer",
                "name": "developer",
                "roleType": 2,
                "lang": null,
                "nulabAccount": {
                    "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                    "name": "developer",
                    "uniqueId": "developer"
                },
                "mailAddress": "developer@nulab.example",
                "lastLoginTime": "2022-09-01T06:35:39Z"
            }
        ],
        "displayOrder": null,
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
        "created": "2013-05-30T09:11:36Z",
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
        "updated": "2013-05-30T09:11:36Z"
    },
    // ...
]

```
   

   
# ライセンス情報の取得 (get-licence)

ライセンスの情報を取得します。

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
/api/v2/space/licence

```
## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "active": true,
    "attachmentLimit": 0,
    "attachmentLimitPerFile": 10485760,
    "attachmentNumLimit": 50,
    "attribute": true,
    "attributeLimit": 100,
    "burndown": true,
    "commentLimit": 0,
    "componentLimit": 0,
    "fileSharing": true,
    "gantt": true,
    "git": true,
    "issueLimit": 0,
    "licenceTypeId": 51,
    "limitDate": "2019-01-02T15:00:00Z",
    "nulabAccount": true,
    "parentChildIssue": true,
    "postIssueByMail": true,
    "projectLimit": 0,
    "pullRequestAttachmentLimitPerFile": 10485760,
    "pullRequestAttachmentNumLimit": 50,
    "remoteAddress": true,
    "remoteAddressLimit": 100,
    "startedOn": "2018-01-03T15:00:00Z",
    "storageLimit": 1073741824000,
    "subversion": true,
    "subversionExternal": true,
    "userLimit": 0,
    "versionLimit": 0,
    "wikiAttachment": true,
    "wikiAttachmentLimitPerFile": 10485760,
    "wikiAttachmentNumLimit": 50
}

```
   

   
# プルリクエストコメント情報の更新 (update-pull-request-comment-information)

プルリクエストコメントの情報を更新します。

認証ユーザー自身が登録したコメントのみ更新することが出来ます。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/:number/comments/:commentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |
| number | 数値 | プルリクエストの番号 |
| commentId | 数値 | コメントのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| content | 文字列 | コメントの本文 |

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
   

   
# ユーザー情報の取得 (get-user)

ユーザー情報を取得します。

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
/api/v2/users/:userId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | ユーザーのID |

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
}

```
## レスポンス説明

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| lang | 文字列 | ユーザーの言語設定。`"en"` 英語`"ja"` 日本語`null` 未指定 |
| roleType | 数値 | ユーザーの権限。[利用するスペースの契約プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)により値の意味が異なります。クラシックプランの場合:`1` 管理者`2` 一般ユーザー`3` レポーター`4` ビューワー`5` ゲストレポーター`6` ゲストビューワー新プランの場合:`1` 管理者`2` 一般ユーザー、ゲスト（制限：制限なし）`3` 一般ユーザー、ゲスト（制限：課題の登録のみ）`4` 一般ユーザー、ゲスト（制限：課題の閲覧のみ） |

   

   
# 課題情報の更新 (update-issue)

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
   

   
# チーム情報の取得 (get-team)

チームの情報を取得します。

## 実行可能な権限

```
管理者

```
## メソッド

```
GET

```
## URL

```
/api/v2/teams/:teamId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| teamId | 数値 | チームのID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# プロジェクト管理者一覧の取得 (get-list-of-project-administrators)

プロジェクト管理者に設定されているユーザーの一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/administrators

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
[
    {
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
    // ...
]

```
   

   
# プロジェクト情報の取得 (get-project)

プロジェクトの情報を取得します。

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
    "useSubversion": true,
    "useGit": true,
    "textFormattingRule": "markdown",
    "archived":false,
    "displayOrder": 2147483646,
    "useDevAttributes": true
}

```
   

   
# 課題共有ファイル一覧の取得 (get-list-of-linked-shared-files)

課題にリンクされた共有ファイルの一覧を取得します。

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
/api/v2/issues/:issueIdOrKey/sharedFiles

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |

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
        "id": 4056,
        "projectId": 5,
        "type": "file",
        "dir": "/design/",
        "name": "site.png",
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
        "updated":"2010-05-02T17:37:10Z"
    },
    // ...
]

```
   

   
# スターの追加 (add-star)

課題、コメント、Wikiページにスターを一つ追加します。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
POST

```
## URL

```
/api/v2/stars

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueId | 数値 | 課題のID |
| commentId | 数値 | コメントのID |
| wikiId | 数値 | WikiページのID |
| pullRequestId | 数値 | プルリクエストのID |
| pullRequestCommentId | 数値 | プルリクエストコメントのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 204 NO_CONTENT

```
   

   
# ユーザーの最近の活動の取得 (get-user-recent-updates)

ユーザーの最近の活動の一覧を取得します。

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
/api/v2/users/:userId/activities

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | ユーザーのID |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| activityTypeId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | type(1-17) |
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

2022年2月9日にレスポンスボディからnotificationsのコンテンツが削除され空の配列になります。
詳しくは[こちら](https://backlog.com/ja/product-updates/announcement/backlog-will-changes-to-the-get-recent-updates-apis/)をご確認下さい。

```
[
    {
        "id": 3153,
        "project": {
            "id": 92,
            "projectKey": "SUB",
            "name": "サブタスク",
            "chartEnabled": true,
            "useResolvedForChart": true,
            "subtaskingEnabled": true,
            "projectLeaderCanEditProjectLeader": false,
            "useWiki": true,
            "useFileSharing": true,
            "useWikiTreeView": true,
            "useOriginalImageSizeAtWiki": false,
            "textFormattingRule": "backlog",
            "archived": false,
            "displayOrder": 3,
            "useDevAttributes": true
        },
        "type": 2,
        "content": {
            "id": 4809,
            "key_id": 121,
            "summary": "コメント",
            "description": "",
            "comment": {
                "id": 7237,
                "content": ""
            },
            "changes": [
                {
                    "field": "milestone",
                    "new_value": " R2014-07-23",
                    "old_value": "",
                    "type": "standard"
                },
                {
                    "field": "status",
                    "new_value": "4",
                    "old_value": "1",
                    "type": "standard"
                }
            ]
        },
        "notifications": [],
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
        "created": "2013-12-27T07:50:44Z"
    },
    // ...
]

```
## レスポンス説明

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| type | 数値 | 最近の更新の種別：1:課題の追加2:課題の更新3:課題にコメント4:課題の削除5:Wikiを追加6:Wikiを更新7:Wikiを削除8:共有ファイルを追加9:共有ファイルを更新10:共有ファイルを削除11:Subversionコミット12:GITプッシュ13:GITリポジトリ作成14:課題をまとめて更新15:プロジェクトに参加16:プロジェクトから脱退17:コメントにお知らせを追加18:プルリクエストの追加19:プルリクエストの更新20:プルリクエストにコメント21:プルリクエストの削除22:マイルストーンの追加23:マイルストーンの更新24:マイルストーンの削除25:グループがプロジェクトに参加26:グループがプロジェクトから脱退 |
| reason | 数値 | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 |

   

   
# カテゴリーの削除 (delete-category)

カテゴリーを削除します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/categories/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カテゴリーのID |

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
    "projectId": 5,
    "name": "開発",
    "displayOrder": 0
}

```
   

   
# Wikiページタグ一覧の取得 (get-wiki-page-tag-list)

プロジェクト内のWikiページで使用されているタグの一覧を取得します。

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
/api/v2/wikis/tags

```
## クエリパラメーター

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
[
    {
        "id": 1,
        "name": "test"
    },
    // ...
]

```
   

   
# 課題コメントの削除 (delete-comment)

課題コメントを削除します。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/issues/:issueIdOrKey/comments/:commentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |
| commentId | 数値 | コメントのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 6586,
    "projectId": 5,
    "issueId": 50,
    "content": "テスト",
    "changeLog": null,
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
    "created": "2013-08-05T06:15:06Z",
    "updated": "2013-08-05T06:15:06Z",
    "stars": [],
    "notifications": []
}

```
   

   
# バージョン(マイルストーン)情報の更新 (update-version-milestone)

バージョン(マイルストーン)の情報を更新します。

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
/api/v2/projects/:projectIdOrKey/versions/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | バージョンのID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | バージョンの名前 |
| description | 文字列 | バージョンの説明 |
| startDate | 文字列 | バージョンの開始日 (yyyy-MM-dd) |
| releaseDueDate | 文字列 | バージョンのリリース予定日 (yyyy-MM-dd) |
| archived | 真偽値 | プロジェクトホームに表示しない場合はtrue |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 3,
    "projectId": 1,
    "name": "いますぐ",
    "description": "",
    "startDate": null,
    "releaseDueDate": null,
    "archived": false,
    "displayOrder": 0
}

```
   

   
# 状態の並び替え (update-order-of-status)

状態の表示順を変更します。

## 実行可能な権限

```
管理者

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/projects/:projectIdOrKey/statuses/updateDisplayOrder

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| statusId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 表示順に並べた、状態のIDのリスト。そのプロジェクトで使える全ての状態を渡してください。表示順には以下の制限があります  * 未対応は先頭にあること * 完了は末尾にあること * 処理中は処理済みよりも前にあること |

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
        "name": "未対応",
        "color": "#ed8077",
        "displayOrder": 1000
    },
    {
        "id": 101,
        "projectId": 1,
        "name": "調査待ち",
        "color": "#ed8077",
        "displayOrder": 1001
    },
    // ...
]

```
   

   
# 課題コメント数の取得 (count-comment)

課題に登録されているコメントの数を取得します。

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
/api/v2/issues/:issueIdOrKey/comments/count

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "count": 10
}

```
   

   
# 認証ユーザー情報の取得 (get-own-user)

APIとの認証に使用しているユーザーの情報を取得します。

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
/api/v2/users/myself

```
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
}

```
   

   
# チームの削除 (delete-team)

チームを削除します。
[新プラン](https://support-ja.backlog.com/hc/ja/articles/360036151453)のスペースではこのAPIを利用できません。

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
/api/v2/teams/:teamId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| teamId | 数値 | チームのID |

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
    "name": "test",
    "members": [
        {
            "id": 2,
            "userId": "developer",
            "name": "developer",
            "roleType": 2,
            "lang": null,
            "nulabAccount": {
                "nulabId": "wZmTYcgsR75zebBQpyYRNES4cBZySC5rRizXxNeLJ83swN4nrS",
                "name": "developer",
                "uniqueId": "developer"
            },
            "mailAddress": "developer@nulab.example",
            "lastLoginTime": "2022-09-01T06:35:39Z"
        }
    ],
    "displayOrder": null,
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
    "created": "2013-05-30T09:11:36Z",
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
    "updated": "2013-05-30T09:11:36Z"
}

```
   

   
# お知らせ一覧の取得 (get-notification)

自分の受け取ったお知らせの一覧を取得します。

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
/api/v2/notifications

```
## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| minId | 数値 | 最小ID |
| maxId | 数値 | 最大ID |
| count | 数値 | 取得上限(1-100) 指定が無い場合は20 |
| order | 文字列 | ”asc”または”desc” 指定が無い場合は”desc” |
| senderId | 数値 | 送信者ID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
### レスポンスボディ
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
[
    {
        "id": 299,
        "alreadyRead": true,
        "reason": 2,
        "resourceAlreadyRead": true,
        "project": {
            "id": 2,
            "projectKey": "TEST2",
            "name": "test2",
            "chartEnabled": true,
            "useResolvedForChart": true,
            "subtaskingEnabled": true,
            "projectLeaderCanEditProjectLeader": false,
            "useWiki": true,
            "useFileSharing": true,
            "useWikiTreeView": true,
            "useOriginalImageSizeAtWiki": false,
            "textFormattingRule": "backlog",
            "archived": false,
            "displayOrder": 3,
            "useDevAttributes": true
        },
        "issue": {
            "id": 4531,
            "projectId": 2,
            "issueKey": "TEST2-17",
            "keyId": 17,
            "issueType": {
                "id": 7,
                "projectId": 2,
                "name": "バグ",
                "color": "#990000",
                "displayOrder": 0
            },
            "summary": "aaa",
            "description": "",
            "resolution": null,
            "priority": {
                "id": 3,
                "name": "中"
            },
            "status": {
                "id": 1,
                "projectId": 2,
                "name": "未対応",
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
        "comment": {
            "id": 7007,
            "projectId": 5,
            "issueId": 50,
            "content": "hoge",
            "changeLog": null,
            "createdUser": {
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
            "created": "2013-10-31T06:58:58Z",
            "updated": "2013-10-31T06:58:58Z",
            "stars": [],
            "notifications": []
        },
        "pullRequest": null,
        "pullRequestComment": null,
        "sender": {
            "id": 2
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
        "created": "2013-10-31T06:58:59Z"
    },
    // ...
]

```
## レスポンス説明

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| reason | 数値 | 通知の種別：1:課題の担当者に設定2:課題にコメント3:課題の追加4:課題の更新5:ファイルを追加6:プロジェクトユーザーの追加9:その他10:プルリクエストの担当者に設定11:プルリクエストにコメント12:プルリクエストの追加13:プルリクエストの更新 |

   

   
# Wiki添付ファイル一覧の取得 (get-list-of-wiki-attachments)

Wikiの添付ファイルの一覧を取得します。

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
/api/v2/wikis/:wikiId/attachments

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |

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
        "name": "IMGP0088.JPG",
        "size": 85079
    },
    // ...
]

```
   

   
# Webhookの削除 (delete-webhook)

Webhookを削除します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/webhooks/:webhookId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| webhookId | 文字列 | WebhookのID |

* クエリパラメーター

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 3,
    "name": "webhook",
    "description": "",
    "hookUrl": "http://nulab.test/",
    "allEvent": false,
    "activityTypeIds": [1, 2, 3, 4, 5],
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
    "created": "2014-11-30T01:22:21Z",
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
    "updated": "2014-11-30T01:22:21Z"
}

```
   

   
# ウォッチの既読化 (mark-watching-as-read)

ウォッチを既読にします。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
POST

```
## URL

```
/api/v2/watchings/:watchingId/markAsRead

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| watchingId | 数値 | ウォッチのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 204 NO_CONTENT

```
   

   
# 優先度一覧の取得 (get-priority-list)

課題に設定できる優先度の一覧を取得します。

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
/api/v2/priorities

```
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
        "name": "高"
    },
    {
        "id": 3,
        "name": "中"
    },
    {
        "id": 4,
        "name": "低"
    }
]

```
   

   
# Gitリポジトリ一覧の取得 (get-list-of-git-repositories)

Gitリポジトリの一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/git/repositories

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
### レスポンスボディ
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
[
    {
        "id":1,
        "projectId":151,
        "name":"app",
        "description":"",
        "hookUrl":null,
        "httpUrl":"https://xx.backlog.jp/git/BLG/app.git",
        "sshUrl":"xx@xx.git.backlog.jp:/BLG/app.git",
        "displayOrder":0,
        "pushedAt":null,
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
        "created": "2013-05-30T09:11:36Z",
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
        "updated": "2013-05-30T09:11:36Z"
    },
    // ...
]

```
   

