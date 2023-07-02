# 正则表达式
import re

str = 'Hello world python3.11 everyday'

print("-----------match()-----------")
print(re.match("H", str).group())  # H
print(re.match("\w", str).group())  # H
print(re.match(".", str).group())  # H
print(re.match("\S", str).group())  # H
print("-----------search()-----------")
print(re.search("3.11", str).group())  # 3.11
print(re.search("world", str).group())  # world
print(re.search("w\w+", str).group())  # world
print(re.search("H(\w+)", str).group(0))  # Hello
print("-----------findall()-----------")
print(re.findall("l", str))  # ['l', 'l', 'l']
print(re.findall("3", str))  # ['3']
print(re.findall("p\w+", str))  # ['python3']
print(re.findall("p\S+", str))  # ['python3.11']
print(re.findall("p.+", str))  # ['python3.11 everyday']
print(re.findall("p.+\d", str))  # ['python3.11']
print("-----------sub()-----------")
print(re.sub("p.+\d", 'python3.13', str))  # Hello world python3.13 everyday
