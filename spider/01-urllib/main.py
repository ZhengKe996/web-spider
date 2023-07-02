from urllib.request import urlopen

url = "https://baidu.com/"
response = urlopen(url)  # 发送请求

info = response.read()  # 读取内容

# print(info) # 打印内容
# print(info.decode()) # 打印内容(转码)

print(response.getcode())  # 返回http请求的状态码
print(response.geturl())  # 返回http请求的 实际url
print(response.info())  # 返回 HTTP的响应头
