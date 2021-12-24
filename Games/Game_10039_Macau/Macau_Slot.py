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

        s_mix_long = 0
        s_mix_mul = 0
        b_mix_long = 0
        b_mix_mul = 0
        mix_kind = None

        for i in range(len(line_combo)):
            if line_combo[i] in [Config.Wild, Config.S1, Config.S2, Config.S3]:
                s_mix_long += 1
                s_mix_mul = self.paytable[Config.Mix_S][s_mix_long - 1]
            else:
                break


        for i in range(len(line_combo)):
            if line_combo[i] in [Config.Wild, Config.B1, Config.B2]:
                b_mix_long += 1
                b_mix_mul = self.paytable[Config.Mix_B][b_mix_long - 1]
            else:
                break

        if s_mix_mul >= line_mul:
            line_mul = s_mix_mul
            kind = mix_kind
            long = s_mix_long

        if b_mix_mul >= line_mul:
            line_mul = b_mix_mul
            kind = mix_kind
            long = b_mix_long


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
        result.update(MixSymStandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable, Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild).evaluate())

        return result


# for x in Config.Const.C_LineSym + [Config.Bonus]:
#     for y in Config.Const.C_LineSym + [Config.Bonus]:
#         for z in Config.Const.C_LineSym + [Config.Bonus]:
#             for m in Config.Const.C_LineSym + [Config.Bonus]:
#                 for n in Config.Const.C_LineSym + [Config.Bonus]:
#                     line_combo = [x, y, z, m, n]
#                     oneline = {Const.R_Line_Combo: line_combo,Const.R_Line_Pos: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]}
#                     reel = []
#                     line_result = MixSymStandardLineEvaluator(100000, reel, Config.Const.C_PayLine, Config.Const.C_Paytable,
#                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub,
#                                                 Config.Const.C_LineSym, Config.Wilds, Config.Wild).evaluateLine(oneline)
#                     line_mul = line_result[Const.R_Line_Mul]
#                     if line_mul > 0:
#                         print(x, y, z, m, n,'\t',line_mul)
