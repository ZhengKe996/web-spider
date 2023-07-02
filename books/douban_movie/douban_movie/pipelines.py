from json import dumps


class DoubanMoviePipeline:
    def open_spider(self, spider):
        self.filename = open("movies.md", 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.filename.close()

    def process_item(self, item, spider):
        self.filename.write(dumps(dict(item), ensure_ascii=False) + "\n")
        return item
