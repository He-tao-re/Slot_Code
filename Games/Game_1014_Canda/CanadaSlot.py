import random
import Games.Game_1014_Canda.Canada_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)

class GameSlot(object):
    def __init__(self):
        self.self_data = {
            Const.R_Free_Hit:[]
        }

    def paidspin(self,totalbet):

        result = {}
        reel = Slot.GetReel(Base_ReelSets[0], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel
        sc_num = self.scatterwin(reel)

        #Scatter Win
        if sc_num >= 2:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        self.free_hit(result[Const.R_Line])
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result


    def scatterwin(self, reel):
        consecutive_sc = 0
        sc_num = 0
        for x in range(5):
            if Config.Scatter in reel[x]:
                consecutive_sc += 1
            else:
                break

        for y in range(consecutive_sc):
            sc_num += reel[y].count(Config.Scatter)
        return sc_num

    def free_hit(self,lines):
        if len(lines) > 0:
            for line in lines:
                line_long = line[Const.R_Line_Long]
                line_sym = line[Const.R_Line_Combo]
                if Config.Wild in line_sym[:line_long]:
                    hit = {Const.R_Hit_Combo: line_sym,
                           Const.R_Hit_Win: line[Const.R_Line_Win]
                           }
                    self.self_data[Const.R_Free_Hit].append(hit)








