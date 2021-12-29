import random
import Games.Game_Cat.Cat_Config as Config
import Games.Game_Cat.Const as Const
import copy

base_reel_stripes = Config.Const.C_Base_ReelSets[0][Const.C_ReelStrip]

def randlist(one_list):
    Total_Weight = 0
    for i in one_list:
        Total_Weight += i[1]
    ra = random.randint(0,Total_Weight - 1)
    curr_sum = 0

    kind = None
    for k in one_list:
        curr_sum = curr_sum + k[1]
        if ra < curr_sum:
            kind = k[0]
            break
    return kind


def get_line_combo(reel,total_bet,Bet_Line):
    payline = Config.Const.C_PayLine
    line_result = {}
    line_id = 0
    line_win_amount = 0
    for line in payline:
        one_line = {
            Const.R_Line_Combo: [],
            Const.R_Line_Mul: 0,
            Const.R_Line_Win: 0,
        }
        for pos_idx in line:
            one_line[Const.R_Line_Combo].append(reel[pos_idx])

        combo_set = set(one_line[Const.R_Line_Combo])
        if len(combo_set) == 1:
            kind = list(combo_set)[0]
            if kind in Config.Const.C_LineSym:
                one_line[Const.R_Line_Kind] = kind
                one_line[Const.R_Line_Mul] = Config.Const.C_Paytable[kind][0]
                one_line[Const.R_Line_Win] = total_bet / Bet_Line * Config.Const.C_Paytable[kind][0]
                line_win_amount += one_line[Const.R_Line_Win]
                line_result[line_id] = one_line
        line_id += 1
    line_result[Const.R_Line_WinAmount] = line_win_amount

    return line_result

def reel_shuffle(reel):
    list_1 = [reel[0], reel[2], reel[4], reel[6], reel[8]]
    list_2 = [reel[1], reel[3], reel[5], reel[7]]

    random.shuffle(list_1)
    random.shuffle(list_2)
    new_reel = [list_1[0],list_2[0],
                list_1[1],list_2[1],
                list_1[2],list_2[2],
                list_1[3], list_2[3],
                list_1[4]
                ]
    return new_reel


class GameSlot(object):
    def __init__(self):
        self.self_data = {}

    def paid_spin(self,totalbet):

        result = {}
        reel = []

        for strip in base_reel_stripes:
            reel.append(randlist(strip))
        # print(reel)
        result[Const.R_Reel] = reel_shuffle(reel)
        # print(result[Const.R_Reel])
        # print("=====\n")
        bonus_s = reel.count(Config.Bonus_S)
        bonus_r = reel.count(Config.Bonus_R)
        bonus__ = reel.count(Config.Bonus)

        result[Const.R_Line] = get_line_combo(result[Const.R_Reel], totalbet, Config.Const.C_BetLine)

        result[Const.R_Win_Amount] = result[Const.R_Line][Const.R_Line_WinAmount]

        bonus_num = bonus_r + bonus__ + bonus_s
        if bonus_num >= 4:
            result[Const.R_Jackpot_Win] = Config.Bonus_prize[bonus_num - 1] * totalbet
        else:
            result[Const.R_Jackpot_Win] = 0


        if bonus_s >= 3:
            result[Const.R_Free] = {}
            result[Const.R_Free_Win_Amount] = 0


        if bonus_r >= 1:
            result[Const.R_Respin], respin_jackpot_win, respin_line_win, end_reel, bonus_num = Respin(reel).respin_game(totalbet)
            result[Const.R_Bonus_Num] = bonus_num
            result[Const.R_Respin_Win] = respin_jackpot_win + respin_line_win

            r_bonus_s = end_reel.count(Config.Bonus_S)

            if r_bonus_s >= 3:
                result[Const.R_Free] = {}
                result[Const.R_Free_Win_Amount] = 0

        return result



class Respin(object):
    def __init__(self,reel):
        self.reel = reel
        self.unlock_pos_1 = []
        self.unlock_pos_2 = []
        self.pos_pro = {}

    def allocate(self):
        for i in range(len(self.reel)):
            if self.reel[i] in [Config.Bonus_R, Config.Bonus_S, Config.Bonus]:
                pass
            else:
                if i % 2 == 1:
                    self.unlock_pos_1.append(i)
                else:
                    self.unlock_pos_2.append(i)

        random.shuffle(self.unlock_pos_1)
        random.shuffle(self.unlock_pos_2)

        if len(self.unlock_pos_1) >= 1:
            self.pos_pro[self.unlock_pos_1[0]] = Config.Respin_reel[0]
        if len(self.unlock_pos_2) >= 1:
            self.pos_pro[self.unlock_pos_2[0]] = Config.Respin_reel[1]

        for pos_idx in self.unlock_pos_1[1:]:
            self.pos_pro[pos_idx] = Config.Respin_reel[2]
        for pos_idx in self.unlock_pos_2[1:]:
            self.pos_pro[pos_idx] = Config.Respin_reel[3]

    def respin_game(self,totalbet):
        self.allocate()

        respin_result = {}

        respin_line_win = 0

        respin_game = True
        respin_recoder = 0
        while respin_game:
            respin_recoder += 1
            result = {}

            bonus_re = 0

            for i in range(len(self.reel)):
                if self.reel[i] not in [Config.Bonus_R, Config.Bonus_S, Config.Bonus]:
                    new_sym = randlist(self.pos_pro[i])
                    self.reel[i] = new_sym
                    if new_sym == Config.Bonus_R:
                        bonus_re += 1

            respin_reel = copy.deepcopy(self.reel)

            result[Const.R_Line] = get_line_combo(respin_reel, totalbet, Config.Const.C_BetLine)

            result[Const.R_Win_Amount] = result[Const.R_Line][Const.R_Line_WinAmount]
            respin_line_win += result[Const.R_Line][Const.R_Line_WinAmount]

            respin_result[respin_recoder] = copy.deepcopy(result)

            if bonus_re == 1:
                respin_game = True
            else:
                respin_game = False


        bonus_s = self.reel.count(Config.Bonus_S)
        bonus_r = self.reel.count(Config.Bonus_R)
        bonus__ = self.reel.count(Config.Bonus)

        bonus_num = bonus_r + bonus__ + bonus_s
        if bonus_num >= 4:
            respin_jackpot_win = Config.Bonus_prize[bonus_num - 1] * totalbet
        else:
            respin_jackpot_win = 0

        return respin_result,respin_jackpot_win,respin_line_win,self.reel,bonus_num



