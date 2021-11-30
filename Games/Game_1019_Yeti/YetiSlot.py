import Games.Game_1019_Yeti.YetiConfig as Config
import Slot_common.Const as Const
import Slot_common.Slots as Slot
import util.Util as Util
import random
import copy
import numpy as np
import datetime
import json
import math

Base_ReelSet = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSet = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)

Game_Set = Config.Const.C_Game_Set


class GameSlot(object):
    def __init__(self):
        self.self_data = {}

    def paidspin(self, totalbet):
        result = {}

        reel_idx = 0
        reel = Slot.GetReel(Base_ReelSet[reel_idx], Config.Const.C_Shape).get_reel()
        result[Const.R_Show_Reel] = copy.deepcopy(reel)

        self.count_special_sym(reel)


        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)
        result[Const.R_Scatter_Win] = 0
        result.update(Slot.StandardLineEvaluator(totalbet, reel, Config.Const.C_PayLine, Config.Const.C_Paytable,Config.Const.C_BetLine, Config.Const.C_Wild_Sub,Config.Const.C_LineSym,Config.Wilds, Config.Wild).evaluate())
        sc_num = len(self.self_data[Const.R_Scatter_Pos])

        if sc_num >= 3:
            result[Const.R_Scatter_Win] = Config.Const.C_Paytable[Config.Scatter][sc_num-1] * totalbet
            #兔子起始位置
            Rabbit_pos = [[2,2]]
            Carrot_pos = []

            result[Const.R_Free], result[Const.R_Free_Win_Amount] = FreeGame(Rabbit_pos, Carrot_pos).free_result(totalbet)
            result[Const.R_Win_Amount] += result[Const.R_Scatter_Win]
        return result

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
    def __init__(self, Rabbit_Pos, Carrot_Pos):

        self.self_data = {'Rabbit': Rabbit_Pos,
                          'Carrot': Carrot_Pos,
                          'Carrot_Eat': 0,
                          'FreeSpins': 5}
        self.growth_progress = [True, True, True, True]

    def free_result(self, total_bet):
        free = {}
        free_recoder = 0
        free_win_amount = 0

        while self.self_data['FreeSpins'] > 0:
            '''free开始'''
            free_recoder += 1
            self.self_data['FreeSpins'] -= 1
            free_result = self.free_spin(total_bet)
            free_win_amount += free_result[Const.R_Win_Amount]

            free_result[Const.R_Free_Win_Amount] = free_win_amount

            free[free_recoder] = free_result

        return free,free_win_amount


    def free_spin(self, totalbet):
        result = {}

        if self.growth_progress == [True, True, True, True]:
            reel_idx = 0
        elif self.growth_progress == [False, True, True, True]:
            reel_idx = 1
        elif self.growth_progress == [False, False, True, True]:
            reel_idx = 2
        elif self.growth_progress == [False, False, False, True]:
            reel_idx = 3
        else:
            reel_idx = 3

        reel = Slot.GetReel(Free_ReelSet[reel_idx], Config.Const.C_Shape).get_reel()
        result[Const.R_Show_Reel] = copy.deepcopy(reel)

        deal_reel = copy.deepcopy(reel)
        for pos in self.self_data['Rabbit']:
            x = pos[0]
            y = pos[1]
            deal_reel[x][y] = Config.Wild_S

        result.update(Slot.StandardLineEvaluator(totalbet, deal_reel, Config.Const.C_PayLine, Config.Const.C_Paytable,Config.Const.C_BetLine, Config.Const.C_Wild_Sub,Config.Const.C_LineSym,Config.Wilds, Config.Wild).evaluate())

        self.self_data['Carrot'] = self.find_carrot(deal_reel)
        self.self_data['Carrot_Eat'] += len(self.self_data['Carrot'])

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        '''兔子移动'''
        Carrot_List = self.find_carrot(deal_reel)
        while len(Carrot_List) > 0:

            aim_carrot = rank_pos(self.self_data['Rabbit'], Carrot_List)

            '''获得距离目标胡萝卜最近的兔子点【距离，兔子点坐标】'''
            Rabbit_way = rabbit_move(aim_carrot, self.self_data['Rabbit'])

            nearest_rabbit = Rabbit_way[1]

            '''计算移动向量'''
            move = [aim_carrot[0] - nearest_rabbit[0], aim_carrot[1] - nearest_rabbit[1]]

            '''兔子移动后的位置'''
            new_rabbit = []
            for rabbit in self.self_data['Rabbit']:
                new_rabbit.append([rabbit[0] + move[0], rabbit[1] + move[1]])

            self.self_data['Rabbit'] = new_rabbit

            '''删除消化掉的胡萝卜'''
            Carrot_List.remove(aim_carrot)

            '''判定移动后兔子是否覆盖其他的胡萝卜'''
            for Carrot in Carrot_List:
                if Carrot in self.self_data['Rabbit']:
                    Carrot_List.remove(Carrot)

        '''收集所有胡萝卜之后，判断兔子扩张'''
        self.rabbit_track_growth()

        return result


    def find_carrot(self, reel):
        Carrot_Pos = []
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.Wild:
                    Carrot_Pos.append([x, y])
        return Carrot_Pos


    def rabbit_track_growth(self):

        if self.self_data['Carrot_Eat'] >= 4 and self.growth_progress[0] is True:
            self.growth_progress[0] = False
            self.self_data['Rabbit'] = self.rabbit_expand(self.self_data['Rabbit'], 1)
            self.self_data['FreeSpins'] += 3

        elif self.self_data['Carrot_Eat'] >= 9 and self.growth_progress[1] is True:
            self.growth_progress[1] = False
            self.self_data['Rabbit'] = self.rabbit_expand(self.self_data['Rabbit'], 2)
            self.self_data['FreeSpins'] += 2

        elif self.self_data['Carrot_Eat'] >= 13 and self.growth_progress[2] is True:
            self.growth_progress[2] = False
            self.self_data['Rabbit'] = self.rabbit_expand(self.self_data['Rabbit'], 3)
            self.self_data['FreeSpins'] += 2

        elif self.self_data['Carrot_Eat'] >= 17 and self.growth_progress[3] is True:
            self.growth_progress[3] = False
            self.self_data['Rabbit'] = self.rabbit_expand(self.self_data['Rabbit'], 4)
            self.self_data['FreeSpins'] += 1

    def rabbit_expand(self, Rabbit_Pos, Size):
        x_list = []
        y_list = []
        mark_pos = []
        for pos in Rabbit_Pos:
            if pos[0] in x_list:
                pass
            else:
                x_list.append(pos[0])
            if pos[1] in y_list:
                pass
            else:
                y_list.append(pos[1])
        mark_pos.append(min(x_list))
        mark_pos.append(max(y_list))
        if Size == 1:
            if mark_pos[0] <= 2 and mark_pos[1] <= 1:
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1]])
            elif mark_pos[0] >= 3 and mark_pos[1] <= 1:
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1]])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] + 1])
            elif mark_pos[0] <= 2 and mark_pos[1] >= 2:
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] - 1])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1]])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1] - 1])
            elif mark_pos[0] >= 3 and mark_pos[1] >= 2:
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1]])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] - 1])
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] - 1])
        elif Size == 2:
            if mark_pos[0] <= 1 and mark_pos[1] <= 2:
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 2, mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 2, mark_pos[1]])
                Rabbit_Pos.append([mark_pos[0] + 2, mark_pos[1] - 1])
            elif mark_pos[0] >= 2 and mark_pos[1] <= 2:
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] - 1])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1]])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1] + 1])
            elif mark_pos[0] <= 1 and mark_pos[1] >= 3:
                Rabbit_Pos.append([mark_pos[0] + 2, mark_pos[1]])
                Rabbit_Pos.append([mark_pos[0] + 2, mark_pos[1] - 1])
                Rabbit_Pos.append([mark_pos[0] + 2, mark_pos[1] - 2])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1] - 2])
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] - 2])
            elif mark_pos[0] >= 2 and mark_pos[1] >= 3:
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1]])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] - 1])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] - 2])
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] - 2])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1] - 2])
        elif Size == 3:
            if mark_pos[0] <= 1 and mark_pos[1] <= 2:
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 2, mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 3, mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 3, mark_pos[1]])
                Rabbit_Pos.append([mark_pos[0] + 3, mark_pos[1] - 1])
                Rabbit_Pos.append([mark_pos[0] + 3, mark_pos[1] - 2])
            elif mark_pos[0] <= 2 and mark_pos[1] <= 2:

                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] - 2])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] - 1])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1]])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1] + 1])
                Rabbit_Pos.append([mark_pos[0] + 2, mark_pos[1] + 1])
            elif mark_pos[0] <= 1 and mark_pos[1] >= 3:
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] - 3])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1] - 3])
                Rabbit_Pos.append([mark_pos[0] + 2, mark_pos[1] - 3])
                Rabbit_Pos.append([mark_pos[0] + 3, mark_pos[1] - 3])
                Rabbit_Pos.append([mark_pos[0] + 3, mark_pos[1] - 2])
                Rabbit_Pos.append([mark_pos[0] + 3, mark_pos[1] - 1])
                Rabbit_Pos.append([mark_pos[0] + 3, mark_pos[1]])
            elif mark_pos[0] >= 2 and mark_pos[1] >= 3:
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1]])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] - 1])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] - 2])
                Rabbit_Pos.append([mark_pos[0] - 1, mark_pos[1] - 3])
                Rabbit_Pos.append([mark_pos[0], mark_pos[1] - 3])
                Rabbit_Pos.append([mark_pos[0] + 1, mark_pos[1] - 3])
                Rabbit_Pos.append([mark_pos[0] + 2, mark_pos[1] - 3])
        elif Size == 4:
            for x in range(5):
                for y in range(5):
                    if [x, y] not in Rabbit_Pos:
                        Rabbit_Pos.append([x, y])
                    else:
                        pass
        return Rabbit_Pos


