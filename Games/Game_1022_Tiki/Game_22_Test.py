import Slot_common.Const as Const
import datetime
import Games.Game_1022_Tiki.TikiSlot as Game_Slot
import Games.Game_1022_Tiki.Tiki_Config as Config
import json
import multiprocessing
import time


class TestCase(object):
    def __init__(self, static_data):

        self.static_data = static_data

        self.wild_feature_count = {
        }
        self.Game_Data = {
           'State':[
                [0,0,False],
                [0,0,False],
                [0,0,False],
                [0,0,False],
                [0,0,False]
           ]
        }

        '''【收集状态，整列wild剩余次数，是否整列wild】'''

    def test(self, test_time, total_bet, process):
        start_time = datetime.datetime.now()
        times = 0


        while times < test_time:
            times += 1
            '''进度打印'''
            if times % (test_time / 20) == 0:
                print(process + "-" + str(int(times / test_time * 100)) + ' %')
            self.static_data[Const.S_Bet] += total_bet

            result, self.Game_Data = Game_Slot.GameSlot(self.Game_Data).paidspin(total_bet)

            self.static_data[Const.S_Base_Win] += result[Const.R_Win_Amount]

            if result[Const.R_Win_Amount] > 0:
                self.static_data[Const.S_Base_Hit] += 1

            if Const.R_Free in result.keys():
                free_end = max(result[Const.R_Free].keys())
                self.static_data[Const.S_FreeSpin] += free_end
                self.static_data[Const.S_Free_Hit] += 1
                self.static_data[Const.S_Free_Win] += result[Const.R_Free_Win_Amount]

            if Const.R_Collect_Game in result.keys():
                self.static_data[Const.S_Collect_Hit] += 1
                self.static_data[Const.S_Collect_Win] += result[Const.R_Collect_Game_Win]



            act_reel = result[Const.R_Reel]

            wild_reel = ""
            for i in range(5):
                if act_reel[i] == [Config.Long_Wild, Config.Long_Wild, Config.Long_Wild]:
                    wild_reel += str(i)
            if len(wild_reel) > 0:
                if wild_reel in self.wild_feature_count.keys():
                    self.wild_feature_count[wild_reel] += 1
                else:
                    self.wild_feature_count[wild_reel] = 1



            lines = result[Const.R_Line]
            if len(lines) > 0:
                for line in lines:
                    kind = line[Const.R_Line_Kind]
                    long = line[Const.R_Line_Long]

                    if kind in self.static_data[Const.S_Base_Sym_Win].keys():
                        self.static_data[Const.S_Base_Sym_Win][kind][long - 1] += line[Const.R_Line_Win]
                    else:
                        self.static_data[Const.S_Base_Sym_Win][kind] = [0, 0, 0, 0, 0]


        for k, v in self.static_data[Const.S_Base_Sym_Win].items():
            for i in range(len(v)):
                self.static_data[Const.S_Base_Sym_Win][k][i] = v[i] / self.static_data[Const.S_Bet]
        end_time = datetime.datetime.now()
        spend_time = (end_time - start_time).seconds
        print('Spend Time：' + str(spend_time) + 's')


        # print('RTP：{}'.format(self.base_win / self.all_bet + self.free_win / self.all_bet))
        #
        # print('===========')
        #
        # print('Base RTP：{}'.format(self.base_win / self.all_bet))
        # print('Hit Rate：{}'.format(self.base_hit / test_time))
        # print('===========')
        #
        # print('Free RTP：{}'.format(self.free_win / self.all_bet))
        # print('Free间隔：{}'.format(test_time / self.free_hit))
        # print('Free倍数：{}'.format(self.free_win/self.free_hit/total_bet))
        # print('平均Free次数：{}'.format(self.free_spin_times / self.free_hit))
        # print('Freespin次数：{}'.format(self.free_spin_times))
        #
        # # print(self.wild_feature_count)
        # print('Spend Time：' + str(spend_time) + 's')


def fun(process_spin, bet, process_id,static_data):
    TestCase(static_data).test(process_spin, bet, process_id)


static_data = {
    Const.S_Bet: 0,
    Const.S_Spin: 0,
    Const.S_Base_Win: 0,
    Const.S_Base_Hit: 0,
    Const.S_Base_Sym_Win: {},
    Const.S_Free_Hit: 0,
    Const.S_Feature_Win: 0,

}

if __name__ == "__main__":

    Test_Time = 1000000
    Process_Spin = 500000

    Bet = 1000

    pool = multiprocessing.Pool(processes=6)


    result = []

    data = []

    for i in range(int(Test_Time/Process_Spin)):
        process_id = f"{i}/{int(Test_Time/Process_Spin)}"


        result.append(pool.apply_async(fun, (Process_Spin,Bet,process_id,static_data)))
        # print(data)
    pool.close()
    pool.join()
