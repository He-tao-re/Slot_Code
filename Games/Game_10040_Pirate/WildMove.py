from Games.Game_10040_Pirate.Priatefunction import randomReel,randdict,JudgeComboKind,WildMoveComboInWinLine,AllCombo
import random
import Games.Game_10040_Pirate.Pirate_config_100 as Config
import Slot_common.Slots as Slot
import util.Util as Util
import Slot_common.Const as Const
import copy

Test_Time = 10000

Base_ReelSets = Slot.DealReel().ReelStrip(Config.Const.C_Base_ReelSets)

Paytable = [
    [5,20,50,200],
    [0,15,40,150],
    [0,12,30,100],
    [0,10,20, 50],
    [0,10,20, 50],
    [0,8,15, 30],
    [0,8,15, 30],
    [0,5,10, 20],
    [0,5,10, 20],
]
WildPay = [10,20,100,500]

Payline=([1,1,1,1,1],[0,0,0,0,0],[2,2,2,2,2],[0,1,2,1,0],[2,1,0,1,2],[1,0,0,0,1],[1,2,2,2,1],[0,0,1,2,2],[2,2,1,0,0],[1,2,1,0,1],[1,0,1,2,1],[0,1,1,1,0],[2,1,1,1,2],[0,1,0,1,0],[2,1,2,1,2],[1,1,0,1,1],[1,1,2,1,1],[0,0,2,0,0],[2,2,0,2,2],[0,2,2,2,0],[2,0,0,0,2],[1,2,0,2,1],[1,0,2,0,1],[0,2,0,2,0],[2,0,2,0,2],[2,0,1,2,0],[0,2,1,0,2],[0,2,1,2,0],[2,0,1,0,2],[2,1,0,0,1],[0,1,2,2,1],[0,0,2,2,2],[2,2,0,0,0],[1,0,2,1,2],[1,2,0,1,0],[0,1,0,1,2],[2,1,2,1,0],[1,2,2,0,0],[0,0,1,1,2],[2,2,1,1,0],[2,0,0,0,0],[0,2,2,2,2],[2,2,2,2,0],[0,0,0,0,2],[1,0,1,0,1],[1,2,1,2,1],[0,1,2,2,2],[2,1,0,0,0],[0,1,1,1,1],[2,1,1,1,1])


WildChange_AllCombo = AllCombo(12,3,5)
WildChange_AllCombo_Judged = JudgeComboKind(WildChange_AllCombo,Paytable,WildPay)

Line_bet = 1
Total_bet = 50
SpinWin = 0

test_time = 0
while test_time<Test_Time:
    '''进度打印'''
    test_time = test_time + 1
    if test_time%(Test_Time/20) == 0:
        progress = test_time/Test_Time*100
        progress = int(progress)
        print(str(progress)+"%")
    fstime = 10
    wildposition = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while fstime > 0:
        fstime = fstime - 1
        spinresult = Slot.GetReel(Base_ReelSets[0], Config.Const.C_Shape).get_reel()

        '''wild 的位置改变'''
        wildnum1 = 3 - wildposition[1].count(0)

        def wildmove(reel1,reel2):
            reel1 = [0,0,0]
            for wi in reel2:
                if wi != 0:
                    a = random.randint(1,3) - 1
                    reel1[a] = reel1[a] + wi
            return reel1


        wildposition[0] = wildmove(wildposition[0], wildposition[1])
        wildposition[1] = wildmove(wildposition[1], wildposition[2])
        wildposition[2] = wildmove(wildposition[2], wildposition[3])
        wildposition[3] = wildmove(wildposition[3], wildposition[4])
        wildposition[4] = [0,0,0]
        for x in range(5):
            for y in range(3):
                if spinresult[x][y] == 92 and wildposition[x][y] == 0:
                    wildposition[x][y] = 1

        for x in range(5):
            for y in range(3):
                if wildposition[x][y] != 0:
                    spinresult[x][y] = 92
        '''base算钱'''
        ComboInWinLine_BASE = WildMoveComboInWinLine(spinresult, wildposition, Payline)
        for comboo in ComboInWinLine_BASE:
            combo = comboo[0]
            mul = comboo[1]
            double = mul.count(2)
            three = mul.count(3)
            strcombo = str(combo)
            Kinds = WildChange_AllCombo_Judged[strcombo]
            SpinWin = SpinWin + Line_bet*Kinds[1]*(2**double)*(3**three)

print(SpinWin/Test_Time/Total_bet)

