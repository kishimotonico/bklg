   
# チームアイコンの取得

チームアイコン画像を取得します。

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
/api/v2/teams/:teamId/icon

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| teamId | 数値 | チームのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="team_168.gif"

```
   