import Slot_common.Const as Const
import random
import os
import time
import datetime
from multiprocessing import Process


pool_1 = [0.5, 0.5, 0.5, 1, 1, 1]
pool_2 = [0.5, 0.5, 1, 1, 1.5, 1.5]
pool_3 = [1.5, 1.5, 3, 3, 5, 5]
pool_4 = [10, 10, 50]


class CashGame(object):
    def __init__(self):
        self.award_pool = {
            "pool_1": [0.5, 0.5, 0.5, 1, 1, 1],
            "pool_2": [0.5, 0.5, 1, 1, 1.5, 1.5],
            "pool_3": [1.5, 1.5, 3, 3, 5, 5],
            "pool_4": [10, 10, 50],
        }
        self.hit_pro = [
            [0.25],
            [0.12],
            [0.08],
            [0.05],
            [0.02],
            [0.02],
            [0.02],

        ]



    def get_prize(self, time):
        if time in [1, 2]:
            pool = self.award_pool['pool_1']
        elif time in [3, 4]:
            pool = self.award_pool['pool_2']
        elif time in [5, 6]:
            pool = self.award_pool['pool_3']
        elif time in [7]:
            pool = self.award_pool['pool_4']
        random.shuffle(pool)
        prize = [pool.pop(), pool.pop(), pool.pop()]

        return prize


    def game_start(self):
        game_time = 1
        continuous_hit = [0, 0, 0]
        prize_win = 0

        while game_time <= 7:
            prize = self.get_prize(game_time)

            for i in range(3):
                ra = random.random()
                if ra < self.hit_pro[continuous_hit[i]][0]:
                    if continuous_hit[i] == 1:
                        mul = 2
                    elif continuous_hit[i] == 2:
                        mul = 3
                    elif continuous_hit[i] == 3:
                        mul = 4
                    elif continuous_hit[i] == 4:
                        mul = 5
                    elif continuous_hit[i] == 5:
                        mul = 10
                    elif continuous_hit[i] == 6:
                        mul = 12
                    else:
                        mul = 1


                    prize_win += prize[i] * mul
                    continuous_hit[i] += 1
                else:
                    continuous_hit[i] = 0
            game_time += 1

        return prize_win

def test(run_times):
    times = 0
    total_win = 0
    while times < run_times:
        times += 1
        total_win += CashGame().game_start()

    average_win = total_win / run_times

    return average_win



if __name__ == "__main__":
    start_time = datetime.datetime.now()

    average_win = test(500000)
    end_time = datetime.datetime.now()
    spend_time = (end_time - start_time).seconds
    print("平均倍数：{mul}".format(mul=average_win))
    print("花费时间:{time}".format(time=spend_time))
