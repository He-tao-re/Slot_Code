import random
import copy
import json
import Games.Game_10043_Meimaid.Mermaid_Config as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import Games.Game_10043_Meimaid.static_data_10043 as static_data


Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)

s_data = static_data.data


def scatter_count(reel):
    sc_num = 0
    sc_pos = []

    for x in range(len(reel)):
        for y in range(len(reel[x])):
            if reel[x][y] == Config.Scatter:
                sc_num += 1
                sc_pos.append([x,y])

    return sc_num,sc_pos


class GameSlot(object):
    def __init__(self,self_data):
        self.self_data = self_data

    def paidspin(self,totalbet):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel


        self.special_sym_count(reel)


        #Scatter Win
        sc_num = len(self.self_data[Const.R_Scatter_Pos])
        if sc_num >= 1:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0


        result[Const.R_Line],result[Const.R_Win_Amount] = Slot.WayLineEvaluator(Config.Const.C_Paytable, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild, totalbet, Config.Const.C_BetLine, reel).evaluate()

        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)



        if sc_num >= 3:
            result[Const.R_Free], result[Const.R_Free_Win_Amount] = FreeGame(self_data=self.self_data,freespins=10).free(totalbet)
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

        # for line in result[Const.R_Line]:
        #     kind = line[Const.R_Line_Kind]
        #     line_win = line[Const.R_Line_Win]
        #     line_long = line[Const.R_Line_Long]
        #     s_data[Const.S_Base_Sym_Win][kind][line_long-1] += line_win





        # print(json.dumps(result))
        return result

    def special_sym_count(self,reel):
        sc_pos = []
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                idx = y * 5 + x
                if reel[x][y] == Config.Scatter:
                    sc_pos.append([x,y])

        self.self_data[Const.R_Scatter_Pos] = sc_pos


class FreeGame(object):
    def __init__(self,self_data,freespins):
        self.self_data = self_data
        self.freespins = freespins

        self.sc_mark = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]



    def free_begin(self):
        sc_pos = self.self_data[Const.R_Scatter_Pos]
        for pos in sc_pos:
            x = pos[0]
            y = pos[1]
            self.sc_mark[x][y] += 1

    def freespin(self,totalbet):
        result = {}
        reel_idx = 1
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        result[Const.R_Reel] = reel

        sc_num, sc_pos = scatter_count(reel)

        # Scatter Win

        if sc_num >= 1:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num - 1]
        else:
            sc_win = 0

        if sc_num >= 3:
            self.freespins += 3


        # print(reel,self.sc_mul)
        result[Const.R_Line],result[Const.R_Win_Amount] = Slot.WayLineEvaluator(Config.Const.C_Paytable, Config.Const.C_Wild_Sub, Config.Const.C_LineSym, Config.Wilds, Config.Wild, totalbet, Config.Const.C_BetLine, reel).evaluate()


        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win
        result[Const.R_Self_Data] = copy.deepcopy(self.self_data)

        """统计部分"""
        s_data[Const.S_FreeSpin] += 1


        return result


    def free(self,totalbet):

        free_result = {}

        free_recoder = 0

        free_win_amount = 0

        self.free_begin()
        while self.freespins > 0:
            free_recoder += 1
            self.freespins -= 1


            free_spin = self.freespin(totalbet)
            free_win_amount += free_spin[Const.R_Win_Amount]
            free_spin[Const.R_Free_Win_Amount] = copy.deepcopy(free_win_amount)
            # print(json.dumps(free_spin))
            free_result[free_recoder] = free_spin

        return free_result,free_win_amount
