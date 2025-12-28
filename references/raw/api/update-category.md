   
# カテゴリー情報の更新

カテゴリーの情報を更新します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
PATCH

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

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | カテゴリーの名前 |

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
   