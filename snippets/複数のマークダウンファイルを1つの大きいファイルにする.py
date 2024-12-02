from pathlib import Path
import re

input_directory = Path('snippets/docs/raw/api')
output_file = Path('snippets/docs/all_api.md')

with output_file.open('w', encoding='utf-8') as outfile:
    for filepath in input_directory.glob('*.md'):
        with filepath.open('r', encoding='utf-8') as infile:
            content = infile.read()
            # 最初の見出し要素がh1である場合にファイル名を追加
            content = re.sub(r'(^# .*)', r'\1 ({})'.format(filepath.stem), content, count=1, flags=re.MULTILINE)
            outfile.write(content)
            outfile.write('\n\n')

print("結合が完了しました。")