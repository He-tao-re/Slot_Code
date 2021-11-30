import Slot_common.Const as Const
import datetime
import Games.Game_1014_Canda.CanadaSlot as Game_Slot
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
        self.free_extra_count = {}

        self.special_free_hit = 0
        self.special_free_hit_award = 0




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

            result = Game_Slot.GameSlot().paidspin(total_bet)


            if len(result[Const.R_Self_Data][Const.R_Free_Hit]) > 0:
                for hit in result[Const.R_Self_Data][Const.R_Free_Hit]:
                    self.special_free_hit += 1
                    self.special_free_hit_award += hit[Const.R_Hit_Win]


            if Const.R_Free in result.keys():
                free_end = max(result[Const.R_Free].keys())
                self.free_spin_times += free_end
                self.free_hit += 1
                self.free_win += result[Const.R_Free_Win_Amount]


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

        special_free_interval = test_time / self.special_free_hit
        average_hit_award = self.special_free_hit_award / self.special_free_hit / total_bet


        print('===========')

        print('Base RTP：' + str(base_rtp))
        print('Hit Rate：' + str(base_hit_rate))


        print("special free间隔: " + str(special_free_interval))
        print("平均free hit award：" + str(average_hit_award))
        # print('===========')
        # print('Free RTP：' + str(free_rtp))
        # print('Free间隔：' + str(free_interval))
        # print('Free倍数：' + str(free_mul))
        # print('平均Free次数：' + str(average_free_spins))

        print('Spend Time：' + str(spend_time) + 's')


if __name__ == '__main__':
    TestCase().test(1000000, 1000, recoder=False, sym_count=False, print_json=False)
