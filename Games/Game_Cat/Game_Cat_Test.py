
#替换base和free
# import Game_Cat.Cat_Slot as Game_Slot       #Base
import Games.Game_Cat.Cat_Slot as Game_Slot

import Games.Game_Cat.Const as Const
import datetime
import copy


class TestCase(object):
    def __init__(self, static_data, test_time, total_bet):

        self.total_bet = total_bet
        self.test_time = test_time
        self.static_data = static_data
        self.self_data = {}

    def test(self):

        times = 0

        while times < self.test_time:
            times += 1
            if times % (self.test_time / 20) == 0:
                print(str(int(times / self.test_time * 100)) + ' %')

            self.static_data[Const.S_Test_Time] += 1
            self.static_data[Const.S_Total_Bet] += self.total_bet

            result = Game_Slot.GameSlot().paid_spin(self.total_bet)
            self.static_data[Const.S_Base_Line_Win] += result[Const.R_Win_Amount]

            self.static_data[Const.R_Jackpot_Win] += result[Const.R_Jackpot_Win]

            for line_id,line in result[Const.R_Line].items():
                if line_id in range(40):
                    kind = line[Const.R_Line_Kind]

                    if kind not in self.static_data[Const.S_Sym_Win].keys():
                        self.static_data[Const.S_Sym_Win][kind] = 0
                    else:
                        pass

                    self.static_data[Const.S_Sym_Win][kind] += line[Const.R_Line_Win]


            if result[Const.R_Win_Amount] > 0:
                self.static_data[Const.S_Base_Hit] += 1

            if Const.R_Free in result.keys():
                self.static_data[Const.S_Free_Hit] += 1
                self.static_data[Const.S_Free_Win] += result[Const.R_Free_Win_Amount]

            if Const.R_Respin in result.keys():
                self.static_data[Const.S_Feature_Hit] += 1
                self.static_data[Const.S_Feature_Win] += result[Const.R_Respin_Win]
                self.static_data[Const.S_Feature_Count][result[Const.R_Bonus_Num]] += 1




if __name__ == '__main__':
    static_data = {
        Const.S_Test_Time: 0,
        Const.S_Total_Bet: 0,
        Const.S_Base_Line_Win: 0,
        Const.S_Base_SC_Win: 0,
        Const.S_Base_Hit: 0,
        Const.S_Sym_Win: {},

        Const.R_Jackpot_Win: 0,

        Const.S_Free_Hit: 0,
        Const.S_Free_Win: 0,
        Const.S_Free_Spin_Amount: 0,

        Const.S_Feature_Hit: 0,
        Const.S_Feature_Win: 0,
        Const.S_Feature_Count: {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
        }

    }

    static_data_1 = copy.deepcopy(static_data)


    start_time = datetime.datetime.now()


    total_bet = 4000
    TestCase(static_data_1, test_time=5000000, total_bet=total_bet).test()



    Data = static_data_1
    end_time = datetime.datetime.now()



    print(f"Base RTP：{(Data[Const.S_Base_Line_Win] + Data[Const.S_Base_SC_Win]) / Data[Const.S_Total_Bet]}")
    print(f"Hit Rate：{Data[Const.S_Base_Hit] / Data[Const.S_Test_Time]}")
    print(f"Jackpot RTP：{(Data[Const.R_Jackpot_Win]) / Data[Const.S_Total_Bet]}")

    print('Symbol RTP:')
    for k in [1,2,3,4,5,6]:

        print(f'{k} \t {Data[Const.S_Sym_Win][k] / Data[Const.S_Total_Bet]}')

    try:
        print("================")
        print(f"free 间隔：{Data[Const.S_Test_Time] / Data[Const.S_Free_Hit]}")
    except ZeroDivisionError:
        pass

    print("================")
    print(f"feature RTP：{Data[Const.S_Feature_Win] / Data[Const.S_Total_Bet]}")

    print(f"feature 间隔：{Data[Const.S_Test_Time] / Data[Const.S_Feature_Hit]}")
    print(f"feature 倍数：{Data[Const.S_Feature_Win] / Data[Const.S_Feature_Hit] / total_bet}")
    print('respin结束bonus数量分布')
    for k in range(1,10):
        print(f'{k} \t {Data[Const.S_Feature_Count][k] / Data[Const.S_Feature_Hit]}')

    print(f"Spend Time：{(end_time-start_time).seconds} s")
