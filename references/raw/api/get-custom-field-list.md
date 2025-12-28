   
# カスタム属性一覧の取得

プロジェクトに登録されているカスタム属性の一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/customFields

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
        "id": 1,
        "projectId": 5,
        "typeId": 6,
        "name": "custom",
        "description": "",
        "required": false,
        "applicableIssueTypes": [],
        "allowAddItem": false,
        "items": [
            {
                "id": 1,
                "name": "Windows 8",
                "displayOrder": 0
            },
            // ...
        ]
    },
    {
        "id": 2,
        "typeId": 1,
        "name": "バグ専用属性",
        "description": "",
        "required": false,
        "applicableIssueTypes": [1]
    },
    // ...
]

```
   