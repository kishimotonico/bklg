   
# 共有ファイル一覧の取得

共有ファイルの一覧を取得します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
GET

```
## URL

```
/api/v2/projects/:projectIdOrKey/files/metadata/:path

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| path | 文字列 | ディレクトリのパス |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| order | 文字列 | ”asc”または”desc” 指定が無い場合は”desc” |
| offset | 数値 |  |
| count | 数値 | 取得上限(1-1000) 指定が無い場合は1000 |

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
        "id": 825952,
        "projectId": 5,
        "type": "file",
        "dir": "/プレスリリース/20091130/",
        "name": "20091130.txt",
        "size": 4836,
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
        "created": "2009-11-30T01:22:21Z",
        "updatedUser": null,
        "updated": "2009-11-30T01:22:21Z"
    },
    // ...
]

```
   