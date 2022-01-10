import datetime
import multiprocessing
import os
import json
import copy

import Slot_common.Const as Const
import Games.Game_1024_Thor.Thor_Slot as Game_Slot
import Games.Game_1024_Thor.static_data_1024 as static_data




class TestCase(object):
    def __init__(self):
        self.all_bet = 0
        self.base_win = 0
        self.base_hit = 0
        self.base_sym_win = {}


        self.free_win = 0
        self.free_hit = 0
        self.free_spin_times = 0

        self.super_free_win = 0
        self.super_free_hit = 0
        self.super_free_spin_times = 0

        self.self_data = {
            Const.R_Free_Collect: 0,
            Const.R_Reel_Mark: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0}
        }


    def test(self, test_time, p_idx):
        times = 0
        while times < test_time:
            times += 1
            '''进度打印'''
            if times % (test_time / 20) == 0:
                if p_idx == 1:
                    print(str(int(times / test_time * 100)) + ' %')

            result,self.self_data = Game_Slot.GameSlot(self.self_data).paidspin(total_bet)

        file_name = str(p_idx)
        try:
            os.remove(file_name)
        except FileNotFoundError:
            pass
        with open(file_name,'w',newline="") as file:
            file.write(json.dumps(static_data.data))



def run(Test_Time, p_idx):
    TestCase().test(Test_Time, p_idx)


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    total_bet = 12000
    test_time = 500000

    p_1 = multiprocessing.Process(target=run,args=(test_time,1,))
    p_2 = multiprocessing.Process(target=run,args=(test_time,2,))
    p_3 = multiprocessing.Process(target=run,args=(test_time,3,))
    p_4 = multiprocessing.Process(target=run,args=(test_time,4,))
    p_5 = multiprocessing.Process(target=run,args=(test_time,5,))

    p_1.start()
    p_2.start()
    p_3.start()
    p_4.start()
    p_5.start()

    p_1.join()
    p_2.join()
    p_3.join()
    p_4.join()
    p_5.join()

    data_list = []
    file_list = ['1','2','3','4','5']
    for file in file_list:
        with open(file,'r') as f:
            contents = f.read()
            data_list.append(json.loads(contents))
        try:
            os.remove(file)
        except FileNotFoundError:
            pass
    sum_data = copy.deepcopy(static_data.data)
    for k,v in sum_data.items():
        for sub_data in data_list:
            try:
                sum_data[k] += sub_data[k]
            except TypeError:
                for x in sum_data[k].keys():
                    sum_data[k][x][0] += sub_data[k][str(x)][0]
                    sum_data[k][x][1] += sub_data[k][str(x)][1]

    total_bet = 12000
    print(f"Total RTP：{sum_data[Const.S_Win] / sum_data[Const.S_Bet]}")
    print('===========')

    print(f'Base RTP：{sum_data[Const.S_Base_Win] / sum_data[Const.S_Bet]}')
    print(f"Hit Rate：{sum_data[Const.S_Base_Hit] / sum_data[Const.S_Test_Time]}")

    print('===========')
    print(f"Free RTP：{sum_data[Const.S_Free_Win] / sum_data[Const.S_Bet]}")
    print(f"Free平均倍数：{sum_data[Const.S_Free_Win] / sum_data[Const.S_Free_Hit] / total_bet}")
    print(f"Free 间隔：{sum_data[Const.S_Test_Time] / sum_data[Const.S_Free_Hit]}")

    print('===========')
    print(f"Super Free RTP：{sum_data[Const.S_Super_Free_Win] / sum_data[Const.S_Bet]}")
    print(f"Free平均倍数：{sum_data[Const.S_Super_Free_Win] / sum_data[Const.S_Super_Free_Hit] / total_bet}")
    print(f"Super Free 间隔：{sum_data[Const.S_Test_Time] / sum_data[Const.S_Super_Free_Hit]}")

    print('===========Super Free分类')
    for k,v in sum_data[Const.S_Extra_Win].items():
        print(f"Shape ID：{k} \t 平均倍数：{round(v[0] / v[1] / total_bet,2)} \t 触发次数：{v[1]}")

    end_time = datetime.datetime.now()
    spend_time = (end_time - start_time).seconds
    print(f"Test_Time：{sum_data[Const.S_Test_Time]}")
    print('Spend Time：' + str(spend_time) + 's')
