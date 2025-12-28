   
# 状態の追加

プロジェクトに状態を追加します。
1プロジェクトにつき8個まで状態を追加できます。 標準の4つの状態と合わせると、合計12個の状態を設定できます。

## 実行可能な権限

```
管理者

```
## メソッド

```
POST

```
## URL

```
/api/v2/projects/:projectIdOrKey/statuses

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| name (必須) | 文字列 | 状態の名前 |
| color (必須) | 文字列 | 状態の背景色：以下から指定”#ea2c00""#e87758""#e07b9a""#868cb7""#3b9dbd""#4caf93""#b0be3c""#eda62a""#f42858""#393939” |

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
   