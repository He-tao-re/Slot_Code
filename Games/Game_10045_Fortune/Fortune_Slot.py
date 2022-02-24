import random
import copy
import json
import Games.Game_10045_Fortune.Fortune_Config as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import Games.Game_10045_Fortune.static_data_10045 as static_data


Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)

s_data = static_data.data


def scatter_count(reel):
    sc_num = 0
    sc_pos = []

    for x in range(len(reel)):
        for y in range(len(reel[x])):
            if reel[x][y] == Config.Scatter:
                sc_num += 1
                sc_pos.append([x,y])

    return sc_num,sc_pos

def jackpot_hit(sym_num):
    jackpot = None
    jackpot_mul = 0
    if sym_num in [5, 6, 7]:
        jackpot = Const.C_Mini
    elif sym_num in [8, 9]:
        jackpot = Const.C_Minor
    elif sym_num in [10, 11]:
        jackpot = Const.C_Major
    elif sym_num in [12]:
        jackpot = Const.C_Grand

    if jackpot is not None:
        jackpot_mul = Config.Const.C_Jackpot_Set[jackpot]

    return jackpot_mul

class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data

    def paidspin(self,totalbet):

        result = {}
        progress_List = GetProgress(Config.Base_Raise).game_progress()

        s_data[Const.S_Test_Time] += 1
        s_data[Const.S_Bet] += totalbet

        if len(progress_List) == 1:
            result,sc_num = self.normal_spin(totalbet)

            """统计部分"""

            s_data[Const.S_Base_Win] += result[Const.R_Win_Amount]

            s_data[Const.S_Win] += result[Const.R_Win_Amount]
            s_data[Const.S_Win] += result[Const.R_Jackpot_Win]


            if result[Const.R_Win_Amount] > 0:
                s_data[Const.S_Base_Hit] += 1

            if result[Const.R_Jackpot_Win] > 0:
                s_data[Const.S_Jackpot_Win] += result[Const.R_Jackpot_Win]
                s_data[Const.S_Jackpot_Hit] += 1


            if Const.R_Free in result.keys():
                s_data[Const.S_Free_Hit] += 1
                s_data[Const.S_Free_Win] += result[Const.R_Free_Win_Amount]

                s_data[Const.S_Win] += result[Const.R_Free_Win_Amount]

            for line in result[Const.R_Line]:
                kind = line[Const.R_Line_Kind]
                line_win = line[Const.R_Line_Win]
                line_long = line[Const.R_Line_Long]
                s_data[Const.S_Base_Sym_Win][kind][line_long-1] += line_win


        else:
            sc_num = 0

            s_data[Const.S_Feature_Hit] += 1
            # print(progress_List)

            for kind in progress_List:
                if kind in ["A_1","A_2","A_3"]:
                    result,s_num = self.normal_spin(totalbet)
                    sc_num += s_num

                    s_data[Const.S_Feature_Win] += result[Const.R_Win_Amount] + result[Const.R_Jackpot_Win]
                    s_data[Const.S_Win] += result[Const.R_Win_Amount] + result[Const.R_Jackpot_Win]

                elif kind in ["B_1","B_2","B_3"]:
                    result,s_num = self.raise_spin(totalbet)
                    sc_num += s_num

                    s_data[Const.S_Feature_Win] += result[Const.R_Win_Amount] + result[Const.R_Jackpot_Win]
                    s_data[Const.S_Win] += result[Const.R_Win_Amount] + result[Const.R_Jackpot_Win]


        if sc_num >= 3:
            freespins = 10 + (sc_num - 3) * 2
            FreeGame({}).free_progress(freespins,totalbet)

            s_data[Const.S_Free_Hit] += 1

        # print(json.dumps(result))
        return result

    def raise_spin(self,totalbet):

        result = {}
        reel_idx = 1
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        wild_reel = Util.randlist(Config.Base_Feature)
        for i in range(5):
            if wild_reel[i] == "1":
                reel[i] = [Config.Wild_2,Config.Wild_2,Config.Wild_2]


        jackpot_sym_num = Util.randlist(Config.Jackpot_Hit[reel_idx])

        result[Const.R_Jackpot_Win] = jackpot_hit(jackpot_sym_num) * totalbet

        result[Const.R_Reel] = reel


        self.special_sym_count(reel)


        #Scatter Win
        sc_num = len(self.self_data[Const.R_Scatter_Pos])
        if sc_num >= 1:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable, Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild).mul_wild_evaluate_2(2))
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result,sc_num

    def normal_spin(self,totalbet):

        result = {}
        reel_idx = 0
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        jackpot_sym_num = Util.randlist(Config.Jackpot_Hit[reel_idx])

        result[Const.R_Jackpot_Win] = jackpot_hit(jackpot_sym_num) * totalbet

        result[Const.R_Reel] = reel


        self.special_sym_count(reel)


        #Scatter Win
        sc_num = len(self.self_data[Const.R_Scatter_Pos])
        if sc_num >= 1:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable, Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild).mul_wild_evaluate_2(2))
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        # print(json.dumps(result))
        return result,sc_num






    def special_sym_count(self,reel):
        sc_pos = []
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                idx = y * 5 + x
                if reel[x][y] == Config.Scatter:
                    sc_pos.append([x,y])

        self.self_data[Const.R_Scatter_Pos] = sc_pos


