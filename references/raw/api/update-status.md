   
# 状態情報の更新

追加した状態の情報を更新します。

## 実行可能な権限

```
管理者

```
## メソッド

```
PATCH

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
| name | 文字列 | 状態の名前 |
| color | 文字列 | 状態の背景色；以下から指定”#ea2c00""#e87758""#e07b9a""#868cb7""#3b9dbd""#4caf93""#b0be3c""#eda62a""#f42858""#393939” |

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
   