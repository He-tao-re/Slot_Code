import random
import Games.Game_1005_American.American_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)

class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data

    def paidspin(self,totalbet,bet_id):

        result = {Const.R_Bet_ID: bet_id}
        if bet_id == 1:
            extra_reel_idx = random.randint(0,len(Config.Const.R_Base_Extra_Reel))
            self.self_data = {Const.R_Extra_Reel_Idx: extra_reel_idx}

            long_extra_reel = Config.Const.R_Base_Extra_Reel + Config.Const.R_Base_Extra_Reel[:5]

            extra_reel = []
            for x in range(extra_reel_idx,extra_reel_idx + 5):
                if long_extra_reel[x] == 1:
                    prize = Util.randdict(Config.Extra_Reel_Prize)
                    extra_reel.append(prize)
                else:
                    extra_reel.append(0)
            self.self_data[Const.R_Extra_Reel] = extra_reel

        else:
            self.self_data[Const.R_Extra_Reel_Idx] += 1
            if self.self_data[Const.R_Extra_Reel_Idx] > len(Config.Const.R_Base_Extra_Reel):
                self.self_data[Const.R_Extra_Reel_Idx] = 0


            long_extra_reel = Config.Const.R_Base_Extra_Reel + Config.Const.R_Base_Extra_Reel[:15]

            if long_extra_reel[self.self_data[Const.R_Extra_Reel_Idx]+5] == 1:
                prize = Util.randdict(Config.Extra_Reel_Prize)
                extra_reel = self.self_data[Const.R_Extra_Reel][1:]
                extra_reel.append(prize)
                self.self_data[Const.R_Extra_Reel] = extra_reel
            else:
                extra_reel = self.self_data[Const.R_Extra_Reel][1:]
                extra_reel.append(0)
                self.self_data[Const.R_Extra_Reel] = extra_reel


        reel = Slot.GetReel(Base_ReelSets[0], Config.Const.C_Shape).get_reel()

        extra_reel_hit = []
        for x in range(5):
            if Config.Scatter in reel[x]:
                extra_reel_hit.append(self.self_data[Const.R_Extra_Reel][x])

        extra_win_mul = 0
        free_hit = 0
        for y in extra_reel_hit:
            if y != 0:
                if y in Config.Const.C_Jackpot_Set.keys():
                    extra_win_mul += Config.Const.C_Jackpot_Set[y]
                else:
                    extra_win_mul += y
            else:
                free_hit += 1


        result[Const.R_Reel] = reel


        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Extra_Win] = extra_win_mul * totalbet

        if free_hit > 0:
            freespins = free_hit * 10
            result[Const.R_Free], free_win_amount, free_extra_win_amount = self.freegame(freespins,totalbet)
            result[Const.R_Free_Win_Amount] = free_win_amount*2 + free_extra_win_amount
        return result



    def freegame(self,freespin,totalbet):
        free = {}
        free_recoder = 0
        free_win_amount = 0
        free_extra_win_amount = 0

        self_data = {}
        while freespin > 0:
            freespin -= 1
            free_recoder += 1

            result,free_hit = FreeGame(self_data).freespin(totalbet,free_recoder)
            self_data = result[Const.R_Self_Data]

            free[free_recoder] = result

            free_win_amount += result[Const.R_Win_Amount]
            free_extra_win_amount += result[Const.R_Extra_Win]

            if free_hit > 0:
                freespin += free_hit * 2

        return free,free_win_amount,free_extra_win_amount




class FreeGame(object):
    def __init__(self,self_data):
        self.self_data = self_data


    def freespin(self,totalbet,bet_id):

        result = {Const.R_Bet_ID: bet_id}
        if bet_id == 1:
            extra_reel_idx = random.randint(0,len(Config.Const.R_Free_Extra_Reel))
            self.self_data = {Const.R_Extra_Reel_Idx: extra_reel_idx}

            long_extra_reel = Config.Const.R_Free_Extra_Reel + Config.Const.R_Free_Extra_Reel[:5]

            extra_reel = []
            for x in range(extra_reel_idx,extra_reel_idx + 5):
                if long_extra_reel[x] == 1:
                    prize = Util.randdict(Config.Free_ExtraReel_Reel_Prize)
                    extra_reel.append(prize)
                else:
                    extra_reel.append(0)
            self.self_data[Const.R_Extra_Reel] = extra_reel

        else:
            self.self_data[Const.R_Extra_Reel_Idx] += 1
            if self.self_data[Const.R_Extra_Reel_Idx] > len(Config.Const.R_Free_Extra_Reel):
                self.self_data[Const.R_Extra_Reel_Idx] = 0


            long_extra_reel = Config.Const.R_Free_Extra_Reel + Config.Const.R_Free_Extra_Reel[:15]

            if long_extra_reel[self.self_data[Const.R_Extra_Reel_Idx]+5] == 1:
                prize = Util.randdict(Config.Free_ExtraReel_Reel_Prize)
                extra_reel = self.self_data[Const.R_Extra_Reel][1:]
                extra_reel.append(prize)
                self.self_data[Const.R_Extra_Reel] = extra_reel
            else:
                extra_reel = self.self_data[Const.R_Extra_Reel][1:]
                extra_reel.append(0)
                self.self_data[Const.R_Extra_Reel] = extra_reel

        reel = Slot.GetReel(Free_ReelSets[0], Config.Const.C_Shape).get_reel()

        extra_reel_hit = []
        for x in range(5):
            if Config.Scatter in reel[x]:
                extra_reel_hit.append(extra_reel[x])

        extra_win_mul = 0
        free_hit = 0
        for y in extra_reel_hit:
            if y != 0:
                if y in Config.Const.C_Jackpot_Set.keys():
                    extra_win_mul += Config.Const.C_Jackpot_Set[y]
                else:
                    extra_win_mul += y
            else:
                free_hit += 1


        result[Const.R_Reel] = reel


        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Extra_Win] = extra_win_mul * totalbet
        return result,free_hit


