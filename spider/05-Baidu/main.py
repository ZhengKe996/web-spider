from urllib.request import urlopen, Request
from urllib.parse import urlencode


def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }

    request = Request(url, headers=headers)
    resp = urlopen(request)
    return resp.read().decode()


def saveHtml(html, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


def main():
    content = input("请输入要获取的贴吧名：")
    num = int(input("请输入获取多少页："))
    for i in range(num):
        # print(i)
        agrs = {
            "ie": "utf-8", "kw": content, "pn": i * 50
        }
        url = 'https://tieba.baidu.com/f?{}'.format(urlencode(agrs))
        html = getHtml(url)
        saveHtml(html, "第" + str(i + 1) + "页.html")


main()
