## ディレクトリ構造

- agents/
  - claude/: Claudeが出力したドキュメントを格納
  - gemini/: Geminiが出力したドキュメントを格納
-snippets/: バックログのドキュメントをスクレイピングするコードなど
  - docs/raw/: バックログのドキュメントをMarkdownで保存
  - docs/all_api.md: バックログのドキュメントを1ファイルにまとめたテキスト
- src/: ソースコード
- tests/: テストコード

バックログのAPIは snippets/docs 以下のドキュメントを参照して実装してください。
