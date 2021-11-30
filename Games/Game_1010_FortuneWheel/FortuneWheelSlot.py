import random
import Games.Game_1010_FortuneWheel.FortuneWheel_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)


class GameSlot(object):
    def __init__(self):
        self.self_data = {}

    def paidspin(self, totalbet):
        result = {}
        reel = Slot.GetReel(Base_ReelSets[0], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel


        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)
        result.update(GameLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).game1010evaluate())

        return result

class GameLineEvaluator(Slot.StandardLineEvaluator):
    def __init__(self,totalbet, spinreel, payline, paytable, betLine, wild_sub, linesym, wilds, wild):
        super(GameLineEvaluator,self).__init__(totalbet, spinreel, payline, paytable, betLine, wild_sub, linesym, wilds, wild)


    def game1010evaluateLine(self, oneline):
        line_combo = oneline[Const.R_Line_Combo]
        line_sym_set = set(line_combo)
        if line_sym_set.issubset({Config.Wild}):
            kind = Config.Wild
            line_mul = self.paytable[kind][0]
            long = 3

            oneline[Const.R_Line_Kind] = kind
            oneline[Const.R_Line_Mul] = line_mul
            oneline[Const.R_Line_Win] = line_mul * self.linebet
            oneline[Const.R_Line_Pos] = oneline[Const.R_Line_Pos][:long]
            oneline[Const.R_Line_Long] = long

            return oneline

        elif line_sym_set.issubset({Config.Wild, Config.Seven}):
            kind = Config.Seven
            line_mul = self.paytable[kind][0]
            long = 3

            oneline[Const.R_Line_Kind] = kind
            oneline[Const.R_Line_Mul] = line_mul
            oneline[Const.R_Line_Win] = line_mul * self.linebet
            oneline[Const.R_Line_Pos] = oneline[Const.R_Line_Pos][:long]
            oneline[Const.R_Line_Long] = long

            return oneline

        elif line_sym_set.issubset({Config.Wild, Config.Bar_5}):
            kind = Config.Bar_5
            line_mul = self.paytable[kind][0]
            long = 3

            oneline[Const.R_Line_Kind] = kind
            oneline[Const.R_Line_Mul] = line_mul
            oneline[Const.R_Line_Win] = line_mul * self.linebet
            oneline[Const.R_Line_Pos] = oneline[Const.R_Line_Pos][:long]
            oneline[Const.R_Line_Long] = long

            return oneline

        elif line_sym_set.issubset({Config.Wild, Config.Bar}):
            kind = Config.Bar
            line_mul = self.paytable[kind][0]
            long = 3

            oneline[Const.R_Line_Kind] = kind
            oneline[Const.R_Line_Mul] = line_mul
            oneline[Const.R_Line_Win] = line_mul * self.linebet
            oneline[Const.R_Line_Pos] = oneline[Const.R_Line_Pos][:long]
            oneline[Const.R_Line_Long] = long

            return oneline

        elif line_sym_set.issubset({Config.Wild, Config.Ring}):
            kind = Config.Ring
            line_mul = self.paytable[kind][0]
            long = 3

            oneline[Const.R_Line_Kind] = kind
            oneline[Const.R_Line_Mul] = line_mul
            oneline[Const.R_Line_Win] = line_mul * self.linebet
            oneline[Const.R_Line_Pos] = oneline[Const.R_Line_Pos][:long]
            oneline[Const.R_Line_Long] = long

            return oneline

        elif line_sym_set.issubset({Config.Wild, Config.Bar_5, Config.Bar}):
            kind = Config.Mix_Bar
            line_mul = self.paytable[kind][0]
            long = 3

            oneline[Const.R_Line_Kind] = kind
            oneline[Const.R_Line_Mul] = line_mul
            oneline[Const.R_Line_Win] = line_mul * self.linebet
            oneline[Const.R_Line_Pos] = oneline[Const.R_Line_Pos][:long]
            oneline[Const.R_Line_Long] = long

            return oneline

        else:
            oneline[Const.R_Line_Kind] = None
            oneline[Const.R_Line_Mul] = 0
            oneline[Const.R_Line_Win] = 0
            oneline[Const.R_Line_Pos] = None
            oneline[Const.R_Line_Long] = 0
            return oneline


    def game1010evaluate(self):
        line_result = {}
        line_ifo = self.GetAllLine()
        line_result[Const.R_Line] = []
        winAmount = 0
        for singalline in line_ifo:
            oneline = self.game1010evaluateLine(singalline)
            if oneline[Const.R_Line_Win] > 0:
                winAmount += oneline[Const.R_Line_Win]
                line_result[Const.R_Line].append(oneline)
        line_result[Const.R_Line_WinAmount] = winAmount
        line_result[Const.R_Win_Amount] = winAmount
        return line_result

