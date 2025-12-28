   
# Backlog API とは

## Backlog API で何が出来ますか？

課題,Wiki,ファイルの追加や取得を始め、プロジェクトやユーザーの管理などブラウザ上のBacklogでできる操作の大部分をAPIから行うことができます。詳しくは[API リスト](https://developer.nulab.com/ja/docs/backlog/api/2/get-space)を参照してください。
また、Cross Origin Resource Sharing (CORS) によるブラウザ上でのAjaxを使用したクロスドメイン通信が可能です。

## 認証

API Key 方式と OAuth 2.0 方式を提供しているため、用途に応じて使い分けることができます。詳しくは[認証と認可](https://developer.nulab.com/ja/docs/backlog/auth)を参照してください。

## API ライブラリ

公式ライブラリ [Backlog4J](https://github.com/nulab/backlog4j) をはじめ、有志の開発者の方たちが提供されているライブラリを使用することで、各種プログラミング言語を使用して API にアクセスすることができます。詳しくは[ライブラリ](https://developer.nulab.com/ja/docs/backlog/libraries)を参照してください。

## Webhook

Webhook は、課題やコメント、Wiki、ファイルの追加や更新、Subversion や Git へのコミットやプッシュなどのイベントが起きたときに、指定したURLにその情報を送信 (HTTPリクエスト)することができる機能です。

例えば、課題が更新されたときにチャットサービスに通知したり、Git リポジトリにプッシュされたときにビルドシステムに通知する等、他のサービスやシステムとの連携に利用することができます。

[Webhookについて](https://support-ja.backlog.com/hc/ja/articles/360036147713)

   