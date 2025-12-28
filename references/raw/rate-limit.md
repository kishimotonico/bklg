   
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
   