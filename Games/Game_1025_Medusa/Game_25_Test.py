import Slot_common.Const as Const
import datetime
import Games.Game_1025_Medusa.Medusa_Slot as Game_Slot
import json

import Games.Game_1025_Medusa.game_stastic as stastic


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
        self.jackpot_count = {
            Const.C_Grand: 0,
            Const.C_Major: 0,
            Const.C_Minor: 0
        }
        self.bn_num = 0
        self.re_times = 0


    def test(self, test_time, total_bet, sym_count, print_json):
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

                if result[Const.R_Jackpot_Hit] is not None:
                    self.jackpot_count[result[Const.R_Jackpot_Hit]] += 1
                self.bn_num += result[Const.R_Bonus_Num]
                self.re_times += max(result[Const.R_Respin].keys())

            if print_json is True:
                print(json.dumps(result))

            if sym_count is True:
                lines = result[Const.R_Line]
                if len(lines) > 0:
                    for line in lines:
                        kind = line[Const.R_Line_Kind]
                        long = line[Const.R_Line_Long]

                        if kind in self.base_sym_win.keys():
                            self.base_sym_win[kind][long - 1] += line[Const.R_Line_Win]
                        else:
                            self.base_sym_win[kind] = [0, 0, 0, 0, 0]


        for k, v in self.base_sym_win.items():
            for i in range(len(v)):
                self.base_sym_win[k][i] = v[i] / self.all_bet

        end_time = datetime.datetime.now()
        spend_time = (end_time - start_time).seconds

        base_rtp = self.base_win / self.all_bet
        base_hit_rate = self.base_hit / test_time

        # free_rtp = self.free_win / self.all_bet
        # free_interval = test_time / self.free_hit
        # average_free_spins = self.free_spin_times / self.free_hit
        # free_mul = free_interval * free_rtp

        respin_rtp = self.respin_win / self.all_bet
        respin_interval = test_time / self.respin_hit
        respin_mul = self.respin_win / self.respin_hit / total_bet
        print('===========')

        print('Base RTP：{rtp}'.format(rtp=base_rtp))
        print('Hit Rate：{rate}'.format(rate=base_hit_rate))


        # print("special free间隔: {interval}".format(interval=special_free_interval))
        # print("平均free hit award：{award}".format(award=average_hit_award))
        # print('===========')
        # print('Free RTP：' + str(free_rtp))
        # print('Free间隔：' + str(free_interval))
        # print('Free倍数：' + str(free_mul))
        # print('平均Free次数：' + str(average_free_spins))
        print("Respin RTP: {rtp}".format(rtp=respin_rtp))
        print("Respin倍数：{mul}".format(mul=respin_mul))
        print("Respin间隔：{interval}".format(interval=respin_interval))
        print("Bonus平均个数：{}".format(self.bn_num/self.respin_hit))
        print("Blast平均个数：{}".format(stastic.blast_num/self.respin_hit))

        print("Respin平均次数：{}".format(self.re_times/self.respin_hit))


        print('Jackpot Hit：{jackpot}'.format(jackpot=self.jackpot_count))
        print('Spend Time：' + str(spend_time) + 's')


if __name__ == '__main__':
    TestCase().test(5000000, 1000, sym_count=False, print_json=False)
