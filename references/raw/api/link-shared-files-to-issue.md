   
# 課題に共有ファイルをリンク

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
   