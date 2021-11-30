import random
import Games.Game_1011_Clownfish.ClownfishConfig_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)

class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data


    def paidspin(self,totalbet,spin_id):

        result = {Const.C_Spin_Id:spin_id}

        self.self_data[Const.R_Bubble_Extra_Win] = 0

        self.self_data[Const.R_New_Bubble_Num] = 0
        self.self_data[Const.R_New_Bubble_Kind_Num] = {1:0,2:0,3:0,4:0,5:0}

        reel = Slot.GetReel(Base_ReelSets[0], Config.Const.C_Shape).get_reel()

        Bubble_Set = Config.Base_Bubble

        self.count_special_sym(reel)
        '''气泡上升，删除无效气泡'''
        self.bubble_move()

        '''获取新气泡'''

        '''先出底部气泡'''
        self.button_bubble(Bubble_Set)
        '''随机气泡'''
        self.new_bubble(Bubble_Set)

        self.bubble_award(reel)

        result[Const.R_Reel] = reel
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)
        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Bubble_Win] = self.self_data[Const.R_Bubble_All_Award] * totalbet
        result[Const.R_Win_Amount] += self.self_data[Const.R_Bubble_All_Award] * totalbet


        sc_num = len(self.self_data[Const.R_Scatter_Pos])
        if sc_num >= 3:
            self.self_data[Const.R_Free_Collect] += 1
            if self.self_data[Const.R_Free_Collect] in range(1,10):
                Bubble_Set = Config.Free_Bubble
                freespins = Config.Const.C_Trigger_FreeSpins[sc_num]
                free,free_win_amount,free_bubble_win_amount,bubble_hit = self.free_game(totalbet,freespins,Bubble_Set)

                result[Const.R_Free] = free
                result[Const.R_Free_Win_Amount] = free_win_amount
                result[Const.R_Free_Bubble_Win_Amount] = free_bubble_win_amount
                result[Const.R_Free_Bubble_Hit] = bubble_hit

            else:

                self.self_data[Const.R_Free_Collect] = 0
                Bubble_Set = Config.Super_Free_Bubble
                freespins = Config.Const.C_Trigger_FreeSpins[sc_num]
                free, free_win_amount, free_bubble_win_amount, bubble_hit = self.free_game(totalbet, freespins,
                                                                                           Bubble_Set)

                result[Const.R_Super_Free] = free
                result[Const.R_Free_Win_Amount] = free_win_amount
                result[Const.R_Free_Bubble_Win_Amount] = free_bubble_win_amount
                result[Const.R_Free_Bubble_Hit] = bubble_hit

        return result,self.self_data


    '''free game'''
    def free_game(self,totalbet,freespins,Bubble_Set):
        free = {}
        free_recoder = 0
        free_win_amount = 0
        free_bubble_win_amount = 0
        bubble_hit = 0
        free_self_data = {
            Const.R_Bubble: []
        }

        '''free初始给一个大气泡'''
        free_self_data = self.free_begin_bubble(free_self_data,Bubble_Set)

        while freespins > 0:
            freespins -= 1
            free_recoder += 1

            free_result, free_self_data, free_extra = FreeGame(free_self_data).freespin(totalbet,Bubble_Set)
            freespins += free_extra

            if free_result[Const.R_Bubble_Win] > 0:
                bubble_hit += 1

            free_bubble_win_amount += free_result[Const.R_Bubble_Win]
            free_win_amount += free_result[Const.R_Win_Amount]

            free_result[Const.R_Free_Win_Amount] = copy.deepcopy(free_win_amount)

            free[free_recoder] = free_result

        return free,free_win_amount,free_bubble_win_amount,bubble_hit

    '''气泡中奖'''
    def bubble_award(self,reel):
        self.self_data[Const.R_Bubble_Hit_pos] = []
        self.self_data[Const.R_Bubble_All_Award] = 0
        for bubble in self.self_data[Const.R_Bubble]:
            for idx in bubble[Const.R_Bubble_Pos]:
                x = idx % 5
                y = idx // 5
                if x in range(0,5) and y in range(0,4):
                    if reel[x][y] == Config.BN:
                        award = bubble[Const.R_Bubble_Award]
                        if award in Config.Const.C_Jackpot_Set.keys():
                            self.self_data[Const.R_Bubble_All_Award] += Config.Const.C_Jackpot_Set[award]
                            self.self_data[Const.R_Bubble_Hit_pos].append(idx)
                        else:
                            self.self_data[Const.R_Bubble_All_Award] += award
                            self.self_data[Const.R_Bubble_Hit_pos].append(idx)


    '''获得新的随机气泡'''
    def new_bubble(self,Bubble_Set):

        new_random_bubble_num = 0
        bubble_pos_num = 0

        for bubble in self.self_data[Const.R_Bubble]:
            for idx in bubble[Const.R_Bubble_Pos]:
                x = idx % 5
                y = idx // 5
                if x in range(0, 5) and y in range(0, 4):
                    bubble_pos_num += 1

        self.self_data["bubble_pos_num"] = bubble_pos_num

        if bubble_pos_num > 11:
            bubble_pos_num = 11

        new_bubble = False
        random_limit = Bubble_Set[Const.R_Random_Bubble_Hit][bubble_pos_num]

        ra = random.random()

        if ra < random_limit:
            new_bubble = True

        '''气泡一个一个随机
            数量
            每个气泡Kind，位置
            新气泡和之前的气泡重叠，则让后面出的气泡失效
            '''
        if new_bubble is True:
            new_bubble_num = Util.randdict(Bubble_Set[Const.R_Bubble_Num])

            while new_bubble_num > 0:
                new_bubble_num -= 1

                # 原有气泡和新增气泡位置
                bubble_pos_list = self.get_bubble_list()

                bubble_kind = Util.randdict(Bubble_Set[Const.R_Random_Bubble_Kind])
                local_idx = Util.randdict(Bubble_Set[Const.R_Bubble_Local][bubble_kind])

                extra = Util.randdict(Bubble_Set[Const.R_Bubble_Prize][bubble_kind])
                award = Config.Const.R_Bubble_Prize_Kind[extra]
                bubble_pos = return_bubble_pos(local_idx, bubble_kind)

                if len(set(bubble_pos_list) & set(bubble_pos)) == 0:
                    bubble = {Const.R_Bubble_Pos: bubble_pos, Const.R_Bubble_Award: award}
                    self.self_data[Const.R_Bubble].append(bubble)
                    new_random_bubble_num += 1
                    self.self_data[Const.R_New_Bubble_Kind_Num][bubble_kind] += 1
                else:
                    pass

        self.self_data[Const.R_New_Bubble_Num] += new_random_bubble_num

    '''底部的气泡生成，避免重叠'''
    def button_bubble(self,Bubble_Set):

        new_button_bubble_num = 0

        button_bubble_kind = Util.randdict(Bubble_Set[Const.R_Bottom_Bubble_Kind])
        if button_bubble_kind is not None:
            local_idx = Util.randdict(Bubble_Set[Const.R_Bottom_Bubble_Local][button_bubble_kind])

            # 原有气泡和新增气泡位置

            bubble_pos_list = self.get_bubble_list()

            extra = Util.randdict(Bubble_Set[Const.R_Bubble_Prize][button_bubble_kind])
            award = Config.Const.R_Bubble_Prize_Kind[extra]
            bubble_pos = return_bubble_pos(local_idx,button_bubble_kind)

            if len(set(bubble_pos_list) & set(bubble_pos)) == 0:
                bubble = {Const.R_Bubble_Pos: bubble_pos, Const.R_Bubble_Award: award}
                self.self_data[Const.R_Bubble].append(bubble)
                new_button_bubble_num += 1
                self.self_data[Const.R_New_Bubble_Kind_Num][button_bubble_kind] += 1
            else:
                pass
        self.self_data[Const.R_New_Bubble_Num] += new_button_bubble_num


    '''获取气泡位置'''
    def get_bubble_list(self):
        bubble_list = []
        for bubble in self.self_data[Const.R_Bubble]:
            for idx in bubble[Const.R_Bubble_Pos]:
                bubble_list.append(idx)
        return bubble_list

    '''气泡上升和删除'''
    def bubble_move(self):
        for i in range(len(self.self_data[Const.R_Bubble])):
            bubble = self.self_data[Const.R_Bubble][i]
            idx_list = bubble[Const.R_Bubble_Pos]
            new_idx_list = []
            for idx in idx_list:
                new_idx_list.append(idx - 5)
            bubble[Const.R_Bubble_Pos] = new_idx_list

        del_bubble = []
        for x in range(len(self.self_data[Const.R_Bubble])):
            bubble = self.self_data[Const.R_Bubble][x]

            i = 0
            for idx in bubble[Const.R_Bubble_Pos]:
                if idx >= 0:
                    i += 1
            if i == 0:
                del_bubble.append(bubble)

        for bubble in del_bubble:
            self.self_data[Const.R_Bubble].remove(bubble)


    '''统计scatter个数'''
    def count_special_sym(self,reel):
        sc_pos = []
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                idx = y * 5 + x
                if reel[x][y] == Config.Scatter:
                    sc_pos.append(idx)
        self.self_data[Const.R_Scatter_Pos] = sc_pos



    '''free初始给一个大气泡'''

    def free_begin_bubble(self,self_data,Bubble_Set):

        kind = Util.randdict(Config.Free_Bubble[Const.R_Free_Original_Bubble])
        local_idx = Util.randdict(Bubble_Set[Const.R_Bottom_Bubble_Local][kind])
        extra = Util.randdict(Bubble_Set[Const.R_Bubble_Prize][kind])
        award = Config.Const.R_Bubble_Prize_Kind[extra]
        bubble_pos = return_bubble_pos(local_idx, kind)
        bubble = {Const.R_Bubble_Pos: bubble_pos, Const.R_Bubble_Award: award}
        self_data[Const.R_Bubble].append(bubble)

        return self_data

