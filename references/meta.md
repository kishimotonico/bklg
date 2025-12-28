   
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

      
# レート制限

Backlog API は各ユーザーに対して、1分間に受付可能なリクエスト数を制限します。この制限は、以下の種別ごとに適用されます。

## 種別

### 読み込み

アイコンおよび検索に含まれないGETリクエスト

### 更新

POST、PATCHおよびDELETEリクエスト

### 検索

* [課題一覧の取得](https://developer.nulab.com/ja/docs/backlog/api/2/get-issue-list/)
* [課題数の取得](https://developer.nulab.com/ja/docs/backlog/api/2/count-issue/)
* [Wikiページ一覧の取得](https://developer.nulab.com/ja/docs/backlog/api/2/get-wiki-page-list/)
* [Wikiページ数の取得](https://developer.nulab.com/ja/docs/backlog/api/2/count-wiki-page/)

### アイコン

* [スペースアイコン画像の取得](https://developer.nulab.com/ja/docs/backlog/api/2/get-space-logo/)
* [ユーザーアイコンの取得](https://developer.nulab.com/ja/docs/backlog/api/2/get-user-icon/)
* [プロジェクトアイコンの取得](https://developer.nulab.com/ja/docs/backlog/api/2/get-project-icon/)
* [グループアイコンの取得](https://developer.nulab.com/ja/docs/backlog/api/2/get-group-icon/)
* [チームアイコンの取得](https://developer.nulab.com/ja/docs/backlog/api/2/get-team-icon/)

## リクエスト数の上限

リクエスト数の上限は、上記の種別とプランによって異なります。

現在の上限は[レート制限情報の取得](https://developer.nulab.com/ja/docs/backlog/api/2/get-rate-limit)から取得できます。APIを利用する際は、リクエスト数が現在の上限以内に収まるようにしてください。

また、Backlogのシステムに高い負荷がかかり、正常な応答が難しい場合には、リクエスト数の上限が下がる可能性があります。

## レスポンス

### ステータスライン

リクエスト数が上限を超えた場合、APIサーバは429（Too many requests）を返します。429が返された場合のレスポンスボディは、[エラーレスポンス](https://developer.nulab.com/ja/docs/backlog/error-response/)をご確認ください。

### レスポンスヘッダ

すべてのレスポンスに、以下のヘッダが含まれます。これらのヘッダを確認することで、レート制限の動作の詳細を確認できます。

| HTTPヘッダ名 | HTTPヘッダの内容 |
| --- | --- |
| X-RateLimit-Limit | 1分間に受付可能な最大リクエスト数 |
| X-RateLimit-Remaining | X-RateLimit-Resetの時刻までに受付可能な残りリクエスト数 |
| X-RateLimit-Reset | リクエスト数の計測がリセットされる時刻（UNIX時間） |

### レスポンスヘッダ例

2020年11月16日9:00:00(JST)に最初の更新APIへのリクエストを行い、すでに8回のリクエストを実行した場合のレスポンスヘッダの例です。残り142回のアクセスが可能で、2020年11月16日9:01:00（JST/UNIXタイムスタンプ1605484860）にリクエスト数がリセットされることを示しています。

* X-RateLimit-Limit: 150
* X-RateLimit-Remaining: 142
* X-RateLimit-Reset: 1605484860

## レート制限への対策

レート制限に抵触しないために、以下の対策を行ってください。

* 1つのソフトウェアから、同時に複数のリクエストを送信しない。1つのリクエストに対して応答が返されてから、次のリクエストを送信する。
* 大量の更新・検索リクエストを送信する必要がある場合は、リクエストの送信ごとに最低1秒の待ち時間をおく。
* 429 が返された場合は、1分経過後にリクエストを再送する。どうしても待ち時間を1分よりも短くしなければならない場合は、X-RateLimit-Resetの値をもとに待ち時間の長さを調節する。
* 定期的に実行するソフトウェア（定時バッチなど）の場合、過去のリクエスト結果をキャッシュし、なるべくリクエスト数を減らす。
* 定期的に実行するソフトウェア（定時バッチなど）の場合、更新日などの条件を使い、なるべく取得するデータ件数を減らす（例：[課題一覧の取得](https://developer.nulab.com/ja/docs/backlog/api/2/get-issue-list/)のupdatedSinceパラメーター）。

一方、このレート制限を回避するために、 **1つのソフトウェアが、複数のユーザーのAPIキーを用いてリクエストを送信することは推奨しません。** そのようなリクエストが発見された場合、さらに厳しいレート制限の適用や、APIキーの利用停止をさせていただく可能性があります。

## 注意点

この制限はAPIキー単位ではなく、ユーザー単位であることにご注意ください。

あるユーザーがAPIキー1とAPIキー2を作成した場合、APIキー1が制限を受けている時間には、APIキー2も同じ制限を受けます。

また、ヌーラボが提供する以下のソフトウェアもAPIキーを利用します。そのため、複数のソフトウェアを同時に実行した場合は、それらのリクエスト数の合計がレート制限の上限を超える可能性があります。

* [Googleスプレッドシートによる課題一括登録](https://support-ja.backlog.com/hc/ja/articles/360042820873)
* [Backlog移行ツール](https://backlog.com/ja/backlog-migration/releases.html)
* [Backlog Migration for JIRA](https://github.com/nulab/BacklogMigration-Jira)
* [Backlog Redmine Importer](https://backlog.com/ja/redmine_importer/)
   