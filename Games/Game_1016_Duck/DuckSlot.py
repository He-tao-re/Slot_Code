import random
import Games.Game_1016_Duck.duck_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)



class GameSlot(object):
    def __init__(self):
        self.self_data = {}

    def paidspin(self,totalbet):

        result = {}
        reel = Slot.GetReel(Base_ReelSets[0], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel

        self.special_sym_count(reel)

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())



        return result

    def special_sym_count(self,reel):
        sc_num = 0
        sc_pos = []

        bonus_num = 0
        bonus_pos = []


        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.Scatter:
                    sc_num += 1
                    sc_pos.append([x,y])
                elif reel[x][y] == Config.Bonus:
                    bonus_num += 1
                    bonus_pos.append([x,y])



        self.self_data = {Const.R_Scatter_Num: sc_num,
                          Const.R_Scatter_Pos: sc_pos,
                          Const.R_Bonus_Num: bonus_num,
                          Const.R_Bonus_Pos: bonus_pos}




class Feature_Game(object):
    def __init__(self,bonus_pos):
        self.feature_reel = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self.pos_pro = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        for pos in bonus_pos:
            x = pos[0]
            y = pos[1]
            self.feature_reel[x][y] = 1

    def allocate_pro(self):
        blank_pos = []
        for x in range(5):
            for y in range(3):
                if self.feature_reel[x][y] == 0:
                    blank_pos.append([x,y])

        random.shuffle(blank_pos)

        num_idx = 0
        for pos in blank_pos:
            x = pos[0]
            y = pos[1]
            self.pos_pro[x][y] = Config.Feature_Pro[num_idx]
            num_idx += 1

    def feature_spin(self):

        for x in range(5):
            for y in range(3):
                if self.feature_reel[x][y] == 0:
                    _rand = random.random()

                    if _rand < self.pos_pro[x][y]:
                        self.feature_reel[x][y] = 1
        return copy.deepcopy(self.feature_reel)

    def shape_judge(self):
        area_list = {}
        pos_list = set()
        shape_list = {
            "3*5": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
            "3*4": [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
            "2*5": [[0, 1, 3, 4, 6, 7, 9, 10, 12, 13], [1, 2, 4, 5, 7, 8, 10, 11, 13, 14]],
            "3*3": [[0, 1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9, 10, 11], [6, 7, 8, 9, 10, 11, 12, 13, 14]],
            "2*4": [[0, 1, 3, 4, 6, 7, 9, 10], [3, 4, 6, 7, 9, 10, 12, 13], [1, 2, 4, 5, 7, 8, 10, 11],
                    [4, 5, 7, 8, 10, 11, 13, 14]],
            "3*2": [[0, 1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 8], [6, 7, 8, 9, 10, 11], [9, 10, 11, 12, 13, 14]],
            "2*3": [[0, 1, 3, 4, 6, 7], [3, 4, 6, 7, 9, 10], [6, 7, 9, 10, 12, 13], [1, 2, 4, 5, 7, 8],
                    [4, 5, 7, 8, 10, 11], [7, 8, 10, 11, 13, 14]],
            "2*2": [[0, 1, 3, 4], [3, 4, 6, 7], [6, 7, 9, 10], [9, 10, 12, 13], [1, 2, 4, 5], [4, 5, 7, 8],
                    [7, 8, 10, 11], [10, 11, 13, 14]],
            "3*1": [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]],
            "2*1": [[0, 1], [3, 4], [6, 7], [9, 10], [12, 13], [1, 2], [4, 5], [7, 8], [10, 11], [13, 14]],
            "1*1": [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14]]
        }

        for x in range(5):
            for y in range(3):
                if self.feature_reel[x][y] == 1:
                    idx = x + 5 * y
                    pos_list.add(idx)

        for k,v in shape_list:
            for shape in v:
                pass




    def feature(self,respin_times):
        self.allocate_pro()

        feature_result = {}
        feature_recoder = 0

        while respin_times > 0:
            respin_times -= 1
            feature_recoder += 1

            feature_result[feature_recoder] = self.feature_spin()

        return feature_result



