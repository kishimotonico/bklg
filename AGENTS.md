## Rules

- MUST: プルリクエスト、コミットメッセージは日本語で記載すること
- SHOULD: コード内コメントは日本語で記載すること
- SHOULD: 実装はAPIコール数を適切に抑えることを意識ください
- SHOULD: ユーザーは `bklg issue list` などを軽率に実行します。そういった場合でも過剰なAPIコールを発生させないように注意してください

## Directories

- agents/
  - claude/: Claudeが出力したドキュメントを格納
  - gemini/: Geminiが出力したドキュメントを格納
- snippets/: バックログのドキュメントをスクレイピングするコードなど
- reference/: バックログのAPIドキュメント
  - raw/: バックログのドキュメントをMarkdownで保存
  - all_api.md: バックログのドキュメントを1ファイルにまとめたテキスト
- src/: ソースコード
- tests/: テストコード

バックログのAPIは snippets/docs 以下のドキュメントを参照して実装すること
