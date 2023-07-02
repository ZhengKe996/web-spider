from urllib.request import urlopen
from urllib.request import Request

from urllib.parse import quote
from urllib.parse import urlencode

# arg = "你好啊"
args = {"wd": "你好啊", "ie": "utf-8"}

# print(urlencode(args))
# url = "https://baidu.com/s?wd={}".format(quote(arg))
url = "https://baidu.com/s?{}".format(urlencode(args))

# 设置 User_Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

req = Request(url, headers=headers)  # 封装Request对象

resp = urlopen(url)  # 发送请求

print(resp.read().decode())
