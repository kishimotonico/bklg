   
# 添付ファイルの送信

課題、コメントまたはWikiに添付するファイルを送信し、添付ファイルに発行されたIDを取得します。

送信されたファイルは添付された後に削除されます。また添付されなかった場合は1時間後に削除されます。

## 実行可能な権限

```
管理者
一般ユーザー
レポーター
ゲストレポーター

```
## メソッド

```
POST

```
## URL

```
/api/v2/space/attachment

```
## リクエストパラメーター

```
// 全体
--- Content-Type:multipart/form-data
// ファイル部のパート
--- Content-Disposition: form-data; name="file"; filename="ファイル名"
--- Content-Type: application/octet-stream 等

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
    "id": 1,
    "name": "test.txt",
    "size": 8857
}

```
   