class FreeGame(object):
    def __init__(self,self_data):
        self.self_data = self_data

    def freespin(self,totalbet,Bubble_Set):

        result = {}

        self.self_data[Const.R_Bubble_Extra_Win] = 0

        self.self_data[Const.R_New_Bubble_Num] = 0
        self.self_data[Const.R_New_Bubble_Kind_Num] = {1:0,2:0,3:0,4:0,5:0}

        reel = Slot.GetReel(Free_ReelSets[0], Config.Const.C_Shape).get_reel()

        Bubble_Set = Bubble_Set

        self.count_special_sym(reel)
        '''气泡上升，删除无效气泡'''
        self.bubble_move()

        '''获取新气泡'''

        '''先出底部气泡'''
        self.button_bubble(Bubble_Set)
        '''随机气泡'''
        self.new_bubble(Bubble_Set)
        self.bubble_award(reel)
        result[Const.R_Reel] = reel
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)
        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())

        result[Const.R_Bubble_Win] = self.self_data[Const.R_Bubble_All_Award] * totalbet
        result[Const.R_Win_Amount] += self.self_data[Const.R_Bubble_All_Award] * totalbet

        free_extra = 0
        sc_num = len(self.self_data[Const.R_Scatter_Pos])
        if sc_num >= 2:
            free_extra = Config.Const.C_Re_Trigger_FreeSpins[sc_num]

        return result,self.self_data,free_extra


    '''气泡中奖'''
    def bubble_award(self,reel):
        self.self_data[Const.R_Bubble_Hit_pos] = []
        self.self_data[Const.R_Bubble_All_Award] = 0
        for bubble in self.self_data[Const.R_Bubble]:
            for idx in bubble[Const.R_Bubble_Pos]:
                x = idx % 5
                y = idx // 5
                if x in range(0,5) and y in range(0,4):
                    if reel[x][y] == Config.BN:
                        award = bubble[Const.R_Bubble_Award]
                        if award in Config.Const.C_Jackpot_Set.keys():
                            self.self_data[Const.R_Bubble_All_Award] += Config.Const.C_Jackpot_Set[award]
                            self.self_data[Const.R_Bubble_Hit_pos].append(idx)
                        else:
                            self.self_data[Const.R_Bubble_All_Award] += award
                            self.self_data[Const.R_Bubble_Hit_pos].append(idx)


    '''获得新的随机气泡'''
    def new_bubble(self,Bubble_Set):

        new_random_bubble_num = 0
        bubble_pos_num = 0

        for bubble in self.self_data[Const.R_Bubble]:
            for idx in bubble[Const.R_Bubble_Pos]:
                x = idx % 5
                y = idx // 5
                if x in range(0, 5) and y in range(0, 4):
                    bubble_pos_num += 1

        self.self_data["bubble_pos_num"] = bubble_pos_num

        if bubble_pos_num > 11:
            bubble_pos_num = 11

        new_bubble = False
        random_limit = Bubble_Set[Const.R_Random_Bubble_Hit][bubble_pos_num]

        ra = random.random()

        if ra < random_limit:
            new_bubble = True

        '''气泡一个一个随机
            数量
            每个气泡Kind，位置
            新气泡和之前的气泡重叠，则让后面出的气泡失效
            '''
        if new_bubble is True:
            new_bubble_num = Util.randdict(Bubble_Set[Const.R_Bubble_Num])

            while new_bubble_num > 0:
                new_bubble_num -= 1

                # 原有气泡和新增气泡位置
                bubble_pos_list = self.get_bubble_list()

                bubble_kind = Util.randdict(Bubble_Set[Const.R_Random_Bubble_Kind])
                local_idx = Util.randdict(Bubble_Set[Const.R_Bubble_Local][bubble_kind])

                extra = Util.randdict(Bubble_Set[Const.R_Bubble_Prize][bubble_kind])
                award = Config.Const.R_Bubble_Prize_Kind[extra]
                bubble_pos = return_bubble_pos(local_idx, bubble_kind)

                if len(set(bubble_pos_list) & set(bubble_pos)) == 0:
                    bubble = {Const.R_Bubble_Pos: bubble_pos, Const.R_Bubble_Award: award}
                    self.self_data[Const.R_Bubble].append(bubble)
                    new_random_bubble_num += 1
                    self.self_data[Const.R_New_Bubble_Kind_Num][bubble_kind] += 1
                else:
                    pass

        self.self_data[Const.R_New_Bubble_Num] += new_random_bubble_num

    '''底部的气泡生成，避免重叠'''
    def button_bubble(self,Bubble_Set):

        new_button_bubble_num = 0

        button_bubble_kind = Util.randdict(Bubble_Set[Const.R_Bottom_Bubble_Kind])
        if button_bubble_kind is not None:
            local_idx = Util.randdict(Bubble_Set[Const.R_Bottom_Bubble_Local][button_bubble_kind])

            # 原有气泡和新增气泡位置

            bubble_pos_list = self.get_bubble_list()

            extra = Util.randdict(Bubble_Set[Const.R_Bubble_Prize][button_bubble_kind])
            award = Config.Const.R_Bubble_Prize_Kind[extra]
            bubble_pos = return_bubble_pos(local_idx,button_bubble_kind)

            if len(set(bubble_pos_list) & set(bubble_pos)) == 0:
                bubble = {Const.R_Bubble_Pos: bubble_pos, Const.R_Bubble_Award: award}
                self.self_data[Const.R_Bubble].append(bubble)
                new_button_bubble_num += 1
                self.self_data[Const.R_New_Bubble_Kind_Num][button_bubble_kind] += 1
            else:
                pass
        self.self_data[Const.R_New_Bubble_Num] += new_button_bubble_num


    '''获取气泡位置'''
    def get_bubble_list(self):
        bubble_list = []
        for bubble in self.self_data[Const.R_Bubble]:
            for idx in bubble[Const.R_Bubble_Pos]:
                bubble_list.append(idx)
        return bubble_list

    '''气泡上升和删除'''
    def bubble_move(self):
        for i in range(len(self.self_data[Const.R_Bubble])):
            bubble = self.self_data[Const.R_Bubble][i]
            idx_list = bubble[Const.R_Bubble_Pos]
            new_idx_list = []
            for idx in idx_list:
                new_idx_list.append(idx - 5)
            bubble[Const.R_Bubble_Pos] = new_idx_list

        del_bubble = []
        for x in range(len(self.self_data[Const.R_Bubble])):
            bubble = self.self_data[Const.R_Bubble][x]

            i = 0
            for idx in bubble[Const.R_Bubble_Pos]:
                if idx >= 0:
                    i += 1
            if i == 0:
                del_bubble.append(bubble)

        for bubble in del_bubble:
            self.self_data[Const.R_Bubble].remove(bubble)


    '''统计scatter个数'''
    def count_special_sym(self,reel):
        sc_pos = []
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                idx = y * 5 + x
                if reel[x][y] == Config.Scatter:
                    sc_pos.append(idx)
        self.self_data[Const.R_Scatter_Pos] = sc_pos



