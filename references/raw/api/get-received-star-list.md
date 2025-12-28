   
# ユーザーの受け取ったスター一覧の取得

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
   