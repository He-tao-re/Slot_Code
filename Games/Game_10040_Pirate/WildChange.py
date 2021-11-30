from Priatefunction import randomReel,randdict,JudgeComboKind,ComboInWinLine,AllCombo



Test_Time = 1000000

free_reel_1=[	6, 6, 7, 7, 5, 5, 4, 4, 7, 7, 8, 2, 7, 5, 92, 8, 5, 7, 8, 5, 5, 8, 8, 3, 3, 5, 6, 6, 1, 7, 0, 8, 7, 5, 7, 8, 5, 6, 7, 4, 6, 8, 7, 8, 0, 0, 8, 4, 6, 7, 8, 4, 6, 7, 7, 1, 4, 4, 0, 6, 6, 8, 8, 0, 0, 7, 92, 8, 8, 	]
free_reel_2=[	6, 6, 7, 7, 4, 4, 4, 3, 3, 0, 0, 2, 6, 8, 8, 7, 6, 6, 5, 5, 92, 3, 3, 5, 7, 8, 8, 3, 3, 5, 92, 5, 5, 7, 4, 4, 6, 6, 7, 2, 2, 6, 92, 7, 7, 8, 6, 6, 5, 4, 4, 2, 92, 6, 6, 5, 8, 7, 4, 92, 4, 8, 8, 1, 1, 8, 8, 	]
free_reel_3=[	6, 6, 7, 7, 4, 4, 4, 3, 3, 8, 2, 2, 6, 6, 8, 7, 7, 6, 5, 5, 92, 3, 7, 7, 0, 0, 7, 5, 5, 8, 8, 5, 5, 7, 7, 6, 8, 8, 92, 1, 6, 3, 3, 7, 92, 6, 5, 5, 3, 0, 0, 92, 6, 8, 7, 7, 5, 5, 7, 8, 1, 1, 7, 7, 8, 2, 2, 6, 6, 0, 0, 7, 	]
free_reel_4=[	6, 6, 7, 7, 6, 6, 7, 3, 3, 6, 6, 8, 92, 2, 6, 7, 7, 0, 7, 7, 92, 5, 8, 8, 3, 3, 7, 7, 0, 0, 7, 7, 5, 5, 92, 8, 5, 5, 7, 7, 6, 8, 4, 4, 1, 6, 3, 3, 92, 8, 1, 5, 5, 3, 3, 4, 2, 2, 6, 6, 8, 8, 7, 7, 5, 5, 8, 8, 1, 1, 4, 5, 5, 	]
free_reel_5=[	6, 6, 7, 7, 5, 5, 7, 7, 3, 3, 8, 92, 8, 2, 2, 8, 8, 5, 7, 8, 92, 6, 5, 5, 0, 3, 3, 5, 92, 0, 8, 7, 5, 5, 92, 8, 5, 5, 4, 4, 6, 8, 3, 3, 1, 6, 0, 0, 6, 7, 1, 1, 6, 5, 5, 3, 4, 2, 2, 6, 6, 8, 8, 7, 5, 5, 92, 8, 8, 1, 1, 4, 8, 	]

Free_reel=[free_reel_1,free_reel_2,free_reel_3,free_reel_4,free_reel_5]

Paytable = [[5,20,50,200],[0,15,40,150],[0,12,30,100],[0,12,30,100],[0,10,20,50],
            [0,10,20,50],[0,8,15,30],[0,5,10,20],[0,5,10,20]]
WildPay = [10,20,100,500]

Payline=([1,1,1,1,1],[0,0,0,0,0],[2,2,2,2,2],[0,1,2,1,0],[2,1,0,1,2],[1,0,0,0,1],[1,2,2,2,1],[0,0,1,2,2],[2,2,1,0,0],[1,2,1,0,1],[1,0,1,2,1],[0,1,1,1,0],[2,1,1,1,2],[0,1,0,1,0],[2,1,2,1,2],[1,1,0,1,1],[1,1,2,1,1],[0,0,2,0,0],[2,2,0,2,2],[0,2,2,2,0],[2,0,0,0,2],[1,2,0,2,1],[1,0,2,0,1],[0,2,0,2,0],[2,0,2,0,2],[2,0,1,2,0],[0,2,1,0,2],[0,2,1,2,0],[2,0,1,0,2],[2,1,0,0,1],[0,1,2,2,1],[0,0,2,2,2],[2,2,0,0,0],[1,0,2,1,2],[1,2,0,1,0],[0,1,0,1,2],[2,1,2,1,0],[1,2,2,0,0],[0,0,1,1,2],[2,2,1,1,0],[2,0,0,0,0],[0,2,2,2,2],[2,2,2,2,0],[0,0,0,0,2],[1,0,1,0,1],[1,2,1,2,1],[0,1,2,2,2],[2,1,0,0,0],[0,1,1,1,1],[2,1,1,1,1])

symchangeweight = {0: 15, 1: 15, 2: 15, 3: 10, 4: 10, 5: 10, 6: 5, 7: 5, 8: 5}

WildChange_AllCombo = AllCombo(11,3,5)
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
    spinresult = randomReel(Free_reel)
    symcount = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for x in range(5):
        for y in range(3):
            if spinresult[x][y] != 92:
                sym = spinresult[x][y]
                symcount[sym] += 1

    changesym = randdict(symcount)
    # print(symcount,changesym)
    # print(spinresult)
    for x in range(5):
        for y in range(3):
            if spinresult[x][y] == changesym:
                spinresult[x][y] = 92
    # print(spinresult)
    '''base算钱'''
    ComboInWinLine_BASE = ComboInWinLine(spinresult, Payline)
    for combo in ComboInWinLine_BASE:
        strcombo = str(combo)
        Kinds = WildChange_AllCombo_Judged[strcombo]
        SpinWin = SpinWin + Line_bet*Kinds[1]

print(SpinWin/Test_Time/Total_bet)

