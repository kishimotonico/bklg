   
# 状態の並び替え

状態の表示順を変更します。

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
/api/v2/projects/:projectIdOrKey/statuses/updateDisplayOrder

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
| statusId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 表示順に並べた、状態のIDのリスト。そのプロジェクトで使える全ての状態を渡してください。表示順には以下の制限があります  * 未対応は先頭にあること * 完了は末尾にあること * 処理中は処理済みよりも前にあること |

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
        "projectId": 1,
        "name": "未対応",
        "color": "#ed8077",
        "displayOrder": 1000
    },
    {
        "id": 101,
        "projectId": 1,
        "name": "調査待ち",
        "color": "#ed8077",
        "displayOrder": 1001
    },
    // ...
]

```
   