   
# プロジェクト管理者一覧の取得

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
   