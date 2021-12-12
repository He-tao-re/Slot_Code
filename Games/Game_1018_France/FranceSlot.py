import random
import Games.Game_1018_France.france_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)

class GameSlot(object):
    def __init__(self):
        self.self_data = {}

    def paidspin(self,totalbet, collect_data):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel

        result[Const.R_Feature] = self.special_sym_count(reel)

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        if self.self_data[Const.R_Scatter_Num] >= 3:
            result[Const.R_Scatter_Win] = totalbet * Config.Const.C_Paytable[Config.Scatter][self.self_data[Const.R_Scatter_Num] - 1]
            result[Const.R_Win_Amount] += result[Const.R_Scatter_Win]

            freespin = Config.Const.C_Feature_Trigger[Const.C_FreeGame][Const.C_Trigger_FreeSpins][3]

            result[Const.R_Free],result[Const.R_Free_Win_Amount] = self.free_game(freespin,totalbet)

        if self.self_data[Const.R_Bonus_Num] >= 4:
            collect_data['progress'] += 1
            if collect_data['progress'] < collect_data['end']:
                result[Const.R_Respin],result[Const.R_Respin_Win] = Respin().respin_game(self.self_data[Const.R_Bonus_Pos],totalbet,False)
            else:
                collect_data['progress'] = 0
                result[Const.R_Super_Respin],result[Const.R_Respin_Win] = Respin().respin_game(self.self_data[Const.R_Bonus_Pos],totalbet,True)
        result[Const.R_Self_Data][Const.R_Collect_Data] = collect_data
        return result

    def special_sym_count(self,reel):
        sc_num = 0
        sc_pos = []

        bonus_num = 0
        bonus_pos = {}

        feature_get = []

        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.Scatter:
                    sc_num += 1
                    idx = x + 5 * y
                    sc_pos.append(idx)

                elif reel[x][y] == Config.Bonus:
                    bonus_num += 1
                    idx = x + 5 * y
                    bonus_award = Config.Bonus_award[Util.randdict(Config.Num_on_Bonus['base_bonus'])]
                    bonus_pos[idx] = bonus_award

        if sc_num >= Config.Const.C_Feature_Trigger[Const.C_FreeGame][Const.C_Mini_Trigger_Num]:
            feature_get.append(Const.C_FreeGame)

        if bonus_num >= Config.Const.C_Feature_Trigger[Const.C_Respin][Const.C_Mini_Trigger_Num]:
            feature_get.append(Const.C_Respin)

        self.self_data = {Const.R_Scatter_Num: sc_num,
                          Const.R_Scatter_Pos: sc_pos,
                          Const.R_Bonus_Num: bonus_num,
                          Const.R_Bonus_Pos: bonus_pos}

        return feature_get


    def free_game(self,freespins,totalbet):
        free = {}
        free_recoder = 0
        free_win_amount = 0


        while freespins > 0:
            free_result = {}
            freespins -= 1
            free_recoder += 1

            result_1 = FreeGame().paidspin_1(totalbet)
            result_2 = FreeGame().paidspin_2(totalbet)

            free_win_amount += result_1[Const.R_Win_Amount]
            free_win_amount += result_2[Const.R_Win_Amount]


            if Const.C_Re_Trigger_FreeSpins in result_1[Const.R_Feature]:
                freespins += 3
            if Const.C_Re_Trigger_FreeSpins in result_2[Const.R_Feature]:
                freespins += 3

            free_result['table_1'] = result_1
            free_result['table_2'] = result_2

            free_result[Const.R_Free_Win_Amount] = copy.deepcopy(free_win_amount)

            free[free_recoder] = free_result
        return free,free_win_amount


