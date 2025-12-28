   
# ユーザーの削除

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
   