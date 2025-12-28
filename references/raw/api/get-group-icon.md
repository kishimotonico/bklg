   
# グループアイコンの取得

[2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）](https://backlog.com/ja/blog/remove-deprecated-backlog-group-status-api/)

[チームアイコンの取得](/ja/docs/backlog/api/2/get-team-icon)をご利用ください。

グループのアイコン画像を取得します。

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
/api/v2/groups/:groupId/icon

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| groupId | 数値 | グループのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="group_168.gif"

```
   