from selenium import webdriver

chrome = webdriver.Chrome()

url = 'https://bing.com'
chrome.get(url)  # 打开浏览器

# chrome.save_screenshot("bing.png")  # 截图
html = chrome.page_source

print(html)

chrome.quit()
