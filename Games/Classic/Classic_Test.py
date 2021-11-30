import Slot_common.Const as Const
import datetime
import Games.Classic.Classic_Slot as Game_Slot
import Slot_common.DataRecod as Data_deal
import csv
import json


class TestCase(object):
    def __init__(self):
        self.all_bet = 0
        self.base_win = 0
        self.base_hit = 0
        self.base_sym_win = {
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0,
            10:0,
            11:0,
            12:0,
            13:0,
            14:0,
            15:0,
            16:0,
            17:0,
            18:0,
            19:0,
            20:0,
            21:0,
            22:0,
            23:0,
            24:0,
            25:0,
            26:0,
            27:0,
            28:0,
            29:0,
            30:0,
            31:0,
            32:0,
            33:0,
            34:0,
            35:0,
            36:0,
            37:0,

        }
        self.afdaf = [
            [101, 101, 104],
            [101, 104, 101],
            [104, 101, 101],
            [101, 102, 104],
            [101, 104, 102],
            [102, 101, 104],
            [102, 104, 101],
            [104, 101, 102],
            [104, 102, 101],
            [101, 103, 104],
            [101, 104, 103],
            [103, 101, 104],
            [103, 104, 101],
            [104, 101, 103],
            [104, 103, 101],
            [102, 102, 104],
            [102, 104, 102],
            [104, 102, 102],
            [103, 102, 104],
            [103, 104, 102],
            [102, 103, 104],
            [102, 104, 103],
            [104, 103, 102],
            [104, 102, 103],
            [103, 103, 104],
            [103, 104, 103],
            [104, 103, 103],
            [104, 104, 101],
            [104, 101, 104],
            [101, 104, 104],
            [104, 104, 102],
            [104, 102, 104],
            [102, 104, 104],
            [104, 104, 103],
            [104, 103, 104],
            [103, 104, 104],
            [104, 104, 104],

        ]

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


            self.base_win += result[Const.R_Win_Amount]

            if result["combo"] in self.afdaf:
                idx = self.afdaf.index(result["combo"])
                self.base_sym_win[idx+1] += result[Const.R_Win_Amount]

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



        end_time = datetime.datetime.now()
        spend_time = (end_time - start_time).seconds

        base_rtp = self.base_win / self.all_bet
        base_hit_rate = self.base_hit / test_time


        print('===========')

        print('Base RTP：{rtp}'.format(rtp=base_rtp))
        print('Hit Rate：{rate}'.format(rate=base_hit_rate))

        for k,v in self.base_sym_win.items():
            print(self.afdaf[k-1],self.base_sym_win[k]/self.all_bet)
        print('Spend Time：' + str(spend_time) + 's')


if __name__ == '__main__':
    TestCase().test(1000000, 1000, recoder=False, sym_count=False, print_json=False)
