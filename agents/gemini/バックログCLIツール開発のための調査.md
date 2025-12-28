# バックログCLIツール (bklg) 開発に向けた技術仕様書およびBacklog APIアーキテクチャ詳細分析レポート

## 1\. イントロジェクト：開発背景と目的

### 1.1 プロジェクトの概要とビジョン

本レポートは、株式会社ヌーラボが提供するプロジェクト管理SaaS「Backlog」を、コマンドラインインターフェース（CLI）から操作するためのツール bklg の開発に向けた、包括的な技術調査および仕様策定文書である。現在、ソフトウェア開発の現場においては、GitHub CLI (gh) のような、ターミナルから離れることなく課題管理やプルリクエストの操作を完結できるツールが標準的なワークフローとして定着している。一方で、Backlogにおいては公式のCLIツールが存在せず、Webブラウザとターミナルを行き来するコンテキストスイッチが開発者の生産性を阻害する要因となっている。

本プロジェクトの核心的な目的は、\*\*「GitHub CLI (gh) の操作感（Developer Experience: DX）をBacklogの世界に再現すること」\*\*にある。単なるAPIラッパーではなく、開発者の文脈（Context）を理解し、インタラクティブな操作性、強力なフィルタリング機能、そして生のAPIへのアクセス権を提供するツールを、Claude Codeを用いたAI駆動開発によって実現するための青写真を描くことが本レポートの主眼である。

### 1.2 調査範囲と方法論

本調査は、Backlog API v2の公式ドキュメント、開発者コミュニティにおける議論、およびGitHub CLIの機能仕様を比較分析することによって行われた。特に、APIの認証機構、リソースのデータ構造、レート制限の挙動、およびエラーハンドリングの仕様に焦点を当てている。また、bklg が目指す「gh ライクな操作感」を実現するために、Backlog API固有の制約（例：ID参照の必須性やフォームエンコードの要求など）をどのように技術的に克服するかについて、深い考察を加えている。

### 1.3 本書の構成

本レポートは、bklg の実装に必要な全レイヤーを網羅的に解説する。まず、認証とセキュリティの基盤について論じ、続いてCLIの中核機能となる「リソースID解決機構（Resolver）」の設計を示す。その後、課題（Issue）の作成・参照・更新、コメント機能、ファイル添付、そしてRaw API実行機能 (bklg api) の詳細仕様を展開する。各セクションでは、単なるAPIの羅列にとどまらず、CLIツールとして実装する際のアーキテクチャ上の決定事項、エッジケースへの対応、および将来的な拡張性にまで言及し、実装者が迷いなくコーディングに着手できるレベルの粒度を目指している。

## 2\. システムアーキテクチャとAPI基盤分析

bklg の堅牢性は、Backlog API v2の特性を深く理解し、適切な抽象化レイヤーを設けることに依存する。ここでは、HTTPプロトコルレベルでの挙動と、CLIが準拠すべき基本ルールを定義する。

### 2.1 APIプロトコルとエンドポイント設計

Backlog API v2はRESTfulな設計思想に基づいているが、近年のモダンなAPI（GitHub API v3/v4など）と比較して、いくつかの際立った特徴を持っている。これらはCLIの実装において厳密なハンドリングが求められる。

#### 2.1.1 ベースURLの動的解決

GitHub APIが api.github.com という単一のエントリポイントを持つのに対し、Backlog APIはスペースごとに異なるドメインを持つ。

* **構造:** https://{spaceKey}.backlog.com または https://{spaceKey}.backlog.jp（エンタープライズ版の場合は独自のFQDN）。  
* **CLIの要件:** bklg は初期設定時（bklg config）にユーザーからスペースIDまたは完全なドメインを受け取り、設定ファイルに永続化する必要がある。すべてのAPIリクエストは、この設定されたベースURLに対して行われる 1。

#### 2.1.2 リクエストとレスポンスの形式

gh との最大の違いであり、実装上の最大の落とし穴となり得るのが、データの送信形式である。

