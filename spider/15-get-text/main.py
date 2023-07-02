import requests
from fake_useragent import UserAgent
import re

url = 'https://lunaw.cn/joke/'

headers = {
    "User-Agent": UserAgent().random
}

resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"

contents = re.findall('<p class="STYLE1">\s*(.+)', resp.text)

with open("demo.md", 'a', encoding='utf-8') as f:
    for info in contents:
        f.write(info + "\n\n")
