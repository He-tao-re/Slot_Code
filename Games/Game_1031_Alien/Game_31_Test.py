
import Slot_common.Const as Const
import datetime
import Games.Game_1031_Alien.Alien_Slot as Game_Slot
import Slot_common.DataRecod as Data_deal
import csv
import json


class TestCase(object):
    def __init__(self):
        self.all_bet = 0
        self.base_win = 0
        self.base_hit = 0
        self.base_sym_win = {}


        self.free_win = 0
        self.free_hit = 0
        self.free_spin_times = 0

        self.respin_hit = 0
        self.respin_win = 0

        self.bn_num = 0
        self.re_times = 0


    def test(self, test_time, total_bet):
        start_time = datetime.datetime.now()
        times = 0

        while times < test_time:
            times += 1
            '''进度打印'''
            if times % (test_time / 20) == 0:
                print(str(int(times / test_time * 100)) + ' %')
            self.all_bet += total_bet

            result = Game_Slot.GameSlot().paidspin(total_bet)


            if Const.R_Free in result.keys():
                free_end = max(result[Const.R_Free].keys())
                self.free_spin_times += free_end
                self.free_hit += 1
                self.free_win += result[Const.R_Free_Win_Amount]


            self.base_win += result[Const.R_Win_Amount]

            if result[Const.R_Win_Amount] > 0:
                self.base_hit += 1

            if Const.R_Respin in result.keys():
                self.respin_hit += 1
                self.respin_win += result[Const.R_Respin_Win]




        end_time = datetime.datetime.now()
        spend_time = (end_time - start_time).seconds


        print("Total RTP：{}".format((self.base_win + self.respin_win)/self.all_bet))
        print('===========')

        print('Base RTP：{}'.format(self.base_win / self.all_bet))
        print('Hit Rate：{}'.format(self.base_hit / test_time))


        # print('===========')
        # print('Free RTP：' + str(free_rtp))
        # print('Free间隔：' + str(free_interval))
        # print('Free倍数：' + str(free_mul))
        # print('平均Free次数：' + str(average_free_spins))


        print("Respin RTP: {}".format(self.respin_win / self.all_bet))
        print("Respin倍数：{}".format(self.respin_win / self.respin_hit / total_bet))
        print("Respin间隔：{}".format(test_time / self.respin_hit))
        print("Bonus平均个数：{}".format(self.bn_num/self.respin_hit))
        print("Respin平均次数：{}".format(self.re_times/self.respin_hit))
        print('Spend Time：' + str(spend_time) + 's')


if __name__ == '__main__':
    TestCase().test(1000000, 1000)
