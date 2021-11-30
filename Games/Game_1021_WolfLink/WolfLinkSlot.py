import random
import Games.Game_1021_WolfLink.WolfLinkConfig as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy
import numpy as np
import json


Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)
Super_Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)

class GameSlot(object):
    def __init__(self, self_data):
        self.self_data = self_data

    def paidspin(self,totalbet):

        result = {}
        self.self_data[Const.C_Bonus_Prize] = {}
        idx = Util.randdict(Config.Base_Reel_Chose)
        reel = Slot.GetReel(Base_ReelSets[idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel

        result[Const.R_Feature] = self.special_sym_count(reel)


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())

        if self.self_data[Const.R_Bonus_Num] >= 5:
            result[Const.R_Respin] = Respin(totalbet).respin_game(reel,self.self_data[Const.C_Bonus_Prize])
            result[Const.R_Respin_Win] = result[Const.R_Respin][Const.R_Respin_Win]

        if self.self_data[Const.R_Scatter_Num] >= 3:
            result[Const.R_Scatter_Win] = totalbet * Config.Const.C_Paytable[Config.Scatter][self.self_data[Const.R_Scatter_Num] - 1]
            result[Const.R_Win_Amount] += result[Const.R_Scatter_Win]

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result




    def special_sym_count(self,reel):
        sc_num = 0
        sc_pos = []

        bonus_num = 0
        bonus_pos = {}

        feature_get = []

        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.Scatter:
                    sc_num += 1
                    idx = x + 5 * y
                    sc_pos.append(idx)

                elif reel[x][y] == Config.Bonus:
                    bonus_num += 1
                    idx = x + 5 * y
                    bonus_award = Util.randdict(Config.Prize_on_Bonus)
                    bonus_pos[idx] = bonus_award

        if sc_num >= 3:
            feature_get.append(Const.C_FreeGame)

        if bonus_num >= 5:
            feature_get.append(Const.C_Respin)

        self.self_data = {Const.R_Scatter_Num: sc_num,
                          Const.R_Scatter_Pos: sc_pos,
                          Const.R_Bonus_Num: bonus_num,
                          Const.C_Bonus_Prize: bonus_pos}

        return feature_get




class Respin(object):
    def __init__(self,total_bet):
        self.feature_reel = {}
        self.total_bet = total_bet


    def get_trigger_reel(self,reel,bonus_award):
        respin_reel = {
            1: {Const.R_Respin_Reel: copy.deepcopy(reel), Const.R_Bonus_Award: bonus_award, Const.C_Blank_Pos_Pro: {}},
            2: {Const.R_Respin_Reel: copy.deepcopy(reel), Const.R_Bonus_Award: bonus_award, Const.C_Blank_Pos_Pro: {}},
            3: {Const.R_Respin_Reel: copy.deepcopy(reel), Const.R_Bonus_Award: bonus_award, Const.C_Blank_Pos_Pro: {}},
        }
        _map = [1,2,3]
        random.shuffle(_map)
        pro_idx = 0
        for x in range(5):
            for y in range(3):
                if reel[x][y] != Config.Bonus:
                    idx = y * 5 + x

                    respin_reel[_map[0]][Const.C_Blank_Pos_Pro][idx] = Config.Respin_Pro[0][pro_idx]
                    respin_reel[_map[1]][Const.C_Blank_Pos_Pro][idx] = Config.Respin_Pro[1][pro_idx]
                    respin_reel[_map[2]][Const.C_Blank_Pos_Pro][idx] = Config.Respin_Pro[2][pro_idx]

                    pro_idx += 1

        return respin_reel


    def respin_game(self,bonus_reel,bonus_award):
        respin_times = 5

        respin = {}

        respin_reel = self.get_trigger_reel(bonus_reel, bonus_award)
        respin_recoder = 0
        respin_win = 0
        extra_times = Util.randdict(Config.Extra_Respin_Times)
        respin_times += 1
        # print("\n\n")
        while respin_times > 0:


            respin_times -= 1
            respin_recoder += 1
            for reel_idx in respin_reel.keys():
                for x in range(5):
                    for y in range(3):
                        idx = y * 5 + x
                        if respin_reel[reel_idx][Const.R_Respin_Reel][x][y] != Config.Bonus:
                            _random = random.random()
                            if _random < respin_reel[reel_idx][Const.C_Blank_Pos_Pro][idx]:
                                respin_reel[reel_idx][Const.R_Respin_Reel][x][y] = Config.Bonus
                                respin_reel[reel_idx][Const.R_Bonus_Award][idx] = Util.randdict(Config.Prize_on_Bonus)


            respin_result = {
                1: [respin_reel[1][Const.R_Respin_Reel],respin_reel[1][Const.R_Bonus_Award]],
                2: [respin_reel[2][Const.R_Respin_Reel],respin_reel[2][Const.R_Bonus_Award]],
                3: [respin_reel[3][Const.R_Respin_Reel],respin_reel[3][Const.R_Bonus_Award]]
            }

            respin[respin_recoder] = copy.deepcopy(respin_result)
            # print(json.dumps(respin[respin_recoder]))

        reel_bonus_num = [0,0,0]

        for x in range(5):
            for y in range(3):
                idx = y * 5 + x

                if respin_reel[1][Const.R_Respin_Reel][x][y] == Config.Bonus:
                    reel_bonus_num[0] += 1
                    if respin_reel[1][Const.R_Bonus_Award][idx] in Config.Const.C_Jackpot_Set.keys():
                        respin_win += Config.Const.C_Jackpot_Set[respin_reel[1][Const.R_Bonus_Award][idx]]
                    else:
                        respin_win += respin_reel[1][Const.R_Bonus_Award][idx]

                if respin_reel[2][Const.R_Respin_Reel][x][y] == Config.Bonus:
                    reel_bonus_num[1] += 1
                    if respin_reel[2][Const.R_Bonus_Award][idx] in Config.Const.C_Jackpot_Set.keys():
                        respin_win += Config.Const.C_Jackpot_Set[respin_reel[2][Const.R_Bonus_Award][idx]]
                    else:
                        respin_win += respin_reel[2][Const.R_Bonus_Award][idx]

                if respin_reel[3][Const.R_Respin_Reel][x][y] == Config.Bonus:
                    reel_bonus_num[2] += 1
                    if respin_reel[3][Const.R_Bonus_Award][idx] in Config.Const.C_Jackpot_Set.keys():
                        respin_win += Config.Const.C_Jackpot_Set[respin_reel[3][Const.R_Bonus_Award][idx]]
                    else:
                        respin_win += respin_reel[3][Const.R_Bonus_Award][idx]
        # print(reel_bonus_num)

        full_num = reel_bonus_num.count(15)
        # print(full_num)

        if full_num == 3:
            respin_win += 1110
        elif full_num == 2:
            respin_win += 110
        elif full_num == 1:
            respin_win += 10

        respin[Const.R_Respin_Win] = respin_win * self.total_bet
        respin[Const.R_Reel_Count] = reel_bonus_num
        return respin