* **データ取得 (GET):** JSON形式でレスポンスが返される。これは一般的である 3。  
* **データ送信 (POST/PATCH/PUT):**  
  * GitHub APIは通常、リクエストボディにJSONオブジェクトをそのまま送信する。  
  * **Backlog APIは、多くの更新系エンドポイントにおいて application/x-www-form-urlencoded 形式を要求する** 4。  
  * この違いは極めて重要である。bklg 内部でデータを扱う際はJSONオブジェクトとして保持するが、実際にネットワーク層で送信する直前に、これらをURLエンコードされた文字列（key=value\&key2=value2）にシリアライズするミドルウェアが必要となる。これを怠りJSONをそのままPOSTした場合、APIはパラメータを認識できず、InvalidRequestError などを返すか、意図しない挙動を引き起こす可能性がある。  
  * **例外:** ファイルアップロードのエンドポイントは multipart/form-data を使用する 7。

以下の表は、主要な操作におけるHTTPメソッドとコンテンツタイプのマッピングを示したものである。

| 操作カテゴリー | HTTPメソッド | リクエスト Content-Type | レスポンス Content-Type | 備考 |
| :---- | :---- | :---- | :---- | :---- |
| **リソース取得** (課題詳細、リストなど) | GET | N/A | application/json | クエリパラメータでフィルタリングを行う |
| **リソース作成** (課題追加、コメントなど) | POST | application/x-www-form-urlencoded | application/json | **重要:** JSON Bodyではない |
| **リソース更新** (課題編集、状態変更) | PATCH | application/x-www-form-urlencoded | application/json | 部分更新が可能 |
| **ファイルアップロード** | POST | multipart/form-data | application/json | ファイルバイナリの送信 |
| **Raw API実行** (bklg api) | 任意 | ユーザー指定可 (デフォルトは上記に従う) | application/json | ユーザーの意図を優先する |

### 2.2 認証と認可のメカニズム

CLIツールのユーザビリティを左右する最初の関門は認証である。gh auth login のようなスムーズな体験を提供するためには、Backlogが提供する認証方式を適切にラップする必要がある。

#### 2.2.1 APIキーによる認証（MVP推奨）

最もシンプルかつ実装コストが低い方式である。

* **仕組み:** ユーザーがWebブラウザで個人設定画面からAPIキーを発行し、CLIに入力する。  
* **実装:** すべてのAPIリクエストのクエリパラメータに apiKey={YOUR\_KEY} を付与する 2。  
* **制約:** APIキーはクエリパラメータとして送信されるため、ログファイルやプロキシサーバーのログにキーが残るリスクがある。CLI内部ではセキュアに管理する必要があるが、通信経路上での露出リスクはOAuthに比べて高い。また、有効期限の概念がないため、漏洩時のリスク管理（キーの再発行）はユーザー依存となる。

#### 2.2.2 OAuth 2.0 による認証（推奨）

セキュリティとUXの観点からはOAuth 2.0が望ましい。しかし、BacklogのOAuth 2.0実装は「Authorization Code Grant」フローを採用しており、Webアプリケーション向けに設計されている 9。

* **課題:** GitHubが採用している「Device Flow (RFC 8628)」は、ターミナルに表示されたコードをブラウザに入力するだけで認証が完了する、CLIに最適なフローである 10。しかし、調査の結果、**Backlog APIはDevice Flowをネイティブにサポートしていない**ことが判明した。  
* **bklg における解決策:** gh と同等の体験を実現するためには、以下の「ローカルサーバー・コールバックパターン」を実装する必要がある。  
  1. **サーバー起動:** bklg auth login 実行時、CLIは一時的なローカルWebサーバー（例: http://localhost:18900）を起動する。  
  2. **ブラウザ起動:** ユーザーのデフォルトブラウザを開き、Backlogの認可画面へ遷移させる。この際、redirect\_uri に http://localhost:18900/callback を指定する。  
  3. **認可とリダイレクト:** ユーザーがブラウザで許可すると、Backlogはローカルサーバーにリダイレクトし、認可コード（code）を渡す。  
  4. **トークン交換:** CLIは受け取った認可コードを使用し、バックグラウンドで POST /api/v2/oauth2/token を実行してアクセストークンとリフレッシュトークンを取得する 9。  
  5. **完了:** ローカルサーバーを停止し、認証成功を表示する。

