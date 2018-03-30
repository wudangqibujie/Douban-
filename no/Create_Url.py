import re
g = open("all_movies_urls.txt","a",encoding="utf-8")
f = open("TAIWAI.txt",encoding="utf-8")
for i in f:
    g.write(f.readline())

f.close()
g.close()
