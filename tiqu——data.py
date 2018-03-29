import redis
import re
rr = redis.Redis(host="localhost",port=6379)
f = open("CAPOL.txt",encoding="utf-8")
obj = f.read()
print(re.findall(r'}{(.*?)}{',obj))

