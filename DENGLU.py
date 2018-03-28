import requests
data = {
"source": "movie",
"redir": "https://movie.douban.com/subject/1306081/",
"form_email": "18123642476",
"form_password": "Ljj281150",
"login": "登录"
}
s = requests.Session()
url = "https://accounts.douban.com/login?alias=1812364545&redir=https%3A%2F%2Fmovie.douban.com%2Fsubject%2F1306081%2F&source=movie&error=1008"
r = s.post(url,data=data)
r1 = s.get("https://movie.douban.com/subject/5913050/")
print(r1.text)
