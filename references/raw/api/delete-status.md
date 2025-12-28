   
# 状態の削除

プロジェクトから状態を削除します。

## 実行可能な権限

```
管理者

```
## メソッド

```
DELETE

```
## URL

```
/api/v2/projects/:projectIdOrKey/statuses/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | 状態のID |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| substituteStatusId (必須) | 数値 | 紐づく課題を付け替える先の状態のID。削除対象の状態が設定されている課題がある場合、このパラメーターで指定した状態へ一括変更します。 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 101,
    "projectId": 1,
    "name": "レビュー待ち",
    "color": "#e87758",
    "displayOrder": 3999
}

```
   