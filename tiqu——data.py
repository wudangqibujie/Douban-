import redis
import re
rr = redis.Redis(host="localhost",port=6379)
f = open("CAPOL_urls.txt","w",encoding="utf-8")
# obj = f.read()
# print(re.findall(r'}{(.*?)}{',obj))
# print(rr.spop("douban_urls").decode("utf-8"))
while True:
    f.write(rr.spop("douban_urls").decode("utf-8")+"\n")
    print("11")
