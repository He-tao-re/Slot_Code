import random
import Games.Game_1032_Bingo.Bingo_config as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import Games.Game_1032_Bingo.static_data_1032 as static_data
import copy

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)

def get_initial_bonus_prize():
    bonus_prize = {}
    initial_num = Util.randlist(Config.Initial_Num_Weight)
    pos_list = random.sample([0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24],initial_num)

    bonus_prize[pos_list[0]] = Util.randdict(Config.Const.C_Bonus_Set[Const.R_Bonus_Initial_Prize])

    for pos_idx in pos_list[1:]:
        bonus_prize[pos_idx] = Util.randdict(Config.Const.C_Bonus_Set[Const.R_Bonus_Initial_Prize])
    return bonus_prize

def get_bonus_prize(reel):
    bonus_prize = {}
    for x in range(5):
        for y in range(5):
            idx = x * 5 + y
            if reel[x][y] == Config.Bonus:
                bonus_prize[idx] = Util.randdict(Config.Const.C_Bonus_Set[Const.C_Bonus_Prize])
    return bonus_prize

def judge_bingo_hit(self_data):
    bingo_line = [
        [0,1,2,3,4],
        [5,6,7,8,9],
        [10,11,12,13,14],
        [15,16,17,18,19],
        [20,21,22,23,24],
        [0,5,10,15,20],
        [1,6,11,16,21],
        [2,7,12,17,22],
        [3,8,13,18,23],
        [4,9,14,19,24],
        [0,6,12,18,24],
        [4,8,12,16,20]
    ]
    hit_pos = []
    for line in bingo_line:
        num_count = 0
        for x in range(5):
            if len(self_data[Const.R_Bingo_Data][line[x]]) > 0:
                num_count += 1
        if num_count == 5:
            hit_pos += line
    return hit_pos

def scatter_count(reel):
    sc_num = 0
    for x in range(5):
        if Config.Scatter in reel[x]:
            sc_num += 1
    return sc_num

def get_reel(ReelSet):
    ReelStrip = ReelSet[Const.C_ReelStrip]
    reel = []

    r1 = [Util.randlist(ReelStrip[0]),Util.randlist(ReelStrip[0]),Util.randlist(ReelStrip[0]),Util.randlist(ReelStrip[5]),Util.randlist(ReelStrip[10])]
    r2 = [Util.randlist(ReelStrip[1]),Util.randlist(ReelStrip[1]),Util.randlist(ReelStrip[1]),Util.randlist(ReelStrip[6]),Util.randlist(ReelStrip[11])]
    r3 = [Util.randlist(ReelStrip[2]),Util.randlist(ReelStrip[2]),Util.randlist(ReelStrip[7]),Util.randlist(ReelStrip[12])]
    r4 = [Util.randlist(ReelStrip[3]),Util.randlist(ReelStrip[3]),Util.randlist(ReelStrip[3]),Util.randlist(ReelStrip[8]),Util.randlist(ReelStrip[13])]
    r5 = [Util.randlist(ReelStrip[4]),Util.randlist(ReelStrip[4]),Util.randlist(ReelStrip[4]),Util.randlist(ReelStrip[9]),Util.randlist(ReelStrip[14])]
    random.shuffle(r1)
    random.shuffle(r2)
    random.shuffle(r3)
    random.shuffle(r4)
    random.shuffle(r5)
    r3.insert(2,Config.Wild)
    reel.append(r1)
    reel.append(r2)
    reel.append(r3)
    reel.append(r4)
    reel.append(r5)

    return reel

class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data

    def paidspin(self,totalbet):
        static_data.data['test_time'] += 1
        static_data.data['all_bet'] += totalbet

        result = {}

        if self.self_data[Const.R_Bingo_Status] is False:
            initial_bonus_prize = get_initial_bonus_prize()

            for idx in initial_bonus_prize.keys():
                self.self_data[Const.R_Bingo_Data][idx].append(initial_bonus_prize[idx])

            self.self_data[Const.R_Bingo_Status] = True

        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = get_reel(Base_ReelSets[reel_idx])

        result[Const.R_Reel] = reel

        sc_num = scatter_count(reel)

        bonus_prize = get_bonus_prize(reel)
        for idx in bonus_prize.keys():
            self.self_data[Const.R_Bingo_Data][idx].append(bonus_prize[idx])
            static_data.data['base_bonus_num'] += 1

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        bingo_hit_pos = judge_bingo_hit(self.self_data)

        result[Const.R_Bingo_Win] = 0

        if len(bingo_hit_pos) > 0:
            static_data.data['bingo_hit'] += 1
            for pos_idx in bingo_hit_pos:
                if pos_idx == 12:
                    result[Const.R_Wheel_Win] = Util.randdict(Config.Const.C_Bonus_Set[Const.R_Wheel_Prize]) * totalbet

                    static_data.data['base_wheel_hit'] += 1
                    static_data.data['base_wheel_win'] += result[Const.R_Wheel_Win]
                    result[Const.R_Bingo_Win] += result[Const.R_Wheel_Win]
                else:
                    for award in self.self_data[Const.R_Bingo_Data][pos_idx]:
                        result[Const.R_Bingo_Win] += award * totalbet


            static_data.data['bingo_win'] += result[Const.R_Bingo_Win]
            static_data.data['all_win'] += result[Const.R_Bingo_Win]
            self.self_data[Const.R_Bingo_Data] = {0: [],1: [],2: [],3: [],4: [],5: [],6: [],7: [],8: [],9: [],10: [],11: [],12: [Const.R_Wheel],13: [],14: [],15: [],16: [],17: [],18: [],19: [],20: [],21: [],22: [],23: [],24: []}
            self.self_data[Const.R_Bingo_Status] = False

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

        static_data.data['base_win'] += result[Const.R_Win_Amount]
        static_data.data['all_win'] += result[Const.R_Win_Amount]
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        if result[Const.R_Win_Amount] > 0:
            static_data.data['base_hit'] += 1


        if sc_num >= 3:
            static_data.data['free_hit'] += 1
            if sc_num == 3:
                freespins = 8
            elif sc_num == 4:
                freespins = 16
            elif sc_num == 5:
                freespins = 24
            else:
                freespins = 0

            free_type = Config.Free_Type[static_data.data['free_hit'] % 18 - 1]
            result[Const.R_Free],self.self_data = FreeGame(free_type,self.self_data).free_game(freespins,totalbet)

        return result,self.self_data

