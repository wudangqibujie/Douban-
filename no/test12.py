import re
f = open("CAPOL.txt",encoding = "utf-8")
g = open("shangsha.txt","a",encoding="utf-8")
# print(f.read())
item = f.read().split("}{")
item[0] += "}"
item[-1] = "{"+item[-1]
new_item = ["{"+i+"}" for i in item[1:-2]]
for i in new_item:
    g.write(i+"\n")