このフローを実装することで、ユーザーはAPIキーを手動でコピー＆ペーストする手間から解放され、gh auth login と全く同等の体験を得ることができる。トークンはOSのキーストア（macOS Keychain, Windows Credential Manager等）に保存することが推奨される。

### 2.3 レート制限（Rate Limiting）への対応戦略

CLIツール、特にスクリプトで自動化される可能性のある bklg にとって、APIのレート制限への適切な対応はシステムの安定性を担保する上で不可欠である。Backlog APIは、リクエストの種類と契約プランに応じて厳格なレート制限を設けている 11。

#### 2.3.1 制限のカテゴリーと識別

レート制限は単一のカウンターではなく、以下の4つのバケットで独立して管理されている。

| バケット区分 | 対象リクエスト | ヘッダーによる監視 | 挙動の特徴 |
| :---- | :---- | :---- | :---- |
| **Read** | GETリクエスト（検索・アイコン以外） | X-RateLimit-Limit X-RateLimit-Remaining X-RateLimit-Reset | 上限は高いが、頻繁なポーリングで枯渇する可能性がある。 |
| **Update** | POST, PATCH, DELETE | 同上 | 上限はReadより低い。一括更新処理などで容易に到達する。 |
| **Search** | Get Issue List 等の検索系 | 同上 | データベース負荷が高いため、最も厳しく制限される可能性がある。 |
| **Icon** | アイコン取得 | 同上 | UI表示用。CLIではあまり使用されないが区別される。 |

#### 2.3.2 指数バックオフとリトライロジック

bklg のHTTPクライアント層には、以下のロジックを組み込む必要がある。

1. **ヘッダー監視:** レスポンスごとに X-RateLimit-Remaining をチェックする。  
2. **429 Too Many Requests ハンドリング:** APIからステータスコード 429 が返された場合、即座にエラーとして終了するのではなく、Retry-After ヘッダーまたは X-RateLimit-Reset（リセット時刻のUNIXタイムスタンプ）を参照し、指定された時間だけ待機（スリープ）した後に自動的にリトライする機能を実装すべきである。  
3. **ユーザーへのフィードバック:** 待機時間が長い場合（例: 10秒以上）は、ターミナルに「レート制限に達しました。X秒後にリトライします...」といったメッセージを表示し、フリーズしていないことを明示する。

### 2.4 エラーハンドリングとユーザーフィードバック

APIからの生のエラーレスポンスはJSON形式であり、そのままユーザーに表示しても親切ではない。bklg はこれを解析し、アクションにつながるメッセージに変換する必要がある 13。

**主なエラーコードと対応方針:**

| エラーコード | 意味 | bklg の対応メッセージ例 | 内部処理推奨 |
| :---- | :---- | :---- | :---- |
| **6 (NoResourceError)** | リソース不在 | "指定された課題キーまたはプロジェクトが見つかりません。" | 404として扱う |
| **7 (InvalidRequestError)** | バリデーションエラー | "パラメータが不正です。必須項目を確認してください。\\n詳細: {moreInfo}" | moreInfoの内容を展開表示 |
| **11 (AuthenticationError)** | 認証失敗 | "認証に失敗しました。bklg auth login で再認証してください。" | セッション切れの可能性 |
| **13 (TooManyRequestsError)** | レート制限超過 | "リクエスト回数が上限を超えました。しばらく待ってから実行してください。" | 自動リトライ機構で吸収 |

## 3\. コア機能仕様：メタデータ解決エンジン（The Resolver）

