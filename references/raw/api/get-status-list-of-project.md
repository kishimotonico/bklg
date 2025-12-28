   
# プロジェクトの状態一覧の取得

プロジェクト固有の課題に設定できる状態一覧を取得します。

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
/api/v2/projects/:projectIdOrKey/statuses

```
## URL パラメーター

| Parameter Name | Type | Description |
| --- | --- | --- |
| projectIdOrKey | String | Project ID or Project Key |

## レスポンス名

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
    // ...
]

```
   