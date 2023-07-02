from urllib.request import Request, build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar
from fake_useragent import UserAgent

# 声明一个CookieJar对象实例来保存cookie
cookie = CookieJar()
# 利用HTTPCookieProcessor对象来创建cookie处理器
cookiePro = HTTPCookieProcessor(cookie)

url = 'http://httpbin.org/get'
ua = UserAgent()
headers = {
    'User-Agent': ua.random,
}

req = Request(url, headers=headers)
opener = build_opener(cookiePro)

resp = opener.open(req)

print(resp.read().decode())
