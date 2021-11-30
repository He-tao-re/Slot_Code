from Priatefunction import randomReel,randdict,JudgeComboKind,ComboInWinLine,AllCombo
import copy

Test_Time = 10000

free_reel_1=[	6, 7, 7, 7, 5, 5, 4, 4, 3, 3, 8, 2, 7, 5, 92, 8, 5, 7, 8, 5, 5, 8, 3, 3, 3, 5, 6, 92, 2, 7, 0, 8, 7, 5, 5, 8, 5, 5, 7, 4, 6, 8, 7, 8, 1, 6, 6, 4, 6, 7, 8, 4, 6, 5, 5, 3, 4, 4, 0, 6, 6, 8, 8, 7, 5, 5, 92, 8, 8, 1, 4, 8, 4, 4, 0, 6, 1, 1, 4, 4, 0, 4, 8, 8, 4, 5, 0, 4, 1, 6, 6, 92, 4, 6, 3, 6, 4, 3, 6, 6, 7, 4, 6, 6, 8, 8, 3, 3, 2, 2, 4, 	]
free_reel_2=[	6, 8, 7, 7, 5, 4, 4, 3, 3, 0, 0, 2, 6, 6, 7, 8, 7, 8, 6, 5, 0, 0, 3, 3, 5, 7, 0, 8, 7, 5, 5, 92, 8, 5, 5, 7, 4, 6, 8, 7, 2, 1, 6, 6, 92, 7, 8, 1, 6, 5, 3, 4, 2, 0, 6, 6, 8, 8, 7, 5, 92, 4, 8, 8, 1, 1, 4, 8, 2, 2, 1, 1, 4, 4, 5, 1, 1, 5, 5, 0, 0, 3, 6, 1, 6, 2, 3, 3, 2, 2, 3, 3, 1, 2, 5, 5, 2, 2, 7, 7, 3, 3, 2, 2, 4, 	]
free_reel_3=[	6, 7, 7, 7, 5, 4, 4, 3, 3, 8, 8, 2, 6, 7, 92, 7, 8, 6, 5, 4, 92, 5, 3, 5, 7, 0, 8, 7, 5, 5, 8, 8, 5, 5, 7, 4, 6, 8, 7, 92, 1, 6, 0, 6, 7, 92, 6, 5, 5, 3, 4, 0, 92, 6, 8, 7, 7, 5, 5, 7, 8, 8, 1, 1, 4, 8, 2, 2, 6, 6, 0, 0, 7, 2, 92, 8, 5, 0, 0, 3, 8, 1, 5, 6, 2, 3, 3, 2, 2, 8, 5, 1, 2, 5, 8, 8, 6, 6, 3, 3, 	]
free_reel_4=[	6, 7, 7, 7, 5, 5, 4, 4, 3, 3, 0, 8, 92, 2, 6, 7, 8, 0, 7, 8, 6, 5, 8, 0, 3, 3, 5, 7, 0, 8, 7, 7, 5, 5, 92, 8, 5, 5, 7, 4, 6, 8, 7, 8, 1, 6, 0, 6, 92, 8, 1, 6, 5, 5, 3, 4, 2, 0, 6, 6, 8, 8, 7, 5, 5, 92, 8, 8, 1, 1, 4, 8, 5, 5, 4, 5, 6, 6, 0, 0, 7, 2, 6, 6, 5, 0, 0, 3, 8, 1, 5, 92, 7, 3, 3, 2, 2, 7, 7, 5, 1, 1, 2, 2, 5, 5, 8, 8, 7, 7, 3, 3, 2, 2, 4, 	]
free_reel_5=[	6, 7, 7, 7, 5, 5, 4, 4, 3, 3, 8, 92, 8, 2, 6, 7, 8, 5, 7, 8, 92, 6, 5, 8, 0, 3, 3, 5, 92, 0, 8, 7, 5, 5, 92, 8, 5, 5, 7, 4, 6, 8, 7, 8, 1, 6, 6, 0, 6, 7, 8, 1, 6, 5, 5, 3, 4, 2, 0, 6, 6, 8, 8, 7, 5, 5, 92, 8, 8, 1, 1, 4, 8, 5, 5, 4, 4, 6, 6, 5, 5, 4, 2, 6, 6, 5, 0, 0, 3, 6, 5, 5, 92, 7, 3, 3, 2, 2, 7, 7, 5, 1, 7, 8, 1, 5, 5, 3, 3, 5, 5, 3, 3, 2, 2, 4, 	]

