from selenium import webdriver
from lxml import etree
from time import sleep

chrome = webdriver.Chrome()

chrome.get("https://search.jd.com/Search?keyword=%E8%BF%90%E5%8A%A8%E9%9E%8B&enc=utf-8&wq=%E8%BF%90%E5%8A%A8%E9%9E%8B&pvid=cb83850f79af4c8592fd775ea1c088a9")
js = 'document.documentElement.scrollTop=100000'
chrome.execute_script(js)
sleep(3)
html = chrome.page_source
e = etree.HTML(html)
titles = e.xpath('//div[@id="J_goodsList"]//div[@class="p-name p-name-type-2"]/a/em/text()')
# titles = e.xpath('//div[@id="J_goodsList"]//div[@class="p-name p-name-type-2"]/a/@title')

nums = e.xpath('//div[@id="J_goodsList"]//div[@class="p-price"]/strong/i/text()')

for title, num in zip(titles, nums):
    print(title, ':', num)
# print(len(nums), len(titles))
