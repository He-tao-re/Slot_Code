import random
import Games.Game_1001_Britain.Britain_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy


Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)


class GameSlot(object):
    def __init__(self):
        self.self_data = {
        }

    def paidspin(self, totalbet):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel

        bonus_prize, bonus_num = self.get_bonus_prize(reel)

        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        if bonus_num >= 5:
            result[Const.R_Free] = []
        return result

    def get_bonus_prize(self, bonus_reel):
        bonus_prize = {}
        bonus_num = 0
        self.self_data = {}
        for i in range(5):
            for j in range(3):
                idx = j * 5 + i
                if bonus_reel[i][j] == Config.Bonus:
                    bonus_num += 1
                    bonus_prize[idx] = Util.randdict(Config.Const.C_Bonus_Prize)
        return bonus_prize, bonus_num



