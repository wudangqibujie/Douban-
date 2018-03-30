import heapq
from collections import OrderedDict
from collections import defaultdict
import numpy as np
#每条电影信息都是字典形式，全部单条信息放在列表容器
def extract_data():
    f = open("Chinese_movie_list.txt",encoding="utf-8")
    return [eval(i.strip()) for i in f.readlines()]

def specil_data(data,n):
    score_rank = heapq.nlargest(n,data,lambda s:s["评分"])
    comment_num_rank = heapq.nlargest(n,data,lambda s:s["评论数"])
    short_comment_rank = heapq.nlargest(n,data,lambda s:s["短评人数"])
    score_num_rank = heapq.nlargest(n,data,lambda s:s["打分人数"])
    d = defaultdict(list)
    #d = defaultdict(set)
    #d["a].add(1)
    d["打分排名"].append(score_rank)
    d["评论人数排名"].append(comment_num_rank)
    d["短评人数排名"].append(short_comment_rank)
    d["评分人数排名"].append(score_num_rank)
    return d
#构造出一个单个变量的字典{电影名:变量},输入的初始数据为第一个函数返回值形式
def one2one(data):
    name_list = [i["电影名字"] for i in data]
    name2score = dict(zip(name_list,[i["评分"] for i in data]))
    name2com_num = dict(zip(name_list,[i["评论数"] for i in data]))
    name2vie_num = dict(zip(name_list,[i["看过的人"] for i in data]))
    name2shorcom_num = dict(zip(name_list,[i["短评人数"] for i in data]))
    name2sco_num = dict(zip(name_list,[i["打分人数"] for i in data]))
    return [name2score,name2com_num,name2vie_num,name2shorcom_num,name2sco_num]
#对上面简化过的键值对进行排序
def max_min_data(data):
    #为了排序对键值对作变化
    max_score = max(zip(data[0].values(),data[0].keys()))
    min_score = min(zip(data[0].values(),data[0].keys()))
    max_rank = [max(zip(i.values(),i.keys())) for i in data]
    min_rank = [min(zip(i.values(),i.keys())) for i in data]
    return max_rank,min_rank
#对各个变量进行排序
def sort_data(data):
    b = [sorted(zip(i.values(),i.keys()),reverse=True) for i in data]
    return np.array(b)



if __name__ == '__main__':
    data1 = extract_data()
    data2 = one2one(data1)
    sor = sort_data(data2)
    print(sor)
