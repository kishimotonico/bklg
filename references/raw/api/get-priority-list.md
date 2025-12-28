   
# 優先度一覧の取得

課題に設定できる優先度の一覧を取得します。

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
/api/v2/priorities

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
        "id": 2,
        "name": "高"
    },
    {
        "id": 3,
        "name": "中"
    },
    {
        "id": 4,
        "name": "低"
    }
]

```
   