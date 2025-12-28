   
# ユーザーアイコンの取得

ユーザーのアイコン画像を取得します。

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
/api/v2/users/:userId/icon

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| userId | 数値 | ユーザーのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="person_168.gif"

```
   