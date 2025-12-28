   
# プルリクエスト数の取得

プルリクエストの数を取得します。

## 実行可能な権限

```
管理者
一般ユーザー

```
## メソッド

```
GET

```
## URL

```
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/count

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |

## クエリパラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| statusId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 状態のID |
| assigneeId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 担当者のID |
| issueId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 関連課題のID |
| createdUserId[][(複数指定可)](/ja/docs/backlog/tips) | 数値 | 登録者のID |
| offset | 数値 |  |
| count | 数値 | 取得上限(1-100) 指定が無い場合は20 |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "count": 10
}

```
   