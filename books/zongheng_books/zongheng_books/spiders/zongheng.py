import scrapy


class ZonghengSpider(scrapy.Spider):
    name = "zongheng"
    allowed_domains = ["zhongheng.com"]
    start_urls = ["https://www.zongheng.com/rank/details.html?rt=9&d=1"]

    def parse(self, response):
        names = response.xpath('//div[@class="rank_d_b_name"]/@title').extract()
        authors = response.xpath('//div[@class="rank_d_b_cate"]/@title').extract()
        descriptions = response.xpath('//div[@class="rank_d_b_info"]/text()').extract()
        books = []
        for name, author, description in zip(names, authors, descriptions):
            books.append({"name": name, "author": author, "description": description})
        return books
