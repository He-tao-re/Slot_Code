import Slot_common.Const as Const
import datetime
import Games.Game_1011_Clownfish.ClownfishSlot as Game_Slot

import Slot_common.DataRecod as Data_deal
import csv
import json


class TestCase(object):
    def __init__(self):
        self.all_bet = 0
        self.base_win = 0
        self.base_hit = 0
        self.base_sym_win = {}

        self.base_line_win = 0

        self.bubble_win = 0
        self.bubble_hit = 0
        self.base_new_bubble_num = 0
        self.base_new_bubble_kind_num = {1:0,2:0,3:0,4:0,5:0}

        self.free_win = 0
        self.free_hit = 0
        self.free_spin_times = 0
        self.free_extra_count = {}

        self.free_bubble_win = 0
        self.free_bubble_hit = 0


        self.super_free_win = 0
        self.super_free_hit = 0
        self.super_free_spin_times = 0
        self.super_free_extra_count = {}
        self.super_free_bubble_win = 0
        self.super_free_bubble_hit = 0

        self.self_data = {
            Const.R_Free_Collect: 0,
            Const.R_Bubble: []
            }


        self.base_bubble_pos_count = 0

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

            result,self.self_data = Game_Slot.GameSlot(self.self_data).paidspin(total_bet,times)

            if result[Const.R_Bubble_Win] > 0:
                self.bubble_win += result[Const.R_Bubble_Win]
                self.bubble_hit += 1

            if Const.R_Free in result.keys():
                free_end = max(result[Const.R_Free].keys())
                self.free_spin_times += free_end
                self.free_hit += 1
                self.free_win += result[Const.R_Free_Win_Amount]
                self.free_bubble_win += result[Const.R_Free_Bubble_Win_Amount]
                self.free_bubble_hit += result[Const.R_Free_Bubble_Hit]

            if Const.R_Super_Free in result.keys():
                free_end = max(result[Const.R_Super_Free].keys())
                self.super_free_spin_times += free_end
                self.super_free_hit += 1
                self.super_free_win += result[Const.R_Free_Win_Amount]
                self.super_free_bubble_win += result[Const.R_Free_Bubble_Win_Amount]
                self.super_free_bubble_hit += result[Const.R_Free_Bubble_Hit]

            for k,v in self.self_data[Const.R_New_Bubble_Kind_Num].items():
                self.base_new_bubble_kind_num[k] += v

            self.base_new_bubble_num += self.self_data[Const.R_New_Bubble_Num]
            self.base_win += result[Const.R_Win_Amount]
            self.base_line_win += result[Const.R_Line_WinAmount]

            self.base_bubble_pos_count += self.self_data["bubble_pos_num"]

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

        base_line_rtp = self.base_line_win / self.all_bet
        base_bubble_rtp = self.bubble_win / self.all_bet
        base_bubble_hit = self.bubble_hit / test_time
        base_average_bubble_pos = self.base_bubble_pos_count / test_time
        base_average_bubble_num = self.base_new_bubble_num / test_time
        free_rtp = self.free_win / self.all_bet
        free_interval = test_time / self.free_hit
        average_free_spins = self.free_spin_times / self.free_hit
        free_mul = free_interval * free_rtp
        free_bubble_rtp = self.free_bubble_win / self.all_bet
        free_bubble_hit = self.free_bubble_hit / self.free_spin_times

        super_free_rtp = self.super_free_win / self.all_bet
        super_free_interval = test_time / self.super_free_hit
        super_average_free_spins = self.super_free_spin_times / self.super_free_hit
        super_free_mul = super_free_interval * super_free_rtp
        super_free_bubble_rtp = self.super_free_bubble_win / self.all_bet
        super_free_bubble_hit = self.super_free_bubble_hit / self.super_free_spin_times


        total_rtp = base_rtp + free_rtp + super_free_rtp
        print('RTP：' + str(total_rtp))

        print('===========')
        print('Base RTP：' + str(base_rtp))

        print('Base Line RTP：' + str(base_line_rtp))
        print('Hit Rate：' + str(base_hit_rate))
        print('===========')
        print("Base Bubble RTP：" + str(base_bubble_rtp))
        print("Base Bubble Hit：" + str(base_bubble_hit))
        print("气泡平均格子数: " + str(base_average_bubble_pos))
        print('平均新增气泡数：' + str(base_average_bubble_num))
        print('Base下气泡生成个数')
        print(self.base_new_bubble_kind_num)
        print('===========')
        print('Free RTP：' + str(free_rtp))
        print('Free间隔：' + str(free_interval))
        print('Free倍数：' + str(free_mul))
        print('平均Free次数：' + str(average_free_spins))
        print("Free Bubble RTP：" + str(free_bubble_rtp))
        print("Free Bubble Hit：" + str(free_bubble_hit))

        print('===========')
        print('Super Free RTP：' + str(super_free_rtp))
        print('Super Free间隔：' + str(super_free_interval))
        print('Super Free倍数：' + str(super_free_mul))
        print('Super 平均Free次数：' + str(super_average_free_spins))
        print("Super Free Bubble RTP：" + str(super_free_bubble_rtp))
        print("Super Free Bubble Hit：" + str(super_free_bubble_hit))

        print('Spend Time：' + str(spend_time) + 's')



if __name__ == '__main__':
    TestCase().test(1000000, 500, recoder=False, sym_count=True, print_json=False)
