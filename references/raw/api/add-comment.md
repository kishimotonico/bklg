   
# 課題コメントの追加

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
   