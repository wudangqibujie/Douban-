import requests
import json
import logging
import redis
import random
logging.basicConfig(level=logging.INFO)
red = redis.Redis(host="localhost",port = 6379)
url = "http://www.mogumiao.com/proxy/free/listFreeIp"
def get_ip():
    r = requests.get(url)
    r_d = json.loads(r.text)
    ip_port = [i["ip"]+":"+i["port"] for i in r_d["msg"]]
    return ip_port

def create_ip(func):
    def wrapper(url):
        ip_port1 = random.choice(get_ip())
        ip_port2 = random.choice(get_ip())
        proxies = {"http":ip_port1,"https":ip_port2}
        logging.info("装饰器")
        logging.info(proxies)
        return func(url,proxies)
    return wrapper

def run1():
        k=0
        while True:
            u = red.spop("gude")
            print(u)
            code = get_test(u)
            print(code)
            if code is None:
                k += 1
                if k == 15:
                    red.sadd("gude",u)
                    break
                else:
                    continue



if __name__ == '__main__':
    pass
