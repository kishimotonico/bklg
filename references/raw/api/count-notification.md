   
# お知らせ数の取得

自分の受け取ったお知らせの数を取得します。

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
/api/v2/notifications/count

```
## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| alreadyRead | 真偽値 |  |
| resourceAlreadyRead | 真偽値 |  |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "count": 138
}

```
   