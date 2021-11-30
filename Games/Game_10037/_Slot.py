import Games.Game_10037._Config as Config
import Slot_common.Const as Const
import Slot_common.Slots as Slot
import util.Util as Util
import random
import copy
import types
import datetime
import json

ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_ReelSets)

Game_Set = Config.Const.C_Game_Set


class GameSlot(object):
    def __init__(self, game_data):
        self.game_data = game_data


    def spin(self,totalbet):

        if self.game_data[Const.R_Free_Spin_Left] == 0:

            _random_num = random.random()

            if _random_num < Config.Wild_Feature_Hit:
                result = self.wild_feature_spin(totalbet)
            else:
                result = self.normal_spin(totalbet)

        else:

            _random_num = random.random()

            if _random_num < Config.Free_Wild_Feature_Hit:
                result = self.free_wild_feature_spin(totalbet)
            else:
                result = self.free_spin(totalbet)

        result[Const.R_Game_Data] = self.game_data

        return result



    def normal_spin(self, totalbet):
        result = {Const.R_Spin_Type: Const.R_Base_Type}

        reel_idx = 0
        reel = Slot.GetReel(ReelSets[reel_idx], [5, 6, 6, 6, 6, 6]).get_reel()

        reel = reel_correction(reel)
        attach_prize = base_sym_attach_prize(reel)

        result[Const.R_Reel] = reel
        result[Const.R_Self_Data] = attach_prize
        result[Const.R_Line], result[Const.R_Way_WinAmount] = WildFeatureWayEvaluator(Config.Const.C_Paytable, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild, totalbet, Config.Const.C_BetLine, reel).evaluate()

        win_pos = get_win_pos(result[Const.R_Line])

        hit_attach_pos = attach_prize_judge(win_pos, attach_prize)

        result[Const.R_Extra_Win] = 0

        if len(hit_attach_pos) > 0:
            for hit_pos in hit_attach_pos:
                result[Const.R_Extra_Win] += hit_pos[1] * totalbet

        result[Const.R_Win_Amount] = result[Const.R_Way_WinAmount]

        result[Const.R_Free] = False
        sc_num = scatter_count(reel)
        if sc_num >= 3:
            freespins = Config.Free_Trigger[sc_num - 3]
            result[Const.R_Free] = True
            self.game_data[Const.R_Free_Spin_Total] = freespins
            self.game_data[Const.R_Free_Spin_Left] = freespins


        return result

    def wild_feature_spin(self, totalbet):
        result = {Const.R_Spin_Type: Const.R_Respin_Type}

        reel_idx = 1
        reel = Slot.GetReel(ReelSets[reel_idx], [5, 6, 6, 6, 6, 6]).get_reel()

        reel = reel_correction(reel)
        reel = wild_feature(reel)
        attach_prize = base_sym_attach_prize(reel)

        result[Const.R_Reel] = reel
        result[Const.R_Self_Data] = attach_prize
        result[Const.R_Line], result[Const.R_Way_WinAmount] = WildFeatureWayEvaluator(Config.Const.C_Paytable, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild, totalbet, Config.Const.C_BetLine, reel).evaluate()

        win_pos = get_win_pos(result[Const.R_Line])

        hit_attach_pos = attach_prize_judge(win_pos, attach_prize)

        result[Const.R_Extra_Win] = 0

        if len(hit_attach_pos) > 0:
            for hit_pos in hit_attach_pos:
                result[Const.R_Extra_Win] += hit_pos[1] * totalbet

        result[Const.R_Win_Amount] = result[Const.R_Way_WinAmount]

        return result

    def free_spin(self,totalbet):
        result = {Const.R_Spin_Type: Const.R_Free_Type}
        self.game_data[Const.R_Free_Spin_Left] -= 1


        reel_idx = 2
        reel = Slot.GetReel(ReelSets[reel_idx], [5, 6, 6, 6, 6, 6]).get_reel()

        reel = reel_correction(reel)

        #free
        attach_prize = free_sym_attach_prize(reel)

        result[Const.R_Reel] = reel
        result[Const.R_Self_Data] = attach_prize
        result[Const.R_Line], result[Const.R_Way_WinAmount] = WildFeatureWayEvaluator(Config.Const.C_Paytable, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild, totalbet, Config.Const.C_BetLine, reel).evaluate()

        win_pos = get_win_pos(result[Const.R_Line])


        #free
        hit_attach_pos = attach_prize_judge(win_pos, attach_prize)

        result[Const.R_Extra_Win] = 0

        if len(hit_attach_pos) > 0:
            for hit_pos in hit_attach_pos:
                result[Const.R_Extra_Win] += hit_pos[1] * totalbet

        result[Const.R_Win_Amount] = result[Const.R_Way_WinAmount]

        sc_num = scatter_count(reel)
        if sc_num >= 3:

            free_extra = Config.Free_Trigger[sc_num-3]
            result[Const.C_Re_Trigger_FreeSpins] = free_extra

            self.game_data[Const.R_Free_Spin_Total] += free_extra
            self.game_data[Const.R_Free_Spin_Left] += free_extra

        return result

    def free_wild_feature_spin(self, totalbet):
        result = {Const.R_Spin_Type: 11}
        self.game_data[Const.R_Free_Spin_Left] -= 1

        reel_idx = 3
        reel = Slot.GetReel(ReelSets[reel_idx], [5, 6, 6, 6, 6, 6]).get_reel()

        reel = reel_correction(reel)
        reel = wild_feature(reel)

        attach_prize = free_sym_attach_prize(reel)

        result[Const.R_Reel] = reel
        result[Const.R_Self_Data] = attach_prize
        result[Const.R_Line], result[Const.R_Way_WinAmount] = WildFeatureWayEvaluator(Config.Const.C_Paytable, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild, totalbet, Config.Const.C_BetLine, reel).evaluate()

        win_pos = get_win_pos(result[Const.R_Line])

        hit_attach_pos = attach_prize_judge(win_pos, attach_prize)

        result[Const.R_Extra_Win] = 0

        if len(hit_attach_pos) > 0:
            for hit_pos in hit_attach_pos:
                result[Const.R_Extra_Win] += hit_pos[1] * totalbet

        result[Const.R_Win_Amount] = result[Const.R_Way_WinAmount]


        return result




