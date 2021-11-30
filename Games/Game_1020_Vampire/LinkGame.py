import copy

import Slot_common.Slots as Slot
import Slot_common.Const as Const
import util.Util as Util
import Games.Game_1020_Vampire.LinkReel as Config


Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)



test_times = 10000
times = 0

total_mul = 0
mul_1 = 0
mul_2 = 0
mul_3 = 0
mul_4 = 0
bonus_static = [0,0,0,0,0,0]
extra_count = [0,0,0,0,0,0]

if __name__ == '__main__':
    while times < test_times:
        times += 1

        ReelSet = copy.deepcopy(Base_ReelSets)

        stripe_choose = [
            0,
            Util.randlist(Config.reel_strip_choose[0]),
            Util.randlist(Config.reel_strip_choose[1]),
            Util.randlist(Config.reel_strip_choose[2]),
            Util.randlist(Config.reel_strip_choose[3]),
            Util.randlist(Config.reel_strip_choose[4]),
        ]
        ReelSet[0][Const.R_Dealed_ReelStrip] = [
            Base_ReelSets[0][Const.R_Dealed_ReelStrip][stripe_choose[0]],
            Base_ReelSets[0][Const.R_Dealed_ReelStrip][stripe_choose[1]-1],
            Base_ReelSets[0][Const.R_Dealed_ReelStrip][stripe_choose[2]-1],
            Base_ReelSets[0][Const.R_Dealed_ReelStrip][stripe_choose[3]-1],
            Base_ReelSets[0][Const.R_Dealed_ReelStrip][stripe_choose[4]-1],
            Base_ReelSets[0][Const.R_Dealed_ReelStrip][stripe_choose[5]-1]
        ]
        reel = Slot.GetReel(ReelSet[0],[3,4,4,4,4,4]).get_reel()

        mul = 0

        bonus_dic = {}

        bonus_dic[1] = {}
        bonus_dic[2] = {}
        bonus_dic[3] = {}
        bonus_dic[4] = {}
        bonus_dic[5] = {}

        for x in range(len(reel[1])):
            if reel[1][x] == 94:
                bonus_dic[1][x] = Util.randdict(Config.bonus_award)

        for x in range(len(reel[2])):
            if reel[2][x] == 94:
                bonus_dic[2][x] = Util.randdict(Config.bonus_award)

        for x in range(len(reel[3])):
            if reel[3][x] == 94:
                bonus_dic[3][x] = Util.randdict(Config.bonus_award)

        for x in range(len(reel[4])):
            if reel[4][x] == 94:
                bonus_dic[4][x] = Util.randdict(Config.bonus_award)

        for x in range(len(reel[5])):
            if reel[5][x] == 95:
                bonus_dic[5][x] = 1

        win_mul = 0
        long = 0
        if len(bonus_dic[1].keys()) > 0:
            win_mul += sum(bonus_dic[1].values())
            long = 1
            if len(bonus_dic[2].keys()) > 0:
                win_mul += sum(bonus_dic[2].values())
                long = 2
                if len(bonus_dic[3].keys()) > 0:
                    win_mul += sum(bonus_dic[3].values())
                    long = 3
                    if len(bonus_dic[4].keys()) > 0:
                        win_mul += sum(bonus_dic[4].values())
                        long = 4
                        if len(bonus_dic[5].keys()) > 0:
                            win_mul = win_mul * sum(bonus_dic[5].values()) * 2
                            long = 5
                        if len(bonus_dic[5].keys()) == 0:
                            extra_count[0] += win_mul
                        elif len(bonus_dic[5].keys()) == 1:
                            extra_count[1] += win_mul
                        elif len(bonus_dic[5].keys()) == 2:
                            extra_count[2] += win_mul
                        elif len(bonus_dic[5].keys()) == 3:
                            extra_count[3] += win_mul

        if long < 4:
            extra_count[0] += win_mul
        bonus_static[long] += win_mul
        total_mul += win_mul

print("平均倍数：{}".format(total_mul / test_times))

for i in extra_count:
    print(i/test_times)

print("end win")
for mul in bonus_static:
    print(mul / test_times)

