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
        self.all_win = 0
        self.base_win = 0
        self.base_hit = 0
        self.base_sym_win = {}

        self.free_win = 0
        self.free_hit = 0
        self.free_spin_times = 0

        self.respin_win = 0
        self.respin_hit = 0
        self.respin_times = 0
        self.respin_unlock_count = [0,0,0,0,0,0,0,0,0]

        self.super_respin_win = 0
        self.super_respin_hit = 0
        self.super_respin_times = 0
        self.super_respin_unlock_count = [0,0,0,0,0,0,0,0,0]

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
                self.all_win += result[Const.R_Free_Win_Amount]

            if Const.R_Respin in result.keys():

                self.respin_hit += 1
                self.respin_win += result[Const.R_Respin_Win]
                self.all_win += result[Const.R_Respin_Win]

                respin_end = max(result[Const.R_Respin].keys())
                self.respin_times += respin_end

                unlock_level = int(len(result[Const.R_Respin][respin_end]['Unlock_Pos']) / 5)
                self.respin_unlock_count[unlock_level] += 1

            if Const.R_Super_Respin in result.keys():
                self.super_respin_win += result[Const.R_Respin_Win]
                self.all_win += result[Const.R_Respin_Win]
                self.super_respin_hit += 1

                respin_end = max(result[Const.R_Super_Respin].keys())
                self.super_respin_times += respin_end

                unlock_level = int(len(result[Const.R_Super_Respin][respin_end]['Unlock_Pos']) / 5)
                self.super_respin_unlock_count[unlock_level] += 1

            self.base_win += result[Const.R_Win_Amount]
            self.all_win += result[Const.R_Win_Amount]

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

        for i in range(9):
            self.respin_unlock_count[i] = self.respin_unlock_count[i] / self.respin_hit
            self.super_respin_unlock_count[i] = self.super_respin_unlock_count[i] / self.super_respin_hit


        # print(self.base_sym_win)
        end_time = datetime.datetime.now()

        print('\n\n')
        print(f'Total RTP：{self.all_win / self.all_bet}')
        print('===========')
        print(f'Base RTP：{self.base_win / self.all_bet}')
        print(f'Hit Rate：{self.base_hit / test_time}')
        print('===========')
        print(f'Free RTP：{self.free_win / self.all_bet}')
        print(f'Free间隔：{test_time / self.free_hit}')
        print(f'Free倍数：{self.free_win / self.free_hit / total_bet}')
        print(f'平均Free次数：{self.free_spin_times / self.free_hit}')
        print('===========')
        print(f'Respin RTP：{self.respin_win / self.all_bet}')
        print(f'Respin 间隔：{test_time / self.respin_hit}')
        print(f'Respin倍数：{self.respin_win / self.respin_hit / total_bet}')
        print(f'平均respin次数：{self.respin_times / self.respin_hit}')
        print(f'解锁分布：{self.respin_unlock_count}')
        print('===========')
        print(f'Super Respin RTP：{self.super_respin_win / self.all_bet}')
        print(f'Super Respin 间隔：{test_time / self.super_respin_hit}')
        print(f'Super Respin倍数：{self.super_respin_win / self.super_respin_hit / total_bet}')
        print(f'平均respin次数：{self.super_respin_times / self.super_respin_hit}')
        print(f'解锁分布：{self.super_respin_unlock_count}')


        print(f'Spend Time：{(end_time - start_time).seconds} s')


if __name__ == '__main__':
    TestCase().test(5000000, 500, recoder=False, sym_count=True, print_json=False)
