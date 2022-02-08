import Slot_common.Const as Const
import datetime
import Games.Game_10037_Mammoth.Mammoth_Slot as Game_Slot
import Games.Game_10037_Mammoth.static_data_10037 as static_data
import json
import copy
import os
import multiprocessing

class TestCase(object):
    def __init__(self):

        self.game_data = {
            Const.R_Collect_Data: {
                Const.R_Collect_Progress: 0,
            },
            Const.R_Collect_Progress: 0,
            Const.R_Free_Spin_Total: 0,
            Const.R_Free_Spin_Left: 0,

        }
        self.static_data = {
            Const.S_Bet: 0,
            Const.S_Win: 0,
            Const.S_Base_Win: 0,
            Const.S_Base_Hit: 0,
            Const.S_Base_Sym_Win: 0,

            Const.S_Extra_Win: 0,
            Const.S_Extra_Win_Hit: 0,

            Const.S_Feature_Win: 0,
            Const.S_Feature_Hit: 0,
            Const.S_Feature_Win_Time: 0,
            Const.S_Feature_Extra_Win: 0,
            Const.S_Feature_Extra_Hit: 0,

            Const.S_Free_Hit: 0,
            Const.S_Free_Win: 0,
            Const.S_Free_Extra_Win: 0,
            Const.S_Free_Extra_Hit: 0,
            Const.S_FreeSpin: 0,
            Const.S_Free_Feature_Win: 0,
            Const.S_Free_Feature_Hit: 0,
            Const.S_Free_Feature_Extra_Win: 0,
            Const.S_Free_Feature_Extra_Hit: 0,

            Const.S_Super_Free_Win: 0,
            Const.S_Super_Free_Hit: 0,
            Const.S_Super_Free_Extra_Win: 0,
            Const.S_Super_Free_Extra_Hit: 0,
            Const.S_Super_Free_Spin: 0,
            Const.S_Super_Free_Feature_Win: 0,
            Const.S_Super_Free_Feature_Hit: 0,
            Const.S_Super_Free_Feature_Extra_Win: 0,
            Const.S_Super_Free_Feature_Extra_Hit: 0,

        }

    def test(self, Test_Time, Total_bet, p_idx):
        times = 0
        while times < Test_Time:
            times += 1
            '''进度打印'''
            if times % (Test_Time / 20) == 0:
                if p_idx == 1:
                    print(str(int(times / Test_Time * 100)) + ' %')

            result = Game_Slot.GameSlot(self.game_data).paid_spin(Total_bet)
            self.game_data = result[Const.R_Game_Data]

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
    test_time = 200000

    p_1 = multiprocessing.Process(target=run,args=(test_time,total_bet,1,))
    p_2 = multiprocessing.Process(target=run,args=(test_time,total_bet,2,))
    p_3 = multiprocessing.Process(target=run,args=(test_time,total_bet,3,))
    p_4 = multiprocessing.Process(target=run,args=(test_time,total_bet,4,))
    p_5 = multiprocessing.Process(target=run,args=(test_time,total_bet,5,))

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
    data = copy.deepcopy(static_data.data)
    for k,v in data.items():
        for sub_data in data_list:
            if isinstance(sub_data[k],int) or isinstance(sub_data[k],float):
                data[k] += sub_data[k]
            elif isinstance(sub_data[k],dict):
                for k2 in sub_data[k].keys():
                    for i in range(len(sub_data[k][k2])):
                        data[k][int(k2)][i] += sub_data[k][k2][i]

    end_time = datetime.datetime.now()
    print(f"Total RTP：{data[Const.S_Win] / data[Const.S_Bet]}")
    print("==========================")
    print(f"Base RTP：{data[Const.S_Base_Win] / data[Const.S_Bet]}")
    print(f"Base Hit Rate：{data[Const.S_Base_Hit] / data[Const.S_Test_Time]}")
    print(f"Base Extra RTP：{data[Const.S_Extra_Win] / data[Const.S_Bet]}")
    print(f"Base Extra Hit：{data[Const.S_Extra_Win_Hit] / data[Const.S_Test_Time]}")

    print("==========================")
    print(f"Feature RTP：{data[Const.S_Feature_Win] / data[Const.S_Bet]}")
    print(f"Feature Hit Rate：{data[Const.S_Feature_Win_Time] / data[Const.S_Feature_Hit]}")
    print(f"Feature 倍数：{data[Const.S_Feature_Win] / total_bet / data[Const.S_Feature_Hit]}")
    print(f"Feature 间隔：{data[Const.S_Test_Time] / data[Const.S_Feature_Hit]}")
    print(f"Feature Extra RTP：{data[Const.S_Feature_Extra_Win] / data[Const.S_Bet]}")
    print(f"Feature Extra Hit：{data[Const.S_Feature_Extra_Hit] / data[Const.S_Feature_Hit]}")
    print(f"Feature Extra 间隔：{ data[Const.S_Feature_Hit] / data[Const.S_Feature_Extra_Hit]}")


    print("==========================")
    print(f"Free RTP：{data[Const.S_Free_Win] / data[Const.S_Bet]}")
    print(f"Free间隔：{data[Const.S_Test_Time] / data[Const.S_Free_Hit]}")
    print(f"Free倍数：{data[Const.S_Free_Win] / data[Const.S_Free_Hit] / total_bet}")
    print(f"Free平均次数：{data[Const.S_FreeSpin] / data[Const.S_Free_Hit]}")
    print(f"Free Extra RTP：{data[Const.S_Free_Extra_Win] / data[Const.S_Bet]}")
    print(f"Free Extra Hit：{data[Const.S_Free_Extra_Hit] / data[Const.S_FreeSpin]}")
    print("==========================")

    print(f"Free Feature RTP：{data[Const.S_Free_Feature_Win] / data[Const.S_Bet]}")
    print(f"Free Feature 倍数：{data[Const.S_Free_Feature_Win] / total_bet / data[Const.S_Free_Feature_Hit]}")
    print(f"Free Feature 间隔：{data[Const.S_FreeSpin] / data[Const.S_Free_Feature_Hit]}")
    print(f"Free Feature Extra RTP：{data[Const.S_Free_Feature_Extra_Win] / data[Const.S_Bet]}")
    print(f"Free Feature Extra Hit：{data[Const.S_Free_Feature_Extra_Hit] / data[Const.S_Free_Feature_Hit]}")
    print(f"Free Feature Extra 间隔：{ data[Const.S_Free_Feature_Hit] / data[Const.S_Free_Feature_Extra_Hit]}")

    print("==========================")
    print(f"Super Free RTP：{data[Const.S_Super_Free_Win] / data[Const.S_Bet]}")
    print(f"Super Free间隔：{data[Const.S_Test_Time] / data[Const.S_Super_Free_Hit]}")
    print(f"Super Free倍数：{data[Const.S_Super_Free_Win] / data[Const.S_Super_Free_Hit] / total_bet}")
    print(f"Super Free平均次数：{data[Const.S_Super_Free_Spin] / data[Const.S_Super_Free_Hit]}")
    print(f"Super Free Extra RTP：{data[Const.S_Super_Free_Extra_Win] / data[Const.S_Bet]}")
    print(f"Super Free Extra Hit：{data[Const.S_Super_Free_Extra_Hit] / data[Const.S_Super_Free_Spin]}")
    print("==========================")

    print(f"Super Free Feature RTP：{data[Const.S_Super_Free_Feature_Win] / data[Const.S_Bet]}")
    print(f"Super Free Feature 倍数：{data[Const.S_Super_Free_Feature_Win] / total_bet / data[Const.S_Super_Free_Feature_Hit]}")
    print(f"Super Free Feature 间隔：{data[Const.S_Super_Free_Spin] / data[Const.S_Super_Free_Feature_Hit]}")
    print(f"Super Free Feature Extra RTP：{data[Const.S_Super_Free_Feature_Extra_Win] / data[Const.S_Bet]}")
    print(f"Super Free Feature Extra Hit：{data[Const.S_Super_Free_Feature_Extra_Hit] / data[Const.S_Super_Free_Feature_Hit]}")
    print(f"Super Free Feature Extra 间隔：{ data[Const.S_Super_Free_Feature_Hit] / data[Const.S_Super_Free_Feature_Extra_Hit]}")






    print(f"Spend Time：{(end_time - start_time).seconds} s")

