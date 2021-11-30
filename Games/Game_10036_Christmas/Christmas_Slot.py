import random
import Games.Game_10036_Christmas.Christmas_Config as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

import numpy as np

ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_ReelSets)



def scatter_count(reel):
    sc_num = 0
    sc_pos = []

    for x in range(len(reel)):
        for y in range(len(reel[x])):
            if reel[x][y] == Config.Scatter:
                sc_num += 1

    return sc_num,sc_pos

def base_wild_mirror(reel):
    mirror_reel = copy.deepcopy(reel)
    for i in range(3):

        if reel[i] == [0, 0, 0]:
            mirror_reel[5 - i] = [0, 0, 0]
        elif reel[i] == [100, 100, 100]:
            mirror_reel[5 - i] = [100, 100, 100]

    return mirror_reel

def free_wild_mirror(reel):
    mirror_reel = copy.deepcopy(reel)
    for i in range(3):
        if reel[i] == [0, 0, 0]:
            mirror_reel[5-i] = [0, 0, 0]
        elif reel[i] == [100, 100, 100]:
            mirror_reel[5 - i] = [100, 100, 100]

    for i in range(3,6):
        if reel[i] == [0, 0, 0]:
            mirror_reel[5 - i] = [0, 0, 0]
        elif reel[i] == [100, 100, 100]:
            mirror_reel[5 - i] = [100, 100, 100]

    return mirror_reel


class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data

    def paidspin(self,totalbet):

        result = {}
        reel_idx = 0
        reel = Slot.GetReel(ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        for x in range(6):
            if reel[x] == [0, 0, 0]:
                _rand_num = random.random()
                if _rand_num < Config.Base_Wild_Change[x]:
                    reel[x] = [100, 100, 100]

        result[Const.R_Reel] = reel

        mirror_reel = base_wild_mirror(reel)

        sc_num,sc_pos = scatter_count(mirror_reel)


        # print(reel)
        # print(mirror_reel)
        # print('\n')

        #Scatter Win

        if sc_num >= 1:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0



        result.update(Slot.StandardLineEvaluator(totalbet,mirror_reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())



        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)



        if sc_num >= 3:
            freespins = Config.Free_Spins[sc_num - 1]
            result[Const.R_Free],result[Const.R_Free_Win_Amount] = FreeGame(self_data={}).free(totalbet,freespins)

        return result


class FreeGame(object):
    def __init__(self,self_data):
        self.self_data = self_data

        self.free_win_amount = 0
    def free_spin(self,totalbet):
        result = {}

        reel_idx = 1
        reel = Slot.GetReel(ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        for x in range(6):
            if reel[x] == [0, 0, 0]:
                _rand_num = random.random()

                if _rand_num < Config.Free_Wild_Change[x]:
                    reel[x] = [100, 100, 100]

        result[Const.R_Reel] = reel

        mirror_reel = free_wild_mirror(reel)



        result.update(Slot.StandardLineEvaluator(totalbet, mirror_reel, Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub,
                                                 Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        self.free_win_amount += result[Const.R_Win_Amount]

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)
        result[Const.R_Free_Win_Amount] = copy.deepcopy(self.free_win_amount)

        return result


    def free(self,totalbet,freespins):
        free = {}
        free_recoder = 0

        while freespins > 0 :
            free_recoder += 1
            freespins -= 1

            free[free_recoder] = self.free_spin(totalbet)

        return free, self.free_win_amount