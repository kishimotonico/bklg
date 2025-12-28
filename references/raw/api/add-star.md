   
# スターの追加

課題、コメント、Wikiページにスターを一つ追加します。

## 実行可能な権限

```
すべての権限

```
## メソッド

```
POST

```
## URL

```
/api/v2/stars

```
## リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| issueId | 数値 | 課題のID |
| commentId | 数値 | コメントのID |
| wikiId | 数値 | WikiページのID |
| pullRequestId | 数値 | プルリクエストのID |
| pullRequestCommentId | 数値 | プルリクエストコメントのID |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 204 NO_CONTENT

```
   