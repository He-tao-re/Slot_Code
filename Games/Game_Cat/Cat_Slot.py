import random
import Games.Game_Cat.Cat_Config as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

base_reel_stripes = Config.Const.C_Base_ReelSets[0][Const.C_ReelStrip]


class GameSlot(object):
    def __init__(self):
        self.self_data = {}

    def paidspin(self,totalbet):

        result = {}
        reel = []

        for strip in base_reel_stripes:
            reel.append(Util.randlist(strip))

        result[Const.R_Reel] = reel






        # result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
        #                                          Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
        #                                          Config.Wilds, Config.Wild).evaluate())
        # result[Const.R_Self_Data] = copy.deepcopy(self.self_data)


        return result

class fun(object):
    def get_line_combo(self,reel):
        payline = Config.C_PayLine
        line_result = {}
        line_id = 0
        for line in payline:
            one_line = {
                Const.R_Line_Combo: [],
                Const.R_Line_Mul: 0,
                Const.R_Line_Win: 0,
            }
            for pos_idx in line:
                one_line[Const.R_Line_Combo].append(reel[pos_idx])





if __name__ == '__main__':
    print(GameSlot().paidspin(100))