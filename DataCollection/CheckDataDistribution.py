import matplotlib
import os
import json
from typing import Dict, List
import matplotlib.pyplot as plt


def average_mmr(d: Dict) -> int:
    for j in range(10):

        if d['elo']:
            return sum(d['elo'])/len(d['elo'])


if __name__ == "__main__":

    files = os.listdir(os.getcwd()+'\\data\\')
    mmr = []
    for i in files:
        f = open('data\\' + i)
        data = json.load(f)
        mmr.append(average_mmr(data))

    plt.hist(mmr)
    plt.show()




