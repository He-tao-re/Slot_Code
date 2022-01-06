import random
import Games.Game_1024_Thor.Thor_config_100 as Config
import Slot_common.Slots as Slot
import Games.Game_1024_Thor.static_data_1024 as static_data
import util.Util as Util
import Slot_common.Const as Const
import copy


Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_ReelSets)
Game_Set = Config.Const.C_Game_Set

s_data = static_data.data

class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data

    def paidspin(self,totalbet):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        #统计scatter数量
        self.special_sym_count(reel)

        mark_num = 0
        for value in self.self_data[Const.R_Reel_Mark].values():
            if value == 1:
                mark_num += 1
        # print(self.self_data[Const.R_Reel_Mark])

        mark_random = random.random()
        # print(mark_num)

        if mark_random < Game_Set["random_add_pro"][mark_num]:
            add_num = Util.randlist(Game_Set["add_num"])
            no_mark_pos = []
            for key,value in self.self_data[Const.R_Reel_Mark].items():
                if value == 0:
                    no_mark_pos.append(key)
            if add_num >= len(no_mark_pos):
                random_mark_pos = random.sample(no_mark_pos,len(no_mark_pos))
            else:
                random_mark_pos = random.sample(no_mark_pos,add_num)


            for pos in random_mark_pos:
                if pos >= 22:
                    print(random_mark_pos)
                    print(pos,"false")
                self.self_data[Const.R_Reel_Mark][pos] = 1
        else:
            pass



        result[Const.R_Reel] = reel

        pos_connect = self.feature_connect(reel)
        change_pos, feature_reel = self.wild_feature(reel, pos_connect)

        result.update(Slot.StandardLineEvaluator(totalbet,feature_reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        #重置
        for pos_idx in change_pos:
            self.self_data[Const.R_Reel_Mark][pos_idx] = 0
        #结算完之后，mark新的标记点
        idx = 0
        for x in range(len(reel)):
            for y in range(len(reel[x])):

                if reel[x][y] == Config.WS and idx not in change_pos:
                    self.self_data[Const.R_Reel_Mark][idx] = 1
                idx += 1


        if len(self.self_data[Const.R_Scatter_Pos]) >= 3:
            self.self_data[Const.R_Free_Collect] += 1
            free_spins = Config.Free_Spins[len(self.self_data[Const.R_Scatter_Pos])]

            if self.self_data[Const.R_Free_Collect] % 5 != 0:

                result[Const.R_Free],result[Const.R_Free_Win_Amount],self.self_data = self.free_result(free_spins,totalbet)

            else:
                feature_shape = Util.randlist(Game_Set['super_free_shape'])
                result[Const.R_Super_Free], result[Const.R_Free_Win_Amount], self.self_data = self.super_free_result(free_spins,totalbet,feature_shape)
                result[Const.R_Feature_Shape] = feature_shape
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        """统计部分"""
        s_data[Const.S_Test_Time] += 1
        s_data[Const.S_Bet] += totalbet
        s_data[Const.S_Base_Win] += result[Const.R_Win_Amount]

        s_data[Const.S_Win] += result[Const.R_Win_Amount]

        if result[Const.R_Win_Amount] > 0:
            s_data[Const.S_Base_Hit] += 1

        if Const.R_Free in result.keys():
            s_data[Const.S_Free_Hit] += 1
            s_data[Const.S_Free_Win] += result[Const.R_Free_Win_Amount]

            s_data[Const.S_Win] += result[Const.R_Free_Win_Amount]

        if Const.R_Super_Free in result.keys():
            s_data[Const.S_Super_Free_Hit] += 1
            s_data[Const.S_Super_Free_Win] += result[Const.R_Free_Win_Amount]

            s_data[Const.S_Win] += result[Const.R_Free_Win_Amount]

            '''分支统计'''
            shape_idx = static_data.shape_list.index(result[Const.R_Feature_Shape])
            s_data[Const.S_Extra_Win][shape_idx][0] += result[Const.R_Free_Win_Amount]
            s_data[Const.S_Extra_Win][shape_idx][1] += 1

        return result, self.self_data


    def wild_feature(self,reel,pos_connect):

        feature_reel = copy.deepcopy(reel)
        change_wild_pos = set()

        hit_pos = []

        #排除相同项
        mark_pos = set()
        for area in pos_connect:
            mark_pos.update(area)

        idx = 0
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.WS and self.self_data[Const.R_Reel_Mark][idx] == 1:
                    hit_pos.append(idx)

                idx += 1

        for pos_idx in hit_pos:
            for area in pos_connect:
                if pos_idx in area:
                    change_wild_pos.update(area)

        idx = 0
        for x in range(len(feature_reel)):
            for y in range(len(feature_reel[x])):
                if idx in change_wild_pos:
                    feature_reel[x][y] = Config.Wild
                idx += 1

        return change_wild_pos,feature_reel


    def feature_connect(self,reel):
        pos_connect = {
            0: {1,4,5},
            1: {0,2,5,6},
            2: {1,3,6,7},
            3: {2,7,8},
            4: {0,5,9},
            5: {0,1,4,6,9,10},
            6: {1,2,5,7,10,11},
            7: {2,3,6,8,11,12},
            8: {3,7,12},
            9: {4,5,10,13,14},
            10: {5,6,9,11,14,15},
            11: {6,7,10,12,15,16},
            12: {7,8,11,16,17},
            13: {9,14,18},
            14: {9,10,13,15,18,19},
            15: {10,11,14,16,19,20},
            16: {11,12,15,17,20,21},
            17: {12,16,21},
            18: {13,14,19},
            19: {14,15,18,20},
            20: {15,16,19,21},
            21: {16,17,20},
        }

        mark_pos = {}
        area_list = {}

        idx = 0
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if self.self_data[Const.R_Reel_Mark][idx] == 1:
                    mark_pos[idx] = 1
                else:
                    mark_pos[idx] = 0

                idx += 1

        # mark_pos = {0: 1, 1: 1, 2: 0, 3: 1, 4: 1, 5: 1, 6: 0, 7: 0, 8: 1, 9: 1, 10: 1, 11: 0, 12: 1, 13: 1, 14: 0, 15: 1, 16: 0, 17: 0, 18: 1, 19: 0, 20: 1, 21: 0}
        # print("mark_pos:{}".format(mark_pos))

        for pos_idx in mark_pos.keys():


            if mark_pos[pos_idx] == 1:
                area_list[pos_idx] = {pos_idx}

                connect_pos = pos_connect[pos_idx]


                active = True
                while active:
                    count_idx = 0

                    for pos in connect_pos:
                        count_idx += 1
                        if mark_pos[pos] == 1:

                            area_list[pos_idx].add(pos)


                            connect_pos.update(pos_connect[pos_idx])

                    if count_idx == len(connect_pos):
                        active = False

                s_set = set()
                for k_1 in area_list.keys():
                    for k_2 in area_list.keys():
                        if k_1 != k_2:
                            if len(area_list[k_1].intersection(area_list[k_2])) > 0:
                                area_list[k_1].update(area_list[k_2])
                                s_set.add(k_2)

        # print("area_list:{}".format(area_list))



        get_area = []
        for value in area_list.values():
            if value in get_area:
                pass
            else:
                get_area.append(value)


        return get_area


    def special_sym_count(self,reel):
        pos_idx = 0
        self.self_data[Const.R_Scatter_Pos] = []
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.Scatter:
                    self.self_data[Const.R_Scatter_Pos].append(pos_idx)
                pos_idx += 1


    def free_result(self,free_spins,totalbet):
        free = {}

        free_recoder = 0
        free_win_amount = 0

        self_data = copy.deepcopy(self.self_data)
        while free_spins > 0:
            free_spins -= 1
            free_recoder += 1

            result, self_data, extra_free_spins = FreeGame(self_data).freespin(totalbet)
            free_win_amount += result[Const.R_Win_Amount]

            free_spins += extra_free_spins
            result[Const.R_Free_Win_Amount] = free_win_amount

            free[free_recoder] = result

        return free, free_win_amount,self_data


    def super_free_result(self,free_spins,totalbet,shape):
        free = {}

        free_recoder = 0
        free_win_amount = 0

        self_data = copy.deepcopy(self.self_data)
        while free_spins > 0:
            free_spins -= 1
            free_recoder += 1

            result, self_data, extra_free_spins = FreeGame(self_data).super_freespin(totalbet,shape)
            free_win_amount += result[Const.R_Win_Amount]

            result[Const.R_Free_Win_Amount] = free_win_amount

            free[free_recoder] = result

        return free, free_win_amount,self_data





class FreeGame(object):
    def __init__(self,self_data):
        self.self_data = self_data


    def freespin(self,totalbet):


        result = {}
        reel_idx = 1
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()


        add_WS_num = Util.randlist(Game_Set['free_add_WS'])
        add_pos = random.sample(self.self_data[Const.R_Reel_Mark].keys(),add_WS_num)

        pos_idx = 0
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if pos_idx in add_pos:
                    reel[x][y] = 1
                pos_idx += 1

        #统计scatter数量
        self.special_sym_count(reel)


        result[Const.R_Reel] = reel



        pos_connect = self.feature_connect(reel)
        change_pos, feature_reel = self.wild_feature(reel, pos_connect)

        result.update(Slot.StandardLineEvaluator(totalbet,feature_reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        #重置
        for pos_idx in change_pos:
            self.self_data[Const.R_Reel_Mark][pos_idx] = 0

        #结算完之后，mark新的标记点
        idx = 0
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.WS and idx not in change_pos:
                    self.self_data[Const.R_Reel_Mark][idx] = 1
                idx += 1


        if len(self.self_data[Const.R_Scatter_Pos]) >= 3:
            extra_free_spins = Config.Free_Spins[len(self.self_data[Const.R_Scatter_Pos])]
        else:
            extra_free_spins = 0

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result, self.self_data, extra_free_spins


    def super_freespin(self,totalbet,shape):


        result = {}
        reel_idx = 2
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        for pos_idx in shape:
            self.self_data[Const.R_Reel_Mark][pos_idx] = 1

        add_WS_num = Util.randlist(Game_Set['super_free_add_WS'])
        add_pos = random.sample(self.self_data[Const.R_Reel_Mark].keys(),add_WS_num)

        pos_idx = 0
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if pos_idx in add_pos:
                    reel[x][y] = 1
                pos_idx += 1

        #统计scatter数量
        self.special_sym_count(reel)


        result[Const.R_Reel] = reel



        pos_connect = self.feature_connect(reel)
        change_pos, feature_reel = self.wild_feature(reel, pos_connect)

        result.update(Slot.StandardLineEvaluator(totalbet,feature_reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        #重置
        for pos_idx in change_pos:
            self.self_data[Const.R_Reel_Mark][pos_idx] = 0

        #结算完之后，mark新的标记点
        idx = 0
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.WS and idx not in change_pos:
                    self.self_data[Const.R_Reel_Mark][idx] = 1
                idx += 1


        if len(self.self_data[Const.R_Scatter_Pos]) >= 3:
            extra_free_spins = Config.Free_Spins[len(self.self_data[Const.R_Scatter_Pos])]
        else:
            extra_free_spins = 0

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result, self.self_data, extra_free_spins


    def wild_feature(self, reel, pos_connect):

        feature_reel = copy.deepcopy(reel)
        change_wild_pos = set()

        hit_pos = []
        mark_pos = set()
        for area in pos_connect:
            mark_pos.update(area)

        idx = 0
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.WS and self.self_data[Const.R_Reel_Mark][idx] == 1:
                    hit_pos.append(idx)

                idx += 1

        for pos_idx in hit_pos:
            for area in pos_connect:
                if pos_idx in area:
                    change_wild_pos.update(area)

        idx = 0
        for x in range(len(feature_reel)):
            for y in range(len(feature_reel[x])):
                if idx in change_wild_pos:
                    feature_reel[x][y] = Config.Wild
                idx += 1

        return change_wild_pos, feature_reel


    def feature_connect(self, reel):
        pos_connect = {
            0: {1, 4, 5},
            1: {0, 2, 5, 6},
            2: {1, 3, 6, 7},
            3: {2, 7, 8},
            4: {0, 5, 9},
            5: {0, 1, 4, 6, 9, 10},
            6: {1, 2, 5, 7, 10, 11},
            7: {2, 3, 6, 8, 11, 12},
            8: {3, 7, 12},
            9: {4, 5, 10, 13, 14},
            10: {5, 6, 9, 11, 14, 15},
            11: {6, 7, 10, 12, 15, 16},
            12: {7, 8, 11, 16, 17},
            13: {9, 14, 18},
            14: {9, 10, 13, 15, 18, 19},
            15: {10, 11, 14, 16, 19, 20},
            16: {11, 12, 15, 17, 20, 21},
            17: {12, 16, 21},
            18: {13, 14, 19},
            19: {14, 15, 18, 20},
            20: {15, 16, 19, 21},
            21: {16, 17, 20},
        }

        mark_pos = {}
        area_list = {}

        idx = 0
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if self.self_data[Const.R_Reel_Mark][idx] == 1:
                    mark_pos[idx] = 1
                else:
                    mark_pos[idx] = 0

                idx += 1

        # mark_pos = {0: 1, 1: 1, 2: 0, 3: 1, 4: 1, 5: 1, 6: 0, 7: 0, 8: 1, 9: 1, 10: 1, 11: 0, 12: 1, 13: 1, 14: 0, 15: 1, 16: 0, 17: 0, 18: 1, 19: 0, 20: 1, 21: 0}
        # print("mark_pos:{}".format(mark_pos))

        for pos_idx in mark_pos.keys():

            if mark_pos[pos_idx] == 1:
                area_list[pos_idx] = {pos_idx}

                connect_pos = pos_connect[pos_idx]

                active = True
                while active:
                    count_idx = 0

                    for pos in connect_pos:
                        count_idx += 1
                        if mark_pos[pos] == 1:
                            area_list[pos_idx].add(pos)

                            connect_pos.update(pos_connect[pos_idx])

                    if count_idx == len(connect_pos):
                        active = False

                s_set = set()
                for k_1 in area_list.keys():
                    for k_2 in area_list.keys():
                        if k_1 != k_2:
                            if len(area_list[k_1].intersection(area_list[k_2])) > 0:
                                area_list[k_1].update(area_list[k_2])
                                s_set.add(k_2)

        # print("area_list:{}".format(area_list))

        get_area = []
        for value in area_list.values():
            if value in get_area:
                pass
            else:
                get_area.append(value)

        return get_area


    def special_sym_count(self, reel):
        pos_idx = 0
        self.self_data[Const.R_Scatter_Pos] = []
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.Scatter:
                    self.self_data[Const.R_Scatter_Pos].append(pos_idx)
                pos_idx += 1



