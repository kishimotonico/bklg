import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from pathlib import Path
from markdownify import markdownify as md

save_dir = Path('snippets/docs/raw')
save_dir.mkdir(parents=True, exist_ok=True)

# ナビゲーションバーのHTMLを解析してURLを取得
url = 'https://developer.nulab.com/ja/docs/backlog/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
nav_links = soup.select('nav a[href]')

# URLから#content要素を抽出してファイルに保存
for link in tqdm(nav_links):
    link_url = link['href']
    if link_url.startswith('#'):
        continue
    full_url = f"https://developer.nulab.com{link_url}"

    response = requests.get(full_url)
    page_soup = BeautifulSoup(response.content, 'html.parser')
    content = page_soup.select_one('#contents')

    if content:
        # HTMLをMarkdownにする
        markdown_content = md(str(content), heading_style="ATX")
        # ファイル名にURL構造を反映
        filename = link_url.strip('/').replace('/', '_') + '.md'
        file_path = save_dir / filename
        file_path.write_text(markdown_content, encoding='utf-8')

print("抽出が完了しました。")


"""
# この後の手動操作

```
cd snippets/docs/raw
rename s/ja_docs_backlog_// *

mkdir api
mv api_2_* api/
cd api
rename s/api_2_// *
```

"""