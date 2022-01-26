import multiprocessing
import datetime
import json
import copy
import os

import Games.Game_1028_Aladdin.Aladdin_Slot as Game_Slot
import Games.Game_1028_Aladdin.static_data_10028 as static_data
import Slot_common.Const as Const


class TestCase(object):
    def __init__(self):

        self.self_data = {
            Const.R_Spin_Process: 0,
            Const.R_Collect_Mark: [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
        }

    def test(self, Test_time, p_idx):
        times = 0
        Total_bet = 12000
        while times < Test_time:
            times += 1
            '''进度打印'''
            if times % (Test_time / 20) == 0:
                if p_idx == 1:
                    print(str(int(times / Test_time * 100)) + ' %')

            result = Game_Slot.GameSlot(self.self_data).paidspin(Total_bet)
            self.self_data = result[Const.R_Self_Data]
        file_name = str(p_idx)
        try:
            os.remove(file_name)
        except FileNotFoundError:
            pass
        with open(file_name, 'w', newline="") as f:
            f.write(json.dumps(static_data.data))


def run(Test_time, p_idx):
    TestCase().test(Test_time, p_idx)


if __name__ == '__main__':

    start_time = datetime.datetime.now()
    test_time = 1000000

    p_1 = multiprocessing.Process(target=run, args=(test_time, 1,))
    p_2 = multiprocessing.Process(target=run, args=(test_time, 2,))
    p_3 = multiprocessing.Process(target=run, args=(test_time, 3,))
    p_4 = multiprocessing.Process(target=run, args=(test_time, 4,))
    p_5 = multiprocessing.Process(target=run, args=(test_time, 5,))

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
    file_list = ['1', '2', '3', '4', '5']
    for file in file_list:
        with open(file, 'r') as f:
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
    print('=============================')
    print(f'Base RTP：{sum_data[Const.S_Base_Win] / sum_data[Const.S_Bet]}')
    print(f'Base Hit Rate：{sum_data[Const.S_Base_Hit] / sum_data[Const.S_Test_Time]}')
    print(f"Base 10 Mark 平均数量：{sum_data[Const.S_Count_Num_2] / sum_data[Const.S_Count_Num_5]}")
    print(f"Base 1-9 RTP：{sum_data[Const.S_Count_Num_4] / sum_data[Const.S_Bet]}")
    print(f"Base 10 RTP：{sum_data[Const.S_Count_Num_3] / sum_data[Const.S_Bet]}")
    print(f"Base 10 倍数：{sum_data[Const.S_Count_Num_3] / sum_data[Const.S_Count_Num_5] / total_bet}")

    print('=============================')
    print(f'Free RTP：{(sum_data[Const.S_Free_Win] - sum_data[Const.S_Free_Feature_Win]) / sum_data[Const.S_Bet]}')
    print(f'Free Hit Rate：{sum_data[Const.S_Free_Win_Hit] / sum_data[Const.S_FreeSpin_Times]}')
    print(f'Free触发间隔：{sum_data[Const.S_Test_Time] / sum_data[Const.S_Free_Hit]}')
    print(f'Free触发次数：{sum_data[Const.S_Free_Hit]}')
    print(f'Free平均倍数：{(sum_data[Const.S_Free_Win] - sum_data[Const.S_Free_Feature_Win]) / sum_data[Const.S_Free_Hit] / total_bet}')
    print(f"Free Feature RTP：{sum_data[Const.S_Free_Feature_Win] / sum_data[Const.S_Bet]}")
    print(f"Free Feature触发间隔：{sum_data[Const.S_FreeSpin_Times] / sum_data[Const.S_Free_Feature_Hit]}")
    print(f"Free Feature平均倍数：{sum_data[Const.S_Free_Feature_Win] / sum_data[Const.S_Free_Feature_Hit] / total_bet}")

    print('=============================')
    print(f'Respin RTP：{sum_data[Const.S_Feature_Win] / sum_data[Const.S_Bet]}')
    print(f'Respin触发间隔：{sum_data[Const.S_Test_Time] / sum_data[Const.S_Feature_Hit]}')
    print(f'Respin触发次数：{sum_data[Const.S_Feature_Hit]}')
    print(f'Respin平均倍数：{sum_data[Const.S_Feature_Win] / sum_data[Const.S_Feature_Hit] / total_bet}')
    print(f'Respin平均图标数量：{sum_data[Const.S_Count_Num_1] / sum_data[Const.S_Feature_Hit]}')




    end_time = datetime.datetime.now()
    spend_time = (end_time - start_time).seconds
    print(f"Test_Time：{sum_data[Const.S_Test_Time]}")
    print('Spend Time：' + str(spend_time) + 's')
