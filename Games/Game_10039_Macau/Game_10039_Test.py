import multiprocessing
import datetime
import json
import copy
import os

import Games.Game_10039_Macau.Macau_Slot as Game_Slot
import Games.Game_10039_Macau.static_data_10039 as static_data
import Slot_common.Const as Const


class TestCase(object):
    def __init__(self):

        self.game_data = {}

    def test(self, Test_time, p_idx):
        times = 0
        Total_bet = 12000
        while times < Test_time:
            times += 1
            '''进度打印'''
            if times % (Test_time / 20) == 0:
                if p_idx == 1:
                    print(str(int(times / Test_time * 100)) + ' %')

            result = Game_Slot.GameSlot(self.game_data).paidspin(Total_bet)

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
    test_time = 10000

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
    for k, v in sum_data.items():
        for sub_data in data_list:
            sum_data[k] += sub_data[k]

    total_bet = 12000
    print(f"Total RTP：{sum_data[Const.S_Win] / sum_data[Const.S_Bet]}")
    print('=============================')
    print(f'Base RTP：{sum_data[Const.S_Base_Win] / sum_data[Const.S_Bet]}')
    print(f'Base Hit Rate：{sum_data[Const.S_Base_Hit] / sum_data[Const.S_Test_Time]}')
    print('=============================')
    print(f'Free RTP：{sum_data[Const.S_Free_Win] / sum_data[Const.S_Bet]}')
    print(f'Free Hit Rate：{sum_data[Const.S_Free_Win_Hit] / sum_data[Const.S_FreeSpin]}')
    print(f'Free触发间隔：{sum_data[Const.S_Test_Time] / sum_data[Const.S_Free_Hit]}')
    print(f'Free触发次数：{sum_data[Const.S_Free_Hit]}')
    print(f'Free平均倍数：{sum_data[Const.S_Free_Win] / sum_data[Const.S_Free_Hit] / total_bet}')
    print('=============================')
    print(f'Respin RTP：{sum_data[Const.S_Feature_Win] / sum_data[Const.S_Bet]}')
    print(f'Respin触发间隔：{sum_data[Const.S_Test_Time] / sum_data[Const.S_Feature_Hit]}')
    print(f'Respin触发次数：{sum_data[Const.S_Feature_Hit]}')
    print(f'Respin平均倍数：{sum_data[Const.S_Feature_Win] / sum_data[Const.S_Feature_Hit] / total_bet}')
    print(f'Respin平均图标数量：{sum_data[Const.S_Feature_Sym_Count] / sum_data[Const.S_Feature_Hit]}')
    print(f'Respin平均次数：{sum_data[Const.S_Feature_Spin] / sum_data[Const.S_Feature_Hit]}')


    print(f"Bonus_2X平均数量：{sum_data['Bonus_2X']/sum_data[Const.S_Feature_Hit]}")
    print(f"Bonus_3X平均数量：{sum_data['Bonus_3X']/sum_data[Const.S_Feature_Hit]}")
    print(f"Bonus_5X平均数量：{sum_data['Bonus_5X']/sum_data[Const.S_Feature_Hit]}")

    print(f"Grand：{sum_data[Const.S_Grand]}")
    print(f"Major：{sum_data[Const.S_Major]}")
    print(f"Minor：{sum_data[Const.S_Minor]}")
    print(f"Mini：{sum_data[Const.S_Mini]}")

    print(f"Bonus图标数据统计")
    print(f"Bonus_2X平均倍数：{sum_data['Bonus_2X_Win'] / sum_data['Bonus_2X']}")
    print(f"Bonus_3X平均倍数：{sum_data['Bonus_3X_Win'] / sum_data['Bonus_3X']}")
    print(f"Bonus_5X平均倍数：{sum_data['Bonus_5X_Win'] / sum_data['Bonus_5X']}")

    print(f"Bonus_2X随机次数比：{sum_data['Bonus_2X_Times'] / sum_data['Bonus_2X']}")
    print(f"Bonus_3X随机次数比：{sum_data['Bonus_3X_Times'] / sum_data['Bonus_3X']}")
    print(f"Bonus_5X随机次数比：{sum_data['Bonus_5X_Times'] / sum_data['Bonus_5X']}")


    end_time = datetime.datetime.now()
    spend_time = (end_time - start_time).seconds
    print(f"Test_Time：{sum_data[Const.S_Test_Time]}")
    print('Spend Time：' + str(spend_time) + 's')
