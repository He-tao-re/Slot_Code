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
Test_Time = 100000
time = 0
Pick_Number = 0
All_Win_Mul = 0
More_pick = {1:[0.3, 0.1], 2:[0.3, 0], 3: [0.3, 0]}

JackPot_hit = {1: 0, 2: 0, 3: 0, 4: 0}


while time < Test_Time:
    time = time + 1
    if time % (Test_Time / 10) == 0:
        print(time)

    Prize_Pool = {1:1,2:10,3:50,4:100,5:1000,6:1000,7:1000,8:1000,9:1000,10:1000,11:1000,12:1000,13:1000,14:1000,15:1000}
    JackPot_Weight = {1:1,2:5,3:20,4:50,5:30,6:40,7:50,8:100,9:100,10:200,11:200,12:300,13:300,14:500,15:500}
    Corresponding_Ward = {1:2000,2:500,3:50,4:10,5:20,6:18,7:15,8:12,9:10,10:8,11:8,12:5,13:5,14:3,15:3}
    Extra_Pick_Num = {1: 20, 2: 60, 3: 30, 4: 10}


    Pick_List = randdict_list_del(Prize_Pool)

    Pick_List_Weight = {}


    extra_pick_list = random.sample(Pick_List,Util.randdict(Extra_Pick_Num))

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

        if Pick_Get in extra_pick_list:
            Extra_Pick_Get_1 = Util.randdict(Pick_List_Weight)
            del Pick_List_Weight[Extra_Pick_Get_1]
            Reward_Gotten.append(Extra_Pick_Get_1)

            Extra_Pick_Get_2 = Util.randdict(Pick_List_Weight)
            del Pick_List_Weight[Extra_Pick_Get_2]
            Reward_Gotten.append(Extra_Pick_Get_2)


            if Extra_Pick_Get_1 in extra_pick_list:
                Extra_Pick_Get_3 = Util.randdict(Pick_List_Weight)
                del Pick_List_Weight[Extra_Pick_Get_3]
                Reward_Gotten.append(Extra_Pick_Get_3)

                Extra_Pick_Get_4 = Util.randdict(Pick_List_Weight)
                del Pick_List_Weight[Extra_Pick_Get_4]
                Reward_Gotten.append(Extra_Pick_Get_4)

                if Extra_Pick_Get_3 in extra_pick_list:
                    Extra_Pick_Get_7 = Util.randdict(Pick_List_Weight)
                    del Pick_List_Weight[Extra_Pick_Get_7]
                    Reward_Gotten.append(Extra_Pick_Get_7)

                    Extra_Pick_Get_8 = Util.randdict(Pick_List_Weight)
                    del Pick_List_Weight[Extra_Pick_Get_8]
                    Reward_Gotten.append(Extra_Pick_Get_8)

                if Extra_Pick_Get_4 in extra_pick_list:
                    Extra_Pick_Get_7 = Util.randdict(Pick_List_Weight)
                    del Pick_List_Weight[Extra_Pick_Get_7]
                    Reward_Gotten.append(Extra_Pick_Get_7)

                    Extra_Pick_Get_8 = Util.randdict(Pick_List_Weight)
                    del Pick_List_Weight[Extra_Pick_Get_8]
                    Reward_Gotten.append(Extra_Pick_Get_8)

            if Extra_Pick_Get_2 in extra_pick_list:
                Extra_Pick_Get_5 = Util.randdict(Pick_List_Weight)
                del Pick_List_Weight[Extra_Pick_Get_5]
                Reward_Gotten.append(Extra_Pick_Get_5)

                Extra_Pick_Get_6 = Util.randdict(Pick_List_Weight)
                del Pick_List_Weight[Extra_Pick_Get_6]
                Reward_Gotten.append(Extra_Pick_Get_6)

                if Extra_Pick_Get_5 in extra_pick_list:
                    Extra_Pick_Get_7 = Util.randdict(Pick_List_Weight)
                    del Pick_List_Weight[Extra_Pick_Get_7]
                    Reward_Gotten.append(Extra_Pick_Get_7)

                    Extra_Pick_Get_8 = Util.randdict(Pick_List_Weight)
                    del Pick_List_Weight[Extra_Pick_Get_8]
                    Reward_Gotten.append(Extra_Pick_Get_8)

                if Extra_Pick_Get_6 in extra_pick_list:
                    Extra_Pick_Get_7 = Util.randdict(Pick_List_Weight)
                    del Pick_List_Weight[Extra_Pick_Get_7]
                    Reward_Gotten.append(Extra_Pick_Get_7)

                    Extra_Pick_Get_8 = Util.randdict(Pick_List_Weight)
                    del Pick_List_Weight[Extra_Pick_Get_8]
                    Reward_Gotten.append(Extra_Pick_Get_8)

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
print('平均倍数:'+ str(average_mul))
print(JackPot_hit)