class FreeGame(object):

    def __init__(self):
        self.self_data = {}

    def paidspin_1(self, totalbet):

        result = {}
        reel = Slot.GetReel(Free_ReelSets[0], [4,4,4]).get_big_234_symReel([4, 4, 4])

        result[Const.R_Reel] = reel

        result[Const.R_Feature] = self.special_sym_count(reel)
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Free_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        bonus_win = 0

        for values in self.self_data[Const.R_Bonus_Pos].values():

            bonus_win += Config.Bonus_award[values] * totalbet

        result[Const.R_Free_Bonus_Win] = bonus_win

        result[Const.R_Win_Amount] += bonus_win

        return result

    def paidspin_2(self, totalbet):

        result = {}
        reel = Slot.GetReel(Free_ReelSets[1], [4, 4, 4]).get_big_234_symReel([4, 4, 4])

        result[Const.R_Reel] = reel

        result[Const.R_Feature] = self.special_sym_count(reel)
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        result.update(Slot.StandardLineEvaluator(totalbet, reel, Config.Const.C_PayLine, Config.Const.C_Free_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub,
                                                 Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        bonus_win = 0

        for values in self.self_data[Const.R_Bonus_Pos].values():
            bonus_win += Config.Bonus_award[values] * totalbet

        result[Const.R_Free_Bonus_Win] = bonus_win

        result[Const.R_Win_Amount] += bonus_win

        return result

    def special_sym_count(self,reel):
        sc_num = 0
        sc_pos = []

        bonus_num = 0
        bonus_pos = {}

        feature_get = []
        for x in [0, 4]:
            for y in range(len(reel[x])):


                if reel[x][y] == Config.Bonus:
                    bonus_num += 1
                    idx = x + 5 * y
                    bonus_award = Util.randdict(Config.Num_on_Bonus['free_15_bonus'])
                    bonus_pos[idx] = bonus_award


        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.Scatter:
                    sc_num += 1
                    idx = x + 5 * y
                    sc_pos.append(idx)

        bonus_reel = [Config.Bonus, Config.Bonus, Config.Bonus, Config.Bonus]

        if sc_num >= 12:
            feature_get.append(Const.C_Re_Trigger_FreeSpins)


        if reel[1] == bonus_reel:
            if reel[2] == bonus_reel:
                if reel[3] == bonus_reel:
                    idx = 234
                    bonus_award = Util.randdict(Config.Num_on_Bonus['free_234_bonus'])
                    bonus_pos[idx] = bonus_award
                else:
                    print("False")
            else:
                print("False")

        self.self_data = {Const.R_Scatter_Num: sc_num,
                          Const.R_Scatter_Pos: sc_pos,
                          Const.R_Bonus_Num: bonus_num,
                          Const.R_Bonus_Pos: bonus_pos}

        return feature_get


class Respin(object):
    def __init__(self):
        self.feature_reel = {}
        self.pos_type = {}
        self.unlock_pos = {i for i in range(20)}

        self.lock_1 = True
        self.lock_2 = True
        self.lock_3 = True
        self.lock_4 = True

    def get_trigger_reel(self,bonus_pos):
        # print(bonus_pos)
        blank_pos = []
        for idx in range(40):
            if idx in bonus_pos.keys():
                self.feature_reel[idx] = bonus_pos[idx]
            else:
                self.feature_reel[idx] = 0

                self.pos_type[idx] = [Config.get_bonus_pro, 0]
                blank_pos.append(idx)

        return blank_pos

    def allocate_kind(self,bonus_pos):
        blank_pos = self.get_trigger_reel(bonus_pos)

        high_mul_pos = random.sample(blank_pos,Config.high_mul_num)
        for idx in high_mul_pos:
            self.pos_type[idx][1] = 1

    def lock_judge(self):
        useful_pos = 0


        for idx in self.unlock_pos:
            if self.feature_reel[idx] != 0:
                useful_pos += 1

        if useful_pos >= 8 and self.lock_1 is True:
            self.lock_1 = False
            unlock_row = {20, 21, 22, 23, 24}
            self.unlock_pos.update(unlock_row)

            for idx in unlock_row:
                if self.feature_reel[idx] != 0:
                    useful_pos += 1

        if useful_pos >= 12 and self.lock_2 is True:
            self.lock_2 = False
            unlock_row = {25, 26, 27, 28, 29}
            self.unlock_pos.update(unlock_row)
            for idx in unlock_row:
                if self.feature_reel[idx] != 0:
                    useful_pos += 1

        if useful_pos >= 16 and self.lock_3 is True:
            self.lock_3 = False
            unlock_row = {30, 31, 32, 33, 34}
            self.unlock_pos.update(unlock_row)
            for idx in unlock_row:
                if self.feature_reel[idx] != 0:
                    useful_pos += 1

        if useful_pos >= 20 and self.lock_4 is True:
            self.lock_4 = False
            unlock_row = {35, 36, 37, 38, 39}
            self.unlock_pos.update(unlock_row)
            for idx in unlock_row:
                if self.feature_reel[idx] != 0:
                    useful_pos += 1
        return useful_pos

    def respin_game(self,bonus_pos,totalbet,super_respin):
        self.allocate_kind(bonus_pos)
        respin_times = copy.deepcopy(Config.Const.C_Feature_Trigger[Const.C_Respin][Const.R_Respin_Times])
        respin = {}
        respin_recoder = 0
        respin_win = 0

        # print(self.pos_type)

        while respin_times > 0:
            respin_result = {}

            respin_times -= 1
            respin_recoder += 1
            boost_pos = []
            for idx in self.feature_reel.keys():
                if self.feature_reel[idx] == 0:

                    '''
                    随机数
                    判断是否出bonus图标
                    '''
                    ra = random.random()
                    if ra < self.pos_type[idx][0]:

                        '''
                        判断是否在解锁区域
                        处于解锁区域则进行Boost图标判断
                        '''
                        if idx in self.unlock_pos:
                            if super_respin is False:
                                change_to_boost_bonus = Config.change_to_boost_bonus
                            else:
                                change_to_boost_bonus = Config.super_change_to_boost_bonus

                            boost_ra = random.random()

                            '''
                            每次最多出现1个boost bonus
                            Boost_Max_Num = 1
                            '''
                            if boost_ra < change_to_boost_bonus and len(boost_pos) < Config.Boost_Max_Num:

                                if self.pos_type[idx][1] == 0:
                                    self.feature_reel[idx] = Config.Bonus_award[Util.randdict(Config.Num_on_Bonus['respin_low_bonus'])]

                                elif self.pos_type[idx][1] == 1:
                                    self.feature_reel[idx] = Config.Bonus_award[Util.randdict(Config.Num_on_Bonus['respin_high_bonus'])]

                                boost_pos.append(idx)
                                respin_times = 3

                            else:
                                if self.pos_type[idx][1] == 0:
                                    self.feature_reel[idx] = Config.Bonus_award[Util.randdict(Config.Num_on_Bonus['respin_low_bonus'])]

                                elif self.pos_type[idx][1] == 1:
                                    self.feature_reel[idx] = Config.Bonus_award[Util.randdict(Config.Num_on_Bonus['respin_high_bonus'])]

                                respin_times = 3


                        else:
                            if self.pos_type[idx][1] == 0:
                                self.feature_reel[idx] = Config.Bonus_award[Util.randdict(Config.Num_on_Bonus['respin_low_bonus'])]

                            elif self.pos_type[idx][1] == 1:
                                self.feature_reel[idx] = Config.Bonus_award[Util.randdict(Config.Num_on_Bonus['respin_high_bonus'])]

                            if idx in self.unlock_pos:
                                respin_times = 3


            useful_bonus_pos = []
            for idx in self.unlock_pos:
                if self.feature_reel[idx] != 0:
                    useful_bonus_pos.append(idx)

            boost_get = {}
            for idx in boost_pos:

                boost_add = Util.randdict(Config.Bonus_Extra_Award)
                boost_num = Util.randdict(Config.Boost_bonus_Num)

                if boost_num >= len(useful_bonus_pos):
                    boost_num = len(useful_bonus_pos)

                if super_respin is False:
                    boost_pos_idx = random.sample(useful_bonus_pos,boost_num)

                    '''
                    排除boost图标
                    '''
                    if idx in boost_pos_idx:
                        boost_pos_idx.remove(idx)
                else:
                    boost_pos_idx = useful_bonus_pos

                    '''
                    排除boost图标
                    '''
                    boost_pos_idx.remove(idx)


                '''
                给选中的Boost位置增加倍数
                '''
                for x in boost_pos_idx:
                    self.feature_reel[x] += boost_add

                boost_get[idx] = boost_pos_idx



            useful_bonus_num = self.lock_judge()
            respin_result['Boost_Pos'] = boost_get
            respin_result[Const.R_Respin_Reel] = copy.deepcopy(self.feature_reel)
            respin_result['Unlock_Pos'] = copy.deepcopy(list(self.unlock_pos))
            respin_result[Const.R_Respin_Times] = copy.deepcopy(respin_times)
            respin_result["Useful_Num"] = useful_bonus_num

            respin[respin_recoder] = respin_result

        for idx in self.unlock_pos:
            respin_win += self.feature_reel[idx] * totalbet

        return respin,respin_win


