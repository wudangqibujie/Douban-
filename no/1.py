import requests
import json
import logging
import time
import os
logging.basicConfig(level=logging.INFO)
f = open("move_result.txt","a")
def get_data(url1):
    r = requests.get(url1)
    return json.loads(r.text)
def taiwan():
    f = open("Taiwan_move_result.txt","w",encoding="utf-8")
    for i in range(28):
        url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1,%E5%8F%B0%E6%B9%BE&start={}".format(str(i*20))
        dic =get_data(url)
        f.write(str(dic)+"\n")
    f.close()
def hongkong():
    f = open("Hongkong_move_result.txt","w",encoding="utf-8")
    for i in range(235):
        try:
            url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1,%E9%A6%99%E6%B8%AF&start={}".format(str(i*20))
            logging.info(url)
            dic =get_data(url)
            f.write(str(dic)+"\n")
        except:
            break
    f.close()
def dalu():
    f = open("Dalu_move_result.txt","w",encoding="utf-8")
    for i in range(342):
        try:
            url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1,%E5%A4%A7%E9%99%86&start={}".format(str(i*20))
            logging.info(url)
            dic =get_data(url)
            print(dic)
            f.write(str(dic)+"\n")
        except:
            break
    f.close()
def create_urls():
    g = open("TAIWAI.txt","w")
    f = open("Taiwan_move_result.txt",encoding="utf-8")
    for i in f:
        b = eval(i.strip())
        # print(b)
        for j in eval(i)["data"]:
            print(j["url"])
            g.write(j["url"]+"\n")
    g.close()
if __name__ == '__main__':
    create_urls()



