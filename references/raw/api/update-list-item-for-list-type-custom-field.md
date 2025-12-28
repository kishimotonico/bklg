   
# 選択リストカスタム属性のリスト項目の更新

選択リスト形式のカスタム属性のリスト項目を更新します。
指定されたカスタム属性が選択リスト形式でない場合はエラーになります。

## 実行可能な権限

```
管理者
プロジェクト管理者

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/projects/:projectIdOrKey/customFields/:id/items/:itemId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カスタム属性のID |
| itemId | 数値 | リスト項目のID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name | 文字列 | リスト項目の名前 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 8,
    "projectId": 5,
    "typeId": 5,
    "name": "language",
    "description": "",
    "required": false,
    "applicableIssueTypes": [ ],
    "allowAddItem": true,
    "items": [
        {
            "id": 1,
            "name": "java",
            "displayOrder": 0
        },
        // ...
    ]
}

```
   