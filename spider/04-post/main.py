from urllib.request import urlopen, Request
from urllib.parse import urlencode

url = 'https://www.imooc.com/passport/user/login'

args = {"username": "19816896292", "password": "123456"}
# 设置 User_Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

request = Request(url, headers=headers, data=urlencode(args).encode())

resp = urlopen(request)

print(resp.read().decode())
