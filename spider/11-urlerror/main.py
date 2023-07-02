from urllib.request import Request, urlopen
from urllib.error import URLError

url = "http://www.sx435334t.cn/index/us3er.html"
try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    req = Request(url, headers=headers)
    resp = urlopen(url, timeout=1)
    print(resp.read().decode())
except URLError as e:
    if len(e.args) == 0:
        print(e.code)
    else:
        print(e.args[0])

print("获取数据完毕")
