import util.Util as Util
import random
import datetime


def randdict_list_del(onedict):
    Pick_List = []
    while len(Pick_List) < 12:
        Total_Weight = sum(onedict.values())
        ra = random.randint(0, Total_Weight-1)
        curr_sum = 0
        keys = onedict.keys()
        for k in keys:
            curr_sum = curr_sum + onedict[k]
            if ra < curr_sum:
                multiply = k
                Pick_List.append(multiply)
                del onedict[k]
                break
    return Pick_List


starttime = datetime.datetime.now()
Test_Time = 500000
time = 0
Pick_Number = 0
All_Win_Mul = 0
More_pick = {0:0.3, 1:0.3, 2: 0.3}

JackPot_hit = {1: 0, 2: 0, 3: 0, 4: 0}


while time < Test_Time:
    time = time + 1
    if time % (Test_Time / 10) == 0:
        print(time)

    Prize_Pool = {1:1,2:10,3:50,4:100,5:1000,6:1000,7:1000,8:1000,9:1000,10:1000,11:1000,12:1000,13:1000,14:1000,15:1000}
    JackPot_Weight = {1:1,2:5,3:20,4:50,5:30,6:40,7:50,8:100,9:100,10:200,11:200,12:300,13:300,14:500,15:500}
    Corresponding_Ward = {1:2000,2:500,3:50,4:10,5:20,6:18,7:15,8:12,9:10,10:8,11:8,12:5,13:5,14:3,15:3}


    Pick_List = randdict_list_del(Prize_Pool)

    Pick_List_Weight = {}

    for reward in Pick_List:
        Pick_List_Weight[reward] = JackPot_Weight[reward]

    Pick_Time = 3
    Reward_Gotten = []
    Reward_Mul_Gotten = []

    while Pick_Time > 0:
        Pick_Time = Pick_Time - 1
        Pick_Get = Util.randdict(Pick_List_Weight)
        del Pick_List_Weight[Pick_Get]
        Reward_Gotten.append(Pick_Get)

        random_num1 = random.random()
        if random_num1 < More_pick[Pick_Time]:
            Extra_Pick_Get_1 = Util.randdict(Pick_List_Weight)
            del Pick_List_Weight[Extra_Pick_Get_1]
            Reward_Gotten.append(Extra_Pick_Get_1)

            Extra_Pick_Get_2 = Util.randdict(Pick_List_Weight)
            del Pick_List_Weight[Extra_Pick_Get_2]
            Reward_Gotten.append(Extra_Pick_Get_2)




    for element in Reward_Gotten:
        Reward_Mul_Gotten.append(Corresponding_Ward[element])

        if element in JackPot_hit.keys():
            JackPot_hit[element] += 1


    Pick_Number = Pick_Number + len(Reward_Mul_Gotten)
    All_Win_Mul = All_Win_Mul + sum(Reward_Mul_Gotten)


endtime = datetime.datetime.now()
average_pick_number = Pick_Number / Test_Time
average_mul = All_Win_Mul / Test_Time
print('pick 个数:' + str(average_pick_number))
print('平均倍数:' + str(average_mul))
print(JackPot_hit)