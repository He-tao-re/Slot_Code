
import Slot_common.Const as Const
import datetime
import Games.Game_1032_Bingo.Bingo_Slot as Game_Slot
import Games.Game_1032_Bingo.static_data_1032 as static_data

import Slot_common.DataRecod as Data_deal
import csv
import json


from multiprocessing.pool import Pool
from multiprocessing import Manager
from multiprocessing import Process

class TestCase(object):
    def __init__(self):

        self.self_data = {
            Const.R_Bingo_Data:{0: [],1: [],2: [],3: [],4: [],5: [],6: [],7: [],8: [],9: [],10: [],11: [],12: [Const.R_Wheel],13: [],14: [],15: [],16: [],17: [],18: [],19: [],20: [],21: [],22: [],23: [],24: []},
            Const.R_Bingo_Status: False
        }

    def test(self, test_time, total_bet, progress_id):
        start_time = datetime.datetime.now()
        times = 0

        while times < test_time:
            times += 1
            '''进度打印'''
            if times % (test_time / 20) == 0:
                print(str(int(times / test_time * 100)) + ' %')
            static_data.all_bet[progress_id] += total_bet

            result,self.self_data = Game_Slot.GameSlot(self.self_data).paidspin(total_bet,progress_id)





        end_time = datetime.datetime.now()
        spend_time = (end_time - start_time).seconds


        # print("Total RTP：{}".format((static_data.base_win + static_data.bingo_win + static_data.free_win + static_data.free_bingo_win) / static_data.all_bet))
        # print('===========')
        #
        # print('Base RTP：{}'.format(static_data.base_win / static_data.all_bet))
        # print('Hit Rate：{}'.format(static_data.base_hit / static_data.test_time))
        #
        # print('===========')
        # print('Free RTP：{}'.format((static_data.free_win + static_data.free_bingo_win)/static_data.all_bet))
        # print('Free间隔：{}'.format(static_data.test_time / static_data.free_hit))
        # print('Free倍数：{}'.format((static_data.free_win + static_data.free_bingo_win) / static_data.free_hit / total_bet))
        # print('平均Free次数：{}'.format(static_data.free_spin_times / static_data.free_hit))
        # print("Free Bingo间隔：{}".format(static_data.free_spin_times / static_data.free_bingo_hit))
        # print("Free Bingo RTP：{}".format(static_data.free_bingo_win / static_data.all_bet))
        #
        # print('===========')
        # print("Bingo RTP: {}".format(static_data.bingo_win / static_data.all_bet))
        # print("Bingo倍数：{}".format(static_data.bingo_win / static_data.bingo_hit / total_bet))
        # print("Bingo间隔：{}".format(static_data.test_time / static_data.bingo_hit))
        print('Spend Time：' + str(spend_time) + 's')


if __name__ == '__main__':
    TestCase().test(100000, 1000, 0)
