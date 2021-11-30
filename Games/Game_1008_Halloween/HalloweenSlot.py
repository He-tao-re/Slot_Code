import random
import Games.Game_1008_Halloween.HalloweenConfig_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)

class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data


    def paidspin(self,totalbet):

        result = {}
        self.self_data[Const.R_Jackpot_Hit] = []
        self.self_data[Const.R_Bubble_Extra_Win] = 0
        reel = Slot.GetReel(Base_ReelSets[0], Config.Const.C_Shape).get_reel()

        result[Const.R_Show_Reel] = reel
        self.count_special_sym(reel)
        '''气泡上升，删除无效气泡'''
        self.bubble_move()

        '''获取新气泡'''

        '''先出底部气泡'''
        self.button_bubble()
        '''随机气泡'''
        self.new_bubble()

        act_reel = copy.deepcopy(reel)

        act_reel,bubble_bomb = self.bubble_to_wild(act_reel)

        self.self_data[Const.R_Bubble_Bomb] = bubble_bomb
        self.self_data[Const.R_Bubble_Active_Pos] = 0
        self.self_data[Const.R_Bubble_Num] = 0

        #统计有效气泡个数
        for bubble in self.self_data[Const.R_Bubble]:
            bubble_pos_list = bubble[Const.R_Bubble_Pos]
            r_set = {i for i in range(30)}
            if len(r_set & set(bubble_pos_list)) > 0:
                self.self_data[Const.R_Bubble_Num] += 1

        #统计有效格子数
        bubble_pos = self.get_bubble_list()
        for idx in bubble_pos:
            x = idx % 5
            y = idx // 5
            if x in range(0,5) and y in range(0,6):
                self.self_data[Const.R_Bubble_Active_Pos] += 1


        result[Const.R_Reel] = act_reel
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)
        result.update(Slot.StandardLineEvaluator(totalbet,act_reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Bubble_Extra_Win] = self.self_data[Const.R_Bubble_Extra_Win] * totalbet


        sc_num = len(self.self_data[Const.R_Scatter_Pos])
        if sc_num >= 3:
            pick_time = Config.Scatter_to_Pick[sc_num]
            free,free_self_data, free_win_amount = FreeGame(self.self_data).free_game(pick_time,totalbet)

            result[Const.R_Free] = free
            result[Const.R_Free_Win_Amount] = free_win_amount

        return result,self.self_data


    '''底部的气泡'''
    def button_bubble(self):

        button_new_bubble_num = 0
        button_bubble_kind = Util.randdict(Config.Base_Bubble['button_bubble_kind'])

        if button_bubble_kind == 1:
            for i in range(5):
                ra = random.random()

                # 原有气泡位置
                bubble_pos_list = self.get_bubble_list()

                if ra <= Config.Base_Bubble['button_bubble_kind_1'][i]:

                    new_bubble_pos_list = [30+i]

                    if len(set(bubble_pos_list) & set(new_bubble_pos_list)) == 0:
                        button_new_bubble_num += 1

                        extra = Util.randdict(Config.Base_Bubble['extra_award_kind_1'])
                        bubble = {Const.R_Bubble_Pos: new_bubble_pos_list, Const.R_Bubble_Extra: extra}
                        self.self_data[Const.R_Bubble].append(bubble)

        elif button_bubble_kind == 4:
            for i in range(5):
                ra = random.random()

                # 原有气泡位置
                bubble_pos_list = self.get_bubble_list()

                if ra <= Config.Base_Bubble['button_bubble_kind_4'][i]:
                    new_bubble_pos_list = [29 + i, 30 + i, 34 + i, 35 + i]

                    if len(set(bubble_pos_list) & set(new_bubble_pos_list)) == 0:
                        button_new_bubble_num += 1

                        extra = Util.randdict(Config.Base_Bubble['extra_award_kind_4'])
                        bubble = {Const.R_Bubble_Pos: new_bubble_pos_list, Const.R_Bubble_Extra: extra}
                        self.self_data[Const.R_Bubble].append(bubble)

        self.self_data[Const.R_New_Bubble_Num] = button_new_bubble_num

    '''获得新的随机气泡'''
    def new_bubble(self):
        #气泡数量
        bubble_num = len(self.self_data[Const.R_Bubble])

        bubble_list = self.get_bubble_list()
        random_new_bubble_num = 0

        if bubble_num > 8:
            bubble_num = 8

        new_bubble = False
        random_limit = Config.Base_Bubble['bubble_hit'][bubble_num]

        ra = random.random()

        if ra < random_limit:
            new_bubble = True

        if new_bubble is True:
            kind = Util.randdict(Config.Base_Bubble['bubble_kind'])
            if kind == 1:
                num = Util.randdict(Config.Base_Bubble['bubble_num_kind_1'])
                local_pos = get_bubble_local_pos(Config.Base_Bubble['bubble_local_pos_kind_1'],num)

                for idx in local_pos:

                    '''避免气泡重叠，重叠就跳过-不出气泡'''

                    if idx not in bubble_list:
                        extra = Util.randdict(Config.Base_Bubble['extra_award_kind_1'])
                        bubble = {Const.R_Bubble_Pos: [idx], Const.R_Bubble_Extra: extra}
                        random_new_bubble_num += 1
                        self.self_data[Const.R_Bubble].append(bubble)
                    else:
                        pass

            elif kind == 4:
                num = Util.randdict(Config.Base_Bubble['bubble_num_kind_4'])
                local_pos = get_bubble_local_pos(Config.Base_Bubble['bubble_local_pos_kind_4'], num)

                for idx in local_pos:

                    '''避免气泡重叠，重叠就跳过'''
                    if idx not in bubble_list and idx-1 not in bubble_list and idx-5 not in bubble_list and idx-6 not in bubble_list:

                        extra = Util.randdict(Config.Base_Bubble['extra_award_kind_4'])
                        bubble = {Const.R_Bubble_Pos: [idx,idx-1,idx-5,idx-6], Const.R_Bubble_Extra: extra}
                        random_new_bubble_num += 1
                        self.self_data[Const.R_Bubble].append(bubble)
                    else:
                        pass

        self.self_data[Const.R_New_Bubble_Num] += random_new_bubble_num

    '''气泡生效变为wild，和爆气泡'''
    def bubble_to_wild(self,reel):
        bubble_bomb = False
        act_reel = copy.deepcopy(reel)
        for bubble in self.self_data[Const.R_Bubble]:
            bubble_kind = len(bubble[Const.R_Bubble_Pos])
            if bubble_kind == 1:
                idx = bubble[Const.R_Bubble_Pos][0]
                x = idx % 5
                y = idx // 5

                if x in range(0, 5) and y in range(0, 6):
                    act_reel[x][y] = Config.Wild
                    if reel[x][y] == Config.M1:
                        if bubble[Const.R_Bubble_Extra] != "blank":
                            self.self_data[Const.R_Bubble_Extra_Win] += Config.Const.C_Jackpot_Set[bubble[Const.R_Bubble_Extra]]
                            self.self_data[Const.R_Jackpot_Hit].append(bubble[Const.R_Bubble_Extra])

                        bubble_bomb = True
                        for i in [x-1, x, x+1]:
                            for j in [y-1, y, y+1]:
                                if i in range(0, 5) and j in range(0, 6):
                                    act_reel[i][j] = Config.Wild



            elif bubble_kind == 4:
                idx = max(bubble[Const.R_Bubble_Pos])
                x = idx % 5
                y = idx // 5

                bubble_4_hit = 0

                for bubble_idx in bubble[Const.R_Bubble_Pos]:
                    x_1 = bubble_idx % 5
                    y_1 = bubble_idx // 5
                    if x_1 in range(0, 5) and y_1 in range(0, 6):
                        #大气泡下图标变wild使用
                        act_reel[x_1][y_1] = Config.Wild
                        #统计气泡和M1重叠个数
                        if reel[x_1][y_1] == Config.M1:
                            bubble_4_hit += 1
                    else:
                        pass

                if bubble_4_hit > 0:
                    if bubble[Const.R_Bubble_Extra] != "blank":
                        self.self_data[Const.R_Bubble_Extra_Win] += Config.Const.C_Jackpot_Set[bubble[Const.R_Bubble_Extra]]
                        self.self_data[Const.R_Jackpot_Hit].append(bubble[Const.R_Bubble_Extra])

                    bubble_bomb = True
                    for i in [x-2, x-1, x, x+1]:
                        for j in [y-2, y-1, y, y+1]:
                            if [i,j] in [[x-2,y-2],[x-2,y+1],[x+1,y-2],[x+1,y+1]]:
                                pass
                            else:
                                if i in range(0, 5) and j in range(0, 6):
                                    act_reel[i][j] = Config.Wild

        return act_reel,bubble_bomb

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


class FreeGame(object):
    def __init__(self,self_data):
        self.self_data = self_data


    def free_game(self,pick_time, totalbet):
        free = {}
        free_recoder = 0
        free_win_amount = 0
        free_extra_win_amount = 0
        freespins, pick_get = freespin_pick(pick_time, Config.FreeSpin_Pick)

        while freespins > 0:
            freespins -= 1
            free_recoder += 1

            free_result, self.self_data = FreeSpin(self.self_data).paidspin(totalbet)

            if self.self_data[Const.R_Free_Extra_Freespin] > 0:
                freespins += self.self_data[Const.R_Free_Extra_Freespin]

            free[free_recoder] = free_result

            free_win_amount += free_result[Const.R_Win_Amount]
            free_win_amount += free_result[Const.R_Bubble_Extra_Win]


            free_extra_win_amount += free_result[Const.R_Bubble_Extra_Win]

            free_result[Const.R_Free_Win_Amount] = free_win_amount

        return free,self.self_data,free_win_amount


class FreeSpin(object):
    def __init__(self, self_data):
        self.self_data = self_data

    def paidspin(self, totalbet):

        result = {}
        self.self_data[Const.R_Jackpot_Hit] = []
        self.self_data[Const.R_Bubble_Extra_Win] = 0
        reel = Slot.GetReel(Free_ReelSets[0], Config.Const.C_Shape).get_reel()

        result[Const.R_Show_Reel] = reel
        self.count_special_sym(reel)
        '''气泡上升，删除无效气泡'''
        self.bubble_move()

        '''获取新气泡'''

        '''先出底部气泡'''
        self.button_bubble()
        '''随机气泡'''
        self.new_bubble()

        act_reel = copy.deepcopy(reel)

        act_reel,bubble_bomb = self.bubble_to_wild(act_reel)

        self.self_data[Const.R_Bubble_Bomb] = bubble_bomb
        self.self_data[Const.R_Bubble_Active_Pos] = 0
        self.self_data[Const.R_Bubble_Num] = 0

        #统计有效气泡个数
        for bubble in self.self_data[Const.R_Bubble]:
            bubble_pos_list = bubble[Const.R_Bubble_Pos]
            r_set = {i for i in range(30)}
            if len(r_set & set(bubble_pos_list)) > 0:
                self.self_data[Const.R_Bubble_Num] += 1

        #统计有效格子数
        bubble_pos = self.get_bubble_list()
        for idx in bubble_pos:
            x = idx % 5
            y = idx // 5
            if x in range(0,5) and y in range(0,6):
                self.self_data[Const.R_Bubble_Active_Pos] += 1


        result[Const.R_Reel] = act_reel
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)
        result.update(Slot.StandardLineEvaluator(totalbet,act_reel,Config.Const.C_PayLine, Config.Const.C_Free_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Bubble_Extra_Win] = self.self_data[Const.R_Bubble_Extra_Win] * totalbet


        sc_num = len(self.self_data[Const.R_Scatter_Pos])

        if sc_num >= 3:
            pick_time = Config.Scatter_to_Pick[sc_num]
            extra_freespins, pick_get = freespin_pick(pick_time, Config.FreeSpin_Pick)

            self.self_data[Const.R_Free_Extra_Freespin] = extra_freespins

        else:
            self.self_data[Const.R_Free_Extra_Freespin] = 0

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        return result, self.self_data


    '''底部的气泡'''
    def button_bubble(self):

        button_new_bubble_num = 0
        button_bubble_kind = Util.randdict(Config.Free_Bubble['button_bubble_kind'])

        if button_bubble_kind == 1:
            for i in range(5):
                ra = random.random()

                # 原有气泡位置
                bubble_pos_list = self.get_bubble_list()

                if ra <= Config.Free_Bubble['button_bubble_kind_1'][i]:

                    new_bubble_pos_list = [30+i]

                    if len(set(bubble_pos_list) & set(new_bubble_pos_list)) == 0:
                        button_new_bubble_num += 1

                        extra = Util.randdict(Config.Free_Bubble['extra_award_kind_1'])
                        bubble = {Const.R_Bubble_Pos: new_bubble_pos_list, Const.R_Bubble_Extra: extra}
                        self.self_data[Const.R_Bubble].append(bubble)

        elif button_bubble_kind == 4:
            for i in range(5):
                ra = random.random()

                # 原有气泡位置
                bubble_pos_list = self.get_bubble_list()

                if ra <= Config.Free_Bubble['button_bubble_kind_4'][i]:
                    new_bubble_pos_list = [29 + i, 30 + i, 34 + i, 35 + i]

                    if len(set(bubble_pos_list) & set(new_bubble_pos_list)) == 0:
                        button_new_bubble_num += 1

                        extra = Util.randdict(Config.Free_Bubble['extra_award_kind_4'])
                        bubble = {Const.R_Bubble_Pos: new_bubble_pos_list, Const.R_Bubble_Extra: extra}
                        self.self_data[Const.R_Bubble].append(bubble)

        self.self_data[Const.R_New_Bubble_Num] = button_new_bubble_num

    '''获得新的随机气泡'''
    def new_bubble(self):
        #气泡数量
        bubble_num = len(self.self_data[Const.R_Bubble])

        bubble_list = self.get_bubble_list()
        random_new_bubble_num = 0

        if bubble_num > 8:
            bubble_num = 8

        new_bubble = False
        random_limit = Config.Free_Bubble['bubble_hit'][bubble_num]

        ra = random.random()

        if ra < random_limit:
            new_bubble = True

        if new_bubble is True:
            kind = Util.randdict(Config.Free_Bubble['bubble_kind'])
            if kind == 1:
                num = Util.randdict(Config.Free_Bubble['bubble_num_kind_1'])
                local_pos = get_bubble_local_pos(Config.Free_Bubble['bubble_local_pos_kind_1'],num)

                for idx in local_pos:

                    '''避免气泡重叠，重叠就跳过-不出气泡'''

                    if idx not in bubble_list:
                        extra = Util.randdict(Config.Free_Bubble['extra_award_kind_1'])
                        bubble = {Const.R_Bubble_Pos: [idx], Const.R_Bubble_Extra: extra}
                        random_new_bubble_num += 1
                        self.self_data[Const.R_Bubble].append(bubble)
                    else:
                        pass

            elif kind == 4:
                num = Util.randdict(Config.Free_Bubble['bubble_num_kind_4'])
                local_pos = get_bubble_local_pos(Config.Free_Bubble['bubble_local_pos_kind_4'], num)

                for idx in local_pos:

                    '''避免气泡重叠，重叠就跳过'''
                    if idx not in bubble_list and idx-1 not in bubble_list and idx-5 not in bubble_list and idx-6 not in bubble_list:

                        extra = Util.randdict(Config.Free_Bubble['extra_award_kind_4'])
                        bubble = {Const.R_Bubble_Pos: [idx,idx-1,idx-5,idx-6], Const.R_Bubble_Extra: extra}
                        random_new_bubble_num += 1
                        self.self_data[Const.R_Bubble].append(bubble)
                    else:
                        pass

        self.self_data[Const.R_New_Bubble_Num] += random_new_bubble_num

    '''气泡生效变为wild，和爆气泡'''
    def bubble_to_wild(self,reel):
        bubble_bomb = False
        act_reel = copy.deepcopy(reel)
        for bubble in self.self_data[Const.R_Bubble]:
            bubble_kind = len(bubble[Const.R_Bubble_Pos])
            if bubble_kind == 1:
                idx = bubble[Const.R_Bubble_Pos][0]
                x = idx % 5
                y = idx // 5

                if x in range(0, 5) and y in range(0, 6):
                    act_reel[x][y] = Config.Wild
                    if reel[x][y] == Config.M1:
                        if bubble[Const.R_Bubble_Extra] != "blank":
                            self.self_data[Const.R_Bubble_Extra_Win] += Config.Const.C_Jackpot_Set[bubble[Const.R_Bubble_Extra]]
                            self.self_data[Const.R_Jackpot_Hit].append(bubble[Const.R_Bubble_Extra])

                        bubble_bomb = True
                        for i in [x-1, x, x+1]:
                            for j in [y-1, y, y+1]:
                                if i in range(0, 5) and j in range(0, 6):
                                    act_reel[i][j] = Config.Wild



            elif bubble_kind == 4:
                idx = max(bubble[Const.R_Bubble_Pos])
                x = idx % 5
                y = idx // 5

                bubble_4_hit = 0

                for bubble_idx in bubble[Const.R_Bubble_Pos]:
                    x_1 = bubble_idx % 5
                    y_1 = bubble_idx // 5
                    if x_1 in range(0, 5) and y_1 in range(0, 6):
                        #大气泡下图标变wild使用
                        act_reel[x_1][y_1] = Config.Wild
                        #统计气泡和M1重叠个数
                        if reel[x_1][y_1] == Config.M1:
                            bubble_4_hit += 1
                    else:
                        pass

                if bubble_4_hit > 0:
                    if bubble[Const.R_Bubble_Extra] != "blank":
                        self.self_data[Const.R_Bubble_Extra_Win] += Config.Const.C_Jackpot_Set[bubble[Const.R_Bubble_Extra]]
                        self.self_data[Const.R_Jackpot_Hit].append(bubble[Const.R_Bubble_Extra])

                    bubble_bomb = True
                    for i in [x-2, x-1, x, x+1]:
                        for j in [y-2, y-1, y, y+1]:
                            if [i,j] in [[x-2,y-2],[x-2,y+1],[x+1,y-2],[x+1,y+1]]:
                                pass
                            else:
                                if i in range(0, 5) and j in range(0, 6):
                                    act_reel[i][j] = Config.Wild

        return act_reel,bubble_bomb

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




def get_bubble_local_pos(local_weight,num):
    pos_list = []
    weight = copy.deepcopy(local_weight)
    while num > 0:
        num -= 1
        pos_idx = Util.randdict(weight)
        pos_list.append(pos_idx)
        del weight[pos_idx]

    return pos_list


def freespin_pick(pick_time, pick_items):
    freespins = 0
    pick_list = copy.deepcopy(pick_items)
    pick_get = []

    while pick_time > 0:
        pick_time -= 1
        pick = Util.randdict(pick_list)
        pick_list[pick] -= 1
        if pick in [1, 2, 3, 4, 5]:
            freespins += pick

        elif pick == 102:
            pick_time += 2

        elif pick == 103:
            pick_time += 3

        pick_get.append(pick)

    return freespins, pick_get