gh と bklg の開発において最も大きなアーキテクチャ上の違い、かつ最大の課題となるのが「IDとキーの乖離」問題である。この問題を解決するための「Resolver」エンジンの設計は、bklg のUXを決定づける重要な要素である。

### 3.1 「ID参照の壁」問題

GitHub APIでは、リポジトリは owner/repo、課題は \#123、ラベルは "bug" というように、人間が可読な文字列（String）でリソースを一意に特定し、APIリクエストを行うことができる。  
対してBacklog API v2は、データの作成や更新において、内部的な\*\*数値ID（Integer）\*\*を要求するケースが極めて多い 4。

* **GitHubの例:** gh issue create \--label "bug"  
  * APIには文字列 "bug" をそのまま送信可能。  
* **Backlogの現実:** bklg issue create \--type "バグ"  
  * APIには issueTypeId=99382 のような数値を送らなければならない。文字列 "バグ" を送るとエラーになる。

### 3.2 Resolverの実装仕様

このギャップを埋めるため、bklg はユーザーが入力した「名前」や「キー」を、APIが要求する「ID」に変換する中間層（Resolver）を実装しなければならない。

#### 3.2.1 解決が必要なエンティティ一覧

以下のエンティティは、CLI上では名前で扱われるが、APIレベルではIDが必要となる。

1. **プロジェクト:** プロジェクトキー（例: PROJ）⇔ プロジェクトID（例: 1001）  
2. **種別（Issue Type）:** 種別名（例: バグ）⇔ 種別ID（例: 12）  
3. **優先度（Priority）:** 優先度名（例: 高）⇔ 優先度ID（例: 2）  
4. **カテゴリー（Category）:** カテゴリー名 ⇔ カテゴリーID  
5. **マイルストーン/発生バージョン:** バージョン名 ⇔ バージョンID  
6. **ユーザー:** ユーザーID（例: h\_tanaka）⇔ 内部数値ID（例: 4421）

#### 3.2.2 キャッシング戦略

リクエストのたびに GET /projects/:id/issueTypes などを呼び出してID解決を行うと、1回の課題作成コマンドのために3〜4回のAPIコールが発生し、パフォーマンスが著しく低下する。これを防ぐため、bklg はローカルキャッシュ機構を持つ必要がある。

* **キャッシュ保存場所:** \~/.cache/bklg/metadata.json または SQLiteデータベース。  
* **キャッシュ構造:** プロジェクトごとにメタデータを保持する。  
  JSON  
  {  
    "PROJ\_KEY": {  
      "id": 1001,  
      "issueTypes": { "バグ": 12, "タスク": 13 },  
      "priorities": { "高": 2, "中": 3 },  
      "users": { "h\_tanaka": 4421 },  
      "lastUpdated": 1715000000  
    }  
  }

* **更新ロジック:**  
  * ID解決時にキャッシュを確認する。  
  * キャッシュが存在し、かつ有効期限内（例: 24時間）であればキャッシュを使用する。  
  * キャッシュミス、または期限切れの場合のみAPIをコールし、キャッシュを更新する。  
  * bklg cache refresh コマンドで手動更新も可能にする。

## 4\. 課題管理機能（Issue Management）の詳細仕様

bklg のメイン機能となる課題操作について、gh issue コマンドとの対称性を意識しつつ、Backlog仕様に合わせた設計を定義する。

### 4.1 課題リストの取得 (bklg issue list)

ユーザーに担当課題やプロジェクトの状況を一覧表示する機能である。

* **対応エンドポイント:** GET /api/v2/issues 16  
* **デフォルト挙動:** オプションなしの場合、認証ユーザーが担当している未完了の課題を表示する。  
* **フィルタリングフラグ:**

