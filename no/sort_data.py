import heapq
f = open("shangsha.txt",encoding="utf-8")
def form_data():
    return [eval(i) for i in f.readlines()]


def sort_data(formed_data):
    data = heapq.nlargest(100,formed_data,key  = lambda s:s["评分"])
    return data


if __name__ == '__main__':
    form_data = form_data()
    formed_data = sort_data(form_data)
    for i in formed_data:
        print(i)

