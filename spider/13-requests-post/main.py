import requests

url = 'https://www.imooc.com/passport/user/login'

args = {"username": "19816896292", "password": "123456"}

resp = requests.post(url, data=args)

resp.encoding = "utf-8"
print(resp.text)
