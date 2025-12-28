   
# カスタム属性の削除

カスタム属性を削除します。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/customFields/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カスタム属性のID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 2,
    "projectId": 5,
    "typeId": 1,
    "name": "バグ専用属性",
    "description": "",
    "required": false,
    "applicableIssueTypes": [1]
}

```
   