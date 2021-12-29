import random
import Games.Game_10039_Macau.Macau_Config as Config
import Games.Game_10039_Macau.static_data_10039 as static_data
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy
import numpy as np

ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_ReelSets)
FreeReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)
ClassicReelSets = Slot.DealReel().ReelStrip(Const.C_Classic_ReelSets)
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

def special_sym_count(reel):
    wild_pos = []
    bonus_pos = []
    for x in range(5):
        for y in range(3):
            if reel[x][y] == Config.Wild:
                wild_pos.append([x,y])
            elif reel[x][y] == Config.Bonus:
                bonus_pos.append([x,y])
                change_bonus = Util.randlist(Config.Base_Bonus_Change)

                reel[x][y] = change_bonus
            else:
                pass
    return wild_pos, bonus_pos, reel

class GameSlot(object):
    def __init__(self,game_data):
        self.game_data = game_data

    def paidspin(self,totalbet):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        wild_pos, bonus_pos, reel = special_sym_count(reel)

        result[Const.R_Reel] = reel
        result.update(MixSymStandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable, Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild).evaluate())


        self.game_data[Const.R_Scatter_Pos] = wild_pos
        self.game_data[Const.R_Bonus_Pos] = bonus_pos

        if len(wild_pos) >= 6:
            free_spin_times = len(wild_pos)
            result[Const.R_Free] = FreeGame(self.game_data).free(totalbet, free_spin_times)
        if len(bonus_pos) >= 6:
            respin,respin_mul = RespinGame(reel,Config.Const.C_Blank_Pos_Pro).respin(totalbet)
            result[Const.R_Respin] = respin
            result[Const.R_Respin_Win] = respin_mul * totalbet





        '''base 统计部分'''
        static_data.data[Const.S_Bet] += totalbet
        static_data.data[Const.S_Test_Time] += 1

        static_data.data[Const.S_Base_Win] += result[Const.R_Win_Amount]
        static_data.data[Const.S_Win] += result[Const.R_Win_Amount]

        if result[Const.R_Win_Amount] > 0:
            static_data.data[Const.S_Base_Hit] += 1

        return result


