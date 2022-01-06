import random
import copy
import json
import Games.Game_10035_Frog.Frog_Config as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import Games.Game_10035_Frog.static_data_10035 as static_data

import numpy as np

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)

s_data = static_data.data


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
            # print('free end',sc_mul)
        """统计部分"""
        s_data[Const.S_Test_Time] += 1
        s_data[Const.S_Bet] += totalbet
        s_data[Const.S_Base_Win] += result[Const.R_Win_Amount]

        s_data[Const.S_Win] += result[Const.R_Win_Amount]

        if result[Const.R_Win_Amount] > 0:
            s_data[Const.S_Base_Hit] += 1

        if Const.R_Free in result.keys():
            s_data[Const.S_Free_Hit] += 1
            s_data[Const.S_Free_Win] += result[Const.R_Free_Win_Amount]

            s_data[Const.S_Win] += result[Const.R_Free_Win_Amount]

        for line in result[Const.R_Line]:
            kind = line[Const.R_Line_Kind]
            line_win = line[Const.R_Line_Win]
            line_long = line[Const.R_Line_Long]
            s_data[Const.S_Base_Sym_Win][kind][line_long-1] += line_win





        # print(json.dumps(result))
        return result


class FreeGame(object):
    def __init__(self,self_data,freespins,sc_mul):
        self.self_data = self_data
        self.freespins = freespins
        self.sc_mul = 1

        self.lock_wild = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,1,0]]
        self.wild_local_weight = copy.deepcopy(Config.Wild_Dance)

    def wild_dance(self):
        local_pos = Util.randdict(self.wild_local_weight)
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


        #第一次free，乘倍wild落点固定
        if free_recoder == 1:
            reel[4][1] = Config.M_Wild

        #wild倍数大于 0时乘倍wild 跳跃
        else:

            if self.sc_mul > 1:

                lock_wild_pos = self.wild_dance()
                del self.wild_local_weight[lock_wild_pos]
                x = lock_wild_pos % 5
                y = lock_wild_pos // 5
                # print(x,y,lock_wild_pos)
                # print(f"X:{x} \t Y:{y} \t Pos:{lock_wild_pos}")
                for i in range(5):
                    for j in range(3):
                        if self.lock_wild[i][j] == 1:
                            reel[i][j] = Config.Wild


                reel[x][y] = Config.M_Wild
                self.lock_wild[x][y] = 1
                self.sc_mul -= 1

            else:
                pass
        # print(reel,self.sc_mul)
        result.update(Slot.StandardLineEvaluator(totalbet, reel, Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub,
                                                 Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).mul_wild_evaluate(Config.M_Wild,self.sc_mul))



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
            # print(json.dumps(free_spin))
            free_result[free_recoder] = free_spin

        return free_result,free_win_amount