def return_bubble_pos(local_idx,kind):
    pos_list = []
    if kind == 1:
        pos_list.append(local_idx)
    elif kind == 2:
        pos_list.append(local_idx)
        pos_list.append(local_idx-1)
        pos_list.append(local_idx-5)
        pos_list.append(local_idx-6)
    elif kind == 3:
        pos_list.append(local_idx)
        pos_list.append(local_idx-1)
        pos_list.append(local_idx-2)
        pos_list.append(local_idx-5)
        pos_list.append(local_idx-6)
        pos_list.append(local_idx-7)
        pos_list.append(local_idx-10)
        pos_list.append(local_idx-11)
        pos_list.append(local_idx-12)
    elif kind == 4:
        pos_list.append(local_idx)
        pos_list.append(local_idx-1)
        pos_list.append(local_idx-2)
        pos_list.append(local_idx-3)
        pos_list.append(local_idx-5)
        pos_list.append(local_idx-6)
        pos_list.append(local_idx-7)
        pos_list.append(local_idx-8)
        pos_list.append(local_idx-10)
        pos_list.append(local_idx-11)
        pos_list.append(local_idx-12)
        pos_list.append(local_idx-13)
        pos_list.append(local_idx-15)
        pos_list.append(local_idx-16)
        pos_list.append(local_idx-17)
        pos_list.append(local_idx-18)
    elif kind == 5:
        pos_list.append(local_idx)
        pos_list.append(local_idx-1)
        pos_list.append(local_idx-2)
        pos_list.append(local_idx-3)
        pos_list.append(local_idx-4)

        pos_list.append(local_idx-5)
        pos_list.append(local_idx-6)
        pos_list.append(local_idx-7)
        pos_list.append(local_idx-8)
        pos_list.append(local_idx-9)

        pos_list.append(local_idx-10)
        pos_list.append(local_idx-11)
        pos_list.append(local_idx-12)
        pos_list.append(local_idx-13)
        pos_list.append(local_idx-14)

        pos_list.append(local_idx-15)
        pos_list.append(local_idx-16)
        pos_list.append(local_idx-17)
        pos_list.append(local_idx-18)
        pos_list.append(local_idx-19)

        pos_list.append(local_idx-20)
        pos_list.append(local_idx-21)
        pos_list.append(local_idx-22)
        pos_list.append(local_idx-23)
        pos_list.append(local_idx-24)

    return pos_list



