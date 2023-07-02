from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import re

url = 'https://lunaw.cn/joke/'

headers = {
    "User-Agent": UserAgent().random
}

resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"

soup = BeautifulSoup(resp.text, "lxml")  # 创建一个BeautifulSoup对象

print(soup.find_all('p', class_='STYLE1'))
