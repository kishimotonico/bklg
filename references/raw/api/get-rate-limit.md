   
# レート制限情報の取得

使用中のAPIキーに対応するユーザーに対して、現在設定されているレート制限に関する情報を取得します。

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
/api/v2/rateLimit

```
## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
  "rateLimit": {
    "read": {
      "limit": 600,
      "remaining": 600,
      "reset": 1603881873
    },
    "update": {
      "limit": 150,
      "remaining": 150,
      "reset": 1603881873
    },
    "search": {
      "limit": 150,
      "remaining": 150,
      "reset": 1603881873
    },
    "icon": {
      "limit": 60,
      "remaining": 60,
      "reset": 1603881873
    }
  }
}

```
   