class FreeGame(object):

    def __init__(self, game_data):
        self.game_data = game_data

    def freespin(self, totalbet):

        result = {}
        reel_idx = 0
        reel = Slot.GetReel(FreeReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel

        wild_pos = self.game_data[Const.R_Scatter_Pos]
        for pos in wild_pos:
            x = pos[0]
            y = pos[1]

            reel[x][y] = Config.Wild

        result.update(MixSymStandardLineEvaluator(totalbet, reel, Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                  Config.Const.C_BetLine, Config.Const.C_Wild_Sub,
                                                  Config.Const.C_LineSym, Config.Wilds, Config.Wild).evaluate())


        '''统计部分'''
        static_data.data[Const.S_Free_Win] += result[Const.R_Win_Amount]
        static_data.data[Const.S_Win] += result[Const.R_Win_Amount]
        static_data.data[Const.S_FreeSpin] += 1

        if result[Const.R_Win_Amount] > 0:
            static_data.data[Const.S_Free_Win_Hit] += 1

        return result

    def free(self,totalbet,free_spin_times):

        free = {}
        free_recoder = 0

        free_win_amount = 0
        while free_spin_times > 0:
            free_spin_times -= 1
            free_recoder += 1

            free_result = self.freespin(totalbet)
            free_win_amount += free_result[Const.R_Win_Amount]
            free_result[Const.R_Free_Win_Amount] = copy.deepcopy(free_win_amount)

            free[free_recoder] = free_result

        '''统计部分'''
        static_data.data[Const.S_Free_Hit] += 1

        return free


class RespinGame(object):
    def __init__(self,reel,pro):
        self.bonus_reel = reel
        self.pos_pro = {}
        self.bonus_account = {}

        self.respin_times = 3
        self.respin_recoder = 0

        self.allocate_pro(pro)

    def allocate_pro(self, pro):
        blank_pos = []
        for x in range(5):
            for y in range(3):
                if self.bonus_reel[x][y] in [Config.Bonus_5X,Config.Bonus_3X,Config.Bonus_2X]:
                    pass
                else:
                    idx = x + y * 5
                    blank_pos.append(idx)

        random.shuffle(blank_pos)

        i = 0
        for idx in blank_pos:
            self.pos_pro[idx] = pro[i]
            i += 1

    def respin(self,totalbet):
        respin = {}

        while self.respin_times > 0:
            self.respin_recoder += 1
            self.respin_times -= 1

            for x in range(5):
                for y in range(3):
                    if self.bonus_reel[x][y] in [Config.Bonus_5X,Config.Bonus_3X,Config.Bonus_2X]:
                        pass
                    else:
                        rand_num1 = random.random()

                        idx = x + y * 5
                        if self.pos_pro[idx] > rand_num1:
                            self.bonus_reel[x][y] = Util.randlist(Config.Feature_Bonus_Change)
                            self.respin_times = 3

            respin_result = {
                Const.R_Respin_Reel: copy.deepcopy(self.bonus_reel)
            }

            respin[self.respin_recoder] = respin_result

        for x in range(5):
            for y in range(3):

                if self.bonus_reel[x][y] is Config.Bonus_2X:
                    static_data.data['Bonus_2X'] += 1
                    active = True
                    while active:
                        mul = bonus_2x_game()
                        if mul > 0:
                            idx = x + y * 5
                            self.bonus_account[idx] = mul
                            static_data.data['Bonus_2X_Win'] += mul

                            active = False


                elif self.bonus_reel[x][y] is Config.Bonus_3X:
                    static_data.data['Bonus_3X'] += 1
                    active = True
                    while active:
                        mul = bonus_3x_game()

                        if mul > 0:
                            idx = x + y * 5
                            self.bonus_account[idx] = mul
                            static_data.data['Bonus_3X_Win'] += mul

                            active = False


                elif self.bonus_reel[x][y] is Config.Bonus_5X:
                    static_data.data['Bonus_5X'] += 1
                    active = True
                    while active:
                        mul = bonus_5x_game()

                        if mul > 0:
                            idx = x + y * 5
                            self.bonus_account[idx] = mul
                            static_data.data['Bonus_5X_Win'] += mul

                            active = False


        respin_mul = sum(self.bonus_account.values())

        if len(self.bonus_account.keys()) == 15:
            #Grand
            respin_mul += Config.Const.C_Jackpot_Set[Const.C_Grand]
            static_data.data[Const.S_Grand] += 1


        respin[Const.R_Respin_Account] = copy.deepcopy(self.bonus_account)


        '''respin 统计'''
        static_data.data[Const.S_Feature_Hit] += 1
        static_data.data[Const.S_Feature_Win] += respin_mul * totalbet
        static_data.data[Const.S_Feature_Spin] += self.respin_recoder
        static_data.data[Const.S_Feature_Sym_Count] += len(self.bonus_account.keys())

        static_data.data[Const.S_Win] += respin_mul * totalbet

        return respin,respin_mul



def get_line_combo(reel,lines):
    combos = []
    for line in lines:
        combo = [reel[0][line[0]],reel[1][line[1]],reel[2][line[2]]]
        combos.append(combo)
    return combos

def get_line_mul(combo):
    paytable = Config.Classic_Paytable

    sym_set = set(combo)

    if sym_set == {Config.C_5X}:
        #Major
        mul = paytable[Config.C_5X]
        static_data.data[Const.S_Major] += 1

    elif sym_set == {Config.C_3X}:
        #Minor
        mul = paytable[Config.C_3X]
        static_data.data[Const.S_Minor] += 1

    elif sym_set == {Config.C_2X}:
        #Mini
        mul = paytable[Config.C_2X]
        static_data.data[Const.S_Mini] += 1


    elif sym_set <= {Config.C_2X,Config.C_3X,Config.C_5X,Config.C_S1}:
        mul = paytable[Config.C_S1] * pow(2,combo.count(Config.C_2X)) * pow(3, combo.count(Config.C_3X)) * pow(5, combo.count(Config.C_5X))

    elif sym_set <= {Config.C_2X,Config.C_3X,Config.C_5X,Config.C_S2}:
        mul = paytable[Config.C_S2] * pow(2,combo.count(Config.C_2X)) * pow(3, combo.count(Config.C_3X)) * pow(5, combo.count(Config.C_5X))

    elif sym_set <= {Config.C_2X,Config.C_3X,Config.C_5X,Config.C_B1}:
        mul = paytable[Config.C_B1] * pow(2,combo.count(Config.C_2X)) * pow(3, combo.count(Config.C_3X)) * pow(5, combo.count(Config.C_5X))

    elif sym_set <= {Config.C_2X,Config.C_3X,Config.C_5X,Config.C_B2}:
        mul = paytable[Config.C_B2] * pow(2,combo.count(Config.C_2X)) * pow(3, combo.count(Config.C_3X)) * pow(5, combo.count(Config.C_5X))

    elif sym_set <= {Config.C_2X,Config.C_3X,Config.C_5X,Config.C_B3}:
        mul = paytable[Config.C_B3] * pow(2,combo.count(Config.C_2X)) * pow(3, combo.count(Config.C_3X)) * pow(5, combo.count(Config.C_5X))

    elif sym_set <= {Config.C_2X,Config.C_3X,Config.C_5X,Config.C_S1,Config.C_S2}:
        mul = paytable[Config.C_Mix_S] * pow(2,combo.count(Config.C_2X)) * pow(3, combo.count(Config.C_3X)) * pow(5, combo.count(Config.C_5X))

    elif sym_set <= {Config.C_2X,Config.C_3X,Config.C_5X,Config.C_B1,Config.C_B2,Config.C_B3}:
        mul = paytable[Config.C_Mix_B] * pow(2,combo.count(Config.C_2X)) * pow(3, combo.count(Config.C_3X)) * pow(5, combo.count(Config.C_5X))

    elif sym_set == {Config.C_2X,Config.C_Blank}:
        if combo.count(Config.C_2X) == 1:
            mul = 1
        elif combo.count(Config.C_2X) == 2:
            mul = 5

    elif sym_set == {Config.C_3X,Config.C_Blank}:
        if combo.count(Config.C_3X) == 1:
            mul = 2
        elif combo.count(Config.C_3X) == 2:
            mul = 10

    elif sym_set == {Config.C_5X,Config.C_Blank}:
        if combo.count(Config.C_5X) == 1:
            mul = 4
        elif combo.count(Config.C_5X) == 2:
            mul = 20

    else:
        mul = 0

    # print(combo,'\t',sym_set,'\t',mul)

    return mul

def bonus_2x_game():
    reel = Slot.GetReel(ClassicReelSets[0], [3,3,3]).get_reel()
    lines = [
        [1, 1, 1]
    ]

    combos = get_line_combo(reel,lines)

    mul = 0

    for combo in combos:
        mul += get_line_mul(combo)

    static_data.data['Bonus_2X_Times'] += 1

    return mul


def bonus_3x_game():
    reel = Slot.GetReel(ClassicReelSets[1], [3, 3, 3]).get_reel()
    lines = [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ]

    combos = get_line_combo(reel, lines)

    mul = 0

    for combo in combos:
        mul += get_line_mul(combo)

    static_data.data['Bonus_3X_Times'] += 1

    return mul


def bonus_5x_game():
    reel = Slot.GetReel(ClassicReelSets[2], [3, 3, 3]).get_reel()
    lines = [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2],
        [0, 1, 2],
        [2, 1, 0]
    ]

    combos = get_line_combo(reel, lines)

    mul = 0

    for combo in combos:
        mul += get_line_mul(combo)

    static_data.data['Bonus_5X_Times'] += 1

    return mul