def scatter_count(reel):
    sc_num = 0
    for x in range(len(reel)):
        for y in range(len(reel[x]) - 1):
            if reel[x][y:y+2] == [Config.Scatter, Config.Scatter]:
                sc_num += 1
    return sc_num

def reel_correction(reel):
    correction_sym = [Config.H1, Config.H2, Config.H3, Config.H4, Config.H5, Config.H6, Config.Scatter]
    reel_size = Config.Const.C_Shape
    correction_reel = [[],[],[],[],[],[]]

    for x in [0]:
        if reel[x][1] in correction_sym and reel[x][2] != reel[x][1]:
            correction_col = reel[x][0:0+reel_size[x]]
            correction_reel[x] = correction_col

        elif reel[x][3] in correction_sym and reel[x][2] != reel[x][3]:
            correction_col = reel[x][2:2+reel_size[x]]
            correction_reel[x] = correction_col

        else:
            correction_reel[x] = reel[x][1:-1]

    for x in [1,2,3,4]:
        if reel[x][1] is Config.Scatter and reel[x][2] is not Config.Scatter:
            correction_col = reel[x][0:0+reel_size[x]]
            correction_reel[x] = correction_col

        elif reel[x][4] is Config.Scatter and reel[x][3] is not Config.Scatter:
            correction_col = reel[x][2:2+reel_size[x]]
            correction_reel[x] = correction_col

        else:
            correction_reel[x] = reel[x][1:-1]

    for x in [5]:
        if reel[x][1] in correction_sym and reel[x][2] != reel[x][1]:
            correction_col = reel[x][0:0+reel_size[x]]
            correction_reel[x] = correction_col

        elif reel[x][4] in correction_sym and reel[x][3] != reel[x][4]:
            correction_col = reel[x][2:2+reel_size[x]]
            correction_reel[x] = correction_col

        else:
            correction_reel[x] = reel[x][1:-1]




    return correction_reel

def get_win_pos(Lines):
    win_pos = [[],[],[],[],[],[]]
    for line in Lines:
        long = line[Const.R_Line_Long]
        for x in range(6):
            if x < long:
                for y in line[Const.R_Line_Pos][x]:
                    if y in win_pos[x]:
                        pass
                    else:
                        win_pos[x].append(y)

    return win_pos