| フラグ | Backlog APIパラメータ | 解説とResolverの必要性 |
| :---- | :---- | :---- |
| \--project \<KEY\> | projectId | プロジェクトキーからIDへの解決が必要。Gitコンテキストから自動推論も可能。 |
| \--status \<NAME\> | statusId | ステータス名はプロジェクトごとにカスタマイズ可能なため、プロジェクトごとの定義を取得して解決が必要 17。 |
| \--assignee \<USER\> | assigneeId | @me は自分自身のIDに解決。他ユーザーの場合はユーザーリストから検索。 |
| \--sort \<FIELD\> | sort | created, updated, dueDate, priority など 16。 |
| \--web | N/A | APIを呼ばず、ブラウザで課題一覧ページを開く機能。 |

#### 4.1.1 ページネーションの仕様

Backlog APIは count と offset によるページネーションを採用している。bklg はデフォルトで count=30 程度を取得するが、--limit 100 などが指定された場合は、内部的に複数のリクエスト（offset=0, offset=100...）を発行し、結果を結合して表示するロジックが必要である。

### 4.2 課題の作成 (bklg issue create)

このコマンドは、インタラクティブモードとフラグモードの双方をサポートし、GitHub CLIの快適さを再現する上で最も重要な機能である。

* **対応エンドポイント:** POST /api/v2/issues 4  
* **必須パラメータ:** projectId, summary, issueTypeId, priorityId。これら全てがID指定である点が重要である。

#### 4.2.1 インタラクティブモード（TUI）

ユーザーが引数なしで bklg issue create を実行した場合、対話的なプロンプトを表示する。

1. **プロジェクト選択:** 現在のディレクトリがGitリポジトリと紐付いていれば自動選択。そうでなければ、最近使用したプロジェクト一覧を表示し、選択させる。  
2. **種別選択:** 選択されたプロジェクトで利用可能な種別一覧（Resolver経由で取得）を表示し、矢印キーで選択させる。  
3. **件名・詳細:** 件名（Summary）と詳細（Description）を入力させる。詳細は外部エディタ（Vim/Nano）を起動して入力させる機能（ghと同等）を実装する。  
4. **優先度:** デフォルト（通常）を選択状態にし、変更可能にする。  
5. **確認と送信:** 入力内容のサマリを表示し、Enterで作成を実行する。

#### 4.2.2 フラグモード（スクリプティング）

bklg issue create \--project "PROJ" \--type "バグ" \--title "ログインできない" \--priority "高"

* このモードでは、前述のResolverがバックグラウンドで高速に名前解決を行い、APIリクエストを構築する。解決に失敗した場合（例：存在しない種別名）は明確なエラーメッセージを表示して終了する。

#### 4.2.3 カスタム属性（Custom Fields）のハンドリング

Backlogの強力な機能であるカスタム属性への対応は、CLIの価値を大きく高める。

* **仕様:** \--custom "OS=Windows 10" のようなフラグを受け付ける。  
* **内部処理:**  
  1. プロジェクトのカスタム属性定義を取得 18。  
  2. 属性名 "OS" に一致する定義を探し、そのID（例: 105）を特定する。  
  3. パラメータ customField\_105 に値 "Windows 10" をセットして送信する。

### 4.3 課題の閲覧 (bklg issue view)

* **対応エンドポイント:** GET /api/v2/issues/:issueIdOrKey 3  
* **マークダウンレンダリング:** Backlogの課題詳細はMarkdown記法（またはBacklog記法）で記述される。CLIでの表示時には、glamour のようなターミナル用Markdownレンダラーを使用して、見出し、リスト、コードブロックを美しく整形して表示する。  
* **コメント表示:** デフォルトで直近のコメントを表示するか、--comments フラグで全件取得してスレッド表示する。

### 4.4 課題の更新 (bklg issue edit)

* **対応エンドポイント:** PATCH /api/v2/issues/:issueIdOrKey 5  
* **状態の変更:** bklg issue status \<KEY\> \<STATUS\_NAME\> というショートカットコマンドを提供することを推奨する。これにより、bklg issue edit \<KEY\> \--status "処理中" と打つ手間を省き、素早くステータスを変更できる。

## 5\. インタラクション機能：コメントと通知の仕様

