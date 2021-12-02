import random
import Games.Game_10040_Pirate.Pirate_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

import numpy as np
import json
Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)


class GameSlot(object):
    def __init__(self):
        self.self_data = {
        }

    def paidspin(self,totalbet):

        result = {}
        reel_idx = 0
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel

        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())

        sc_num = scatter_count(reel)
        if sc_num >= 3:
            result[Const.R_Free], result[Const.R_Free_Win_Amount] = MoveFreeGame().free_game(totalbet)


        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result

class MoveFreeGame(object):
    def __init__(self):
        self.wild_pos = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def wild_move(self):
        new_wild_pos = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for x in range(5):
            for y in range(3):
                if self.wild_pos[x][y] != 0:
                    if x - 1 >= 0:
                        new_wild_pos[x - 1][random.randint(0,2)] += self.wild_pos[x][y]
                    else:
                        pass
        return new_wild_pos

    def free_spin(self,totalbet):

        #移动
        self.wild_pos = self.wild_move()

        result = {}
        reel_idx = 1
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Show_Reel] = reel

        act_reel = copy.deepcopy(reel)
        for x in range(5):
            for y in range(3):
                if self.wild_pos[x][y] != 0:
                    act_reel[x][y] = Config.Wild

        result[Const.R_Reel] = act_reel

        result.update(Slot.StandardLineEvaluator(totalbet,act_reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())

        result[Const.R_Line_WinAmount] = 0
        result[Const.R_Win_Amount] = 0
        for line in result[Const.R_Line]:
            for line_pos in line[Const.R_Line_Pos]:
                x = line_pos[0]
                y = line_pos[1]

                if self.wild_pos[x][y] != 0:
                    line[Const.R_Line_Mul] = line[Const.R_Line_Mul] * self.wild_pos[x][y]
                    line[Const.R_Line_Win] = line[Const.R_Line_Win] * self.wild_pos[x][y]
                else:
                    pass
            result[Const.R_Win_Amount] += line[Const.R_Line_Win]
            result[Const.R_Line_WinAmount] += line[Const.R_Line_Win]

        for x in range(5):
            for y in range(3):
                if reel[x][y] == 0 and self.wild_pos[x][y] == 0:
                    self.wild_pos[x][y] = 1

        return result

    def free_game(self,totalbet):

        free_spin_times = 10

        free = {}
        free_recoder = 0
        free_win_amount = 0

        while free_spin_times > 0:
            free_spin_times -= 1
            free_recoder += 1

            spin_result = self.free_spin(totalbet)
            free_win_amount += spin_result[Const.R_Win_Amount]

            free[free_recoder] = spin_result

            # print(json.dumps(spin_result))
        return free, free_win_amount





def scatter_count(reel):
    sc_num = 0
    for x in range(len(reel)):
        for y in range(len(reel[x])):
            if reel[x][y] is Config.Scatter or reel[x][y] == 91:
                sc_num += 1
    return sc_num