def base_sym_attach_prize(reel):
    attach_prize = []

    for x in range(3):
        if reel[5][x:x+2] in [[Config.H1, Config.H1], [Config.H2, Config.H2], [Config.H3, Config.H3], [Config.H4, Config.H4], [Config.H5, Config.H5], [Config.H6, Config.H6]]:

            kind = reel[5][x]
            prize = Util.randlist(Config.Sym_Attach_Prize[kind][1])

            #列，图标种类，位置，奖励
            attach_prize.append([[5,kind,[x,x+1]],prize])

    return attach_prize

def attach_prize_judge(win_pos, attach_prize):
    hit_attach_prize = []
    for _list in attach_prize:
        col = _list[0][0]
        kind = _list[0][1]
        sym_pos = set(_list[0][2])
        sym_prize = _list[1]

        win_pos_col = set(win_pos[col])

        hit_pos = sym_pos.intersection(win_pos_col)

        if len(hit_pos) > 0:
            hit_attach_prize.append(_list)
    return hit_attach_prize

def wild_feature(reel):
    wild_num = Util.randlist(Config.Wild_Feature)
    blank_pos = []
    for x in range(len(reel)):
        for y in range(len(reel[x])):
            if reel[x][y] == Config.Blank:
                blank_pos.append([x,y])

    choose_pos = random.sample(blank_pos,wild_num)

    for pos in choose_pos:
        x = pos[0]
        y = pos[1]
        reel[x][y] = Config.E_Wild

    return reel

def free_sym_attach_prize(reel):
    attach_prize = []
    for x in range(1,5):
        for y in range(4):
            if reel[x][y] in [Config.H1, Config.H2, Config.H3, Config.H4, Config.H5, Config.H6]:
                _rand_num = random.random()
                if _rand_num < Config.Free_Attach_Prize_Pro:
                    kind = reel[x][y]
                    prize = Util.randlist(Config.Sym_Attach_Prize[kind][0])

                    #列，图标种类，位置，奖励
                    attach_prize.append([[x,kind,[y]],prize])

    for x in [5]:
        for y in range(3):
            if reel[x][y: y + 2] in [[Config.H1, Config.H1], [Config.H2, Config.H2], [Config.H3, Config.H3], [Config.H4, Config.H4], [Config.H5, Config.H5], [Config.H6, Config.H6]]:
                kind = reel[x][y]
                prize = Util.randlist(Config.Sym_Attach_Prize[kind][1])

                # 列，图标种类，位置，奖励
                attach_prize.append([[5, kind, [x, x + 1]], prize])

    return attach_prize



class WildFeatureWayEvaluator(Slot.WayLineEvaluator):

    def __init__(self, Paytable, Wild_Sub, LineSym, Wilds, Wild, totalbet, line_num, spinreel):
        super(WildFeatureWayEvaluator, self).__init__( Paytable, Wild_Sub, LineSym, Wilds, Wild, totalbet, line_num, spinreel)

    def wild_feature_check(self):
        sym_count = self.Symbol_Count()
        sym_count_check = []
        for sym_data in sym_count:
            sym_state = False
            sym_kind = sym_data[Const.R_Line_Kind]
            sym_pos = sym_data[Const.R_Line_Pos]
            sym_long = sym_data[Const.R_Line_Long]
            for x in range(len(sym_pos)):
                for y in sym_pos[x]:
                    if x < sym_long:
                        if self.spinreel[x][y] == sym_kind:
                            sym_state = True

            if sym_state == True:
                sym_count_check.append(sym_data)

        return sym_count_check

    def evaluate(self):
        sym_count = self.wild_feature_check()
        line_result = []
        win_amount = 0

        for v in sym_count:
            kind = v[Const.R_Line_Kind]
            long = v[Const.R_Line_Long]
            if long >= 1:
                basic_mul = self.Paytable[kind][long - 1]

                if basic_mul == 0:
                    pass

                else:
                    mul = basic_mul
                    for num in v[Const.R_Number_Count][:long]:
                        mul = mul * num

                    v[Const.R_Sym_Basic_Mul] = basic_mul
                    v[Const.R_Sym_Mul] = mul
                    v[Const.R_Sym_Win] = mul * self.line_bet

                    win_amount += mul * self.line_bet
                    line_result.append(v)

        return line_result, win_amount

