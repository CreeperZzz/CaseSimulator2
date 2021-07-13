import bisect
import random

def getRateList(num: int) -> list:
    file = open('weapList.txt', 'r')
    return file.readline().split(',')[-num:]

def randItem():
    # random.random()
    rate = getRateList(3)
    weight = [('a', int(rate[0])), ('b', int(rate[1])), ('c', int(rate[2]))]
    # print(weight)
    # def weightRand(weight:"list"):
    r = random.uniform(0, sum(w for _, w in weight))

    range = []
    pre = 0
    for _, i in weight:
        pre += i
        range.append(pre)
    # print(range)
    result = bisect.bisect(range, r)
    # print(weight[result][0])
    return weight[result][0]
    # weightRand(weight);

