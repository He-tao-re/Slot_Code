import Slot_common.Const as Const
import Slot_common.Slots as Slot
import util.Util as Util
import Games.EndlessFortune.Super_Free as Config
import Slot_common.LinesConfig as Lines
import random
import copy



ReelSet = Slot.DealReel().ReelStrip(Config.ReelSets)
class Test(object):
    def __init__(self, test_time):


        self.test_time = test_time
        self.free_win_amount = 0

    def test(self):
        total_bet = 500
        time = 0

        while time < self.test_time:
            time += 1
            '''进度打印'''
            if time % (self.test_time / 20) == 0:
                print(str(int(time / self.test_time * 100)) + ' %')

            free, free_win_amount = SuperFree().super_free(Config.free_spins,total_bet)
            self.free_win_amount += free_win_amount
        average_mul = self.free_win_amount / total_bet / self.test_time
        print('平均倍数:' + str(average_mul))



class SuperFree(object):
    def __init__(self):
        self.mystery_pos = []

    def super_free(self, free_spins, total_bet):
        free = {}
        free_recoder = 0
        free_win_amount = 0
        while free_spins > 0:
            free_spins -= 1
            free_recoder += 1
            result = {}
            idx = 0
            reel = Slot.GetReel(ReelSet[idx], [3, 5]).get_reel()

            for x in range(5):
                for y in range(3):
                    if reel[x][y] == Config.Mystery:
                        pos = [x, y]
                        if pos in self.mystery_pos:
                            pass
                        else:
                            self.mystery_pos.append(pos)


            change_sym = Util.randdict(Config.Mystery_Change)

            change_reel = copy.deepcopy(reel)

            for pos in self.mystery_pos:
                change_reel[pos[0]][pos[1]] = change_sym

            sc_num = 0
            for x in range(5):
                for y in range(3):
                    if change_reel[x][y] == Config.Scatter:
                        sc_num += 1


            result.update(
                Slot.StandardLineEvaluator(Config, total_bet, Config.Const.C_PayLine,change_reel).evaluate())

            if sc_num >= 3:
                free_spins += Config.free_spins
                result[Const.R_Scatter_Win] = total_bet * Config.SC_Award[sc_num]
                result[Const.R_Win_Amount] += total_bet * Config.SC_Award[sc_num]

            free_win_amount += result[Const.R_Win_Amount]
            result[Const.R_Free_Win_Amount] = copy.deepcopy(result[Const.R_Win_Amount])


            free[free_recoder] = result
        return free, free_win_amount


if  __name__ == "__main__":
    Test(100000).test()
