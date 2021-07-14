import bisect
import random


# No use method
def getRateList(num: int) -> list:
    file = open('weapList.txt', 'r')
    return file.readline().split(',')[-num:]


def rand_qua(rate: list):
    # random.random()
    # rate = getRateList(3)
    # print(rate)
    weight = [('0', rate[0]),
              ('1', rate[1]),
              ('2', rate[2]),
              ('3', rate[3]),
              ('4', rate[4]),
              ('5', rate[5]),
              ('6', rate[6])]
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


def rand_weap(weaplist: list) -> 'tuple':
    return random.choice(weaplist)


# def rand_