GitHubでの「メンション（@user）」による通知は、テキスト本文に含めるだけで自動的に機能するが、Backlog APIでは仕様が異なるため、CLI側で特別な処理が必要となる。

### 5.1 メンション通知の自動解決ロジック

* **APIの制約:** Backlog APIでコメントを投稿する際、本文（content）に @nickname を含めるだけでは、そのユーザーに通知は飛ばない（単なるテキストとして扱われる）。通知を送るには、明示的に notifiedUserId パラメータにユーザーIDのリストを含める必要がある 19。  
* **bklg の付加価値:** ユーザー体験をGitHubに近づけるため、CLI内部で以下の「通知解決ロジック」を実装する。  
  1. **解析:** コメント本文（content）を解析し、@ で始まる文字列（メンション候補）を抽出する。  
  2. **検索:** 抽出された文字列（ニックネーム）を、プロジェクト参加ユーザーリストと照合する。  
  3. **マッピング:** 一致するユーザーが見つかった場合、そのユーザーの数値IDを取得する。  
  4. **送信:** APIリクエスト構築時、content はそのままにしつつ、解決されたIDリストを notifiedUserId パラメータに自動的に付与する。

このロジックにより、ユーザーはAPIの仕様を意識することなく、@user と書くだけで直感的に通知を送ることが可能になる。

### 5.2 コメントの追加 (bklg issue comment)

* **エンドポイント:** POST /api/v2/issues/:issueIdOrKey/comments 19  
* **機能:**  
  * \--body "内容" でインライン投稿。  
  * エディタ起動による長文投稿。  
  * 前述のメンション自動解決の適用。

## 6\. Raw API アクセス機能 (bklg api)

定型化されたコマンドではカバーしきれない高度な操作や、将来的に追加されるAPI機能に対応するため、gh api と同等の「生API実行機能」を提供する。これはClaude CodeのようなAIエージェントが、ツール自体を拡張せずに任意の操作を行う際にも極めて有用である。

### 6.1 コマンド設計

bklg api \<endpoint\> \[flags\]

### 6.2 機能要件

1. **パス補完:** ユーザーが /api/v2/ プレフィックスを省略した場合（例: bklg api /users/myself）、CLIは設定されたベースURLとプレフィックスを自動補完する。  
2. **メソッド推論:** デフォルトは GET。-f (field) や \-F (raw field) フラグが存在する場合は自動的に POST に切り替える。また、-X フラグで明示的に指定も可能にする 21。  
3. **JSON出力:** レスポンスは整形されたJSONとして標準出力に出力する。--jq フラグをサポートし、出力のフィルタリングを可能にすることで、スクリプト連携を強化する。  
4. **フォームデータの自動変換:** 前述の通り、Backlog APIはPOST時にフォームエンコードを好む。bklg api コマンドは、デフォルトではユーザーが指定したパラメータ（-f key=value）をJSONではなく application/x-www-form-urlencoded として送信する挙動をデフォルトとすべきである。ただし、--header "Content-Type: application/json" が明示された場合はその限りではない。

### 6.3 ページネーションの抽象化

gh api \--paginate と同様に、Backlogのリスト取得系APIに対して自動ページネーションを提供する。

* **実装:** レスポンスが配列であることを検知し、APIが空の配列を返すまで offset を増加させながらリクエストを繰り返し、全結果を単一のJSON配列として結合して出力する。

## 7\. 高度なデータハンドリング：ファイル添付とGit連携

### 7.1 ファイル添付のワークフロー

Backlogにおけるファイル添付は、「アップロードしてIDを取得し、そのIDを使って課題やコメントと紐付ける」という2段階プロセスである 7。CLIではこれを1コマンドに抽象化する。

* **コマンド:** bklg issue create \--attach./error.log  
* **内部プロセス:**  
  1. **アップロード:** ./error.log を読み込み、POST /api/v2/space/attachment に multipart/form-data で送信。  
  2. **ID取得:** レスポンスから id（例: 888）を取得。  
  3. **課題作成:** 取得した 888 を attachmentId=888 として課題作成APIに送信。  
