   
# チームの削除

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
   