   
# 課題添付ファイルのダウンロード

課題の添付ファイルをダウンロードします。

## 実行可能な権限

```
管理者
一般ユーザー
レポーター
ゲストレポーター

```
## メソッド

```
GET

```
## URL

```
/api/v2/issues/:issueIdOrKey/attachments/:attachmentId

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueIdOrKey | 文字列 | 課題のID または 課題キー |
| attachmentId | 数値 | 添付ファイルのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/octet-stream
Content-Disposition:attachment;filename="attachment.doc"

```
   