   
# バージョン(マイルストーン)情報の更新

バージョン(マイルストーン)の情報を更新します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
PATCH

```
## URL

```
/api/v2/projects/:projectIdOrKey/versions/:id

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| id | 数値 | バージョンのID |

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
| archived | 真偽値 | プロジェクトホームに表示しない場合はtrue |

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
   