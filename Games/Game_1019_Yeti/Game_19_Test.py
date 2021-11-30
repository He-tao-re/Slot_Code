import Slot_common.Const as Const
import datetime
import Games.Game_1019_Yeti.YetiSlot as Game_Slot
import Slot_common.DataRecod as Data_deal
import csv
import json

class TestProcess(object):
    def __init__(self):
        super().__init__()
        self.sym_count = False
        self.print_json = False

        self.test_time = 10000000
        self.total_bet = 1200
        self.times = 0

        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()

        self.all_bet = 0
        self.base_win = 0
        self.base_hit = 0
        self.base_sym_win = {}

        self.collect_win = 0
        self.collect_hit = 0

        self.free_win = 0
        self.free_hit = 0
        self.free_spin_times = 0


    def run(self):

        self.start_time = datetime.datetime.now()

        while self.times < self.test_time:
            self.times += 1
            '''进度打印'''
            if self.times % (self.test_time / 20) == 0:
                print(str(int(self.times / self.test_time * 100)) + ' %')


            self.all_bet += self.total_bet

            result = Game_Slot.GameSlot().paidspin(self.total_bet)

            if Const.R_Free in result.keys():
                free_end = max(result[Const.R_Free].keys())
                self.free_spin_times += free_end
                self.free_hit += 1
                self.free_win += result[Const.R_Free_Win_Amount]


            self.base_win += result[Const.R_Win_Amount]

            if result[Const.R_Win_Amount] > 0:
                self.base_hit += 1

            if self.print_json is True:
                print(json.dumps(result))

            if self.sym_count is True:
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
                self.base_sym_win[k][i] = round(v[i] / self.all_bet, 6)
        self.end_time = datetime.datetime.now()

        spend_time = (self.end_time - self.start_time).seconds

        base_rtp = self.base_win / self.all_bet
        base_hit_rate = self.base_hit / self.test_time

        free_rtp = self.free_win / self.all_bet
        free_interval = self.test_time / self.free_hit
        average_free_spins = self.free_spin_times / self.free_hit
        free_mul = free_interval * free_rtp

        total_rtp = base_rtp + free_rtp
        print('RTP：' + str(total_rtp))

        print('===========')

        print('Base RTP：' + str(base_rtp))
        print('Hit Rate：' + str(base_hit_rate))

        print('===========')
        print('Free RTP：' + str(free_rtp))
        print('Free间隔：' + str(free_interval))
        print('Free倍数：' + str(free_mul))
        print('平均Free次数：' + str(average_free_spins))

        if self.sym_count is True:
            sym_list = self.base_sym_win.keys()
            for sym in sorted(self.base_sym_win.keys()):
                print(sym,self.base_sym_win[sym])
        print('Spend Time：' + str(spend_time) + 's')



s1 = TestProcess()

if __name__ == '__main__':
    s1.run()
