import random
import Games.Game_1025_Medusa.Medusa_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

import Games.Game_1025_Medusa.game_stastic as stastic
import numpy as np

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)


class GameSlot(object):
    def __init__(self):
        self.self_data = {
        }

    def paidspin(self,totalbet):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel


        sc_num = self.scatterwin(reel)
        bonus_prize = self.get_bonus_prize(reel)
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
            respin_result, respin_win, jackpot_hit, bn_num = Respin(reel,bonus_prize).respin()
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


    def get_bonus_prize(self,reel):
        bonus_prize = {}
        for i in range(5):
            for j in range(3):
                idx = j * 5 + i
                if reel[i][j] == Config.Bonus:
                    bonus_prize[idx] = Util.randdict(Config.Const.C_Bonus_Prize)
        return bonus_prize


class Respin(object):
    def __init__(self,reel,bonus_prize):
        self.bonus_reel = reel
        self.bonus_prize = bonus_prize

    def respin(self):


        respin_result = {}

        pos_pro = self.allocate_pro()



        Const.C_Spin_Id = 0
        respin_time = 3
        respin_win_amount = 0
        jackpot_hit = None

        while respin_time > 0:

            blast = False

            respin_time -= 1
            Const.C_Spin_Id += 1

            blank_pos = {}
            for x in range(5):
                for y in range(3):

                    if self.bonus_reel[x][y] != Config.Bonus:
                        idx = y * 5 + x
                        blank_pos[idx] = [x,y]
                        blank_pos[idx] = [x,y]

            blast_pos = random.sample(blank_pos.keys(),1)
            for idx,pos in blank_pos.items():
                x = pos[0]
                y = pos[1]

                if idx not in blast_pos:
                    rand_num = random.random()
                    if rand_num < pos_pro[idx]:
                        self.bonus_reel[x][y] = Config.Bonus
                        self.bonus_prize[idx] = Util.randdict(Config.Const.C_Bonus_Prize)
                        respin_time = 3


                else:
                    rand_num = random.random()
                    if rand_num < pos_pro[idx]:
                        self.bonus_reel[x][y] = Config.Blast
                        self.bonus_prize[idx] = 0
                        blast = True
                        stastic.blast_num += 1

            if blast is True:
                blast_award = 0
                for prize in self.bonus_prize.values():
                    if prize not in Config.Const.C_Jackpot_Set.keys():
                        blast_award += prize
                    else:
                        blast += Config.Const.C_Jackpot_Set[prize]

                respin_win_amount += blast_award

            respin_result[Const.C_Spin_Id] = [copy.deepcopy(self.bonus_reel),copy.deepcopy(self.bonus_prize),copy.deepcopy(respin_win_amount)]

        bn_num = 0

        for prize in self.bonus_prize.values():
            if prize not in Config.Const.C_Jackpot_Set.keys():
                respin_win_amount += prize
            else:
                respin_win_amount += Config.Const.C_Jackpot_Set[prize]


        for idx,prize in self.bonus_prize.items():
            if prize != 0:
                bn_num += 1

        if bn_num == 15:
            respin_win_amount += Config.Const.C_Jackpot_Set[Const.C_Grand]
            jackpot_hit = Const.C_Grand

        return respin_result,respin_win_amount,jackpot_hit,bn_num

    def get_blank_pos(self):
        blank_pos = []
        for x in range(5):
            for y in range(3):
                if self.bonus_reel[x][y] != Config.Bonus:
                    idx = y * 5 + x
                    blank_pos.append(idx)

        return blank_pos

    def allocate_pro(self):
        pos_pro = {}
        blank_pos = self.get_blank_pos()
        random.shuffle(blank_pos)
        for i in range(len(blank_pos)):
            pos_pro[blank_pos[i]] = Config.Const.C_Blank_Pos_Pro[i]
        return pos_pro






