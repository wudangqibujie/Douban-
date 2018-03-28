import requests
import json
url = "https://api.douban.com//v2/movie/subject/1499008"
r = requests.get(url)
a = json.loads(r.text)
for key,value in a.items():
    print(key)
    print(value)