def rank_pos(Rabbit_Pos, Carrot_Pos):
    # print('Rabbit_Mark' + str(Rabbit_Mark))

    x_list = []
    y_list = []
    mark_pos = []

    #找出兔子所有的落点x，y值
    for pos in Rabbit_Pos:
        if pos[0] in x_list:
            pass
        else:
            x_list.append(pos[0])
        if pos[1] in y_list:
            pass
        else:
            y_list.append(pos[1])

    #找出左下标志点
    mark_pos.append(min(x_list))
    mark_pos.append(max(y_list))

    Rabbit_Mark = mark_pos
    distance_pos_list = {}

    #萝卜，优先级，列表
    rank_pos_list = {}

    rank_id = 0

    #遍历萝卜位置
    for Carrot in Carrot_Pos:
        C_x = Carrot[0]
        C_y = Carrot[1]

        #对于每个Carrot，查找最近的Rabbit相对位置
        abs_distance_list = []
        for Rabbit in Rabbit_Pos:
            R_x = Rabbit[0]
            R_y = Rabbit[1]

            abs_distance_list.append(abs(R_x - C_x) + abs(R_y - C_y))

        abs_distance = min(abs_distance_list)
        if abs_distance in distance_pos_list.keys():
            distance_pos_list[abs_distance].append(Carrot)
        else:
            distance_pos_list[abs_distance] = [Carrot]

    min_distance = min(distance_pos_list.keys())
    # print(distance_list)

    if len(distance_pos_list[min_distance]) > 1:

        angle_carrot = {}
        for pos in distance_pos_list[min_distance]:

            r_pos = [pos[0] - Rabbit_Mark[0], pos[1] - Rabbit_Mark[1]]

            # print('实际点' + str(pos))

            #坐标反转，盘面坐标系和XY坐标系，向量Y值相反
            r_pos[1] = r_pos[1] * (-1)

            angle = Calculation_of_the_Angle([-1, -1], r_pos)
            angle_carrot[angle] = pos

        # print("angle_carrot")
        # print(angle_carrot)
        # print("Rabbit_Mark")
        # print(Rabbit_Mark)

        angle_list = sorted(angle_carrot.keys())

        sorted(angle_list)

        for angle in angle_list:
            rank_pos_list[rank_id] = angle_carrot[angle]
            rank_id += 1

    else:
        rank_pos_list[rank_id] = distance_pos_list[min_distance][0]
        rank_id += 1

    '''对同一距离的萝卜排序，并返回最优先的1个胡萝卜'''
    return rank_pos_list[0]