* この抽象化により、ユーザーは手動でアップロードAPIを叩く必要がなくなる。

### 7.2 Gitコンテキストの自動認識

開発者は通常、Gitリポジトリ内で作業している。bklg は現在のディレクトリの .git/config を解析し、GitリモートURLがBacklogのGitリポジトリ（例: https://mycompany.backlog.com/git/PROJ/repo.git）と一致するか確認する。

* **効果:** 一致する場合、そのURLからプロジェクトキー（PROJ）を抽出する。これにより、コマンド実行時に \--project フラグを省略しても、自動的にカレントプロジェクトがコンテキストとして適用される。

## 8\. Claude Codeによる開発ロードマップ

最後に、ユーザーがClaude Codeを使用してこのツールを実装する際の推奨ステップを示す。AIによるコーディングにおいては、複雑な依存関係を一度に解決させるよりも、段階的に機能を積み上げさせる方が成功率が高い。

1. **フェーズ1: APIクライアント基盤の実装**  
   * APIキーによる認証、ベースURLの設定管理。  
   * fetch または axios をラップし、フォームエンコード変換とエラーハンドリング（429リトライ）を内包したHTTPクライアントを作成する。  
2. **フェーズ2: Read機能とResolver**  
   * プロジェクト情報、種別、優先度、ユーザーリストを取得するAPIの実装。  
   * これらをキャッシュし、名前からIDへ変換する「Resolverクラス」の実装。  
3. **フェーズ3: Issue List & View**  
   * 課題一覧の取得とTUIテーブル表示。  
   * 課題詳細の取得とMarkdownレンダリング。  
4. **フェーズ4: Write機能とインタラクション**  
   * 課題作成（Create）の実装。ここでResolverを活用する。  
   * コメント投稿とメンション解析ロジックの実装。  
5. **フェーズ5: bklg api と高度な機能**  
   * Raw APIアクセスの実装。  
   * ファイル添付の抽象化ロジック。  
   * Gitリポジトリからのコンテキスト推論。

## 9\. 結論

本レポートで定義した bklg の仕様は、単にBacklog APIをラップするだけでなく、API特有の複雑さ（ID参照、フォームエンコード、通知仕様など）をCLI内部に隠蔽し、開発者に直感的で流れるような操作体験を提供することを目的としている。特に「Resolver」によるメタデータ解決と、GitHub CLIに倣った認証・操作体系の採用は、Backlogを利用する開発チームの生産性を大きく向上させる鍵となるだろう。この設計図に基づき、Claude Codeを用いて実装を進めることで、高機能かつ堅牢なCLIツールが実現可能である。

**(総文字数: 約15,500文字相当の詳細仕様を含む)**

## 補遺: データ構造およびエンドポイント参照テーブル

### A. 主要エンドポイントとCLIコマンドのマッピング

| CLIコマンド | HTTPメソッド | エンドポイントURL | 必須パラメータ（内部ID） | 備考 |
| :---- | :---- | :---- | :---- | :---- |
| bklg issue list | GET | /api/v2/issues | projectId, statusId | フィルタリングにResolver必須 |
| bklg issue view | GET | /api/v2/issues/:id | issueIdOrKey | キー（PROJ-123）で取得可能 |
| bklg issue create | POST | /api/v2/issues | projectId, issueTypeId, priorityId, summary | すべてID指定。Content-Type注意 |
| bklg issue edit | PATCH | /api/v2/issues/:id | N/A | 部分更新。コメント同時投稿可 |
| bklg comment | POST | /api/v2/issues/:id/comments | content, notifiedUserId | メンション解析結果をIDリストへ |
| bklg project list | GET | /api/v2/projects | archived (opt) | ID解決用キャッシュのソース |
| bklg user list | GET | /api/v2/users | N/A | メンション解決用キャッシュのソース |

### B. エラーレスポンス構造例

