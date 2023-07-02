from lxml import etree
import requests
from fake_useragent import UserAgent

url = 'https://www.qidian.com/rank/yuepiao/'

headers = {
    "User-Agent": UserAgent().random
}

resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"

e = etree.HTML(resp.text)
names = e.xpath("//div[@class='book-mid-info']/h2/a/text()")
authors = e.xpath('//p[@class="author"]/a[@class="name"]/text()')

for name, author in zip(names, authors):
    print(name, ":", author)
