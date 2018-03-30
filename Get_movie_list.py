import requests
import json
import logging
import time
import os
import ProxyManerger
import urllib.parse
logging.basicConfig(level=logging.INFO)

domain = ["日本","韩国","大陆","台湾","香港","美国"]
domain2url = dict(zip(domain,[urllib.parse.quote(i) for i in domain]))
proxies = {"https":"117.57.90.39:30037"}

def req_movie_list(url1):
    r = requests.get(url1,proxies = proxies)
    return json.loads(r.text)

@ProxyManerger.create_ip
def get_test1(url,proxies=None):
    try:
        return requests.get(url,proxies=proxies,timeout = 10).status_code
    except:
        logging.info("连接无效")
        red.sadd("gude",url)
        return None

def get_resp(domain,domain_byte):
    f = open(domain+"_raw_data.txt","a",encoding="utf-8")
    page = 0
    while True:
        url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1,{domain}&start={page}".format(domain=domain_byte,page=str(page*20))
        logging.info(url)
        rw_dic = req_movie_list(url)
        logging.info(rw_dic)
        page += 1
        if rw_dic["data"]:
            f.write(str(rw_dic)+"\n")
        else:
            break
    f.close()

def urls_extract(damain):
    g = open(damain+"_movie_urls.txt","a",encoding="utf-8")
    f = open(domain+"_raw_data.txt",encoding="utf-8")
    for i in f:
        b = eval(i.strip())
        for j in eval(i)["data"]:
            print(j["url"])
            g.write(j["url"]+"\n")
    g.close()

def main():
    for key,value in domain2url.items():
        get_resp(key,value)
    for key in domain2url.keys():
        urls_extract(key)
if __name__ == '__main__':
    main()



