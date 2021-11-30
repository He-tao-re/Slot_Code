import Games.Game_1022_Tiki.Tiki_Config as Config
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

    def paidspin(self,totalbet):
        result = {}
        reel_idx = 0


        original_reel = Slot.GetReel(ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        bonus_change_reel, self.game_data = bonus_change(original_reel, self.game_data, Const.C_Base)


        # result[Const.R_Show_Reel] = copy.deepcopy(bonus_change_reel)

        '''变wild，计数 -1'''
        wild_feature_reel, self.game_data = wild_feature(bonus_change_reel, self.game_data)
        sc_num, free_spins = free_judge(wild_feature_reel)


        result[Const.R_Reel] = wild_feature_reel
        result.update(Slot.StandardLineEvaluator(totalbet, wild_feature_reel, Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub,
                                                 Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())


        self.game_data = bonus_collect(bonus_change_reel,self.game_data)
        '''重置次数'''
        self.game_data = reset_bonus_collect(self.game_data)
        result[Const.R_Self_Data] = copy.deepcopy(self.game_data)

        if sc_num >= 3:

            free_spins = Util.randdict(Game_Set['FreeSpins'])
            extra_num = Util.randdict((Game_Set['Extra_FS']))
            extra_free_pick = random.sample([2,3,5],extra_num)

            extra_free = sum(extra_free_pick)

            game_data = {
                'State': [
                    [0, 0, False],
                    [0, 0, False],
                    [0, 0, False],
                    [0, 0, False],
                    [0, 0, False]
                ]
            }
            result[Const.R_Free], result[Const.R_Free_Win_Amount] = FreeGame(game_data).free_game(free_spins+extra_free,totalbet)


        return result,self.game_data

class FreeGame(object):
    def __init__(self, game_data):
        self.game_data = game_data

    def freespin(self, totalbet):
        result = {}
        reel_idx = 1

        original_reel = Slot.GetReel(ReelSets[reel_idx], Config.Const.C_Free_Shape).get_reel()
        bonus_change_reel, self.game_data = bonus_change(original_reel, self.game_data, Const.R_Free)


        # result[Const.R_Show_Reel] = copy.deepcopy(bonus_change_reel)

        '''变wild，计数 -1'''
        wild_feature_reel, self.game_data = free_wild_feature(bonus_change_reel, self.game_data)

        result[Const.R_Reel] = wild_feature_reel

        result.update(Slot.StandardLineEvaluator(totalbet, wild_feature_reel, Config.Const.C_Free_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub,
                                                 Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())

        self.game_data = free_bonus_collect(bonus_change_reel, self.game_data)
        '''重置次数'''
        self.game_data = reset_bonus_collect(self.game_data)
        result[Const.R_Self_Data] = copy.deepcopy(self.game_data)
        return result


    def free_game(self,free_spins,total_bet):
        free = {}

        free_recoder = 0
        free_win_amount = 0

        while free_spins > 0:

            free_spins -= 1
            free_recoder += 1


            free_result = self.freespin(total_bet)
            free_win_amount += free_result[Const.R_Win_Amount]
            free_result[Const.R_Free_Win_Amount] = copy.deepcopy(free_win_amount)



            free[free_recoder] = free_result


        return free,free_win_amount





'''free触发判断'''
def free_judge(reel):
    sc_num = 0
    for x in range(len(reel)):
        for y in range(len(reel[x])):
            if reel[x][y] == Config.Scatter:
                sc_num += 1
    else:
        free_spins = 0
    return sc_num,free_spins



'''bonus-94变换'''
def bonus_change(original_reel, game_data, status):
    reel = copy.deepcopy(original_reel)

    for x in range(len(reel)):
        for y in range(len(reel[x])):
            if reel[x][y] is Config.Bonus:
                if game_data['State'][x][0] == 0:

                    if status == Const.C_Base:

                        sym_change = Util.randdict(Game_Set['Base_Wild_Feature']['Collect_0'])
                        reel[x][y] = sym_change

                    elif status == Const.R_Free:
                        sym_change = Util.randdict(Game_Set['Free_Wild_Feature']['Collect_0'])
                        reel[x][y] = sym_change

                elif game_data['State'][x][0] == 1:
                    if status == Const.C_Base:

                        sym_change = Util.randdict(Game_Set['Base_Wild_Feature']['Collect_1'])
                        reel[x][y] = sym_change

                    elif status == Const.R_Free:
                        sym_change = Util.randdict(Game_Set['Free_Wild_Feature']['Collect_1'])
                        reel[x][y] = sym_change


                elif game_data['State'][x][0] == 2:
                    if status == Const.C_Base:

                        sym_change = Util.randdict(Game_Set['Base_Wild_Feature']['Collect_2'])
                        reel[x][y] = sym_change

                    elif status == Const.R_Free:
                        sym_change = Util.randdict(Game_Set['Free_Wild_Feature']['Collect_2'])
                        reel[x][y] = sym_change

                elif game_data['State'][x][0] == 3:
                    if status == Const.C_Base:

                        sym_change = Util.randdict(Game_Set['Base_Wild_Feature']['Collect_3'])
                        reel[x][y] = sym_change

                    elif status == Const.R_Free:
                        sym_change = Util.randdict(Game_Set['Free_Wild_Feature']['Collect_3'])
                        reel[x][y] = sym_change

    return reel, game_data



'''bonus收集结算'''
def bonus_collect(reel, game_data):
    for x in range(5):
        for y in range(3):
            if reel[x][y] == Config.Bonus_1:
                game_data['State'][x][0] += 1
            elif reel[x][y] == Config.Bonus_2:
                game_data['State'][x][0] += 2
            elif reel[x][y] == Config.Bonus_3:
                game_data['State'][x][0] += 3


    for x in range(5):
        if game_data['State'][x][0] >= 3 and game_data['State'][x][2] is False:
            game_data['State'][x][1] = 3
            game_data['State'][x][2] = True
            '''重置次数'''
            for y in range(5):
                if game_data['State'][y][2] is True and game_data['State'][y][1] > 0:
                    game_data['State'][y][1] = 3
    return game_data


'''bonus收集结算'''
def free_bonus_collect(reel, game_data):
    for x in range(5):
        for y in range(6):
            if reel[x][y] == Config.Bonus_1:
                game_data['State'][x][0] += 1
            elif reel[x][y] == Config.Bonus_2:
                game_data['State'][x][0] += 2
            elif reel[x][y] == Config.Bonus_3:
                game_data['State'][x][0] += 3


    for x in range(5):
        if game_data['State'][x][0] >= 3 and game_data['State'][x][2] is False:
            game_data['State'][x][1] = 3
            game_data['State'][x][2] = True
            '''重置次数'''
            for y in range(5):
                if game_data['State'][y][2] is True and game_data['State'][y][1] > 0:
                    game_data['State'][y][1] = 3
    return game_data







'''wild feature，处理wild feature结束，收集重置'''
def wild_feature(reel, game_data):

    for i in range(5):
        if game_data['State'][i][1] in [1,2,3]:
            reel[i] = [Config.Long_Wild, Config.Long_Wild, Config.Long_Wild]
            game_data['State'][i][1] = copy.deepcopy(game_data['State'][i][1] - 1)
    return reel, game_data

def free_wild_feature(reel, game_data):
    for i in range(5):
        if game_data['State'][i][1] in [1,2,3]:
            reel[i] = [Config.Long_Wild, Config.Long_Wild, Config.Long_Wild, Config.Long_Wild, Config.Long_Wild, Config.Long_Wild]
            game_data['State'][i][1] = copy.deepcopy(game_data['State'][i][1] - 1)
    return reel, game_data


'''清空次数'''
def reset_bonus_collect(game_data):
    for i in range(5):
        if game_data['State'][i][1] == 0 and game_data['State'][i][2] is True:
            game_data['State'][i][0] = 0
            game_data['State'][i][2] = False
    return game_data
