import scrapy
from ..items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        names = response.xpath('//div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
        stars = response.xpath('//div[@class="star"]/span[@class="rating_num"]/text()').extract()
        quotes = response.xpath('//p[@class="quote"]/span[@class="inq"]/text()').extract()

        movies = []
        item = DoubanItem()
        for name, star, quote in zip(names, stars, quotes):
            # yield {"name": name, "star": star, "quote": quote}

            item['name'] = name
            item['star'] = star
            yield item

        # return movies
