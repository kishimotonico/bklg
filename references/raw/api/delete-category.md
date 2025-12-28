   
# カテゴリーの削除

カテゴリーを削除します。

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
/api/v2/projects/:projectIdOrKey/categories/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カテゴリーのID |

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
    "projectId": 5,
    "name": "開発",
    "displayOrder": 0
}

```
   