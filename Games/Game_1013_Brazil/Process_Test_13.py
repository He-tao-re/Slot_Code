import Slot_common.Const as Const
import datetime
import Games.Game_1013_Brazil.BrazilSlot as Game_Slot
import Slot_common.DataRecod as Data_deal
import csv
import json
import multiprocessing
import os
import time

test_time = 100000
total_bet = 500


sym_count = False
print_json = False


times = 0

all_bet = 0
base_win = 0
base_hit = 0
base_sym_win = {}

free_win = 0
free_hit = 0
free_spin_times = 0

super_free_win = 0
super_free_hit = 0
super_free_spin_times = 0

respin_win = 0
respin_hit = 0
bonus_num = {6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}

special_free_hit = 0
special_free_hit_award = 0

self_data = {
    Const.R_Collect_Data: 0,
    Const.R_Jackpot_Hit: {
      "Grand": 0,
      "Major": 0,
      "Minor": 0,
      "Mini": 0,
    }
}


def test():

    global sym_count
    global print_json

    global test_time
    global total_bet
    global times

    global all_bet
    global base_win
    global base_hit
    global base_sym_win
    global free_win
    global free_hit
    global free_spin_times

    global super_free_win
    global super_free_hit
    global super_free_spin_times
    global respin_win
    global respin_hit
    global bonus_num

    global special_free_hit
    global special_free_hit_award
    global self_data

    process_test_time = 100000

    while times < test_time:
        times += 1

        all_bet += total_bet

        result = Game_Slot.GameSlot(self_data).paidspin(total_bet)
        self_data = result[Const.R_Self_Data]


        if Const.R_Free in result.keys():
            free_end = max(result[Const.R_Free].keys())
            free_spin_times += free_end
            free_hit += 1
            free_win += result[Const.R_Free_Win_Amount]


        if Const.R_Super_Free in result.keys():
            free_end = max(result[Const.R_Super_Free].keys())
            super_free_spin_times += free_end
            super_free_hit += 1
            super_free_win += result[Const.R_Free_Win_Amount]


        if Const.R_Respin in result.keys():
            respin_hit += 1
            respin_win += result[Const.R_Respin_Win]
            bonus_num[result[Const.R_Bonus_Num]] += 1

        base_win += result[Const.R_Win_Amount]

        if result[Const.R_Win_Amount] > 0:
            base_hit += 1

        if print_json is True:
            print(json.dumps(result))

        if sym_count is True:
            lines = result[Const.R_Line]
            if len(lines) > 0:
                for line in lines:
                    kind = line[Const.R_Line_Kind]
                    long = line[Const.R_Line_Long]

                    if kind in base_sym_win.keys():
                        base_sym_win[kind][long - 1] += line[Const.R_Line_Win]
                    else:
                        base_sym_win[kind] = [0, 0, 0, 0, 0]



def get_statistics():
    for k, v in base_sym_win.items():
        for i in range(len(v)):
            base_sym_win[k][i] = v[i] / all_bet

    base_rtp = base_win / all_bet
    base_hit_rate = base_hit / test_time

    free_rtp = free_win / all_bet
    free_interval = test_time / free_hit
    average_free_spins = free_spin_times / free_hit
    free_mul = free_interval * free_rtp

    super_free_rtp = super_free_win / all_bet
    super_free_interval = test_time / super_free_hit
    super_average_free_spins = super_free_spin_times / super_free_hit
    super_free_mul = super_free_interval * super_free_rtp


    respin_rtp = respin_win / all_bet
    respin_interval = test_time / respin_hit
    respin_mul = respin_interval * respin_rtp


    print("Total RTP：{rtp}".format(rtp=base_rtp+free_rtp+super_free_rtp+respin_rtp))
    print('===========')

    print('Base RTP：{rtp}'.format(rtp=base_rtp))
    print('Hit Rate：{hit_rate}'.format(hit_rate=base_hit_rate))


    print('===========')
    print('Free RTP：{rtp}'.format(rtp=free_rtp))
    print('Free间隔：{interval}'.format(interval=free_interval))
    print('Free倍数：{mul}'.format(mul=free_mul))
    print('平均Free次数：{avg_fs}'.format(avg_fs=average_free_spins))

    print('===========')
    print('Super Free RTP：{rtp}'.format(rtp=super_free_rtp))
    print('Super Free间隔：{interval}'.format(interval=super_free_interval))
    print('Super Free倍数：{mul}'.format(mul=super_free_mul))
    print('平均Super Free次数：{avg_fs}'.format(avg_fs=super_average_free_spins))

    print('===========')
    print('Respin RTP：{rtp}'.format(rtp=respin_rtp))
    print('Respin 间隔：{interval}'.format(interval=respin_interval))
    print('Respin倍数：{mul}'.format(mul=respin_mul))
    print("Jackpot Hit：{hit}".format(hit=self_data[Const.R_Jackpot_Hit]))
    for x in range(6,16):
        print("{x}: {num}".format(x=x,num=bonus_num[x]))






if __name__ == '__main__':

    p = multiprocessing.Pool(3)
    res_l = []
    for i in range(10):
        res = p.apply(test, args=())
        print(res_l)
    get_statistics()


