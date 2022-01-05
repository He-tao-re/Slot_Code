
import random
import Games.Game_1031_Alien.Alien_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

import numpy as np

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)


def get_bonus_prize(reel):
    bonus_prize = {}
    for i in range(5):
        for j in range(3):
            idx = j * 5 + i
            if reel[i][j] == Config.Bonus:
                bonus_prize[idx] = Util.randdict(Config.Const.C_Bonus_Prize)
    return bonus_prize


def scatter_count(reel):
    sc_num = 0
    for x in range(5):
        if Config.Scatter in reel[x]:
            sc_num += 1
    return sc_num


class GameSlot(object):
    def __init__(self):
        self.self_data = {
        }

    def paidspin(self,totalbet):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel


        sc_num = scatter_count(reel)
        bonus_prize = get_bonus_prize(reel)
        # self.self_data[Const.C_Bonus_Prize] = bonus_prize


        #Scatter Win

        if sc_num >= 2:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0

        bonus_num = len(bonus_prize.keys())


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        if bonus_num >= 6:
            result[Const.R_Respin],respin_mul = RespinGame(bonus_prize).respin()
            result[Const.R_Respin_Win] = respin_mul * totalbet
        return result



class RespinGame(object):
    def __init__(self,bonus_prize):
        self.bonus_reel = {
            1: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            2: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            3: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            4: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        }
        for idx in bonus_prize.keys():
            x = idx % 5
            y = idx // 5
            self.bonus_reel[1][x][y] = bonus_prize[idx]

        self.bonus_pos_pro = {
            1: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            2: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            3: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            4: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        }

    def allocate_pro(self):
        pro_list = copy.deepcopy(Config.Const.C_Blank_Pos_Pro)

        for reel_idx in range(1, 5):
            pro_idx = 0
            for x in range(5):
                for y in range(3):
                    if self.bonus_reel[reel_idx][x][y] == 0:
                        self.bonus_pos_pro[reel_idx][x][y] = pro_list[reel_idx-1][pro_idx]
                        pro_idx += 1

    def count_blank(self):
        count_blank = [0,0,0,0]
        for i in range(4):
            for x in range(5):
                for y in range(3):
                    if self.bonus_reel[i+1][x][y] != 0:
                        count_blank[i] += 1
        return count_blank

    def balance_respin(self):
        respin_mul = 0
        count_blank = self.count_blank()
        if count_blank[0] == 15:
            respin_mul += np.sum(self.bonus_reel[1]) * 2
        else:
            respin_mul += np.sum(self.bonus_reel[1])

        if count_blank[1] == 15:
            respin_mul += np.sum(self.bonus_reel[2]) * 3
        else:
            respin_mul += np.sum(self.bonus_reel[2])

        if count_blank[2] == 15:
            respin_mul += np.sum(self.bonus_reel[3]) * 5
        else:
            respin_mul += np.sum(self.bonus_reel[3])

        if count_blank[3] == 15:
            respin_mul += np.sum(self.bonus_reel[4]) * 10
        else:
            respin_mul += np.sum(self.bonus_reel[4])

        return respin_mul

    def respin(self):
        self.allocate_pro()

        respin = {}

        respin_times = 3
        respin_recoder = 0
        while respin_times > 0:
            respin_times -= 1
            respin_recoder += 1

            count_blank = self.count_blank()

            if count_blank[0] < 15:

                for x in range(5):
                    for y in range(3):
                        if self.bonus_reel[1][x][y] == 0:
                            x_random = random.random()

                            if x_random < self.bonus_pos_pro[1][x][y]:
                                self.bonus_reel[1][x][y] = Util.randdict(Config.Const.C_Bonus_Prize)
                                respin_times = 3

            else:
                if count_blank[1] < 15:
                    for x in range(5):
                        for y in range(3):
                            if self.bonus_reel[2][x][y] == 0:
                                x_random = random.random()

                                if x_random < self.bonus_pos_pro[2][x][y]:
                                    self.bonus_reel[2][x][y] = Util.randdict(Config.Const.C_Bonus_Prize)
                                    respin_times = 3

                else:
                    if count_blank[2] < 15:
                        for x in range(5):
                            for y in range(3):
                                if self.bonus_reel[3][x][y] == 0:
                                    x_random = random.random()

                                    if x_random < self.bonus_pos_pro[3][x][y]:
                                        self.bonus_reel[3][x][y] = Util.randdict(Config.Const.C_Bonus_Prize)
                                        respin_times = 3
                    else:
                        if count_blank[3] < 15:
                            for x in range(5):
                                for y in range(3):
                                    if self.bonus_reel[4][x][y] == 0:
                                        x_random = random.random()

                                        if x_random < self.bonus_pos_pro[4][x][y]:
                                            self.bonus_reel[4][x][y] = Util.randdict(Config.Const.C_Bonus_Prize)
                                            respin_times = 3

            respin[respin_recoder] = {Const.R_Respin_Reel: copy.deepcopy(self.bonus_reel)}

        respin_mul = self.balance_respin()


        return respin,respin_mul