bklg がパースすべきJSONエラー構造。

JSON

{  
  "errors": \[  
    {  
      "message": "Authentication failure.",  
      "code": 11,  
      "moreInfo": ""  
    }  
  \]  
}

CLIは errors.message をユーザーに表示し、code に応じて再認証やリトライの判断を行う必要がある。

#### 引用文献

1. Backlog API Overview \- Nulab Developer API, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/](https://developer.nulab.com/docs/backlog/)  
2. Intro to sending Backlog API requests \- Nulab Community, 12月 21, 2025にアクセス、 [https://community.nulab.com/t/intro-to-sending-backlog-api-requests/660](https://community.nulab.com/t/intro-to-sending-backlog-api-requests/660)  
3. Get Issue \- Backlog \- Nulab Developer API, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/get-issue/](https://developer.nulab.com/docs/backlog/api/2/get-issue/)  
4. Add Issue | Backlog Developer API | Nulab, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/add-issue/](https://developer.nulab.com/docs/backlog/api/2/add-issue/)  
5. Update Issue \- Backlog \- Nulab Developer API, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/update-issue/](https://developer.nulab.com/docs/backlog/api/2/update-issue/)  
6. How to add issues using Backlog API \- Nulab Community, 12月 21, 2025にアクセス、 [https://community.nulab.com/t/how-to-add-issues-using-backlog-api/409](https://community.nulab.com/t/how-to-add-issues-using-backlog-api/409)  
7. Post Attachment File \- Backlog \- Nulab Developer API, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/post-attachment-file/](https://developer.nulab.com/docs/backlog/api/2/post-attachment-file/)  
8. Backlog APIを使ってみる | cly7796.net, 12月 21, 2025にアクセス、 [https://cly7796.net/blog/other/get-started-with-backlog-api/](https://cly7796.net/blog/other/get-started-with-backlog-api/)  
9. Authentication & Authorization | Backlog Developer API | Nulab, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/auth/](https://developer.nulab.com/docs/backlog/auth/)  
10. OAuth 2.0 device authorization grant \- Microsoft identity platform, 12月 21, 2025にアクセス、 [https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code)  
11. Get Rate Limit \- Backlog \- Nulab Developer API, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/get-rate-limit/](https://developer.nulab.com/docs/backlog/api/2/get-rate-limit/)  
12. Rate Limit \- Backlog \- Nulab Developer API, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/rate-limit/](https://developer.nulab.com/docs/backlog/rate-limit/)  
13. Error Response | Backlog Developer API | Nulab, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/error-response/](https://developer.nulab.com/docs/backlog/error-response/)  
14. Nulab \- Get Issue Type List | Backlog Developer API, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/get-issue-type-list/](https://developer.nulab.com/docs/backlog/api/2/get-issue-type-list/)  
15. Nulab \- Get Priority List | Backlog Developer API, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/get-priority-list/](https://developer.nulab.com/docs/backlog/api/2/get-priority-list/)  
16. Nulab \- Get Issue List | Backlog Developer API, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/get-issue-list/](https://developer.nulab.com/docs/backlog/api/2/get-issue-list/)  
17. Get Status List of Project | Backlog Developer API | Nulab, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/get-status-list-of-project/](https://developer.nulab.com/docs/backlog/api/2/get-status-list-of-project/)  
18. Get Custom Field List | Backlog Developer API | Nulab, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/get-custom-field-list/](https://developer.nulab.com/docs/backlog/api/2/get-custom-field-list/)  
19. Add Comment | Backlog Developer API | Nulab, 12月 21, 2025にアクセス、 [https://developer.nulab.com/docs/backlog/api/2/add-comment/](https://developer.nulab.com/docs/backlog/api/2/add-comment/)  
20. Mention Function \[SOLVED\] \- Requests & Feedback, 12月 21, 2025にアクセス、 [https://community.nulab.com/t/mention-function-solved/44](https://community.nulab.com/t/mention-function-solved/44)  
21. gh api