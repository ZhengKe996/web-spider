from pyquery import PyQuery as pq
import requests
from fake_useragent import UserAgent

url = 'https://www.qidian.com/rank/yuepiao/'

headers = {
    "User-Agent": UserAgent().random
}

resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"

doc = pq(resp.text)

names = [a.text for a in doc('h2 a')]
authors_a = doc('.author a')

authors = []
for num in range(len(authors_a)):
    if num % 3 == 0:
        authors.append(authors_a[num].text)

for name, author in zip(names, authors):
    print(name, ":", author)
