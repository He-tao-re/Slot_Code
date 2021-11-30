import random
def randomReel(reel):   #按照3*5的盘面对卷轴进行随机，得到一次spin的轮盘结果
    result=[]
    for i in range(5):
        j=random.randint(0,len(reel[i])-1)
        if j == len(reel[i])-1:
            row=[reel[i][j],reel[i][0],reel[i][1]]
        elif j==len(reel[i])-2:
            row=[reel[i][j],reel[i][j+1],reel[i][0]]
        else:
            row=reel[i][j:j+3]
        result.append(row)
    return result

def randdict(onedict):
    Total_Weight=sum(onedict.values())
    ra=random.randint(0,Total_Weight-1)

    curr_sum=0
    keys=onedict.keys()
    multiply=None
    for k in keys:
        curr_sum=curr_sum+onedict[k]
        if ra<curr_sum:
            multiply = k
            break
    return multiply

def ComboInWinLine(result,Payline):    #获取输出结果，按照赢钱线，提取
    OneLine=[]
    AllWinLineCombo=[]
    for i in Payline:
        OneLine=[result[0][i[0]],result[1][i[1]],result[2][i[2]],result[3][i[3]],result[4][i[4]]]
        AllWinLineCombo.append(OneLine)
    return AllWinLineCombo

def WildMoveComboInWinLine(result,wildreel,Payline):    #获取输出结果，按照赢钱线，提取
    OneLine=[]
    wildline = []
    AllWinLineCombo=[]
    for i in Payline:
        OneLine=[result[0][i[0]],result[1][i[1]],result[2][i[2]],result[3][i[3]],result[4][i[4]]]
        wildline = [wildreel[0][i[0]],wildreel[1][i[1]],wildreel[2][i[2]],wildreel[3][i[3]],wildreel[4][i[4]]]
        AllWinLineCombo.append([OneLine,wildline])
    return AllWinLineCombo

def AllCombo(NumberOf_sym,row,col):
    combo=[]
    for i in range(NumberOf_sym):
        for j in range(NumberOf_sym):
            for k in range(NumberOf_sym):
                for m in range(NumberOf_sym):
                    for n in range(NumberOf_sym):
                        one_combo=[i,j,k,m,n]
                        for x in range(col):
                            if one_combo[x]==9:one_combo[x]=90
                            if one_combo[x]==10:one_combo[x]=92


                        combo.append(one_combo)
    return combo


def JudgeComboKind(AllCombo,Paytable,WildPay):
    AllComboWith_Mul = {}

    for LineCombo in AllCombo:
        Kind = [0,0,0]
        if LineCombo[0] in [0,1,2,3,4,5,6,7,8]:
            if LineCombo[0] == LineCombo[1] or LineCombo[1] == 92:
                Kind[0] = 2
                Kind[1] = Paytable[LineCombo[0]][0]
                Kind[2] = LineCombo[0]
                if LineCombo[0] == LineCombo[2] or LineCombo[2] == 92:
                    Kind[0] = 3
                    Kind[1] = Paytable[LineCombo[0]][1]
                    Kind[2] = LineCombo[0]
                    if LineCombo[0] == LineCombo[3] or LineCombo[3] == 92:
                        Kind[0] = 4
                        Kind[1] = Paytable[LineCombo[0]][2]
                        Kind[2] = LineCombo[0]
                        if LineCombo[0] == LineCombo[4] or LineCombo[4] == 92:
                            Kind[0] = 5
                            Kind[1] = Paytable[LineCombo[0]][3]
                            Kind[2] = LineCombo[0]
        elif LineCombo[0] == 90:
            pass
        elif LineCombo[0] == 95:
            pass
        elif LineCombo[0] == 99:
            pass
        elif LineCombo[0] == 92:
            if LineCombo[1] in [0,1,2,3,4,5,6,7,8]:
                Kind[0] = 2
                Kind[1] = Paytable[LineCombo[1]][0]
                Kind[2] = LineCombo[1]
                if LineCombo[1] == LineCombo[2] or LineCombo[2] == 92:
                    Kind[0] = 3
                    Kind[1] = Paytable[LineCombo[1]][1]
                    Kind[2] = LineCombo[1]
                    if LineCombo[1] == LineCombo[3] or LineCombo[3] == 92:
                        Kind[0] = 4
                        Kind[1] = Paytable[LineCombo[1]][2]
                        Kind[2] = LineCombo[1]
                        if LineCombo[1] == LineCombo[4] or LineCombo[4] == 92:
                            Kind[0] = 5
                            Kind[1] = Paytable[LineCombo[1]][3]
                            Kind[2] = LineCombo[1]
            elif LineCombo[1] == 92:
                Kind[0] = 2
                Kind[1] = WildPay[0]
                Kind[2] = 92
                if LineCombo[2] in [0,1,2,3,4,5,6,7,8]:
                    if Paytable[LineCombo[2]][1] >= Kind[1]:
                        Kind[0] = 3
                        Kind[1] = Paytable[LineCombo[2]][1]
                        Kind[2] = LineCombo[2]
                    if LineCombo[2] == LineCombo[3] or LineCombo[3] == 92:
                        if Paytable[LineCombo[2]][2] >= Kind[1]:
                            Kind[0] = 4
                            Kind[1] = Paytable[LineCombo[2]][2]
                            Kind[2] = LineCombo[2]
                    if LineCombo[2] == LineCombo[3] or LineCombo[3] == 92:
                        if LineCombo[2] == LineCombo[4] or LineCombo[4] ==92:
                            if Paytable[LineCombo[2]][3] >= Kind[1]:
                                Kind[0] = 5
                                Kind[1] = Paytable[LineCombo[2]][3]
                                Kind[2] = LineCombo[2]


                elif LineCombo[2] == 92:
                    Kind[0] = 3
                    Kind[1] = WildPay[1]
                    Kind[2] = 92
                    if LineCombo[3] in [0,1,2,3,4,5,6,7,8]:
                        if Paytable[LineCombo[3]][2] >= Kind[1]:
                            Kind[0] = 4
                            Kind[1] = Paytable[LineCombo[3]][2]
                            Kind[2] = LineCombo[3]
                        if LineCombo[3] == LineCombo[4] or LineCombo[4] == 92:
                            if Paytable[LineCombo[3]][3] >= Kind[1]:
                                Kind[0] = 5
                                Kind[1] = Paytable[LineCombo[3]][3]
                                Kind[2] = LineCombo[3]
                    elif LineCombo[3] == 92:
                        Kind[0] = 4
                        Kind[1] = WildPay[2]
                        Kind[2] = 92
                        if LineCombo[4] in [0,1,2,3,4,5,6,7,8]:
                            if Paytable[LineCombo[4]][3] >= Kind[1]:
                                Kind[0] = 5
                                Kind[1] = Paytable[LineCombo[4]][3]
                                Kind[2] = LineCombo[4]
                        elif LineCombo[4] == 92:
                            Kind[0] = 5
                            Kind[1] = WildPay[3]
                            Kind[2] = 92
#==============================================================================
        StrLineCombo=str(LineCombo)
        AllComboWith_Mul[StrLineCombo]=Kind

    return AllComboWith_Mul
