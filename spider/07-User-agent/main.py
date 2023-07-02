from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'

ua = UserAgent()

headers = {
    'User-Agent': ua.random,
    'Referer': 'http://www.zhihu.com/articles'
}

req = Request(url, headers=headers)

resp = urlopen(req)

print(resp.read().decode())
