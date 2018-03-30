import redis
r = redis.Redis(host="localhost",port=6379)
f = open("shangsha.txt",encoding="utf-8")
data_list = f.readlines()
for i in data_list:
    r.sadd("filt_data",i.strip())
    print(i.strip())
