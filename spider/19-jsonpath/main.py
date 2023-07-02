from jsonpath import JSONPath
import requests
import json

url = 'http://172.18.180.44:7001/api/get/list'

resp = requests.get(url)

ids =JSONPath("$.data[/(id)].id").parse(json.loads(resp.text))
names = JSONPath("$.data[/(id)].classname").parse(json.loads(resp.text))

for id, name in zip(ids, names):
    print(id, ":", name)
