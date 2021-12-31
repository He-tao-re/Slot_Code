import Slot_common.Const as Const
import datetime
import Games.Game_1024_Thor.Thor_Slot as Game_Slot
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

        self.self_data = {
            Const.R_Free_Collect: 0,
            Const.R_Reel_Mark: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 1, 19: 0, 20: 0, 21: 0}
        }

        self.shape_list = [
            {1, 2, 9, 12, 19, 20},
            {0, 3, 9, 12, 18, 21},
            {1, 2, 5, 6, 7, 14, 15, 16, 19, 20},
            {5, 7, 14, 16},
            {0, 3, 6, 10, 11, 15, 18, 21},
            {1, 2, 4, 8, 10, 11, 13, 17, 19, 20},
            {9, 10, 11, 12},
            {0, 3, 5, 6, 7, 14, 15, 16, 18, 21},
            {4, 5, 6, 7, 8, 13, 14, 15, 16, 17},
            {0, 3, 6, 9, 12, 15, 18, 21},
            {1, 2, 4, 8, 13, 17, 19, 20},
            {5, 7, 10, 11, 14, 16},
            {0, 4, 9, 13, 18, 3, 8, 12, 17, 21},
            {0, 3, 10, 11, 18, 21},
            {1, 2, 10, 11, 19, 20},

        ]

        self.shape_win_count = {
            0: [0,0],
            1: [0,0],
            2: [0,0],
            3: [0,0],
            4: [0,0],
            5: [0,0],
            6: [0,0],
            7: [0,0],
            8: [0,0],
            9: [0,0],
            10: [0,0],
            11: [0,0],
            12: [0,0],
            13: [0,0],
            14: [0,0],
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

            result, self.self_data = Game_Slot.GameSlot(self.self_data).paidspin(total_bet)


            if Const.R_Free in result.keys():
                free_end = max(result[Const.R_Free].keys())
                self.free_spin_times += free_end
                self.free_hit += 1
                self.free_win += result[Const.R_Free_Win_Amount]

            if Const.R_Super_Free in result.keys():
                free_end = max(result[Const.R_Super_Free].keys())
                self.super_free_spin_times += free_end
                self.super_free_hit += 1
                self.super_free_win += result[Const.R_Free_Win_Amount]
                shape_idx = self.shape_list.index(result[Const.R_Feature_Shape])
                self.shape_win_count[shape_idx][0] += result[Const.R_Free_Win_Amount]
                self.shape_win_count[shape_idx][1] += 1




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



        print('Total RTP：{}'.format((self.base_win + self.free_win + self.super_free_win) / self.all_bet))
        print('===========')

        print('Base RTP：{rtp}'.format(rtp=self.base_win / self.all_bet))
        print('Hit Rate：{rate}'.format(rate=self.base_hit / test_time))


        print('===========')
        print('Free RTP：{}'.format(self.free_win / self.all_bet))
        print('Free间隔：{}'.format(test_time / self.free_hit))
        print('Free倍数：{}'.format(self.free_win / self.free_hit / total_bet))
        print('平均Free次数：{}'.format(self.free_spin_times / self.free_hit))

        print('===========')
        print('Super Free RTP：{}'.format(self.super_free_win / self.all_bet))
        print('Super Free间隔：{}'.format(test_time / self.super_free_hit))
        print('Super Free倍数：{}'.format(self.super_free_win / self.super_free_hit / total_bet))
        print('平均Free次数：{}'.format(self.super_free_spin_times / self.free_hit))

        print("==============")
        print('额外统计')
        for k,v in self.shape_win_count.items():
            print('Shape ID：{ID},倍数：{mul}'.format(ID=k,mul=v[0]/v[1]/total_bet))

        print('Spend Time：' + str(spend_time) + 's')



if __name__ == '__main__':
    TestCase().test(1000000, 1000, recoder=False, sym_count=False, print_json=False)
