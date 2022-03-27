import matplotlib
import os
import json
from typing import Dict, List
import matplotlib.pyplot as plt


def average_mmr(d: Dict) -> int:
    s = 0
    dem = 0

    for j in range(10):

        if d[str(j)]['elo'] and d[str(j)]['elo'] > 0:
            s += d[str(j)]['elo']
            dem += 1
    return s/dem


if __name__ == "__main__":

    files = os.listdir(os.getcwd()+'\\data\\')
    mmr = []
    for i in files:
        f = open('data\\' + i)
        data = json.load(f)
        mmr.append(average_mmr(data))

    plt.hist(mmr)
    plt.show()