class FreeGame(object):
    def __init__(self,free_type,self_data):
        self.free_type = free_type
        self.self_data = self_data

    def free_spin(self,totalbet):

        static_data.data['free_spin_times'] += 1
        result = {}
        re_hit = 0
        if self.self_data[Const.R_Bingo_Status] is False:
            initial_bonus_prize = get_initial_bonus_prize()

            for idx in initial_bonus_prize.keys():
                self.self_data[Const.R_Bingo_Data][idx].append(initial_bonus_prize[idx])

            self.self_data[Const.R_Bingo_Status] = True



        reel = get_reel(Base_ReelSets[self.free_type])

        result[Const.R_Reel] = reel


        sc_num = scatter_count(reel)

        bonus_prize = get_bonus_prize(reel)
        for idx in bonus_prize.keys():
            if self.free_type == 1:
                self.self_data[Const.R_Bingo_Data][idx].append(bonus_prize[idx])

            elif self.free_type == 2:
                for around_idx in [idx,idx + 1,idx - 1, idx + 5, idx - 5]:
                    if around_idx in range(25) and around_idx != 12:
                        self.self_data[Const.R_Bingo_Data][around_idx].append(bonus_prize[idx])

            elif self.free_type == 3:
                for around_idx in [idx,idx + 1,idx - 1, idx + 5, idx - 5, idx + 4, idx - 4, idx + 6, idx - 6]:
                    if around_idx in range(25) and around_idx != 12:
                        self.self_data[Const.R_Bingo_Data][around_idx].append(bonus_prize[idx])



        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        bingo_hit_pos = judge_bingo_hit(self.self_data)

        result[Const.R_Bingo_Win] = 0

        if len(bingo_hit_pos) > 0:
            static_data.data['free_bingo_hit'] += 1

            for pos_idx in bingo_hit_pos:
                if pos_idx == 12:
                    result[Const.R_Wheel_Win] = Util.randdict(Config.Const.C_Bonus_Set[Const.R_Wheel_Prize]) * totalbet

                    static_data.data['free_wheel_hit'] += 1
                    static_data.data['free_wheel_win'] += result[Const.R_Wheel_Win]

                    result[Const.R_Bingo_Win] += result[Const.R_Wheel_Win]
                else:
                    for award in self.self_data[Const.R_Bingo_Data][pos_idx]:
                        result[Const.R_Bingo_Win] += award * totalbet



            static_data.data['free_bingo_win'] += result[Const.R_Bingo_Win]
            static_data.data['all_win'] += result[Const.R_Bingo_Win]

            self.self_data[Const.R_Bingo_Data] = {0: [],1: [],2: [],3: [],4: [],5: [],6: [],7: [],8: [],9: [],10: [],11: [],12: [Const.R_Wheel],13: [],14: [],15: [],16: [],17: [],18: [],19: [],20: [],21: [],22: [],23: [],24: []}
            self.self_data[Const.R_Bingo_Status] = False


        #Scatter Win

        if sc_num >= 2:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable, Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win

        static_data.data['free_win'] += result[Const.R_Win_Amount]
        static_data.data['free_win'] += result[Const.R_Scatter_Win]

        static_data.data['all_win'] += result[Const.R_Win_Amount]
        static_data.data['all_win'] += result[Const.R_Scatter_Win]

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        if sc_num >= 3:
            if sc_num == 3:
                re_hit = 8
            elif sc_num == 4:
                re_hit = 16
            elif sc_num == 5:
                re_hit = 24

        return result,re_hit

    def free_game(self,free_spins,totalbet):

        Free = {}
        free_recoder = 0
        free_win_amount = 0

        while free_spins > 0:

            free_spins -= 1
            free_recoder += 1
            free_result,re_hit = self.free_spin(totalbet)

            free_spins += re_hit

            free_win_amount += free_result[Const.R_Win_Amount]
            free_result[Const.R_Free_Win_Amount] = free_win_amount

            Free[free_recoder] = copy.deepcopy(free_result)

        return Free,self.self_data


