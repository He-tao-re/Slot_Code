import numpy as np
import math
import random

def transSequnce(row, col, rowMax):
    return rowMax * col + row

def transRowCol(position, rowMax):
    row = position % rowMax
    col = position // rowMax
    return row, col

def transposeReels(reels):
    t_reels = [[None for j in range(len(reels))] for i in range(len(reels[0]))]
    for col, reel in enumerate(reels):
        for row, s in enumerate(reel):
            t_reels[row][col] = s
    return t_reels


def formatWeights(weights):
    formated = []
    total = 0
    for w in weights:
        total = total + w
        formated.append(total)
    return total, formated

class Weightable(object):
    def __init__(self, wheel, weights, fast=True):
        self.wheel = wheel
        self.totalWeight, self.weights = formatWeights(weights)
        self.weight_threshhold = 5000
        self.fast = fast
        if fast and self.totalWeight < self.weight_threshhold:
            self.data = []
            for idx, w in enumerate(weights):
                self.data.extend([(wheel[idx],idx) for i in range(w)])
    
    def pickWheelAndIndex(self):
        if self.fast and self.totalWeight < self.weight_threshhold:
            idx = random.randint(0, self.totalWeight - 1)
            return self.data[idx][0], self.data[idx][1]
        else:
            pos = len(self.wheel) - 1
            r = random.randint(0, self.totalWeight-1)
            for idx, weight in enumerate(self.weights):
                if r < weight:
                    pos = idx
                    break
            return self.wheel[pos], pos

    def pick(self):
        w, idx = self.pickWheelAndIndex()
        return w

    def pickIndex(self):
        w, idx = self.pickWheelAndIndex()
        return idx

def randlist(one_list):
    Total_Weight = 0
    for i in one_list:
        Total_Weight += i[1]
    ra = random.randint(0,Total_Weight - 1)
    curr_sum = 0

    kind = None
    for k in one_list:
        curr_sum = curr_sum + k[1]
        if ra<curr_sum:
            kind = k[0]
            break
    return kind

def randdict(onedict):
    Total_Weight=sum(onedict.values())
    ra=random.randint(0,Total_Weight-1)

    curr_sum=0
    keys=onedict.keys()
    kind = None
    for k in keys:
        curr_sum=curr_sum+onedict[k]
        if ra<curr_sum:
            kind = k
            break
    return kind  



