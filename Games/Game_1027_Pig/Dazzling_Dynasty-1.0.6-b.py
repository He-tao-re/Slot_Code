"""Dazzling Dynasty"""

Test_Time = 10000000
Select = 'Free'

test_time = 0

Total_Bet = 60
Line_bet = 1

All_Bet = 0
AllBaseWin = 0
SelectHit = 0
AllFeatureWin = 0
TriggerBonusNunber = 0
Grand_Hit = {'Base': 0, 'Feature': 0}
FeaturePro = {1: [0, 0.0002, 0.0005], 2: [0.08, 0.0, 0.0], 3: [0, 0.02, 0.08]}
Bonus_A_number = 0
Bonus_B_number = 0
Respin_time = 0
Freespin_time = 0
Swildnum = 0
Respin_Count = {6: {'hit': 0, 'prize': 0, 'win': 0}, 7: {'hit': 0, 'prize': 0, 'win': 0}, 8: {'hit': 0, 'prize': 0, 'win': 0},
                9: {'hit': 0, 'prize': 0, 'win': 0}, 10: {'hit': 0, 'prize': 0, 'win': 0}, 11: {'hit': 0, 'prize': 0, 'win': 0},
                12: {'hit': 0, 'prize': 0, 'win': 0}, 13: {'hit': 0, 'prize': 0, 'win': 0}, 14: {'hit': 0, 'prize': 0, 'win': 0},
                15: {'hit': 0, 'prize': 0, 'win': 0}}
EndNumberCount = {6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}
Symbol_win = {0: [0, 0, 0], 1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 5: [0, 0, 0], 6: [0, 0, 0],
              7: [0, 0, 0], 8: [0, 0, 0]}
base_reel_1 = [	5, 2, 3, 0, 0, 0, 2, 4, 5, 1, 6, 0, 4, 2, 5, 3, 6, 7, 0, 1, 1, 3, 6, 1, 1, 1, 6, 2, 0, 94, 94, 5, 1, 3, 5, 6, 2, 2, 2, 3, 1, 5, 6, 3, 3, 3, 7, 4, 1, 3, 3, 4, 4, 4, 5, 2, 1, 7, 4, 1, 2, 7, 4, 94, 94, 94, 4, 7, 	]
base_reel_2 = [	5, 2, 3, 0, 0, 0, 5, 4, 92, 0, 2, 2, 0, 6, 5, 0, 7, 92, 6, 1, 3, 0, 6, 1, 1, 1, 6, 2, 0, 94, 94, 94, 1, 0, 5, 6, 2, 2, 2, 3, 92, 0, 6, 3, 3, 3, 4, 92, 1, 5, 3, 4, 4, 4, 5, 2, 4, 7, 92, 6, 2, 7, 4, 94, 94, 94, 4, 7, 	]
base_reel_3 = [	5, 2, 3, 0, 0, 0, 7, 4, 0, 1, 3, 1, 0, 3, 5, 0, 4, 92, 6, 1, 4, 0, 5, 1, 1, 1, 5, 2, 0, 94, 94, 5, 1, 0, 5, 5, 2, 2, 2, 5, 92, 1, 6, 3, 3, 3, 2, 92, 1, 7, 3, 4, 4, 4, 6, 2, 6, 7, 92, 2, 2, 7, 4, 94, 94, 94, 4, 7, 	]
base_reel_4 = [	5, 2, 3, 0, 0, 0, 3, 4, 92, 1, 3, 0, 0, 4, 5, 0, 3, 92, 4, 3, 4, 0, 6, 1, 1, 1, 6, 2, 0, 94, 94, 5, 1, 0, 5, 6, 2, 2, 2, 3, 92, 7, 6, 3, 3, 3, 6, 92, 1, 1, 3, 4, 4, 4, 6, 1, 2, 7, 92, 1, 2, 7, 4, 94, 94, 94, 2, 7, 	]
base_reel_5 = [	5, 2, 3, 0, 0, 0, 2, 4, 2, 1, 0, 4, 0, 3, 5, 3, 1, 4, 0, 1, 4, 0, 6, 1, 1, 1, 6, 2, 0, 94, 94, 5, 1, 0, 5, 6, 2, 2, 2, 5, 1, 7, 6, 3, 3, 3, 6, 1, 1, 3, 3, 4, 4, 4, 6, 2, 6, 7, 3, 5, 2, 7, 4, 94, 94, 94, 4, 7, 	]


