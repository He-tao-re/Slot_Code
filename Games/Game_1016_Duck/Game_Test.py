import Slot_common.Const as Const
import datetime
import Games.Game_1018_France.FranceSlot as Game_Slot
import Games.Game_1018_France.france_config_100 as Config
import Slot_common.DataRecod as Data_deal
import csv
import json


class TestCase(object):
    def __init__(self):
        self.all_bet = 0
        self.base_win = 0
        self.base_hit = 0
        self.base_sym_win = {}

        self.collect_win = 0
        self.collect_hit = 0

        self.free_win = 0
        self.free_hit = 0
        self.free_spin_times = 0
        self.free_extra_count = {}

        self.respin_win = 0
        self.respin_hit = 0

        self.super_respin_win = 0
        self.super_respin_hit = 0

        self.respin_collect = {'progress': 0,
                               'end': Config.Respin_collect}

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

            result = Game_Slot.GameSlot().paidspin(total_bet,self.respin_collect)
            self.respin_collect = result[Const.R_Self_Data][Const.R_Collect_Data]

            if Const.R_Free in result.keys():
                free_end = max(result[Const.R_Free].keys())
                self.free_spin_times += free_end
                self.free_hit += 1
                self.free_win += result[Const.R_Free_Win_Amount]

            if Const.R_Respin in result.keys():
                self.respin_hit += 1
                self.respin_win += result[Const.R_Respin_Win]

            if Const.R_Super_Respin in result.keys():
                self.super_respin_win += result[Const.R_Respin_Win]
                self.super_respin_hit += 1


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

        free_rtp = self.free_win / self.all_bet
        free_interval = test_time / self.free_hit
        average_free_spins = self.free_spin_times / self.free_hit
        free_mul = free_interval * free_rtp

        respin_rtp = self.respin_win / self.all_bet
        respin_interval = test_time / self.respin_hit
        respin_mul = respin_interval * respin_rtp


        super_respin_rtp = self.super_respin_win / self.all_bet
        super_respin_interval = test_time / self.super_respin_hit
        super_respin_mul = super_respin_interval * super_respin_rtp

        # collect_rtp = self.collect_win / self.all_bet
        # collect_interval = test_time / self.collect_hit

        # total_rtp = base_rtp + free_rtp
        # print('RTP：' + str(total_rtp))

        print('===========')

        print('Base RTP：' + str(base_rtp))
        print('Hit Rate：' + str(base_hit_rate))

        print('===========')
        print('Free RTP：' + str(free_rtp))
        print('Free间隔：' + str(free_interval))
        print('Free倍数：' + str(free_mul))
        print('平均Free次数：' + str(average_free_spins))

        print('===========')
        print('Respin RTP：' + str(respin_rtp))
        print('Respin 间隔：' + str(respin_interval))
        print('Respin倍数：' + str(respin_mul))

        print('===========')
        print('Super Respin RTP：' + str(super_respin_rtp))
        print('Super Respin 间隔：' + str(super_respin_interval))
        print('Super Respin倍数：' + str(super_respin_mul))

        print('Spend Time：' + str(spend_time) + 's')


if __name__ == '__main__':
    TestCase().test(100, 500, recoder=False, sym_count=False, print_json=True)
