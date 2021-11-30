import random
import Games.Game_1015_ChinesePanda.ChinesePanda_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

import numpy as np

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)


class GameSlot(object):
    def __init__(self):
        self.self_data = {
        }

    def paidspin(self,totalbet):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel,bonus_reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).getdouble_reel()

        result[Const.R_Reel] = reel
        result[Const.R_Bonus_Reel] = bonus_reel


        sc_num = self.scatterwin(reel)
        bonus_prize = self.get_bonus_prize(bonus_reel)
        # self.self_data[Const.C_Bonus_Prize] = bonus_prize

        #Scatter Win
        if sc_num >= 2:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0

        bonus_num = np.sum(bonus_reel)


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        if bonus_num >= 6:
            respin_result, respin_win, jackpot_hit, bn_num = Respin(bonus_reel,bonus_prize).respin()
            result[Const.R_Respin] = respin_result
            result[Const.R_Respin_Win] = respin_win * totalbet
            result[Const.R_Jackpot_Hit] = jackpot_hit
            result[Const.R_Bonus_Num] = bn_num

        return result


    def scatterwin(self, reel):
        sc_num = 0
        for x in range(5):
            if Config.Scatter in reel[x]:
                sc_num += 1
        return sc_num


    def get_bonus_prize(self,bonus_reel):
        bonus_prize = {}
        for i in range(5):
            for j in range(3):
                idx = j * 5 + i
                if bonus_reel[i][j] == 1:
                    bonus_prize[idx] = Util.randdict(Config.Const.C_Bonus_Prize)
        return bonus_prize


class Respin(object):
    def __init__(self,bonus_reel,bonus_prize):
        self.bonus_reel = bonus_reel
        self.bonus_prize = bonus_prize

    def respin(self):
        respin_result = {}

        pos_pro,double_win_pos = self.allocate_pro()



        Const.C_Spin_Id = 0
        respin_time = 3

        while respin_time > 0:

            respin_time -= 1
            Const.C_Spin_Id += 1

            for x in range(5):
                for y in range(3):

                    if self.bonus_reel[x][y] == 0:

                        idx = y * 5 + x
                        rand_num = random.random()
                        if rand_num < pos_pro[idx]:
                            self.bonus_reel[x][y] = 1
                            self.bonus_prize[idx] = Util.randdict(Config.Const.C_Bonus_Prize)
                            respin_time = 3

            respin_result[Const.C_Spin_Id] = [copy.deepcopy(self.bonus_reel),copy.deepcopy(self.bonus_prize)]


        double_win_pos_hit = 0
        for idx in double_win_pos:
            x = idx % 5
            y = idx // 5
            if self.bonus_reel[x][y] == 1:
                double_win_pos_hit += 1

        respin_win = 0
        jackpot_hit = None
        if double_win_pos_hit == 3:
            for prize in self.bonus_prize.values():
                respin_win += prize * 2
            if np.sum(self.bonus_reel) == 13:
                respin_win += Config.Const.C_Jackpot_Set[Const.C_Minor]
                jackpot_hit = Const.C_Minor

            elif np.sum(self.bonus_reel) == 14:
                respin_win += Config.Const.C_Jackpot_Set[Const.C_Major]
                jackpot_hit = Const.C_Major

            elif np.sum(self.bonus_reel) == 15:
                respin_win += Config.Const.C_Jackpot_Set[Const.C_Grand]
                jackpot_hit = Const.C_Grand


        elif double_win_pos_hit < 3:
            for idx,prize in self.bonus_prize.items():
                if idx in double_win_pos:
                    respin_win += self.bonus_prize[idx] * 2
                else:
                    respin_win += self.bonus_prize[idx]

            if np.sum(self.bonus_reel) == 13:
                respin_win += Config.Const.C_Jackpot_Set[Const.C_Minor]
                jackpot_hit = Const.C_Minor

            elif np.sum(self.bonus_reel) == 14:
                respin_win += Config.Const.C_Jackpot_Set[Const.C_Major]
                jackpot_hit = Const.C_Major

            elif np.sum(self.bonus_reel) == 15:
                respin_win += Config.Const.C_Jackpot_Set[Const.C_Grand]
                jackpot_hit = Const.C_Grand
        bn_num = np.sum(self.bonus_reel)
        return respin_result, respin_win, jackpot_hit, bn_num

    def get_blank_pos(self):
        blank_pos = []
        for x in range(5):
            for y in range(3):
                if self.bonus_reel[x][y] == 0:
                    idx = y * 5 + x
                    blank_pos.append(idx)

        return blank_pos

    def allocate_pro(self):
        pos_pro = {}
        blank_pos = self.get_blank_pos()
        double_win_pos = random.sample(blank_pos, 3)
        random.shuffle(blank_pos)
        for i in range(len(blank_pos)):
            pos_pro[blank_pos[i]] = Config.Const.C_Blank_Pos_Pro[i]
        return pos_pro,double_win_pos






