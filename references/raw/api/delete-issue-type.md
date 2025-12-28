   
# 種別の削除

プロジェクトから種別を削除します。

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
/api/v2/projects/:projectIdOrKey/issueTypes/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | 種別のID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| substituteIssueTypeId (必須) | 数値 | 紐づく課題を付け替える先の種別のID |

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
    "projectId": 1,
    "name": "バグ",
    "color": "#990000",
    "displayOrder": 0,
    "templateSummary": "件名",
    "templateDescription": "詳細"
}

```
   