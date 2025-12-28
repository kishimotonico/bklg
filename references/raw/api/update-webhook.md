   
# Webhookの更新

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
   