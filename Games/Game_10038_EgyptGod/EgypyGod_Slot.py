import Games.Game_10038_EgyptGod.EgypyGod_Config as Config
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
    def __init__(self, game_data,self_data):

        self.game_data = game_data
        self.self_data = self_data
        self.spin_state = game_data[Const.R_Spin_Type]

        self.game_data[Const.R_Feature_Hit] = []

    def spin(self,totalbet):

        if self.spin_state == Const.R_Base_Type:

            '''重新初始化'''
            self.game_data = {
                Const.R_Spin_Type: Const.R_Base_Type,
                Const.R_Feature_Hit:[],
            }
            self.self_data = {
                Const.R_Next_Spin: Const.R_Base_Type,
            }

            result = self.base_spin(totalbet)

            return result, self.self_data

        elif self.spin_state == Const.R_Respin_Type:
            result = self.respin(totalbet)

            return result, self.self_data

        elif self.spin_state == Const.R_Free_Type:
            result = self.free_spin(totalbet)

            return result, self.self_data

        elif self.spin_state == Const.R_Free_Respin_Type:
            result = self.free_respin(totalbet)

            return result, self.self_data


    def base_spin(self,totalbet):

        reel_idx = 0
        reel = Slot.GetReel(ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result = {Const.R_Spin_Type: Const.R_Base_Type}
        result[Const.R_Reel] = reel

        if respin_hit_check(reel,Config.Base_Respin_H1) == False:

            result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                     Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                     Config.Wilds, Config.Wild).evaluate())
            sc_num,sc_ifo = scatter_count(reel)
            sc_win = 0

            if sc_num >= 3:
                sc_win = Config.Const.C_Paytable[Config.Scatter][sc_num - 1] * totalbet
                freespins = sum(sc_ifo)
                self.game_data[Const.R_Feature_Hit].append(Const.R_Free)

                #下一次spin转为free类型
                self.self_data[Const.R_Next_Spin] = Const.R_Free_Type

                self.game_data[Const.R_Free_Spins] = freespins
                self.game_data[Const.R_Free_Spin_Left] = freespins
                self.game_data[Const.R_Feature_Ifo] = sc_ifo

                self.game_data[Const.R_Free_Win_Amount] = 0


            result[Const.R_Scatter_Win] = sc_win
            result[Const.R_Win_Amount] += sc_win

            result[Const.R_Game_Data] = copy.deepcopy(self.game_data)


        else:
            result[Const.R_Line_WinAmount] = 0
            result[Const.R_Win_Amount] = 0
            result[Const.R_Scatter_Win] = 0

            self.game_data[Const.R_Feature_Hit].append(Const.R_Respin)

            # 下一次spin转为respin类型
            self.self_data[Const.R_Next_Spin] = Const.R_Respin_Type

            self.game_data[Const.R_Respin_Total_Time] = 3
            self.game_data[Const.R_Respin_Times] = 0
            self.game_data["Score_Prize"] = {}
            self.game_data["204_Prize"] = {}
            self.game_data[Const.R_Respin_Win] = 0

            pro_set_Idx = Util.randlist(Config.Const.C_Game_Set['Respin_Pro_Set_Choose'])

            pro_set = Config.Const.C_Game_Set['Respin_Pro_Set'][pro_set_Idx]

            self.self_data["pro_set"] = pro_set
            self.self_data["power_up_pool"] = copy.deepcopy(Game_Set["Power_UP_Pool"])
            random.shuffle(self.self_data["power_up_pool"])

            self.self_data[Const.R_Respin_Reel] = initialize_respin_reel()
            result[Const.R_Game_Data] = copy.deepcopy(self.game_data)

        return result

    def free_spin(self,totalbet):

        # free 计次
        self.game_data[Const.R_Free_Spin_Left] -= 1

        reel_idx = 1
        reel = Slot.GetReel(ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result = {Const.R_Spin_Type: Const.R_Free_Type}
        result[Const.R_Reel] = reel

        if respin_hit_check(reel, Config.Free_Respin_H1) == False:

            result.update(Slot.StandardLineEvaluator(totalbet, reel, Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                     Config.Const.C_BetLine, Config.Const.C_Wild_Sub,
                                                     Config.Const.C_LineSym,
                                                     Config.Wilds, Config.Wild).evaluate())


            sc_num, sc_ifo = scatter_count(reel)
            sc_win = 0

            if sc_num >= 3:
                sc_win = Config.Const.C_Paytable[Config.Scatter][sc_num - 1] * totalbet
                freespins = sum(sc_ifo)
                self.game_data[Const.R_Feature_Hit].append(Const.R_Free)

                # 下一次spin转为free类型
                self.self_data[Const.R_Next_Spin] = Const.R_Free_Type

                self.game_data[Const.R_Free_Spins] += freespins
                self.game_data[Const.R_Free_Spin_Left] += freespins
                self.game_data[Const.R_Feature_Ifo] = sc_ifo


            result[Const.R_Scatter_Win] = sc_win
            result[Const.R_Win_Amount] += sc_win

            self.game_data[Const.R_Free_Win_Amount] += result[Const.R_Win_Amount]

            result[Const.R_Game_Data] = copy.deepcopy(self.game_data)


        else:
            result[Const.R_Line_WinAmount] = 0
            result[Const.R_Win_Amount] = 0
            result[Const.R_Scatter_Win] = 0

            self.game_data[Const.R_Feature_Hit].append(Const.R_Respin)

            # 下一次spin转为respin类型
            self.self_data[Const.R_Next_Spin] = Const.R_Free_Respin_Type

            self.game_data[Const.R_Respin_Total_Time] = 3
            self.game_data[Const.R_Respin_Times] = 0
            self.game_data["Score_Prize"] = {}
            self.game_data["204_Prize"] = {}
            self.game_data[Const.R_Respin_Win] = 0

            pro_set_Idx = Util.randlist(Config.Const.C_Game_Set['Respin_Pro_Set_Choose'])

            pro_set = Config.Const.C_Game_Set['Respin_Pro_Set'][pro_set_Idx]

            self.self_data["pro_set"] = pro_set
            self.self_data["power_up_pool"] = copy.deepcopy(Game_Set["Power_UP_Pool"])
            random.shuffle(self.self_data["power_up_pool"])

            self.self_data[Const.R_Respin_Reel] = initialize_respin_reel()
            result[Const.R_Game_Data] = copy.deepcopy(self.game_data)

        # print(self.game_data[Const.R_Free_Spin_Left])
        if self.game_data[Const.R_Free_Spin_Left] == 0:
            self.self_data[Const.R_Next_Spin] = Const.R_Base_Type


        return result

    def respin(self,totalbet):

        pro_group_idx = copy.deepcopy(self.game_data[Const.R_Respin_Times])
        self.game_data[Const.R_Respin_Times] += 1

        result = {Const.R_Spin_Type: Const.R_Respin_Type}
        reel = self.self_data[Const.R_Respin_Reel]

        if pro_group_idx >= 8:
            pro_group_idx = 7

        pro_group = self.self_data["pro_set"][0][pro_group_idx]
        power_up_pro = self.self_data["pro_set"][1]

        blank_pos = screen_blank(reel)
        pro_list = allocate_pro(blank_pos,pro_group)

        add_respin = False
        power_up_list = []
        for pos_pro in pro_list:
            _rand_1 = random.random()

            if _rand_1 < pos_pro[1]:
                x = pos_pro[0][0]
                y = pos_pro[0][1]

                _rand_2 = random.random()
                if _rand_2 < power_up_pro:
                    try:
                        power_sym = self.self_data["power_up_pool"].pop()
                    except IndexError:
                        power_sym = 204
                    reel[x][y] = power_sym

                    add_respin = True
                    power_up_list.append([[x,y,power_sym]])
                else:
                    reel[x][y] = Config.H1

                    add_respin = True

        if add_respin is True:
            self.game_data[Const.R_Respin_Total_Time] += 1

        power_up_list.sort()
        #从左往右生效Power Up
        for power_up in power_up_list:
            x = power_up[0][0]
            y = power_up[0][1]

            reel,score_prize,mul_prize = power_up_effect(reel[x][y],[x,y],reel)

            if len(score_prize.keys()) > 0:
                self.game_data["Score_Prize"].update(score_prize)
            if len(mul_prize) > 0:
                self.game_data["204_Prize"].update(mul_prize)

        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.H1 and str([x,y]) in self.game_data["Score_Prize"].keys():
                    self.game_data[Const.R_Respin_Win] += totalbet / Config.Const.C_BetLine * self.game_data["Score_Prize"][str([x,y])]

                    del self.game_data["Score_Prize"][str([x,y])]





        result[Const.R_Reel] = reel
        result[Const.R_Win_Amount] = 0

        self.self_data[Const.R_Respin_Reel] = reel

        if self.game_data[Const.R_Respin_Times] == self.game_data[Const.R_Respin_Total_Time]:

            #下一次spin类型转为base

            self.self_data[Const.R_Next_Spin] = Const.R_Base_Type

            cal_reel = copy.deepcopy(reel)

            for x in range(len(reel)):
                for y in range(len(reel[x])):
                    if reel[x][y] in [201,202,203,204]:
                        cal_reel[x][y] = Config.H1


            if len(reel[0]) == 9:
                Payline = Config.Payline_70
            elif len(reel[0]) == 10:
                Payline = Config.Payline_80
            else:
                Payline = Config.Const.C_PayLine



            result.update(Slot.StandardLineEvaluator(totalbet,cal_reel,Payline, Config.Const.C_Paytable,
                                                     Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                     Config.Wilds, Config.Wild).evaluate())

            self.game_data[Const.R_Respin_Win] += result[Const.R_Win_Amount]
            for power_204 in self.game_data["204_Prize"].values():
                for prize in power_204:
                    if prize not in [Const.C_Grand, Const.C_Mega, Config.Major, Const.C_Minor, Const.C_Mini]:
                        self.game_data[Const.R_Respin_Win] += prize * totalbet
                    else:
                        self.game_data[Const.R_Respin_Win] += Config.Const.C_Jackpot_Set[prize] * totalbet


        result[Const.R_Game_Data]  = copy.deepcopy(self.game_data)

        return result

    def free_respin(self,totalbet):

        pro_group_idx = copy.deepcopy(self.game_data[Const.R_Respin_Times])
        self.game_data[Const.R_Respin_Times] += 1

        result = {Const.R_Spin_Type: Const.R_Free_Respin_Type}
        reel = self.self_data[Const.R_Respin_Reel]

        if pro_group_idx >= 8:
            pro_group_idx = 7

        pro_group = self.self_data["pro_set"][0][pro_group_idx]
        power_up_pro = self.self_data["pro_set"][1]

        blank_pos = screen_blank(reel)
        pro_list = allocate_pro(blank_pos,pro_group)

        add_respin = False
        power_up_list = []
        for pos_pro in pro_list:
            _rand_1 = random.random()

            if _rand_1 < pos_pro[1]:
                x = pos_pro[0][0]
                y = pos_pro[0][1]

                _rand_2 = random.random()
                if _rand_2 < power_up_pro:
                    try:
                        power_sym = self.self_data["power_up_pool"].pop()
                    except IndexError:
                        power_sym = 204
                    reel[x][y] = power_sym

                    add_respin = True
                    power_up_list.append([[x,y,power_sym]])
                else:
                    reel[x][y] = Config.H1

                    add_respin = True

        if add_respin is True:
            self.game_data[Const.R_Respin_Total_Time] += 1

        power_up_list.sort()
        #从左往右生效Power Up
        for power_up in power_up_list:
            x = power_up[0][0]
            y = power_up[0][1]

            reel,score_prize,mul_prize = power_up_effect(reel[x][y],[x,y],reel)

            if len(score_prize.keys()) > 0:
                self.game_data["Score_Prize"].update(score_prize)
            if len(mul_prize) > 0:
                self.game_data["204_Prize"].update(mul_prize)

        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.H1 and str([x,y]) in self.game_data["Score_Prize"].keys():
                    self.game_data[Const.R_Respin_Win] += totalbet / Config.Const.C_BetLine * self.game_data["Score_Prize"][str([x,y])]

                    del self.game_data["Score_Prize"][str([x,y])]





        result[Const.R_Reel] = reel
        result[Const.R_Win_Amount] = 0

        self.self_data[Const.R_Respin_Reel] = reel

        if self.game_data[Const.R_Respin_Times] == self.game_data[Const.R_Respin_Total_Time]:

            #下一次spin类型转为base
            if self.game_data[Const.R_Free_Spin_Left] == 0:
                self.self_data[Const.R_Next_Spin] = Const.R_Base_Type
            else:
                self.self_data[Const.R_Next_Spin] = Const.R_Free_Type

            cal_reel = copy.deepcopy(reel)

            for x in range(len(reel)):
                for y in range(len(reel[x])):
                    if reel[x][y] in [201,202,203,204]:
                        cal_reel[x][y] = Config.H1


            if len(reel[0]) == 9:
                Payline = Config.Payline_70
            elif len(reel[0]) == 10:
                Payline = Config.Payline_80
            else:
                Payline = Config.Const.C_PayLine



            result.update(Slot.StandardLineEvaluator(totalbet,cal_reel,Payline, Config.Const.C_Paytable,
                                                     Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                     Config.Wilds, Config.Wild).evaluate())

            self.game_data[Const.R_Respin_Win] += result[Const.R_Win_Amount]
            for power_204 in self.game_data["204_Prize"].values():
                for prize in power_204:
                    if prize not in [Const.C_Grand, Const.C_Mega, Config.Major, Const.C_Minor, Const.C_Mini]:
                        self.game_data[Const.R_Respin_Win] += prize * totalbet
                    else:
                        self.game_data[Const.R_Respin_Win] += Config.Const.C_Jackpot_Set[prize] * totalbet


        result[Const.R_Game_Data]  = copy.deepcopy(self.game_data)

        return result




def scatter_count(reel):
    scatter_num = 0
    scatter_inf = []
    for x in range(len(reel)):
        if reel[x].count(Config.Scatter) > 0:
            scatter_num += 1

    if scatter_num >= 3:
        for i in range(scatter_num*3):
            scatter_inf.append(Util.randlist(Const.C_Game_Set['SC_Freespin']))

    return scatter_num,scatter_inf

def respin_hit_check(reel,num):
    respin_hit = False
    if reel[0].count(Config.H1) >= num:
        respin_hit = True
    return respin_hit

def initialize_respin_reel():
    respin_reel = [
        [Config.H1,Config.H1,Config.H1,Config.H1,Config.H1,Config.H1,Config.H1,Config.H1],
        [Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank],
        [Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank],
        [Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank],
        [Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank,Config.Respin_Blank],
    ]
    return respin_reel

def screen_blank(reel):
    blank_pos = []
    for x in range(len(reel)):
        for y in range(len(reel[x])):
            if reel[x][y] == Config.Respin_Blank:
                blank_pos.append([x,y])
    random.shuffle(blank_pos)
    return blank_pos

def allocate_pro(blank_pos,pro_group):
    pro_list = []
    t1 = pro_group[0][1]
    t2 = pro_group[1][1]
    pos_num = t1 + t2

    # pro type 1
    for pos in blank_pos[0:t1]:

        pro_list.append([pos,pro_group[0][0]])

    # pro type 2
    for pos in blank_pos[t1:t1+t2]:

        pro_list.append([pos,pro_group[1][0]])

    return pro_list

def power_up_effect(power_kind,power_local,reel):
    reel = copy.deepcopy(reel)
    score_prize = {}
    mul_prize = {}
    if power_kind == 201:
        for x in range(len(reel)):
            reel[x].append(Config.H1)
    elif power_kind == 202:
        x = power_local[0]
        y = power_local[1]

        for pos in [[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]:
            try:
                reel[pos[0]][pos[1]] = Config.H1
            except IndexError:
                pass
    elif power_kind == 203:
        score_num = Util.randlist(Game_Set['203_pick_num'])
        blank_pos = screen_blank(reel)
        try:
            choose_pos = random.sample(blank_pos,score_num)
        except ValueError:
            choose_pos = random.sample(blank_pos,len(blank_pos))
        for pos in choose_pos:
            score = Util.randlist(Game_Set["203_prize"])
            score_prize[str(pos)] = score

    elif power_kind == 204:
        prize_1 = Util.randlist(Game_Set["204_Weight_1"])
        prize_2 = Util.randlist(Game_Set["204_Weight_2"])

        x = power_local[0]
        y = power_local[1]
        # reel[x][y] = Config.H1
        mul_prize[str([x,y])] = [prize_1,prize_2]

    return reel,score_prize,mul_prize