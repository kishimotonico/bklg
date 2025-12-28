   
# Wikiページ情報の更新

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
   