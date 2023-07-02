from urllib.request import ProxyHandler, build_opener, Request, HTTPHandler
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'
ua = UserAgent()
headers = {
    'User-Agent': ua.random,
}
req = Request(url, headers=headers)
handler = HTTPHandler(debuglevel=1)

proxy = ProxyHandler({"http": "61.145.212.31:3128"})
opener = build_opener(handler, proxy)

resp = opener.open(req)

print(resp.read().decode())
