import matplotlib
import os
import json
from typing import Dict, List
import matplotlib.pyplot as plt


def average_mmr(elos: Dict) -> int:
    s, d = 0, 0

    for j in elos['elo']:

        if j > 0:
            s += j
            d += 1
    return s/d


def read_data_to_xs_ys():
    matches = os.listdir(os.getcwd()+'\\data\\')
    ys = []
    xs = []

    for i in matches:
        try:
            f = open('data\\' + i)
            data = json.load(f)
            # return data['timeline'], data['elo']

            if data['timeline']:
                if data['elo']:
                    xs.append(data['timeline'])
                    ys.append(average_mmr(data))
        except:
            print(i, 'failed')

    return xs, ys



if __name__ == "__main__":

    # files = os.listdir(os.getcwd()+'\\data\\')
    # mmr = []
    # data_frame = []
    # for i in files:
    #     f = open('data\\' + i)
    #     data = json.load(f)
    #     mmr.append(average_mmr(data))
    #
    # plt.hist(mmr)
    # plt.show()
    print(read_data_to_xs_ys())



