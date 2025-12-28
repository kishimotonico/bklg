   
# スペースの容量使用状況の取得

スペースの容量使用状況の情報を取得します。

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
/api/v2/space/diskUsage

```
## レスポンス例

### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

```
{
    "capacity": 1073741824,
    "issue": 119511,
    "wiki": 48575,
    "file": 0,
    "subversion": 0,
    "git": 0,
    "gitLFS": 0,
    "details":[
        {
            "projectId": 1,
            "issue": 11931,
            "wiki": 0,
            "file": 0,
            "subversion": 0,
            "git": 0,
            "gitLFS": 0
        },
        // ...
    ]
}

```
   