import random
import copy
import json
import Games.Game_10048_BeerGirl.BeerGirl_Config as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import Games.Game_10048_BeerGirl.static_data_10048 as static_data


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
    def __init__(self,game_data):
        self.game_data = game_data

    def paidspin(self,totalbet):

        result = {}
        reel_idx = Util.randdict(Config.Base_Reel_Choose)
        reel = Slot.GetReel(Base_ReelSets[reel_idx], Config.Const.C_Shape).get_reel()

        # Wild feature下的Bonus图标变成L5（展示）不影响RTP
        reel = self.bonus_change(reel)
        # Scatter 图标统计
        sc_num,sc_pos = scatter_count(reel)

        self.bonus_collect(reel)

        reel = self.wild_feature(reel)

        result[Const.R_Reel] = reel
        result[Const.R_Game_Data] = copy.deepcopy(self.game_data)


        if sc_num >= 1:
            sc_win = totalbet * Config.Const.C_Paytable[Config.Scatter][sc_num-1]
        else:
            sc_win = 0


        result.update(Slot.StandardLineEvaluator(totalbet,reel,Config.Const.C_PayLine, Config.Const.C_Paytable,
                                                 Config.Const.C_BetLine, Config.Const.C_Wild_Sub, Config.Const.C_LineSym,
                                                 Config.Wilds, Config.Wild).evaluate())
        result[Const.R_Scatter_Win] = sc_win
        result[Const.R_Win_Amount] += sc_win


        # if sc_num >= 3:
        #     # result[Const.R_Free], result[Const.R_Free_Win_Amount] = FreeGame(self_data=self.self_data,freespins=10).free(totalbet)
        #     pass


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

        for line in result[Const.R_Line]:
            kind = line[Const.R_Line_Kind]
            line_win = line[Const.R_Line_Win]
            line_long = line[Const.R_Line_Long]
            s_data[Const.S_Base_Sym_Win][kind][line_long-1] += line_win

        # print(json.dumps(result))

        return result


    def bonus_change(self,reel):
        for x in range(len(reel)):
            for y in range(len(reel[x])):
                if reel[x][y] == Config.Bonus and self.game_data[Const.R_Collect_Data][0][x] == 2:
                    reel[x][y] = Config.L5
        return reel


    def bonus_collect(self,reel):

        for x in range(5):
            for y in range(4):
                if reel[x][y] == Config.Bonus and self.game_data[Const.R_Collect_Data][0][x] != 2:
                    self.game_data[Const.R_Collect_Data][0][x] += 1

            if self.game_data[Const.R_Collect_Data][0][x] == 2 and self.game_data[Const.R_Collect_Data][1][x] == 0:
                self.game_data[Const.R_Collect_Data][1][x] = 2

    def wild_feature(self,reel):

        for x in range(5):
            if self.game_data[Const.R_Collect_Data][1][x] > 0:
                reel[x] = [Config.Wild,Config.Wild,Config.Wild,Config.Wild]
                self.game_data[Const.R_Collect_Data][1][x] -= 1

                if self.game_data[Const.R_Collect_Data][1][x] == 0:
                    self.game_data[Const.R_Collect_Data][0][x] = 0

        return reel



