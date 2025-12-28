   
# エラーレスポンス

## レスポンス例

### ステータスライン / レスポンスヘッダ

ステータスライン / レスポンスヘッダ

```
HTTP/1.1 404 Not Found
Content-Type:application/json;charset=utf-8

```
### レスポンスボディ

レスポンスボディ

```
{
    "errors":[
        {
            "message": "No project.",
            "code": 6,
            "moreInfo": ""
        }
    ],
    // ...
}

```
## レスポンス説明

### 1: InternalError

プログラムのバグ等に起因する例外などが原因のエラー

### 2: LicenceError

使用しているライセンス(プラン)で使用できない機能が呼び出された場合のエラー

### 3: LicenceExpiredError

ライセンスの期限切れを表すエラー

### 4: AccessDeniedError

IP アドレス制限などでアクセスが拒否された場合のエラー

### 5: UnauthorizedOperationError

ユーザに権限のない操作が呼び出された場合のエラー

### 6: NoResourceError

リクエスト対象のリソースが存在しない場合のエラー

### 7: InvalidRequestError

不正なパラメータのリクエストを表すエラー

### 8: SpaceOverCapacityError

スペースの容量制限を超える場合のエラー

### 9: ResourceOverflowError

リソースを追加する操作が呼び出された時に、そのリソースに設けられた制限を超える場合のエラー

### 10: TooLargeFileError

制限サイズを超えるファイルがアップロードされた場合のエラー

### 11: AuthenticationError

認証に失敗した場合のエラー

### 12: RequiredMFAError

2段階認証を有効にしていないユーザーが、2段階認証が必須なスペースへのアクセスを拒否された場合のエラー

### 13: TooManyRequestsError

API アクセスを実行したユーザーが、レート制限によってアクセスを拒否された場合のエラー

   