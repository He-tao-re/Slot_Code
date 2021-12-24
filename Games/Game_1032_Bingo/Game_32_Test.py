
import Slot_common.Const as Const
import datetime
import multiprocessing
import Games.Game_1032_Bingo.Bingo_Slot as Game_Slot
import Games.Game_1032_Bingo.static_data_1032 as static_data
import os
import Slot_common.DataRecod as Data_deal
import json
import copy



class TestCase(object):
    def __init__(self):

        self.self_data = {
            Const.R_Bingo_Data:{0: [],1: [],2: [],3: [],4: [],5: [],6: [],7: [],8: [],9: [],10: [],11: [],12: [Const.R_Wheel],13: [],14: [],15: [],16: [],17: [],18: [],19: [],20: [],21: [],22: [],23: [],24: []},
            Const.R_Bingo_Status: False
        }

    def test(self, test_time, p_idx):
        times = 0
        total_bet = 12000
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






def run(test_time,p_idx):
    TestCase().test(test_time,p_idx)


if __name__ == '__main__':

    start_time = datetime.datetime.now()
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
            sum_data[k] += sub_data[k]

    total_bet = 12000
    print("Total RTP：{}".format((sum_data['all_win']) / sum_data['all_bet']))
    print('===========')

    print('Base RTP：{}'.format(sum_data['base_win'] / sum_data['all_bet']))
    print('Hit Rate：{}'.format(sum_data['base_hit'] / sum_data['test_time']))
    print(f"平均Bonus数量：{sum_data['base_bonus_num'] / sum_data['test_time']}")
    print('===========')
    print('Free RTP：{}'.format((sum_data['free_win'] + sum_data['free_bingo_win']) / sum_data['all_bet']))
    print('Free间隔：{}'.format(sum_data['test_time'] / sum_data['free_hit']))
    print('Free倍数：{}'.format((sum_data['free_win'] + sum_data['free_bingo_win']) / sum_data['free_hit'] / total_bet))
    print('平均Free次数：{}'.format(sum_data['free_spin_times'] / sum_data['free_hit']))
    print("Free Bingo间隔：{}".format(sum_data['free_spin_times'] / sum_data['free_bingo_hit']))
    print("Free Bingo RTP：{}".format(sum_data['free_bingo_win'] / sum_data['all_bet']))
    print(f"Free平均Bingo触发次数：{sum_data['free_bingo_hit']/sum_data['free_hit']}")
    print('===========')
    print("Bingo RTP: {}".format(sum_data['bingo_win'] / sum_data['all_bet']))
    print("Bingo倍数：{}".format(sum_data['bingo_win'] / sum_data['bingo_hit'] / total_bet))
    print("Bingo间隔：{}".format(sum_data['test_time'] / sum_data['bingo_hit']))
    
    end_time = datetime.datetime.now()
    spend_time = (end_time - start_time).seconds
    print(f"Test_Time：{sum_data['test_time']}")
    print('Spend Time：' + str(spend_time) + 's')
