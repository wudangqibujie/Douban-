import requests
import json
import re
import time
import heapq
import logging
import redis
import UA_Pool
import random
red = redis.Redis(host="localhost",port=6379)
logging.basicConfig(level=logging.INFO)
f = open("grapth_data.txt","a",encoding="utf-8")
def create_one_movie_id(str_obj):
    a = re.findall(r'ject/(.*?)/',str_obj)
    return a[0]

def movie_id_generator(path):
    f = open(path)
    qw = map(create_one_movie_id,f.readlines())
    return qw

def structual_data(movie_id,headers,proxies):
    data = dict()
    url = "https://api.douban.com/v2/movie/subject/{id}".format(id=movie_id)
    r = requests.get(url,headers = headers,proxies=proxies,timeout = 5)
    a = json.loads(r.text)
    data["评分"] = a["rating"]["average"]
    data["评论数"] = a["reviews_count"]
    data["电影名字"] = a["title"]
    data["看过的人"] = a["collect_count"]
    data["主演"] = [[i["name"],i["id"]] for i in a["casts"]]
    data["导演"] = [[i["name"],i["id"]] for i in a["directors"]]
    data["短评人数"] = a["comments_count"]
    data["打分人数"] = a["ratings_count"]
    data["英文名"] = a["aka"]
    return data
#产生一个二维数组
def create_sort_data():
    befor_sort = []
    k=0
    for i in movie_id_generator("TAIWAI.txt"):

        k += 1
        data = structual_data(i)
        befor_sort.append(data)
        if k ==2:
            break
    logging.info(befor_sort)
    print(befor_sort)
    return befor_sort
#对上面产生的二维数组进行排序
def sort_data():
    after_max = heapq.nsmallest(3,create_sort_data,key=lambda s:s["评分"])
    print(after_max)
def get_tempory_ip():
    r = requests.get("http://www.mogumiao.com/proxy/free/listFreeIp")
    dic = eval(r.text)
    ip_list = [i["ip"]+":"+i["port"] for i in dic["msg"]]
    return ip_list
if __name__ == '__main__':
    get_tempory_ip()
    k = 0
    ip_list = get_tempory_ip()
    ip = random.choice(ip_list)
    while True:
        url = red.spop("douban_urls").decode("utf-8")
        try:
            proxies = {"https":ip}
            logging.info(proxies)
            headers = {"User-Agent":random.choice(UA_Pool.user_agent_list)}
            # time.sleep(0.5)
            id = create_one_movie_id(url)
            data = structual_data(id,headers,proxies)
            logging.info(data)
            red.sadd("douban_raw_data",str(data))
        except:
            k += 1
            ip = random.choice(ip_list)
            logging.info("屌你老母又封我IP！")
            red.sadd("douban_urls",url)
            if k == 5:
                time.sleep(10)
                ip_list = get_tempory_ip()
                continue
            else:

                continue





