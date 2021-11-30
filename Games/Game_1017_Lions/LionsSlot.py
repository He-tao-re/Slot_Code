import random
import Games.Game_1017_Lions.lion_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)
Free_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Free_ReelSets)


class GameSlot(object):
    def __init__(self):
        self.self_data = {}

    def paidspin(self, totalbet):
        result = {}
        reel = Slot.GetReel(Base_ReelSets[0], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel

        self.special_sym_count(reel,Config.Wild_Mul['base'])

        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)
        result[Const.R_Line],result[Const.R_Line_WinAmount] = Slot.WayLineEvaluator(Config.Const.C_Paytable, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild, totalbet, Config.Const.C_BetLine, reel).evaluate_wild_mul(self.self_data[Const.R_Wild_Pos])

        sc_num = len(self.self_data[Const.R_Scatter_Pos])

        if sc_num >= 3:
            result[Const.R_Scatter_Win] = Config.Const.C_Paytable[Config.Scatter][sc_num - 1] * totalbet
            result[Const.R_Win_Amount] = result[Const.R_Line_WinAmount] + result[Const.R_Scatter_Win]
            freespin = Config.Const.C_Feature_Trigger[Const.C_FreeGame][Const.C_Trigger_FreeSpins][sc_num]
            result[Const.R_Free],result[Const.R_Free_Win_Amount],result[Const.R_Wheel_Award] = FreeGame().free(totalbet,freespin)
        else:
            result[Const.R_Win_Amount] = result[Const.R_Line_WinAmount]
        return result


    def special_sym_count(self,reel,wild_mul_weight):
        sc_pos = []
        wild_pos = {}
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                idx = y * 5 + x
                if reel[x][y] == Config.Scatter:
                    sc_pos.append(idx)
                if reel[x][y] == Config.Wild:
                    mul = Util.randdict(wild_mul_weight)
                    wild_pos[idx] = mul

        self.self_data[Const.R_Scatter_Pos] = sc_pos
        self.self_data[Const.R_Wild_Pos] = wild_pos

class FreeGame(object):
    def __init__(self):
        self.gold_buffalo_pos = self.get_buffalo()
        self.self_data = {}

    def free(self,totalbet,freespin):

        free_recoder = 0
        free = {}

        self.wheelprize(totalbet)
        free_win_amount = 0
        wheel_award = self.self_data[Const.R_Wheel_Prize]

        while freespin > 0:
            freespin -= 1
            free_recoder += 1

            free_result = self.paidspin(totalbet)
            if Const.R_Free_Extra_Freespin in free_result.keys():
                freespin += free_result[Const.R_Free_Extra_Freespin]

            free_win_amount += free_result[Const.R_Win_Amount]
            free_result[Const.R_Free_Win_Amount] = copy.deepcopy(free_win_amount)
            free[free_recoder] = free_result

        return free,free_win_amount,wheel_award


    def paidspin(self, totalbet):
        result = {}
        reel,reel_pos = GetReelPos(Free_ReelSets[0], Config.Const.C_Shape).get_reel()

        reel = self.sym_level_up(reel)

        show_reel, deal_reel = self.gold_change(reel, reel_pos)


        result[Const.R_Reel] = show_reel

        self.special_sym_count(show_reel,Config.Wild_Mul['free'])
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)
        result[Const.R_Line],result[Const.R_Line_WinAmount] = Slot.WayLineEvaluator(Config.Const.C_Paytable, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild, totalbet, Config.Const.C_BetLine, deal_reel).evaluate_wild_mul(self.self_data[Const.R_Wild_Pos])
        sc_num = len(self.self_data[Const.R_Scatter_Pos])

        if sc_num >= 2:
            free_extra_set = Config.Const.C_Feature_Trigger[Const.C_FreeGame][Const.C_Re_Trigger_FreeSpins]

            free_extra = free_extra_set[sc_num]
            result[Const.R_Scatter_Win] = Config.Const.C_Paytable[Config.Scatter][sc_num - 1] * totalbet
            result[Const.R_Win_Amount] = result[Const.R_Line_WinAmount] + result[Const.R_Scatter_Win]
            result[Const.R_Free_Extra_Freespin] = free_extra
        else:
            result[Const.R_Win_Amount] = result[Const.R_Line_WinAmount]
        return result


    def sym_level_up(self,reel):
        level_set = Config.Const.C_Feature_Trigger[Const.C_FreeGame][Const.R_Sym_Change]
        sym_level_up = [False, False, False, False]

        if self.self_data[Const.R_Gold_Get] >= level_set[0]:
            sym_level_up[0] = True
        if self.self_data[Const.R_Gold_Get] >= level_set[1]:
            sym_level_up[1] = True
        if self.self_data[Const.R_Gold_Get] >= level_set[2]:
            sym_level_up[2] = True
        if self.self_data[Const.R_Gold_Get] >= level_set[3]:
            sym_level_up[3] = True

        for x in range(5):
            for y in range(4):
                if sym_level_up[0] is True:
                    if reel[x][y] == Config.H2:
                        reel[x][y] = Config.H1
                if sym_level_up[1] is True:
                    if reel[x][y] == Config.H3:
                        reel[x][y] = Config.H1
                if sym_level_up[2] is True:
                    if reel[x][y] == Config.H4:
                        reel[x][y] = Config.H1
                if sym_level_up[3] is True:
                    if reel[x][y] == Config.H5:
                        reel[x][y] = Config.H1
        return reel


    def gold_change(self,reel, reel_pos):

        deal_reel = copy.deepcopy(reel)
        show_reel = copy.deepcopy(reel)

        for x in range(5):
            for y in range(4):
                if reel[x][y] == Config.Gold_Buffalo:

                    gold_buffalo_pos = [x, reel_pos[x] + y]

                    if gold_buffalo_pos in self.gold_buffalo_pos:
                        deal_reel[x][y] = Config.H1

                        self.gold_buffalo_pos.remove(gold_buffalo_pos)
                        self.self_data[Const.R_Gold_Get] += 1

                    else:
                        deal_reel[x][y] = Config.H1
                        show_reel[x][y] = Config.H1

        return show_reel, deal_reel

    def special_sym_count(self,reel,wild_mul_weight):
        sc_pos = []
        wild_pos = {}
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                idx = y * 5 + x
                if reel[x][y] == Config.Scatter:
                    sc_pos.append(idx)
                if reel[x][y] == Config.Wild:
                    mul = Util.randdict(wild_mul_weight)
                    wild_pos[idx] = mul

        self.self_data[Const.R_Scatter_Pos] = sc_pos
        self.self_data[Const.R_Wild_Pos] = wild_pos

    def wheelprize(self,totalbet):
        wheel_get = get_wheel()
        mul = 0
        gold_buffalo_num = 0

        for i in wheel_get:
            if i["Kind"] == "Mul":
                mul += i["Extra"]
            elif i["Kind"] == "Gold":
                gold_buffalo_num += i["Extra"]
            elif i["Kind"] in ["Grand", "Major"]:
                mul += i["Extra"]

        self.self_data[Const.R_Wheel_Prize] = mul * totalbet
        self.self_data[Const.R_Gold_Get] = gold_buffalo_num
        self.gold_buffalo_pos = random.sample(self.gold_buffalo_pos, 15 - gold_buffalo_num)


    def get_buffalo(self):
        buffalo_list = []
        DealReelStrip = Free_ReelSets[0][Const.R_Dealed_ReelStrip]
        for x in range(5):
            for y in range(len(DealReelStrip[x][Const.R_Symbol_List])):
                if DealReelStrip[x][Const.R_Symbol_List][y] == Config.Gold_Buffalo:
                    buffalo_list.append([x,y])
        return buffalo_list



