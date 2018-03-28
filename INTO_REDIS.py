import redis
f = open("all_movies_urls.txt")
r = redis.Redis(host="localhost",port=6379)
for i in f:
    r.sadd("douban",f.readline().strip())

f.close()
