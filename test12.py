import redis
r = redis.Redis(host="localhost",port=6379)
f = open("CAPOL_urls.txt",encoding="utf-8")
for i in f:
    r.sadd("douban_urls",f.readline().strip())
# # print(r.spop("douban_urls"))

# import requests
# # url = "http://httpbin.org/ip"
# url = "https://api.douban.com/v2/movie/subject/1291818"
# proxies = {"https":"114.218.248.7:49913"}
# r = requests.get(url,proxies=proxies)
# print(r.text)
