import random
import Games.Game_1028_Aladdin.Aladdin_config_100 as Config
import Games.Game_1028_Aladdin.static_data as static
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

import numpy as np

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)


def scatter_num(reel):
    sc_num = 0
    for x in range(5):
        if Config.Scatter in reel[x]:
            sc_num += 1
    return sc_num


def random_mark(self_data, judge_hit, judge_num):
    mark_num = np.sum(self_data[Const.R_Collect_Mark])

    x_random = random.random()

    if x_random < judge_hit[mark_num]:
        add_num = Util.randlist(judge_num)

        blank_pos = []
        for x in range(len(self_data[Const.R_Collect_Mark])):
            for y in range(len(self_data[Const.R_Collect_Mark][x])):
                if self_data[Const.R_Collect_Mark][x][y] == 0:
                    blank_pos.append([x,y])

        add_mark_pos = random.sample(blank_pos,add_num)

        for pos in add_mark_pos:
            x = pos[0]
            y = pos[1]
            self_data[Const.R_Collect_Mark][x][y] = 1

    return self_data




class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data


    def paidspin(self,totalbet):

        result = {}

        #判断随机增加标记
        self.self_data = random_mark(self.self_data,Config.Base_Mark_Add_Pro,Config.Base_Add_Num)
        self.self_data[Const.R_Spin_Process] += 1

        if self.self_data[Const.R_Spin_Process] < 10:

            reel = Slot.GetReel(Base_ReelSets[0], Config.Const.C_Shape).get_reel()
            result[Const.R_Reel] = reel
            for x in range(len(reel)):
                for y in range(len(reel[x])):
                    if reel[x][y] == Config.Wild:
                        self.self_data[Const.R_Collect_Mark][x][y] = 1

            result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                     Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                     Config.Wilds, Config.Wild).evaluate())
        else:

            reel = Slot.GetReel(Base_ReelSets[1], Config.Const.C_Shape).get_reel()
            result[Const.R_Reel] = reel
            for x in range(len(reel)):
                for y in range(len(reel[x])):
                    if reel[x][y] == Config.Wild:
                        self.self_data[Const.R_Collect_Mark][x][y] = 1



            self.self_data[Const.R_Spin_Process] = 0
            self.self_data[Const.C_Bonus_Prize] = {}
            wild_feature_reel = copy.deepcopy(reel)

            mark_pos = []
            for x in range(len(reel)):
                for y in range(len(reel[x])):
                    if self.self_data[Const.R_Collect_Mark][x][y] == 1:
                        mark_pos.append([x,y])


            bonus_num = Util.randlist(Config.Base_Mark_Change[len(mark_pos)])

            bonus_pos = random.sample(mark_pos,bonus_num)

            for pos in bonus_pos:
                x = pos[0]
                y = pos[1]
                idx = x + y * 5
                self.self_data[Const.C_Bonus_Prize][idx] = Util.randdict(Config.Prize_on_Bonus)

            for pos in mark_pos:
                if pos not in bonus_pos:
                    x = pos[0]
                    y = pos[1]
                    wild_feature_reel[x][y] = Config.Wild


            if len(self.self_data[Const.C_Bonus_Prize]) >= 6:
                result[Const.R_Respin], result[Const.R_Respin_Win], result[Const.R_Bonus_Num] = RespinFeature(self.self_data[Const.C_Bonus_Prize]).respin_game(totalbet)


            #重置标记
            self.self_data[Const.R_Collect_Mark] = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
            result.update(Slot.StandardLineEvaluator(totalbet,wild_feature_reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                     Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                     Config.Wilds, Config.Wild).evaluate())



        sc_num = scatter_num(reel)

        if sc_num >= 3:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0

        if sc_num >= 3:
            result[Const.R_Free],result[Const.R_Free_Win_Amount] = FreeGame().free_game(totalbet)



        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)



        return result


