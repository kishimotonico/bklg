   
# 選択リストカスタム属性のリスト項目の追加

選択リスト形式のカスタム属性のリスト項目を追加します。
「課題の追加/編集時に選択肢を追加できる」の設定が無効な場合は管理者権限のユーザーのみ呼び出せます。
指定されたカスタム属性が選択リスト形式でない場合はエラーになります。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/customFields/:id/items

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | カスタム属性のID |

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
   