import random
import Games.Game_10035_Frog.Frog_Config as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

import numpy as np

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)



def scatter_count(reel):
    sc_num = 0
    sc_pos = []

    for x in range(len(reel)):
        for y in range(len(reel[x])):
            if reel[x][y] == Config.Scatter:
                sc_num += 1
                sc_pos.append([[x,y],Util.randlist(Config.Scatter_Mul)])

    return sc_num,sc_pos


class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data

    def paidspin(self,totalbet):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel


        sc_num,sc_pos = scatter_count(reel)


        #Scatter Win

        if sc_num >= 1:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0



        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)



        if sc_num >= 3:
            sc_mul = 0
            for pos in sc_pos:
                sc_mul += pos[-1]
            result[Const.R_Free], result[Const.R_Free_Win_Amount] = FreeGame(self_data={},freespins=7,sc_mul=sc_mul).free(totalbet)


        return result


class FreeGame(object):
    def __init__(self,self_data,freespins,sc_mul):
        self.self_data = self_data
        self.freespins = freespins
        self.sc_mul = sc_mul

        self.lock_wild = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,1,0]]

    def wild_dance(self):
        blank_pos = {}

        for x in range(len(self.lock_wild)):
            for y in range(len(self.lock_wild[x])):
                idx = y * 5 + x
                blank_pos[idx] = Config.Wild_Dance[idx]

        local_pos = Util.randdict(blank_pos)

        return local_pos

    def freespin(self,totalbet,free_recoder):
        result = {}
        reel_idx = 1
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel

        sc_num, sc_pos = scatter_count(reel)

        # Scatter Win

        if sc_num >= 1:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num - 1]
        else:
            sc_win = 0

        if sc_num >= 3:
            self.freespins += 7

        if free_recoder == 1:
            reel[4][1] = Config.M_Wild

        else:

            if self.sc_mul > 1:

                lock_wild_pos = self.wild_dance()

                x = lock_wild_pos % 5
                y = lock_wild_pos // 5

                for i in range(5):
                    for j in range(3):
                        if self.lock_wild[i][j] == 1:
                            reel[i][j] = Config.Wild


                reel[x][y] = Config.M_Wild
                self.lock_wild[x][y] = 1
            else:
                pass

        result.update(Slot.StandardLineEvaluator(totalbet, reel, Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub,
                                                 Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).mul_wild_evaluate(Config.M_Wild,self.sc_mul))
        self.sc_mul -= 1







        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result


    def free(self,totalbet):

        free_result = {}

        free_recoder = 0

        free_win_amount = 0

        while self.freespins > 0:
            free_recoder += 1
            self.freespins -= 1


            free_spin = self.freespin(totalbet,free_recoder)
            free_win_amount += free_spin[Const.R_Win_Amount]
            free_spin[Const.R_Free_Win_Amount] = copy.deepcopy(free_win_amount)

            free_result[free_recoder] = free_spin

        return free_result,free_win_amount
