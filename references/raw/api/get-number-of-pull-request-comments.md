   
# プルリクエストコメント数の取得

プルリクエストに登録されているコメントの数を取得します。

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
/api/v2/projects/:projectIdOrKey/git/repositories/:repoIdOrName/pullRequests/:number/comments/count

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |
| repoIdOrName | 文字列 | リポジトリのID または リポジトリ名 |
| number | 数値 | プルリクエストの番号 |

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
   