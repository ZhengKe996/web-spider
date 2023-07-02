from scrapy.cmdline import execute

# execute("scrapy crawl zongheng".split())
execute("scrapy crawl zongheng -o boos.json -t json".split())
# execute("scrapy crawl zongheng -o boos.csv -t csv".split())
# execute("scrapy crawl zongheng -o boos.xml -t xml".split())
