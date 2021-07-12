import bisect
import random


def randItem():
    # random.random()
    weight = [('a', 20), ('b', 100), ('c', 500)]

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