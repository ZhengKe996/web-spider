from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()

chrome.get('https://www.huya.com/g/lol')
while True:
    names = chrome.find_elements('class name', 'nick')
    counts = chrome.find_elements('class name', 'js-num')
    for name, count in zip(names, counts):
        print(name.text, ":", count.text)

    if chrome.find_element('class name', 'laypage_next') != -1:
        chrome.find_element('class name', 'laypage_next').click()
        sleep(3)
    else:
        break

chrome.quit()