def get_wheel():
    get_list = []

    wheel_1 = Util.randlist(Config.Wheel_Set["Level_1"])
    get_list.append(wheel_1)
    if wheel_1["Kind"] != "Free":
        wheel_2 = Util.randlist(Config.Wheel_Set["Level_2"])
        get_list.append(wheel_2)

        if wheel_2["Kind"] != "Free":
            wheel_3 = Util.randlist(Config.Wheel_Set["Level_3"])
            get_list.append(wheel_3)

            if wheel_3["Kind"] != "Free":
                wheel_4 = Util.randlist(Config.Wheel_Set["Level_4"])
                get_list.append(wheel_4)

                if wheel_4["Kind"] != "Free":
                    wheel_5 = Util.randlist(Config.Wheel_Set["Level_5"])
                    get_list.append(wheel_5)

                    return get_list
                else:
                    return get_list
            else:
                return get_list
        else:
            return get_list
    else:
        return get_list


class GetReelPos(Slot.GetReel):
    def get_reel(self):
        pos = self.GetPos()
        reel = []

        for reel_idx in range(len(pos)):
            long_reel = self.dealreel[reel_idx][Const.R_Symbol_List] + self.dealreel[reel_idx][Const.R_Symbol_List][0: self.shape[0]]
            reel.append(long_reel[pos[reel_idx]:pos[reel_idx] + self.shape[0]])

        if self.reelset[Const.C_Mystery] is not False:
            mystery_change = Util.randdict(self.reelset[Const.C_Mystery_Weight])
            for x in range(len(reel)):
                for y in range(len(reel[x])):
                    if reel[x][y] == self.reelset[Const.C_Mystery]:
                        reel[x][y] = mystery_change
        if self.reelset[Const.C_Shuffle] is True:
            random.shuffle(reel)
        return reel,pos



# if __name__ == "__main__":
#     FreeGame().paidspin(600)
#     ss = FreeGame().get_buffalo()
#     print(ss)
# #轮子的验证
#
#
# def sswheelprize():
#     wheel_get = get_wheel()
#     mul = 0
#     gold_buffalo_num = 0
#
#     for i in wheel_get:
#         if i["Kind"] == "Mul":
#             mul += i["Extra"]
#         elif i["Kind"] == "Gold":
#             gold_buffalo_num += i["Extra"]
#         elif i["Kind"] in ["Grand", "Major"]:
#             mul += i["Extra"]
#
#     return wheel_get,mul,gold_buffalo_num
#
#
# if __name__ == "__main__":
#     i = 0
#     aa = [0,0]
#     ss = {1: [0, 0],
#           2: [0, 0],
#           3: [0, 0],
#           4: [0, 0],
#           5: [0, 0],
#           }
#     while i < 10000000:
#         i += 1
#         wheel_get, mul, gold_num = sswheelprize()
#         ss[len(wheel_get)][0] += mul
#         ss[len(wheel_get)][1] += gold_num
#         aa[0] += mul
#         aa[1] += gold_num
#     print(ss)
#     print(aa)