free_reel_1_1=[	0, 2, 3, 0, 0, 1, 2, 4, 0, 1, 1, 0, 4, 2, 0, 3, 3, 2, 0, 1, 1, 3, 3, 1, 1, 1, 3, 2, 0, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 3, 1, 0, 1, 3, 3, 3, 2, 3, 1, 3, 1, 1, 4, 4, 0, 2, 0, 2, 4, 1, 2, 2, 4, 2, 3, 4, 4, 2, 	]
free_reel_1_2=[	0, 2, 3, 0, 0, 0, 1, 4, 0, 0, 2, 2, 0, 3, 92, 1, 2, 2, 3, 1, 3, 3, 3, 1, 1, 1, 3, 2, 0, 1, 1, 0, 1, 0, 0, 1, 2, 2, 2, 3, 92, 0, 1, 3, 3, 3, 4, 0, 1, 0, 1, 1, 4, 4, 0, 2, 4, 2, 0, 1, 2, 2, 4, 2, 3, 4, 4, 2, 	]
free_reel_1_3=[	0, 2, 3, 0, 0, 0, 2, 4, 0, 1, 3, 1, 0, 3, 92, 0, 4, 2, 1, 1, 4, 3, 3, 1, 1, 1, 3, 2, 0, 0, 1, 0, 1, 0, 0, 0, 2, 2, 2, 0, 92, 0, 1, 3, 3, 3, 2, 3, 1, 2, 1, 1, 4, 4, 1, 2, 3, 2, 1, 2, 2, 2, 4, 2, 3, 4, 4, 2, 	]
free_reel_1_4=[	0, 2, 3, 0, 0, 0, 3, 4, 0, 1, 3, 0, 0, 4, 92, 0, 3, 2, 4, 3, 4, 3, 3, 1, 1, 1, 3, 2, 0, 0, 1, 0, 1, 0, 0, 1, 2, 2, 2, 3, 92, 0, 1, 3, 3, 3, 3, 3, 1, 1, 1, 1, 4, 4, 1, 1, 2, 2, 2, 1, 2, 2, 4, 2, 3, 4, 2, 2, 	]
free_reel_1_5=[	0, 2, 3, 0, 0, 0, 2, 4, 2, 1, 0, 4, 0, 3, 0, 3, 1, 4, 0, 1, 4, 0, 3, 1, 1, 1, 3, 2, 0, 1, 1, 0, 1, 0, 0, 1, 2, 2, 2, 0, 1, 2, 1, 3, 3, 3, 1, 1, 1, 3, 1, 1, 4, 4, 1, 2, 3, 2, 3, 0, 2, 2, 4, 2, 3, 4, 4, 2, 	]

