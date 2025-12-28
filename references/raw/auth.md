   
# 認証と認可

## API Key

リクエストパラメーターにユーザーごとに発行された API キーを付加して認証する方式です。
リソースへのアクセス時に、発行されたAPI キーをパラメータ名 “apiKey” として付加することで認証が行えます。

### リクエスト例

```
https://xx.backlog.jp/api/v2/users/myself?apiKey=abcdefghijklmn

```

URLがbacklog.comの場合は次のようになります。

```
https://xx.backlog.com/api/v2/users/myself?apiKey=abcdefghijklmn

```
## OAuth 2.0

OAuth2認可フレームワーク(RFC 6749)で定められた認可コードによる認可(Authorization Code Grant)を使用してAPIにアクセスすることができます。

ここで使用するclient\_idとclient\_secretを取得するには、[Backlog Developer サイト](https://backlog.com/developer/applications/)でアプリケーション登録を行ってください。

### 認可リクエスト

#### メソッド

```
GET

```
#### URL

```
/OAuth2AccessRequest.action

```

認可エンドポイントです。
ユーザからの許可が得られた場合、redirect\_uriに認可コードを含めてリダイレクトを行います。

#### クエリパラメーター

| 名前 | 型 | 説明 |
| --- | --- | --- |
| response\_type (必須) | 文字列 | 値は”code”で固定 |
| client\_id (必須) | 文字列 |  |
| redirect\_uri (必須) | 文字列 | [開発アプリケーション](https://backlog.com/developer/applications/) ページで設定したものと同じUri |
| state | 文字列 |  |

### アクセストークンリクエスト

#### メソッド

```
POST

```
#### URL

```
/api/v2/oauth2/token

```

トークンエンドポイントです。
認可エンドポイントのリダイレクトから取得した認可コードを使用して、有効なアクセストークン及びリフレッシュトークンを取得できます。

#### リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| grant\_type (必須) | 文字列 | 値は”authorization\_code”で固定 |
| code (必須) | 文字列 | 認可エンドポイントのリダイレクトから取得した認可コード |
| redirect\_uri (必須) | 文字列 | [開発アプリケーション](https://backlog.com/developer/applications/) ページで設定したものと同じUri |
| client\_id (必須) | 文字列 |  |
| client\_secret (必須) | 文字列 |  |

#### レスポンス例

##### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
##### レスポンスボディ

```
{
    "access_token": "YOUR_ACCESS_TOKEN",
    "token_type":"Bearer",
    "expires_in":3600,
    "refresh_token":"YOUR_REFRESH_TOKEN"
}

```
### アクセストークンを使用したAPIアクセス

トークンエンドポイントから取得したアクセストークンをAuthorizationヘッダーに含めてAPIを呼び出すことができます

```
GET /api/v2/space
HTTP/1.1
Host: example.backlog.jp (URLがbacklog.comの場合はexample.backlog.comになります)
Authorization: Bearer YOUR_ACCESS_TOKEN

```

認証エラーが発生した場合、ステータスコード401を返却します。
エラーの詳細はレスポンスのWWW-Authenticateヘッダーを確認して下さい。

* アクセストークンが間違っている場合

```
"Bearer error="invalid_token", error_description="The access token is invalid"

```

* アクセストークンの有効期限切れの場合

```
"Bearer error="invalid_token", error_description="The access token expired"

```
### アクセストークンの更新

アクセストークンは新規に生成されてから3600秒（1時間）で有効期限切れになります。リフレッシュトークンを使ってトークンエンドポイントから有効なアクセストークンを取得することができます。

#### メソッド

```
POST

```
#### URL

```
/api/v2/oauth2/token

```
#### リクエストパラメーター

```
Content-Type:application/x-www-form-urlencoded

```

| パラメーター名 | 型 | 内容 |
| --- | --- | --- |
| grant\_type (必須) | 文字列 | 値は”refresh\_token”で固定 |
| client\_id (必須) | 文字列 |  |
| client\_secret (必須) | 文字列 |  |
| refresh\_token (必須) | 文字列 |  |

#### レスポンス例

##### ステータスライン / レスポンスヘッダ

```
HTTP/1.1 200 OK
Content-Type:application/json;charset=utf-8

```
##### レスポンスボディ

```
{
    "access_token": "YOUR_ACCESS_TOKEN",
    "token_type":"Bearer",
    "expires_in":3600,
    "refresh_token":"YOUR_REFRESH_TOKEN"
}

```
   