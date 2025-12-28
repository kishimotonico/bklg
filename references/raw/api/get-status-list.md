   
# 状態一覧の取得

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[プロジェクトの状態一覧の取得](/ja/docs/backlog/api/2/get-status-list-of-project)をご利用ください。

課題に設定できる状態の一覧を取得します。

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
/api/v2/statuses

```
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
        "name": "未対応"
    },
    {
        "id": 2,
        "name": "処理中"
    },
    {
        "id": 3,
        "name": "処理済み"
    },
    {
        "id": 4,
        "name": "完了"
    }
]

```
   