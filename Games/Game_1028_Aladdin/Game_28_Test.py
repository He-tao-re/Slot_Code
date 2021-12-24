import Slot_common.Const as Const
import datetime
import Games.Game_1028_Aladdin.Aladdin_Slot as Game_Slot
import Games.Game_1028_Aladdin.static_data as static
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
        self.jackpot_count = {
            Const.C_Grand: 0,
            Const.C_Major: 0,
            Const.C_Minor: 0
        }
        self.bn_num = 0
        self.re_times = 0

        self.mark_pos_num = 0
        self.self_data = {
            Const.R_Spin_Process: 0,
            Const.R_Collect_Mark: [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
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


            self.base_win += result[Const.R_Win_Amount]


            if result[Const.R_Win_Amount] > 0:
                self.base_hit += 1

            if Const.R_Respin in result.keys():
                self.respin_hit += 1
                self.respin_win += result[Const.R_Respin_Win]

                self.bn_num += result[Const.R_Bonus_Num]
                self.re_times += max(result[Const.R_Respin].keys())
                if result[Const.R_Bonus_Num] == 20:
                    self.jackpot_count[Const.C_Grand] += 1
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

        print("Total RTP：{}".format((self.base_win+self.free_win+self.respin_win)/self.all_bet))
        print('===========')

        print('Base RTP：{rtp}'.format(rtp=self.base_win / self.all_bet))
        print('Hit Rate：{rate}'.format(rate=self.base_hit / test_time))
        print(f'Avg Mark Pos Num：{self.mark_pos_num / test_time * 10}')
        print('===========')
        print('Free RTP：{}'.format(self.free_win / self.all_bet))
        print('Free间隔：{}'.format(test_time/self.free_hit))
        print('Free倍数：{}'.format(self.free_win/total_bet/self.free_hit))
        print('平均Free次数：{}'.format(self.free_spin_times/self.free_hit))
        print(f'Free Feature间隔：{self.free_spin_times/static.free_feature_hit}')
        print(f'Free Feature平均倍数：{static.free_feature_win/static.free_feature_hit/total_bet}')
        print(f'Free Line Win倍数：{static.free_line_win / self.free_hit / total_bet}')
        print('===========')

        print("Respin RTP: {}".format(self.respin_win / self.all_bet))
        print("Respin倍数：{}".format(self.respin_win / self.respin_hit / total_bet))
        print("Respin间隔：{}".format(test_time / self.respin_hit))
        print("Bonus平均个数：{}".format(self.bn_num/self.respin_hit))
        print("Respin平均次数：{}".format(self.re_times/self.respin_hit))
        print(f"Grand触发次数：{self.jackpot_count[Const.C_Grand]}")

        print('===========')

        print('Spend Time：{}'.format((end_time - start_time).seconds))


if __name__ == '__main__':
    TestCase().test(5000000, 1000, recoder=False, sym_count=False, print_json=False)