free_reel_2_1=[	0, 2, 3, 0, 0, 0, 2, 4, 0, 1, 1, 0, 4, 2, 0, 3, 3, 2, 0, 1, 1, 3, 3, 1, 1, 1, 3, 2, 0, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 3, 1, 0, 1, 3, 3, 3, 2, 3, 1, 3, 1, 1, 4, 4, 0, 2, 0, 2, 4, 1, 2, 2, 4, 2, 3, 4, 4, 2, 	]
free_reel_2_2=[	0, 2, 3, 0, 0, 0, 0, 4, 92, 0, 2, 2, 0, 3, 0, 1, 2, 2, 3, 1, 3, 92, 0, 3, 1, 1, 1, 3, 2, 0, 92, 0, 1, 0, 3, 1, 2, 2, 2, 3, 92, 1, 3, 3, 3, 2, 1, 0, 1, 92, 92, 4, 4, 0, 2, 92, 4, 2, 0, 1, 2, 2, 4, 2, 3, 4, 4, 2, 	]
free_reel_2_3=[	0, 2, 3, 0, 0, 0, 2, 4, 92, 1, 3, 1, 0, 3, 0, 0, 4, 2, 1, 1, 4, 92, 0, 3, 1, 1, 1, 3, 2, 0, 92, 0, 1, 0, 3, 0, 2, 2, 2, 0, 92, 1, 3, 3, 3, 2, 1, 2, 1, 92, 92, 4, 4, 1, 2, 92, 3, 2, 1, 2, 2, 2, 4, 2, 3, 4, 4, 2, 	]
free_reel_2_4=[	0, 2, 3, 0, 0, 0, 3, 4, 92, 1, 3, 0, 0, 4, 0, 0, 3, 2, 4, 3, 4, 92, 0, 3, 1, 1, 1, 3, 2, 0, 92, 0, 1, 0, 3, 1, 2, 2, 2, 3, 92, 1, 3, 3, 3, 2, 1, 1, 1, 92, 92, 4, 4, 1, 1, 92, 2, 2, 2, 1, 2, 2, 4, 2, 3, 4, 2, 2, 	]
free_reel_2_5=[	0, 2, 3, 0, 0, 0, 2, 4, 2, 1, 0, 4, 0, 3, 0, 3, 1, 4, 0, 1, 4, 0, 3, 1, 1, 1, 3, 2, 0, 1, 1, 0, 1, 0, 0, 1, 2, 2, 2, 0, 1, 2, 1, 3, 3, 3, 1, 1, 1, 3, 1, 1, 4, 4, 1, 2, 3, 2, 3, 0, 2, 2, 4, 2, 3, 4, 4, 2, 	]


Base_reel = [base_reel_1, base_reel_2, base_reel_3, base_reel_4, base_reel_5]
Free_Reel_1 = [free_reel_1_1, free_reel_1_2, free_reel_1_3, free_reel_1_4, free_reel_1_5]
Free_Reel_2 = [free_reel_2_1, free_reel_2_2, free_reel_2_3, free_reel_2_4, free_reel_2_5]

Paytable = [[0, 25, 50, 150], [0, 15, 35, 100], [0, 12, 30, 75], [0, 10, 25, 60], [0, 8, 20, 50], [0, 5, 8, 15],
            [0, 5, 8, 15], [0, 5, 8, 15], [0, 5, 8, 15]]
Prize_on_Bonus = {10: 1, 2: 6, 1: 52, 50/60: 15, 40/60: 10, 30/60: 9, 20/60: 7}

from Dazzling_Dynasty_Def import randomReel
from Dazzling_Dynasty_Def import randdict
import datetime
import numpy as np
import random

P1 = {6: 6.892954866641233,
7: 5.885384158366278,
8: 4.971927014995778,
9: 4.055357226370679,
10: 9.822377781571909,
11: 13.422256097560975,
12: 5.6716417910447765,
13: 1, 14: 1.0}

