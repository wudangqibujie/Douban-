import redis
rr = redis.Redis(host="localhost",port=6379)
f = open("shangsha.txt","a",encoding="utf-8")
while True:
    a = rr.spop("douban_raw_data").decode("utf-8")
    f.write(a+"\n")
    print("aaaaa")

f.close()