class FreeGame(object):
    def __init__(self):
        self.self_data = {
            Const.R_Spin_Process: 0,
            Const.R_Collect_Mark: [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
        }

    def freespin(self,totalbet):

        result = {}


        reel = Slot.GetReel(Free_ReelSets[0], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel

        #判断随机增加的标记
        self.self_data = random_mark(self.self_data, Config.Free_Mark_Add_Pro, Config.Free_Add_Num)

        #遍历 wild 信号，新增标记
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.Wild:
                    self.self_data[Const.R_Collect_Mark][x][y] = 1


        self.self_data[Const.C_Bonus_Prize] = {}
        wild_feature_reel = copy.deepcopy(reel)

        #统计标记数量，记录位置
        mark_pos = []
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if self.self_data[Const.R_Collect_Mark][x][y] == 1:
                    mark_pos.append([x, y])

        #按照表格，随机出bonus图标的数量，获得bonus图标的位置
        bonus_num = Util.randlist(Config.Free_Mark_Change[len(mark_pos)])
        bonus_pos = random.sample(mark_pos, bonus_num)

        #bonus图标的信息
        for pos in bonus_pos:
            x = pos[0]
            y = pos[1]
            idx = x + y * 5
            self.self_data[Const.C_Bonus_Prize][idx] = Util.randdict(Config.Prize_on_Bonus)

        #标记位置变为wild，排除bonus位置
        for pos in mark_pos:
            if pos not in bonus_pos:
                x = pos[0]
                y = pos[1]
                wild_feature_reel[x][y] = Config.Wild

        result.update(Slot.StandardLineEvaluator(totalbet,wild_feature_reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        static.free_line_win += result[Const.R_Win_Amount]

        if len(self.self_data[Const.C_Bonus_Prize]) >= 6:
            result[Const.R_Respin], result[Const.R_Respin_Win], result[Const.R_Bonus_Num] = RespinFeature(self.self_data[Const.C_Bonus_Prize]).respin_game(totalbet)

            result[Const.R_Win_Amount] += result[Const.R_Respin_Win]
            static.free_feature_hit += 1
            static.free_feature_win += result[Const.R_Respin_Win]
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result


    def free_game(self,totalbet):

        free = {}
        free_spins = 10
        free_recoder = 0
        free_win_amount = 0


        while free_spins > 0:
            free_spins -= 1
            free_recoder += 1

            free_result = self.freespin(totalbet)
            free_win_amount += free_result[Const.R_Win_Amount]
            free_result[Const.R_Free_Win_Amount] = copy.deepcopy(free_win_amount)


            free[free_recoder] = free_result

        return free,free_win_amount



class RespinFeature(object):
    def __init__(self, prize_on_bonus):
        self.prize_on_bonus = prize_on_bonus
        self.bonus_pro = {}
        self.bonus_reel = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]

    def feature_begin(self):

        for key, value in self.prize_on_bonus.items():
            x = key % 5
            y = key // 5
            self.bonus_reel[x][y] = 1

    def respin_game(self,totalbet):

        respin_result = {}

        self.feature_begin()


        respin_time = 3
        respin_recoder = 0
        while respin_time > 0:


            respin_time -= 1
            respin_recoder += 1
            blank_pos_idx = 0
            for x in range(len(self.bonus_reel)):
                for y in range(len(self.bonus_reel[x])):
                    if self.bonus_reel[x][y] == 0:
                        idx = y * 5 + x
                        if respin_recoder == 1:
                            self.bonus_pro[idx] = Config.Bonus_Pro[blank_pos_idx]
                            blank_pos_idx += 1


                        x_random = random.random()

                        if x_random < self.bonus_pro[idx]:
                            respin_time = 3
                            self.bonus_reel[x][y] = 1
                            self.prize_on_bonus[idx] = Util.randdict(Config.Prize_on_Bonus)


            respin_result[respin_recoder] = {Const.R_Respin_Reel: copy.deepcopy(self.bonus_reel), Const.R_Bonus_Award: copy.deepcopy(self.prize_on_bonus)}

        respin_mul = 0

        for k, v in self.prize_on_bonus.items():

            if v in Config.Const.C_Jackpot_Set.keys():

                respin_mul += Config.Const.C_Jackpot_Set[v] * totalbet
            else:
                respin_mul += v * totalbet

        bn_num = np.sum(self.bonus_reel)
        if bn_num == 20:
            respin_mul += Config.Const.C_Jackpot_Set[Const.C_Grand] * totalbet
        return respin_result,respin_mul,bn_num