Free_reel = [free_reel_1,free_reel_2,free_reel_3,free_reel_4,free_reel_5]

a = [0 for i in range(500)]

Paytable = [[5,20,50,200],[0,15,40,150],[0,12,30,100],[0,12,30,100],[0,10,20,50],
            [0,10,20,50],[0,8,15,30],[0,5,10,20],[0,5,10,20]]
WildPay = [10,20,100,500]


Payline=([1,1,1,1,1],[0,0,0,0,0],[2,2,2,2,2],[0,1,2,1,0],[2,1,0,1,2],[1,0,0,0,1],[1,2,2,2,1],[0,0,1,2,2],[2,2,1,0,0],[1,2,1,0,1],[1,0,1,2,1],[0,1,1,1,0],[2,1,1,1,2],[0,1,0,1,0],[2,1,2,1,2],[1,1,0,1,1],[1,1,2,1,1],[0,0,2,0,0],[2,2,0,2,2],[0,2,2,2,0],[2,0,0,0,2],[1,2,0,2,1],[1,0,2,0,1],[0,2,0,2,0],[2,0,2,0,2],[2,0,1,2,0],[0,2,1,0,2],[0,2,1,2,0],[2,0,1,0,2],[2,1,0,0,1],[0,1,2,2,1],[0,0,2,2,2],[2,2,0,0,0],[1,0,2,1,2],[1,2,0,1,0],[0,1,0,1,2],[2,1,2,1,0],[1,2,2,0,0],[0,0,1,1,2],[2,2,1,1,0],[2,0,0,0,0],[0,2,2,2,2],[2,2,2,2,0],[0,0,0,0,2],[1,0,1,0,1],[1,2,1,2,1],[0,1,2,2,2],[2,1,0,0,0],[0,1,1,1,1],[2,1,1,1,1])


WildChange_AllCombo = AllCombo(15,3,5)
WildChange_AllCombo_Judged = JudgeComboKind(WildChange_AllCombo,Paytable,WildPay)

Line_bet = 1
Total_bet = 50
AllSpinWin = 0
lock = 0
win10 = 0


AllWin = 0
test_time = 0
while test_time<Test_Time:
    '''进度打印'''
    test_time = test_time + 1
    if test_time%(Test_Time/20) == 0:
        progress = test_time/Test_Time*100
        progress = int(progress)
        print(str(progress)+"%")

    LockwildWin = 0
    LockwildHit = 0
    LockWild = {}
    Wild_reel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    Times = 10
    while Times > 0:
        LockedWild = 0
        SpinWin = 0
        Times = Times - 1
        lockwild_result = randomReel(Free_reel)
        final_lockwild_result = copy.deepcopy(lockwild_result)

        for x in range(5):
            for y in range(3):
                if lockwild_result[x][y] == 92:
                    Wild_reel[x][y] = 1

        for x in range(5):
            for y in range(3):
                if Wild_reel[x][y] == 1:
                    final_lockwild_result[x][y] = 92

        ComboInWinLine_lockwild = ComboInWinLine(final_lockwild_result, Payline)
        for combo in ComboInWinLine_lockwild:
            strcombo = str(combo)
            Kinds = WildChange_AllCombo_Judged[strcombo]
            SpinWin = SpinWin + Line_bet * Kinds[1]
        LockwildWin = LockwildWin + SpinWin
        if SpinWin != 0:
            LockwildHit = LockwildHit + 1
        for i in range(5):
            LockedWild = LockedWild + sum(Wild_reel[i])
        lock = lock + LockedWild
        if Times == 0:
            win10 = win10 + SpinWin





        AllSpinWin = AllSpinWin + SpinWin
    x = int(LockwildWin/Total_bet/10)
    a[x] = a[x] + 1


print(AllSpinWin/Test_Time/Total_bet)
print(win10/Test_Time/Total_bet)
print(lock/Test_Time)
