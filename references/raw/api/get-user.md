   
# ユーザー情報の取得

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

   