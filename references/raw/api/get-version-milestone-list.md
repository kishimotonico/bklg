   
# バージョン(マイルストーン)一覧の取得

プロジェクトに登録されているバージョン(マイルストーン)の一覧を返します。

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
/api/v2/projects/:projectIdOrKey/versions

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
        "id": 3,
        "projectId": 1,
        "name": "いますぐ",
        "description": "",
        "startDate": null,
        "releaseDueDate": null,
        "archived": false,
        "displayOrder": 0
    },
    // ...
]

```
   