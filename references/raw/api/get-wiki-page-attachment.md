   
# Wiki添付ファイルのダウンロード

Wikiの添付ファイルをダウンロードします。

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
/api/v2/wikis/:wikiId/attachments/:attachmentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| wikiId | 数値 | WikiページのID |
| attachmentId | 数値 | 添付ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="attachment.doc"

```
### レスポンスボディ

   