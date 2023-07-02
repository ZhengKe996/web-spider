from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()

url = 'https://cn.bing.com'
chrome.get(url)  # 打开浏览器

chrome.find_element('id', 'sb_form_q').send_keys("我是帅哥")
chrome.find_element('id', 'search_icon').click()
sleep(3)

html = chrome.page_source
print(html)

chrome.quit()