class FreeGame(object):
    def __init__(self,self_data):
        self.self_data = self_data


    def raise_spin(self,totalbet):

        result = {}
        reel_idx = 3
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        wild_reel = Util.randlist(Config.Base_Feature)
        for i in range(5):
            if wild_reel[i] == "1":
                reel[i] = [Config.Wild_2,Config.Wild_2,Config.Wild_2]


        jackpot_sym_num = Util.randlist(Config.Jackpot_Hit[reel_idx])

        result[Const.R_Jackpot_Win] = jackpot_hit(jackpot_sym_num) * totalbet

        result[Const.R_Reel] = reel


        self.special_sym_count(reel)


        #Scatter Win
        sc_num = len(self.self_data[Const.R_Scatter_Pos])
        if sc_num >= 1:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable, Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild).mul_wild_evaluate_2(3))
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result,sc_num

    def normal_spin(self,totalbet):

        result = {}
        reel_idx = 2
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        jackpot_sym_num = Util.randlist(Config.Jackpot_Hit[reel_idx])

        result[Const.R_Jackpot_Win] = jackpot_hit(jackpot_sym_num) * totalbet

        result[Const.R_Reel] = reel


        self.special_sym_count(reel)


        #Scatter Win
        sc_num = len(self.self_data[Const.R_Scatter_Pos])
        if sc_num >= 1:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable, Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild).mul_wild_evaluate_2(3))
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        # print(json.dumps(result))
        return result,sc_num


    def free_progress(self,freespins,totalbet):

        while freespins > 0:
            freespins -= 1
            progress_List = GetProgress(Config.Free_Raise).game_progress()

            s_data[Const.S_FreeSpin] += 1

            sc_num = 0
            if len(progress_List) == 1:
                result,sc_num = self.normal_spin(totalbet)

                """统计部分"""

                s_data[Const.S_Free_Win] += result[Const.R_Win_Amount] + result[Const.R_Jackpot_Win]
                s_data[Const.S_Win] += result[Const.R_Win_Amount] + result[Const.R_Jackpot_Win]

            else:
                s_data[Const.S_Free_Feature_Hit] += 1
                # print(progress_List)

                for kind in progress_List:
                    if kind in ["A_1", "A_2", "A_3"]:
                        result, s_num = self.normal_spin(totalbet)
                        sc_num += s_num

                        s_data[Const.S_Free_Feature_Win] += result[Const.R_Win_Amount] + result[Const.R_Jackpot_Win]
                        s_data[Const.S_Win] += result[Const.R_Win_Amount] + result[Const.R_Jackpot_Win]

                    elif kind in ["B_1", "B_2", "B_3"]:
                        result, s_num = self.raise_spin(totalbet)
                        sc_num += s_num

                        s_data[Const.S_Free_Feature_Win] += result[Const.R_Win_Amount] + result[Const.R_Jackpot_Win]
                        s_data[Const.S_Win] += result[Const.R_Win_Amount] + result[Const.R_Jackpot_Win]




    def special_sym_count(self,reel):
        sc_pos = []
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                idx = y * 5 + x
                if reel[x][y] == Config.Scatter:
                    sc_pos.append([x,y])

        self.self_data[Const.R_Scatter_Pos] = sc_pos


class GetProgress(object):
    def __init__(self,pro_set):
        p1 = pro_set[0]
        p2 = pro_set[1]
        p3 = pro_set[2]
        self.p1_1 = p1[0]
        self.p2_1 = p2[0]
        self.p3_1 = p3[0]
        self.p1_2 = p1[1]
        self.p2_2 = p2[1]
        self.p3_2 = p3[1]

        self.reel_1_C = 0
        self.reel_2_C = 0
        self.reel_3_C = 0


    def reel_1(self):
        rand_num_1 = random.random()
        if self.reel_1_C == 0:

            p_1 = self.p1_1
        else:
            p_1 = self.p1_2
        self.reel_1_C += 1

        if rand_num_1 < p_1:
            return "A_1"
        else:
            return "B_1"

    def reel_2(self):
        rand_num_2 = random.random()

        if self.reel_2_C == 0:
            p_2 = self.p2_1
        else:
            p_2 = self.p2_2
        self.reel_2_C += 1

        if rand_num_2 < p_2:
            return "A_2"
        else:
            return "B_2"

    def reel_3(self):
        rand_num_3 = random.random()

        if self.reel_3_C == 0:
            p_3 = self.p3_1
        else:
            p_3 = self.p3_2
        self.reel_3_C += 1

        if rand_num_3 < p_3:
            return "A_3"
        else:
            return "B_3"

    def game_progress(self):
        active = True
        reel = 1

        progress_List = []
        while active:
            if reel == 1:
                r_1 = self.reel_1()
                if r_1 == "B_1":
                    reel = 2
                else:
                    reel = 1
                    active = False

                progress_List.append(r_1)

            elif reel == 2:
                r_2 = self.reel_2()
                if r_2 == "B_2":
                    reel = 3
                else:
                    reel = 1

                progress_List.append(r_2)

            elif reel == 3:
                r_3 = self.reel_3()
                if r_3 == "B_3":
                    reel = 3
                else:
                    reel = 2

                progress_List.append(r_3)

        return progress_List


