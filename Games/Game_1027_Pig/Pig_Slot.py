import random
import Games.Game_1028_Aladdin.Aladdin_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

import numpy as np

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)


def scatter_num(reel):
    sc_num = 0
    for x in range(5):
        if Config.Scatter in reel[x]:
            sc_num += 1
    return sc_num



class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data


    def paidspin(self,totalbet):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel










        return result



