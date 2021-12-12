import random
import Games.Game_10039_Macau.Macau_Config as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy
import numpy as np

ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_ReelSets)

class MixSymStandardLineEvaluator(Slot.StandardLineEvaluator):

    def evaluateLine(self, oneline):
        line_combo = oneline[Const.R_Line_Combo]

        wild_long = 0
        wild_mul = 0
        kind = line_combo[0]

        sym_long = 0
        line_mul = 0
        long = 0

        mix_long = 0
        mix_mul = 0
        mix_kind = None

        if line_combo[0] in self.linesym:
            if line_combo[0] in self.wildsub:
                for x in range(len(line_combo)):
                    if line_combo[x] == line_combo[0] or line_combo[x] in self.wilds:
                        sym_long += 1
                    else:
                        break

                kind = line_combo[0]
                line_mul = self.paytable[kind][sym_long-1]
                long = sym_long

            elif line_combo[0] in self.wilds:
                for x in range(len(line_combo)):
                    if line_combo[x] in self.wilds:
                        wild_long += 1
                    else:
                        break

                if wild_long < len(line_combo):

                    normal_sym = line_combo[wild_long]

                    if normal_sym in self.linesym:
                        for x in range(len(line_combo)):
                            if line_combo[x] == line_combo[wild_long] or line_combo[x] in self.wilds:
                                sym_long += 1
                            else:
                                break

                        if self.paytable[normal_sym][sym_long-1] >= self.paytable[self.wild][wild_long-1]:
                            line_mul = self.paytable[normal_sym][sym_long-1]
                            long = sym_long
                            kind = normal_sym
                        else:
                            line_mul = self.paytable[self.wild][wild_long-1]
                            long = wild_long
                            kind = self.wild
                    else:
                        line_mul = self.paytable[self.wild][wild_long-1]
                        long = wild_long
                        kind = self.wild
                else:
                    line_mul = self.paytable[self.wild][wild_long - 1]
                    long = wild_long
                    kind = self.wild


        # for sym in line_combo:
        #     if sym in Config.Sevens:
        #         mix_kind = Config.Mix_S
        #         break
        #     elif sym in Config.Bars:
        #         mix_kind = Config.Mix_B
        #         break

        # if mix_kind == Config.Mix_S:
        #     for sym in line_combo:
        #         if sym in Config.Sevens + Config.Wilds:
        #             mix_long += 1
        #             mix_kind = Config.Mix_S
        #             mix_mul = Config.Const.C_Paytable[mix_kind][mix_long - 1]
        #         else:
        #             break
        #
        # elif mix_kind == Config.Mix_B:
        #     for sym in line_combo:
        #         if sym in Config.Bars + Config.Wilds:
        #             mix_long += 1
        #             mix_kind = Config.Mix_B
        #             mix_mul = Config.Const.C_Paytable[mix_kind][mix_long - 1]
        #         else:
        #             break
        #
        # if mix_mul > line_mul:
        #     line_mul = mix_mul
        #     kind = mix_kind
        #     long = mix_long


        oneline[Const.R_Line_Kind] = kind
        oneline[Const.R_Line_Mul] = line_mul
        oneline[Const.R_Line_Win] = line_mul * self.linebet
        oneline[Const.R_Line_Pos] = oneline[Const.R_Line_Pos][:long]
        oneline[Const.R_Line_Long] = long

        return oneline

    def evaluate(self):
        line_result = {}
        line_ifo = self.GetAllLine()
        line_result[Const.R_Line] = []
        winAmount = 0
        for singalline in line_ifo:
            oneline = self.evaluateLine(singalline)
            if oneline[Const.R_Line_Win] > 0:
                winAmount += oneline[Const.R_Line_Win]
                line_result[Const.R_Line].append(oneline)
        line_result[Const.R_Line_WinAmount] = winAmount
        line_result[Const.R_Win_Amount] = winAmount
        return line_result



class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data

    def paidspin(self,totalbet):

        result = {}
        reel_idx = 0
        reel = Slot.GetReel(ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel
        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable, Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild).evaluate())

        return result


