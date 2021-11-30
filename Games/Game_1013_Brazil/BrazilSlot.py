import random
import Games.Game_1013_Brazil.Brazil_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)
Super_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Super_ReelSets)


class GameSlot(object):
    def __init__(self, self_Data):
        self.self_data = self_Data

    def paidspin(self, totalbet):

        result = {}
        idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(Base_ReelSets[idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel
        sc_num = self.scatterwin(reel)

        self.bonus_prize(reel)

        if len(self.self_data[Const.R_Bonus]) >= 6:

            bonus_num = 0

            result[Const.R_Respin], bonus_reel = Respin().respin(reel,self.self_data[Const.R_Bonus])
            result[Const.R_Respin_Win] = 0
            for pos in bonus_reel:
                if pos['prize'] in Config.Const.C_Jackpot_Set.keys():
                    result[Const.R_Respin_Win] += Config.Const.C_Jackpot_Set[pos['prize']] * totalbet

                    if pos['prize'] in self.self_data[Const.R_Jackpot_Hit].keys():
                        self.self_data[Const.R_Jackpot_Hit][pos['prize']] += 1

                    if pos['prize'] != "Grand":
                        bonus_num += 1
                else:
                    result[Const.R_Respin_Win] += pos['prize'] * totalbet
                    bonus_num += 1
            result[Const.R_Bonus_Num] = bonus_num


        #Scatter Win

        if sc_num >= 3:
            self.self_data[Const.R_Collect_Data] += 1
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
            freespins = Config.FreeSpins[sc_num - 3]
            if self.self_data[Const.R_Collect_Data] % 10 != 0:
                result[Const.R_Free],result[Const.R_Free_Win_Amount] = self.free(totalbet,freespins)
            else:
                result[Const.R_Super_Free],result[Const.R_Free_Win_Amount] = self.super_free(totalbet, freespins)
        else:
            sc_win = 0


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result

    def free(self, totalbet, freespin):
        free = {}
        free_recoder = 0
        free_win_amount = 0

        while freespin > 0:
            freespin -= 1
            free_recoder += 1

            free_result = self.free_paidspin(totalbet)
            free_win_amount += free_result[Const.R_Win_Amount]


            free_result[Const.R_Free_Win_Amount] = free_win_amount
            free[free_recoder] = free_result


        return free,free_win_amount

    def super_free(self, totalbet, freespin):
        free = {}
        free_recoder = 0
        free_win_amount = 0

        wild_reel = [0, 0, 0, 0, 0]
        while freespin > 0:
            freespin -= 1
            free_recoder += 1

            free_result = self.super_paidspin(totalbet,wild_reel)
            free_win_amount += free_result[Const.R_Win_Amount]

            free_result[Const.R_Free_Win_Amount] = free_win_amount
            free[free_recoder] = free_result

        return free, free_win_amount


    def free_paidspin(self,totalbet):

        result = {}

        reel = Slot.GetReel(Free_ReelSets[0], Config.Const.C_Shape).get_reel()

        result[Const.R_Show_Reel] = reel
        act_reel = self.wildmove(reel)
        result[Const.R_Reel] = act_reel


        sc_num = self.scatterwin(reel)

        #Scatter Win
        if sc_num >= 3:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0


        result.update(Slot.StandardLineEvaluator(totalbet,act_reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result

    def super_paidspin(self, totalbet, wild_reel):

        result = {}

        reel = Slot.GetReel(Super_ReelSets[0], Config.Const.C_Shape).get_reel()

        result[Const.R_Show_Reel] = reel
        wild_reel = self.wild_count(reel,wild_reel)
        act_reel = self.wildmovestick(reel,wild_reel)
        result[Const.R_Reel] = act_reel

        sc_num = self.scatterwin(reel)


        # Scatter Win
        if sc_num >= 3:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num - 1]
        else:
            sc_win = 0

        result.update(Slot.StandardLineEvaluator(totalbet, act_reel, Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub,
                                                 Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result




    def scatterwin(self, reel):
        sc_num = 0
        for x in range(5):
            for y in range(3):
                if reel[x][y] == Config.Scatter:
                    sc_num += 1
        return sc_num


    def wildmove(self,reel):
        act_reel = copy.deepcopy(reel)
        for x in range(5):
            if Config.Wild in reel[x]:
                act_reel[x] = [Config.Wild,Config.Wild,Config.Wild]
        return act_reel

    def wild_count(self, reel, wild_reel):
        for x in range(5):
            if Config.Wild in reel[x]:
                wild_reel[x] = 1
            else:
                pass
        return wild_reel

    def wildmovestick(self,reel,wild_reel):
        act_reel = copy.deepcopy(reel)
        for x in range(5):
            if wild_reel[x] == 1:
                act_reel[x] = [Config.Wild,Config.Wild,Config.Wild]
        return act_reel

    def bonus_prize(self,reel):
        self.self_data[Const.R_Bonus] = []
        for x in range(5):
            for y in range(3):
                if reel[x][y] == Config.Bonus:
                    idx = x + y*5
                    prize = Util.randdict(Config.Prize_on_Bonus)
                    self.self_data[Const.R_Bonus].append({"idx": idx, "prize": prize})



class Respin(object):


    def allocate_pro(self,reel,pro):
        blank_pos = []

        pos_pro = []
        for x in range(5):
            for y in range(3):
                if reel[x][y] != Config.Bonus:
                    idx = x + y*5
                    blank_pos.append(idx)

        random.shuffle(blank_pos)
        pro_i = 0
        for pos in blank_pos:
            pos_pro.append({"idx": pos, "pro": pro[pro_i]})
            pro_i += 1

        return pos_pro

    def respin(self,reel,bonus_reel):
        respin = {}
        respin_recoder = 0
        respin_times = 3

        blank_pos = self.allocate_pro(reel,Config.Respin_Pro)

        active = True

        while active:

            respin_times -= 1
            respin_recoder += 1

            for pos in blank_pos:

                ra = random.random()
                if ra < pos['pro']:
                    prize = Util.randdict(Config.Prize_on_Bonus)
                    idx = pos['idx']
                    bonus_reel.append({"idx": idx, "prize": prize})

                    blank_pos.remove(pos)
                    respin_times = 3

            if len(blank_pos) == 0:
                bonus_reel.append({"idx": -1, "prize": "Grand"})
                active = False

            if respin_times == 0:
                active = False

            respin[respin_recoder] = {Const.R_Respin_Times: respin_times, Const.R_Respin_Reel: bonus_reel}

        return respin, bonus_reel
