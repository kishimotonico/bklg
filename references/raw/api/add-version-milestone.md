   
# バージョン(マイルストーン)の追加

プロジェクトにバージョン(マイルストーン)を追加します。

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
/api/v2/projects/:projectIdOrKey/versions

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
| name (必須) | 文字列 | バージョンの名前 |
| description | 文字列 | バージョンの説明 |
| startDate | 文字列 | バージョンの開始日 (yyyy-MM-dd) |
| releaseDueDate | 文字列 | バージョンのリリース予定日 (yyyy-MM-dd) |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "id": 3,
    "projectId": 1,
    "name": "いますぐ",
    "description": "",
    "startDate": null,
    "releaseDueDate": null,
    "archived": false,
    "displayOrder": 0
}

```
   