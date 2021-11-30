import Slot_common.Const as Const
import datetime
import Games.Game_1008_Halloween.HalloweenSlot as Game_Slot

import Slot_common.DataRecod as Data_deal
import csv
import json


class TestCase(object):
    def __init__(self):
        self.all_bet = 0
        self.base_win = 0
        self.base_hit = 0
        self.base_bubble_extra_win = 0
        self.base_sym_win = {}
        self.base_bubble_bomb = 0

        self.new_bubble_num = 0
        self.bubble_num = 0
        self.bubble_active_pos = 0

        self.free_win = 0
        self.free_hit = 0
        self.free_spin_times = 0
        self.free_extra_count = {}

        self.self_data = {Const.R_Bubble: [],
                          }
        self.jackpot_hit = {
            "Grand": 0,
            "Major": 0,
            "Minor": 0,
            "Mini": 0
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

            result,self.self_data = Game_Slot.GameSlot(self.self_data).paidspin(total_bet)

            if Const.R_Free in result.keys():
                free_end = max(result[Const.R_Free].keys())
                self.free_spin_times += free_end
                self.free_hit += 1
                self.free_win += result[Const.R_Free_Win_Amount]


            self.base_win += result[Const.R_Win_Amount]
            self.base_bubble_extra_win += result[Const.R_Bubble_Extra_Win]

            self.bubble_num += self.self_data[Const.R_Bubble_Num]
            self.new_bubble_num += self.self_data[Const.R_New_Bubble_Num]
            self.bubble_active_pos += self.self_data[Const.R_Bubble_Active_Pos]

            if result[Const.R_Win_Amount] > 0:
                self.base_hit += 1

            if self.self_data[Const.R_Bubble_Bomb] is True:
                self.base_bubble_bomb += 1
            if len(self.self_data[Const.R_Jackpot_Hit]) > 0:
                for jackpot in self.self_data[Const.R_Jackpot_Hit]:
                    self.jackpot_hit[jackpot] += 1
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

        baseline_rtp = self.base_win / self.all_bet
        base_hit_rate = self.base_hit / test_time
        base_bubble_win_rtp = self.base_bubble_extra_win / self.all_bet
        bubble_bomb_interval = test_time / self.base_bubble_bomb
        average_new_bubble_num = self.new_bubble_num / test_time
        average_bubble_num = self.bubble_num / test_time
        average_active_pos = self.bubble_active_pos / test_time

        free_rtp = self.free_win / self.all_bet
        free_interval = test_time / self.free_hit
        average_free_spins = self.free_spin_times / self.free_hit
        free_mul = free_interval * free_rtp

        #
        # total_rtp = base_rtp + free_rtp
        # print('RTP：' + str(total_rtp))

        print('===========')
        print('Base RTP：'+str(baseline_rtp+base_bubble_win_rtp))
        print('Base Line RTP：' + str(baseline_rtp))
        print('气泡 RTP：' + str(base_bubble_win_rtp))
        print('Hit Rate：' + str(base_hit_rate))
        print('气泡爆炸间隔：' + str(bubble_bomb_interval))
        print('平均新增气泡数量：' + str(average_new_bubble_num))
        print('气泡平均数量：' + str(average_bubble_num))
        print('气泡平均有效格子数：' + str(average_active_pos))
        print("气泡个数：" + str(self.new_bubble_num))

        print('===========')
        print('Free RTP：' + str(free_rtp))
        print('Free间隔：' + str(free_interval))
        print('Free倍数：' + str(free_mul))
        print('平均Free次数：' + str(average_free_spins))
        print('===========')

        print("Jackpot")
        print(self.jackpot_hit)
        print('Spend Time：' + str(spend_time) + 's')


if __name__ == '__main__':
    TestCase().test(500000, 500, recoder=False, sym_count=False, print_json=False)
