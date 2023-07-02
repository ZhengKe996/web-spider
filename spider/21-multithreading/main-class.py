from threading import Thread
from queue import Queue
import requests
from lxml import etree
from fake_useragent import UserAgent
from time import sleep


class Spider(Thread):
    def __init__(self, url_queue):
        Thread.__init__(self)
        self.url_queue = url_queue

    def run(self):
        headers = {
            "User-Agent": UserAgent().random
        }
        while not self.url_queue.empty():
            url = self.url_queue.get()
            resp = requests.get(url, headers=headers)
            resp.encoding = "utf-8"
            e = etree.HTML(resp.text)
            contents = e.xpath('//div[@class="hd"]/a/@href')
            # print(contents)
        with open('demo.md', 'a', encoding='utf-8') as f:
            for content in contents:
                f.write(content + '\n')


if __name__ == '__main__':
    base_url = 'https://movie.douban.com/top250?start={}'
    url_queue = Queue()
    for num in range(1, 6):
        url_queue.put(base_url.format(num * 25))
    spider = Spider(url_queue)
    spider.start()
