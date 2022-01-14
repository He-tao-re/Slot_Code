import datetime
import multiprocessing
import os
import json
import copy

import Slot_common.Const as Const
import Games.Game_10035_Frog.Frog_Slot as Game_Slot
import Games.Game_10035_Frog.static_data_10035 as static_data


class TestCase(object):
    def __init__(self):

        self.self_data = {}

    def test(self, Test_Time, Total_bet, p_idx):
        times = 0
        while times < Test_Time:
            times += 1
            '''进度打印'''
            if times % (Test_Time / 20) == 0:
                if p_idx == 1:
                    print(str(int(times / Test_Time * 100)) + ' %')

            result = Game_Slot.GameSlot(self.self_data).paidspin(Total_bet)
            self.self_data = result[Const.R_Self_Data]
        file_name = str(p_idx)
        try:
            os.remove(file_name)
        except FileNotFoundError:
            pass
        with open(file_name,'w',newline="") as data_file:
            data_file.write(json.dumps(static_data.data))



def run(Test_Time, Total_bet, p_idx):
    TestCase().test(Test_Time, Total_bet, p_idx)


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    total_bet = 12000
    test_time = 500000

    p_1 = multiprocessing.Process(target=run,args=(test_time,total_bet,1,))


    p_1.start()


    p_1.join()


    data_list = []
    file_list = ['1']
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
            if isinstance(sub_data[k],int) or isinstance(sub_data[k],float):
                sum_data[k] += sub_data[k]
            elif isinstance(sub_data[k],dict):
                for k2 in sub_data[k].keys():
                    for i in range(len(sub_data[k][k2])):
                        sum_data[k][int(k2)][i] += sub_data[k][k2][i]




    total_bet = 12000
    print(f"Total RTP：{sum_data[Const.S_Win] / sum_data[Const.S_Bet]}")
    print('===========')

    print(f'Base RTP：{sum_data[Const.S_Base_Win] / sum_data[Const.S_Bet]}')
    print(f"Hit Rate：{sum_data[Const.S_Base_Hit] / sum_data[Const.S_Test_Time]}")
    print('===========')
    print("Base Sym Win ")
    for k,v in sum_data[Const.S_Base_Sym_Win].items():
        print(f"Sym:{k} \t {round(v[0] / sum_data[Const.S_Bet],4)} \t {round(v[1] / sum_data[Const.S_Bet],4)} \t {round(v[2] / sum_data[Const.S_Bet],4)} \t {round(v[3] / sum_data[Const.S_Bet],4)} \t {round(v[4] / sum_data[Const.S_Bet],4)}")
        pass
    print('===========')
    print(f"Free RTP：{sum_data[Const.S_Free_Win] / sum_data[Const.S_Bet]}")
    print(f"Free平均倍数：{sum_data[Const.S_Free_Win] / sum_data[Const.S_Free_Hit] / total_bet}")
    print(f"Free 间隔：{sum_data[Const.S_Test_Time] / sum_data[Const.S_Free_Hit]}")
    print(f"sc_avg-num：{sum_data['Sc_num_2'] / sum_data['Sc_num_1']}")
    print('===========')


    end_time = datetime.datetime.now()
    spend_time = (end_time - start_time).seconds
    print(f"Test_Time：{sum_data[Const.S_Test_Time]}")
    print('Spend Time：' + str(spend_time) + 's')
    print(f"开始时间：{start_time}")
