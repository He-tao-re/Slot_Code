import random
import Games.Classic.Classic_Config as Config
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
        reel = Slot.GetReel(Base_ReelSets[0], Config.Const.C_Shape).get_reel()
        mul, combo= self.get_win(reel)

        result[Const.R_Reel] = reel
        result[Const.R_Win_Amount] = mul * totalbet
        result["combo"] = combo



        return result


    def get_win(self,reel):
        line_combo_set = set()
        line_combo_list = []

        line_mul = 0
        for col in reel:
            line_combo_set.add(col[0])
            line_combo_list.append(col[0])

        if line_combo_set.issubset({101,102,103}):
            line_mul = 500
            return line_mul,line_combo_list

        elif line_combo_set.issubset({101,102,103,104}):
            line_mul = 10
            for i in line_combo_list:
                if i == 101:
                    line_mul = line_mul * 5
                if i == 102:
                    line_mul = line_mul * 3
                if i == 103:
                    line_mul = line_mul * 2

            return line_mul,line_combo_list

        elif line_combo_set.issubset({101,102,103,105}):
            line_mul = 8
            for i in line_combo_list:
                if i == 101:
                    line_mul = line_mul * 5
                if i == 102:
                    line_mul = line_mul * 3
                if i == 103:
                    line_mul = line_mul * 2

            return line_mul,line_combo_list

        elif line_combo_set.issubset({101,102,103,106}):
            line_mul = 4
            for i in line_combo_list:
                if i == 101:
                    line_mul = line_mul * 5
                if i == 102:
                    line_mul = line_mul * 3
                if i == 103:
                    line_mul = line_mul * 2
            return line_mul,line_combo_list

        elif line_combo_set.issubset({101,102,103,107}):
            line_mul = 3
            for i in line_combo_list:
                if i == 101:
                    line_mul = line_mul * 5
                if i == 102:
                    line_mul = line_mul * 3
                if i == 103:
                    line_mul = line_mul * 2
            return line_mul,line_combo_list

        elif line_combo_set.issubset({101,102,103,108}):
            line_mul = 2
            for i in line_combo_list:
                if i == 101:
                    line_mul = line_mul * 5
                if i == 102:
                    line_mul = line_mul * 3
                if i == 103:
                    line_mul = line_mul * 2
            return line_mul,line_combo_list

        elif line_combo_set.issubset({101,102,103,104,105}):
            line_mul = 3
            for i in line_combo_list:
                if i == 101:
                    line_mul = line_mul * 5
                if i == 102:
                    line_mul = line_mul * 3
                if i == 103:
                    line_mul = line_mul * 2
            return line_mul,line_combo_list

        elif line_combo_set.issubset({101,102,103,106,107,108}):
            line_mul = 1
            for i in line_combo_list:
                if i == 101:
                    line_mul = line_mul * 5
                if i == 102:
                    line_mul = line_mul * 3
                if i == 103:
                    line_mul = line_mul * 2
            return line_mul,line_combo_list

        else:
            return line_mul,line_combo_list


