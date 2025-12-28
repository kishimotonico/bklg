   
# プロジェクトの容量使用状況の取得

プロジェクトの容量使用状況の情報を取得します。

## 実行可能な権限

```
管理者

```
## メソッド

```
GET

```
## URL

```
/api/v2/projects/:projectIdOrKey/diskUsage

```
## URL パラメーター

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| projectIdOrKey | 文字列 | プロジェクトのID または プロジェクトキー |

## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "projectId": 1,
    "issue": 11931,
    "wiki": 0,
    "file": 0,
    "subversion": 0,
    "git": 0,
    "gitLFS": 0
}

```
   