import Slot_common.Const as Const
import datetime
import Games.Game_10038_EgyptGod.EgypyGod_Slot as Game_Slot
import json

class TestCase(object):
    def __init__(self):

        self.game_data = {
            Const.R_Spin_Type: Const.R_Base_Type,
            Const.R_Feature_Hit:[],
        }
        self.self_data = {
            Const.R_Next_Spin: Const.R_Base_Type,
        }

        self.static_data = {
            Const.S_Bet: 0,
            Const.S_Win: 0,
            Const.S_Base_Win: 0,
            Const.S_Base_Hit: 0,
            Const.S_Base_Sym_Win: 0,

            Const.S_Feature_Win: 0,
            Const.S_Feature_Hit: 0,
            Const.S_Feature_Spin: 0,
            Const.S_Feature_Win_Time: 0,

            Const.S_Free_Hit: 0,
            Const.S_Free_Win: 0,
            Const.S_FreeSpin: 0,

            Const.S_Free_Feature_Win: 0,
            Const.S_Free_Feature_Hit: 0,
            Const.S_Free_Feature_Spin: 0
        }

    def base_static(self,result):
        self.static_data[Const.S_Base_Win] += result[Const.R_Win_Amount]
        self.static_data[Const.S_Win] += result[Const.R_Win_Amount]

        if result[Const.R_Win_Amount] > 0:
            self.static_data[Const.S_Base_Hit] += 1



    def feature_static(self,result):
        if self.game_data[Const.R_Respin_Times] == self.game_data[Const.R_Respin_Total_Time]:

            self.static_data[Const.S_Feature_Win] += self.game_data[Const.R_Respin_Win]
            self.static_data[Const.S_Win] += self.game_data[Const.R_Respin_Win]
            self.static_data[Const.S_Feature_Hit] += 1
            self.static_data[Const.S_Feature_Spin] += self.game_data[Const.R_Respin_Total_Time]

            if self.game_data[Const.R_Respin_Win] > 0:
                self.static_data[Const.S_Feature_Win_Time] += 1





    def free_static(self,result):
        self.static_data[Const.S_FreeSpin] += 1
        self.static_data[Const.S_Free_Win] += result[Const.R_Win_Amount]
        self.static_data[Const.S_Win] += result[Const.R_Win_Amount]

        if self.game_data[Const.R_Free_Spin_Left] == 0:
            self.static_data[Const.S_Free_Hit] += 1

    def free_feature_static(self,result):

        if self.game_data[Const.R_Respin_Times] == self.game_data[Const.R_Respin_Total_Time]:

            self.static_data[Const.S_Free_Feature_Win] += self.game_data[Const.R_Respin_Win]
            self.static_data[Const.S_Win] += self.game_data[Const.R_Respin_Win]
            self.static_data[Const.S_Free_Feature_Hit] += 1
            self.static_data[Const.S_Free_Feature_Spin] += self.game_data[Const.R_Respin_Total_Time]

            if self.game_data[Const.R_Respin_Win] > 0:
                self.static_data[Const.S_Feature_Win_Time] += 1

    def test(self, test_time, total_bet):
        times = 0

        while times < test_time:



            result,self.self_data = Game_Slot.GameSlot(self.game_data,self.self_data).spin(total_bet)

            self.game_data = result[Const.R_Game_Data]

            self.game_data[Const.R_Spin_Type] = self.self_data[Const.R_Next_Spin]

            # print(self.game_data)
            # print(json.dumps(result))

            if result[Const.R_Spin_Type] == Const.R_Base_Type:
                times += 1
                '''进度打印'''
                if times % (test_time / 20) == 0:
                    print(f'{int(times / test_time * 100)} % \t {times}')

                self.static_data[Const.S_Bet] += total_bet

            if result[Const.R_Spin_Type] == 0:
                self.base_static(result)
            elif result[Const.R_Spin_Type] == 1:
                self.free_static(result)
            elif result[Const.R_Spin_Type] == 2:
                self.feature_static(result)
            elif result[Const.R_Spin_Type] == 12:
                self.free_feature_static(result)

        return self.static_data


def fun_1(Test_Time, Total_Bet):
    static_data = TestCase().test(Test_Time, Total_Bet)
    return static_data


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    part_time = 10000000
    total_bet = 600

    data = fun_1(part_time, total_bet)

    end_time = datetime.datetime.now()
    print(f"Total RTP：{data[Const.S_Win] / data[Const.S_Bet]}")
    print("==========================")
    print(f"Base RTP：{data[Const.S_Base_Win] / data[Const.S_Bet]}")
    print(f"Base Hit Rate：{data[Const.S_Base_Hit] / part_time}")

    print("==========================")
    print(f"Feature RTP：{data[Const.S_Feature_Win] / data[Const.S_Bet]}")
    print(f"Feature 倍数：{data[Const.S_Feature_Win] / total_bet / data[Const.S_Feature_Hit]}")
    print(f"Feature 间隔：{part_time / data[Const.S_Feature_Hit]}")
    print(f"Feature Spin 次数：{data[Const.S_Feature_Spin] / data[Const.S_Feature_Hit]}")

    print("==========================")
    print(f"Free RTP：{data[Const.S_Free_Win] / data[Const.S_Bet]}")
    print(f"Free间隔：{part_time / data[Const.S_Free_Hit]}")
    print(f"Free倍数：{data[Const.S_Free_Win] / data[Const.S_Free_Hit] / total_bet}")
    print(f"Free平均次数：{data[Const.S_FreeSpin] / data[Const.S_Free_Hit]}")
    print("==========================")

    print(f"Free Feature RTP：{data[Const.S_Free_Feature_Win] / data[Const.S_Bet]}")
    print(f"Free Feature 倍数：{data[Const.S_Free_Feature_Win] / total_bet / data[Const.S_Free_Feature_Hit]}")
    print(f"Free Feature 间隔：{data[Const.S_FreeSpin] / data[Const.S_Free_Feature_Hit]}")
    print(f"Feature Spin 次数：{data[Const.S_Free_Feature_Spin] / data[Const.S_Free_Feature_Hit]}")
    print(f"触发次数：{data[Const.S_Free_Feature_Hit]}")

    print("==========================")
    print(f"Spend Time：{(end_time - start_time).seconds} s")

