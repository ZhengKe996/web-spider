import requests

url = 'https://baidu.com/s'

params = {
    'wd': '你好啊'
}

resp = requests.get(url, params=params)
resp.encoding = "utf-8"
print(resp.text)
