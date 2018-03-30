import requests
from lxml import etree
import time
data = {
"source": "movie",
"redir": "https://movie.douban.com/subject/1306081/",
"form_email": "18123642476",
"form_password": "Ljj281150",
"login": "登录"
}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
           "Refer":"https://movie.douban.com/subject/1306081/"}
proxies = {"http":"27.154.147.58:27153"}
s = requests.Session()
# url = "https://accounts.douban.com/login?alias=1812364545&redir=https%3A%2F%2Fmovie.douban.com%2Fsubject%2F1306081%2F&source=movie&error=1008"
# r1 = s.post(url,data=data,headers = headers)
data=dict()
g = open("all_movies_urls.txt",encoding="utf-8")
f = open("DATA.txt","a",encoding="utf-8")
j = 0
for i in g:
    j += 1
    time.sleep(1)
    print(requests.get("http://httpbin.org/ip",proxies=proxies).text)
    r = s.get(i.strip(),proxies=proxies,headers=headers)
    print(r.text)
    html = etree.HTML(r.text)
    name = html.xpath('//div[@id="content"]/h1/span[1]/text()')
    data["电影名字"] = name
    director = html.xpath('//div[@id="info"]/span[1]/span[2]/a/text()')
    data["导演"] = director
    actor_item = html.xpath('//span[@class="attrs"]/a')
    actors = [i.xpath('text()') for i in actor_item]
    data["演员"] = actors
    score = html.xpath('/strong[@class="ll rating_num"]/text()')
    data["分数"] = score
    content_num = html.xpath('//a[@class="rating_people"]/span/text()')
    data["评论人数"] = content_num
    spare = html.xpath('//div[@class="ratings-on-weight"]/div')
    rating_weight = [[i.xpath('span[1]/text()')[0].strip(),i.xpath('span[2]/text()')] for i in spare]
    data["评论分布"] = rating_weight
    print(data)
    f.write(str(data)+"\n")
    if j ==2:
        break

f.close()
g.close()