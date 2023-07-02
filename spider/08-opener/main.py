from urllib.request import Request, build_opener, HTTPHandler
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'

ua = UserAgent()

headers = {
    'User-Agent': ua.random,
}
req = Request(url, headers=headers)
handler = HTTPHandler(debuglevel=1)

opener = build_opener(handler)

resp = opener.open(req)

# print(resp.read().decode())
