import Slot_common.Const as Const
import datetime
import Games.Game_1021_WolfLink.WolfLinkSlot as Game_Slot
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

        self.super_free_win = 0
        self.super_free_hit = 0
        self.super_free_spin_times = 0

        self.respin_win = 0
        self.respin_hit = 0
        self.bonus_num = {
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
            13: 0,
            14: 0,
            15: 0
        }
        self.full_reel_count = {
            0: 0,
            1: 0,
            2: 0,
            3: 0
        }

        self.special_free_hit = 0
        self.special_free_hit_award = 0

        self.self_data = {Const.R_Collect_Data: 0,
                          Const.R_Jackpot_Hit: {
                              "Grand": 0,
                              "Major": 0,
                              "Minor": 0,
                              "Mini": 0,
                          }
                          }


    def test(self, test_time, total_bet, recoder, sym_count, print_json):
        start_time = datetime.datetime.now()
        times = 0
        data_recoder = Data_deal.create_csv('ChubbyBunny')

        if recoder is True:
            with open(data_recoder, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    ['次数', 'Bet', 'Base赢钱', 'Free', 'Free赢钱', 'FreeSpin次数', 'Feature', 'Feature赢钱', 'Feature Extra',
                     '收集玩法', '赢钱', '收集 Extra'])

        while times < test_time:
            times += 1
            '''进度打印'''
            if times % (test_time / 20) == 0:
                print(str(int(times / test_time * 100)) + ' %')
            self.all_bet += total_bet

            result = Game_Slot.GameSlot(self.self_data).paidspin(total_bet)
            self.self_data = result[Const.R_Self_Data]


            if Const.R_Free in result.keys():
                free_end = max(result[Const.R_Free].keys())
                self.free_spin_times += free_end
                self.free_hit += 1
                self.free_win += result[Const.R_Free_Win_Amount]


            if Const.R_Respin in result.keys():
                self.respin_hit += 1
                self.respin_win += result[Const.R_Respin_Win]

                reel_count = result[Const.R_Respin][Const.R_Reel_Count]

                for num in reel_count:
                    self.bonus_num[num] += 1

                full_num = reel_count.count(15)
                self.full_reel_count[full_num] += 1

            self.base_win += result[Const.R_Win_Amount]

            if result[Const.R_Win_Amount] > 0:
                self.base_hit += 1

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

            '''Spin记录写入CSV'''
            if recoder is True:
                with open(data_recoder, 'a+', newline='') as file:
                    writer = csv.writer(file)

                    if Const.R_Free in result.keys():
                        writer.writerow(
                            [times, total_bet, result[Const.R_Win_Amount], Const.R_Free, result[Const.R_Free_Win_Amount],
                             result[Const.R_Free_Spin_Total], '', '', ''])

                    elif Const.R_Collect_Game in result.keys():
                        writer.writerow(
                            [times, total_bet, result[Const.R_Win_Amount], '', '', '', '', '', '', Const.R_Collect_Game,
                             result[Const.R_Collect_Game_Win], ''])

                    else:
                        writer.writerow([times, total_bet, result[Const.R_Win_Amount]])

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
        #
        # super_free_rtp = self.super_free_win / self.all_bet
        # super_free_interval = test_time / self.super_free_hit
        # super_average_free_spins = self.super_free_spin_times / self.super_free_hit
        # super_free_mul = super_free_interval * super_free_rtp
        #
        #
        respin_rtp = self.respin_win / self.all_bet
        respin_interval = test_time / self.respin_hit
        respin_mul = respin_interval * respin_rtp

        all_num = 0
        for k,v in self.bonus_num.items():
            all_num += k * v
        average_num = all_num / self.respin_hit / 3

        # print("Total RTP：{rtp}".format(rtp=base_rtp+free_rtp+super_free_rtp+respin_rtp))
        print('===========')

        print('Base RTP：{rtp}'.format(rtp=base_rtp))
        print('Hit Rate：{hit_rate}'.format(hit_rate=base_hit_rate))


        # print('===========')
        # print('Free RTP：{rtp}'.format(rtp=free_rtp))
        # print('Free间隔：{interval}'.format(interval=free_interval))
        # print('Free倍数：{mul}'.format(mul=free_mul))
        # print('平均Free次数：{avg_fs}'.format(avg_fs=average_free_spins))
        #
        # print('===========')
        # print('Super Free RTP：{rtp}'.format(rtp=super_free_rtp))
        # print('Super Free间隔：{interval}'.format(interval=super_free_interval))
        # print('Super Free倍数：{mul}'.format(mul=super_free_mul))
        # print('平均Super Free次数：{avg_fs}'.format(avg_fs=super_average_free_spins))
        #
        # print('===========')
        print('Respin RTP：{rtp}'.format(rtp=respin_rtp))
        print('Respin 间隔：{interval}'.format(interval=respin_interval))
        print('Respin倍数：{mul}'.format(mul=respin_mul))
        print('满轮分布：{full_count}'.format(full_count=self.full_reel_count))
        print("平均每个Reel Bonus图标个数：{}".format(average_num))
        # print("Jackpot Hit：{hit}".format(hit=self.self_data[Const.R_Jackpot_Hit]))
        # for x in range(6,16):
        #     print("{x}: {num}".format(x=x,num=self.bonus_num[x]))

        print('Spend Time：{time} s'.format(time=spend_time))


if __name__ == '__main__':
    TestCase().test(1000000, 1000, recoder=False, sym_count=False, print_json=False)
