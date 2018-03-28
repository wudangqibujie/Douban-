import requests
import json
url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E5%A4%A7%E9%99%86&start=20"
r = requests.get(url)
a = json.loads(r.text)
print(type(a))