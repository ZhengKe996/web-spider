from urllib.request import urlopen, Request
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

i = 0
base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=70%3A60&action=&start={}&limit=20'
while True:
    request = Request(base_url.format(i * 20), headers=headers)
    resp = urlopen(request)
    info = resp.read().decode()

    if info == '[]':
        break
    else:
        i += 1
        print(info)

    sleep(3)  # 休眠三秒
