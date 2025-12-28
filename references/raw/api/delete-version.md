   
# バージョン(マイルストーン)の削除

バージョン(マイルストーン)を削除します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/versions/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | バージョンのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 3,
    "projectId": 1,
    "name": "いますぐ",
    "description": "",
    "startDate": null,
    "releaseDueDate": null,
    "archived": false,
    "displayOrder": 0
}

```
   