stare_time = datetime.datetime.now()
while test_time < Test_Time:

    '''进度打印'''
    test_time = test_time + 1
    if test_time % (Test_Time / 20) == 0:
        progress = test_time / Test_Time * 100
        progress = int(progress)
        print(str(progress) + "%")
    All_Bet = All_Bet + Total_Bet
    Bonus_Number = 0
    spin_win = 0
    base_result = randomReel(Base_reel)
    symbol_combine = {}
    for i in base_result[0]:
        reel_1 = base_result[0].count(i)
        reel_2 = base_result[1].count(i) + base_result[1].count(92)
        reel_3 = base_result[2].count(i) + base_result[2].count(92)
        reel_4 = base_result[3].count(i) + base_result[3].count(92)
        reel_5 = base_result[4].count(i) + base_result[4].count(92)
        symbol_combine[i] = [reel_1, reel_2, reel_3, reel_4, reel_5]

    for key, value in symbol_combine.items():
        line_win = [0, 0]
        if key != 94:
            pay = Paytable[key]
            if value[1] != 0:
                line_win = [0, 0]
                if value[2] != 0:
                    line_win = [pay[1] * Line_bet * value[0] * value[1] * value[2], 3]
                    if value[3] != 0:
                        line_win = [pay[2] * Line_bet * value[0] * value[1] * value[2] * value[3], 4]
                        if value[4] != 0:
                            line_win = [pay[3] * Line_bet * value[0] * value[1] * value[2] * value[3] * value[4], 5]

            Symbol_win[key][line_win[1]-3] = Symbol_win[key][line_win[1]-3] + line_win[0]
            spin_win = spin_win + line_win[0]
    AllBaseWin = AllBaseWin + spin_win

    Bonus_Reel = [[0 for i in range(3)] for i in range(5)]
    for x in range(5):
        for y in range(3):
            if base_result[x][y] == 94:
                Bonus_Number = Bonus_Number + 1
                Bonus_Reel[x][y] = randdict(Prize_on_Bonus) * Total_Bet
    if Bonus_Number >= 6:

        TriggerBonusNunber = TriggerBonusNunber + Bonus_Number
        SelectHit = SelectHit + 1
        Bonus_Prize = np.sum(Bonus_Reel)
        if Select == 'Feature':
            Active = True
            RspinTime = 6
            Respin_Count[Bonus_Number]['hit'] = Respin_Count[Bonus_Number]['hit'] + 1
            Respin_Count[Bonus_Number]['prize'] = Respin_Count[Bonus_Number]['prize'] + Bonus_Prize
            # print('\n')
            # print(Bonus_Reel)
            if Bonus_Number <= 9:
                while Active:
                    RspinTime = RspinTime - 1
                    Respin_time = Respin_time + 1
                    Original_Blank_Positon = []
                    for x in range(5):
                        for y in range(3):
                            if Bonus_Reel[x][y] == 0:
                                Original_Blank_Positon.append([x, y])
                    random.shuffle(Original_Blank_Positon)
                    special_position_2 = [Original_Blank_Positon[0]]
                    special_position_1 = [Original_Blank_Positon.pop()]
                    normal_positon = Original_Blank_Positon

                    new_symbol = {'Bonus A': [], 'Bonus B': [], 'Plus': []}
                    # pp = random.random()
                    # # if pp < 0.3:
                    # #     new_symbol['Plus'].append(special_position_2)
                    for x in range(5):
                        for y in range(3):
                            if Bonus_Reel[x][y] == 0:
                                if [x, y] in special_position_1:
                                    postiton_pro = random.random()
                                    special_pro_1 = FeaturePro[1]
                                    if postiton_pro < special_pro_1[1]:
                                        new_symbol['Bonus A'].append([x, y])
                                    elif postiton_pro < special_pro_1[1] + special_pro_1[2] and postiton_pro > special_pro_1[1]:
                                        new_symbol['Bonus B'].append([x, y])

                                elif [x, y] in normal_positon:
                                    postiton_pro = random.random()
                                    normal_pro = FeaturePro[3]
                                    if postiton_pro < normal_pro[1]:
                                        new_symbol['Bonus A'].append([x, y])
                                    elif postiton_pro < normal_pro[1] + normal_pro[2] and postiton_pro > normal_pro[1]:
                                        new_symbol['Bonus B'].append([x, y])
                                if [x, y] in special_position_2:
                                    postiton_pro = random.random()
                                    special_pro_2 = FeaturePro[2]
                                    if postiton_pro < special_pro_2[0]:
                                        new_symbol['Plus'].append([x, y])
                    for position in new_symbol['Bonus B']:
                        x = position[0]
                        y = position[1]
                        superprize = Bonus_Prize
                        Bonus_Reel[x][y] = superprize
                    for position in new_symbol['Bonus A']:
                        x = position[0]
                        y = position[1]
                        superprize = np.sum(Bonus_Reel)
                        Bonus_Reel[x][y] = superprize
                    for position in new_symbol['Plus']:
                        RspinTime = RspinTime + 1
                    Bonus_A_number = Bonus_A_number + len(new_symbol['Bonus A'])
                    Bonus_B_number = Bonus_B_number + len(new_symbol['Bonus B'])
                    if RspinTime == 0:
                        Active = False
                    blank_position = 0
                    for x in range(5):
                        for y in range(3):
                            if Bonus_Reel[x][y] != 0:
                                blank_position = blank_position + 1
                    if blank_position == 15:
                        Grand_Hit['Feature'] += 1
                        Active = False
                    # print(Bonus_Reel, new_symbol)

            elif Bonus_Number <= 14:
                extra_mul = Bonus_Number - 9 + 1
                Respin_time = Respin_time + 1
                Original_Blank_Positon = []

                while Active:
                    RspinTime = RspinTime - 1
                    for x in range(5):
                        for y in range(3):
                            if Bonus_Reel[x][y] == 0:
                                Original_Blank_Positon.append([x, y])
                    random.shuffle(Original_Blank_Positon)
                    special_position_2 = [Original_Blank_Positon[0]]
                    special_position_1 = [Original_Blank_Positon.pop()]
                    normal_positon = Original_Blank_Positon
                    new_symbol = {'Bonus A': [], 'Bonus B': [], 'Plus': []}
                    for x in range(5):
                        for y in range(3):
                            if Bonus_Reel[x][y] == 0:
                                if [x, y] in special_position_1:
                                    postiton_pro = random.random()
                                    special_pro_1 = FeaturePro[1]
                                    if postiton_pro < special_pro_1[1]:
                                        new_symbol['Bonus A'].append([x, y])
                                    elif postiton_pro < special_pro_1[1] + special_pro_1[2]:
                                        new_symbol['Bonus B'].append([x, y])
                                elif [x, y] in special_position_2:
                                    postiton_pro = random.random()
                                    special_pro_2 = FeaturePro[2]
                                    if postiton_pro < special_pro_2[1]:
                                        new_symbol['Bonus A'].append([x, y])
                                    elif postiton_pro < special_pro_2[1] + special_pro_2[2]:
                                        new_symbol['Bonus B'].append([x, y])
                                    elif postiton_pro < special_pro_2[0] + special_pro_2[1] + special_pro_2[2]:
                                        new_symbol['Plus'].append([x, y])
                                elif [x, y] in normal_positon:
                                    postiton_pro = random.random()
                                    normal_pro = FeaturePro[3]
                                    if postiton_pro < normal_pro[1]:
                                        new_symbol['Bonus A'].append([x, y])
                                    elif postiton_pro < normal_pro[1] + normal_pro[2]:
                                        new_symbol['Bonus B'].append([x, y])
                    for position in new_symbol['Bonus B']:
                        x = position[0]
                        y = position[1]
                        Bonus_Reel[x][y] = (np.sum(Bonus_Reel)) * extra_mul
                    for position in new_symbol['Bonus A']:
                        x = position[0]
                        y = position[1]
                        superprize = (np.sum(Bonus_Reel)) * extra_mul
                        Bonus_Reel[x][y] = superprize
                    for position in new_symbol['Plus']:

                        RspinTime = RspinTime + 1

                    Bonus_A_number = Bonus_A_number + len(new_symbol['Bonus A'])
                    Bonus_B_number = Bonus_B_number + len(new_symbol['Bonus B'])
                    if RspinTime == 0:
                        Active = False
                    blank_position = 0
                    for x in range(5):
                        for y in range(3):
                            if Bonus_Reel[x][y] != 0:
                                blank_position = blank_position + 1
                    if blank_position == 15:
                        Grand_Hit['Feature'] += 1
                        Active = False
            elif Bonus_Number == 15:
                Grand_Hit['Base'] += 1
                pass
            Feature_win = np.sum(Bonus_Reel)
            EndNumberCount[blank_position] = EndNumberCount[blank_position] + 1
            Respin_Count[Bonus_Number]['win'] = Respin_Count[Bonus_Number]['win'] + Feature_win
            AllFeatureWin = AllFeatureWin + np.sum(Bonus_Reel)

        elif Select == 'Free':
            sym_mul = Bonus_Prize / Total_Bet
            freeselect = (sym_mul * P1[Bonus_Number]-24.24749082-7.738085193*sym_mul)/(13.99042262+2.210881484*sym_mul-24.24749082-7.738085193*sym_mul)
            # print(Bonus_Number, sym_mul, freeselect)

            freespin = 8
            special_wild_win = 0
            wild_number_in_free = 0
            free_spin_win = 0
            while freespin > 0 :
                Freespin_time += 1
                freespin = freespin - 1
                freespin_win = 0
                speical_wild_number = 0
                p = random.random()
                if p < freeselect:
                    Free_Reel = Free_Reel_1
                else:
                    Free_Reel = Free_Reel_2
                freeresult = randomReel(Free_Reel)
                symbol_combine = {}
                for i in freeresult[0]:
                    reel_1 = freeresult[0].count(i)
                    reel_2 = freeresult[1].count(i) + freeresult[1].count(92)
                    reel_3 = freeresult[2].count(i) + freeresult[2].count(92)
                    reel_4 = freeresult[3].count(i) + freeresult[3].count(92)
                    reel_5 = freeresult[4].count(i) + freeresult[4].count(92)
                    symbol_combine[i] = [reel_1, reel_2, reel_3, reel_4, reel_5]

                for key, value in symbol_combine.items():
                    line_win = [0, 0]
                    if key != 94:
                        pay = Paytable[key]
                        if value[1] != 0:
                            line_win = [0, 0]
                            if value[2] != 0:
                                line_win = [pay[1] * Line_bet * value[0] * value[1] * value[2], 3]
                                if value[3] != 0:
                                    line_win = [pay[2] * Line_bet * value[0] * value[1] * value[2] * value[3], 4]
                                    if value[4] != 0:
                                        line_win = [pay[3] * Line_bet * value[0] * value[1] * value[2] * value[3] * value[4], 5]

                        Symbol_win[key][line_win[1] - 3] = Symbol_win[key][line_win[1] - 3] + line_win[0]
                        freespin_win = freespin_win + line_win[0]
                free_spin_win = free_spin_win + freespin_win
                for x in range(5):
                    for y in range(3):
                        if freeresult[x][y] == 92:
                            speical_wild_number += 1
                            special_wild_win += Bonus_Prize
                            wild_number_in_free += 1
                Swildnum += speical_wild_number
                if speical_wild_number >= 3:
                    freespin += 3

            AllFeatureWin = AllFeatureWin + free_spin_win + special_wild_win

BaseRTP = AllBaseWin/All_Bet
SelectRTP = AllFeatureWin/All_Bet
SelectInterval = Test_Time/SelectHit
Average_freetime = Freespin_time/SelectHit

end_time = datetime.datetime.now()
running_time = end_time - stare_time
print('Base RTP:'+ str(BaseRTP))
print('Feature RTP:'+ str(SelectRTP))
print('Select间隔:'+ str(SelectInterval))
print('Free平均次数:'+str(Average_freetime))
print(str(running_time.seconds) + "s")

# for k, v in Symbol_win.items():
#     a = v[0] / All_Bet
#     b = v[1] / All_Bet
#     c = v[2] / All_Bet
#     print(a, b, c)
for key, value in Respin_Count.items():

    win = int(value['win'])
    base = int(value['prize'])
    if base != 0:
        mul = win/base
        print(str(key) + '\t' + str(mul) )