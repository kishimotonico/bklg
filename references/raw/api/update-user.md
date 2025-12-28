   
# ユーザーの更新

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
   