def rabbit_move(Carrot, Rabbit_Pos):

    Carrot_Rabbit = [False, False]
    for Rabbit in Rabbit_Pos:
        R_x = abs(Carrot[0] - Rabbit[0])
        R_y = abs(Carrot[1] - Rabbit[1])
        R = R_x + R_y
        if Carrot_Rabbit[0] is False and Carrot_Rabbit[1] is False:
            Carrot_Rabbit[0] = R
            Carrot_Rabbit[1] = Rabbit
        elif R < Carrot_Rabbit[0]:
            Carrot_Rabbit[0] = R
            Carrot_Rabbit[1] = Rabbit

    '''返回距离萝卜最近的兔子点（距离，坐标）'''
    return Carrot_Rabbit


'''计算向量角'''
def get_angle(pos_1, pos_2):
    x = np.array(pos_1)
    y = np.array(pos_2)
    Lx = np.sqrt(x.dot(x))
    Ly = np.sqrt(y.dot(y))
    cos_angle = x.dot(y) / (Lx * Ly)
    angle = np.arccos(cos_angle)
    angle2 = int(angle * 360 / 2 / np.pi + 0.5)
    return angle2


'''计算方位角'''
def azimuthAngle(pos_1, pos_2):
    x1 = pos_1[0]
    y1 = pos_1[1]

    x2 = pos_2[0]
    y2 = pos_2[1]

    angle = 0.0
    dx = x2 - x1
    dy = y2 - y1
    if x2 == x1:
        angle = math.pi / 2.0
        if y2 == y1:
            angle = 0.0
        elif y2 < y1:
            angle = 3.0 * math.pi / 2.0
    # 第一象限
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dy / dx)

    # 第二象限
    elif x2 < x1 and y2 >= y1:
        angle = math.pi - math.atan(dy / -dx)

    # 第三象限
    elif x2 < x1 and y2 < y1:
        angle = math.pi + math.atan(dy / dx)
    # 第四象限
    elif x2 > x1 and y2 < y1:
        angle = 2 * math.pi - math.atan(-dy / dx)

    return (angle * 180 / math.pi)


'''计算两向量的夹角'''
def Calculation_of_the_Angle(pos_1, pos_2):
    angle_1 = azimuthAngle([0, 0], pos_1)
    angle_2 = azimuthAngle([0, 0], pos_2)
    #
    # print('angle_1:' + str(angle_1))
    #
    # print('angle_2:' + str(angle_2) + '\n')
    if angle_2 < angle_1:
        angle = angle_2 + 135
    else:
        angle = angle_2 - 225

    return angle
