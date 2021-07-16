import bisect
import random

"""
_FN = 0.07
_MW = 0.15
_FT = 0.38
_WW = 0.45
_BS = 1
"""

_FL_NAME = ['Factory New', 'Minimal Wear', 'Field-Test', 'Well-Worn', 'Battle Scared']
_FLOAT = [0.07, 0.15, 0.38, 0.45, 1]

_COLOR = [37, 36, 34, 35, 32, 31, 43]

# No use method
def getRateList(num: int) -> list:
    file = open('weapList.txt', 'r')
    return file.readline().split(',')[-num:]


def rand_qua(rate: list):

    # weight = [('0', rate[0]),
    #           ('1', rate[1]),
    #           ('2', rate[2]),
    #           ('3', rate[3]),
    #           ('4', rate[4]),
    #           ('5', rate[5]),
    #           ('6', rate[6])]

    r = random.uniform(0, sum(w for w in rate))

    range = []
    pre = 0
    for i in rate:
        pre += i
        range.append(pre)
    result = bisect.bisect(range, r)
    # print(weight[result][0])
    return result
    # weightRand(weight);


def rand_weap(weaplist: list) -> tuple:
    return random.choice(weaplist)


def rand_float(range: tuple = (0, 0.2)) -> float:
    return random.uniform(*range)


def get_float(fl: float) -> str:
    return _FL_NAME[bisect.bisect_left(_FLOAT, fl)]


def get_color(qua: int) -> int:
    return _COLOR[qua]