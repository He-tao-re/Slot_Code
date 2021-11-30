import Slot_common.Const as Const
import datetime
import Games.Game_10037._Slot as Game_Slot
import json

class TestCase(object):
    def __init__(self):

        self.game_data = {
            Const.R_Collect_Data: {
                Const.R_Collect_Progress: 0,
            },
            Const.R_Free_Spin_Total: 0,
            Const.R_Free_Spin_Left: 0,

        }
        self.static_data = {
            Const.S_Bet: 0,
            Const.S_Win: 0,
            Const.S_Base_Win: 0,
            Const.S_Base_Hit: 0,
            Const.S_Base_Sym_Win: 0,

            Const.S_Extra_Win: 0,
            Const.S_Extra_Win_Hit: 0,

            Const.S_Feature_Win: 0,
            Const.S_Feature_Hit: 0,
            Const.S_Feature_Win_Time: 0,
            Const.S_Feature_Extra_Win: 0,
            Const.S_Feature_Extra_Hit: 0,

            Const.S_Free_Hit: 0,
            Const.S_Free_Win: 0,
            Const.S_Free_Extra_Win: 0,
            Const.S_Free_Extra_Hit: 0,
            Const.S_FreeSpin: 0,
            Const.S_Free_Feature_Win: 0,
            Const.S_Free_Feature_Hit: 0,
            Const.S_Free_Feature_Extra_Win: 0,
            Const.S_Free_Feature_Extra_Hit: 0

        }

    def base_static(self,result):
        self.static_data[Const.S_Base_Win] += result[Const.R_Win_Amount]
        self.static_data[Const.S_Win] += result[Const.R_Win_Amount]

        if result[Const.R_Win_Amount] > 0:
            self.static_data[Const.S_Base_Hit] += 1

        if result[Const.R_Extra_Win] > 0:
            self.static_data[Const.S_Extra_Win] += result[Const.S_Extra_Win]
            self.static_data[Const.S_Win] += result[Const.S_Extra_Win]

            self.static_data[Const.S_Extra_Win_Hit] += 1

    def feature_static(self,result):
        self.static_data[Const.S_Feature_Win] += result[Const.R_Win_Amount]
        self.static_data[Const.S_Win] += result[Const.R_Win_Amount]

        self.static_data[Const.S_Feature_Hit] += 1

        if result[Const.R_Win_Amount] > 0:
            self.static_data[Const.S_Feature_Win_Time] += 1

        if result[Const.R_Extra_Win] > 0:
            self.static_data[Const.S_Feature_Extra_Win] += result[Const.S_Extra_Win]
            self.static_data[Const.S_Win] += result[Const.S_Extra_Win]

            self.static_data[Const.S_Feature_Extra_Hit] += 1

    def free_static(self,result):
        self.static_data[Const.S_FreeSpin] += 1
        self.static_data[Const.S_Free_Win] += result[Const.R_Win_Amount]
        self.static_data[Const.S_Win] += result[Const.R_Win_Amount]

        if result[Const.R_Extra_Win] > 0:
            self.static_data[Const.S_Free_Extra_Win] += result[Const.S_Extra_Win]
            self.static_data[Const.S_Win] += result[Const.S_Extra_Win]

            self.static_data[Const.S_Free_Extra_Hit] += 1

        if self.game_data[Const.R_Free_Spin_Left] == 0:
            self.game_data[Const.R_Free_Spin_Total] = 0

    def free_feature_static(self,result):
        self.static_data[Const.S_Free_Feature_Win] += result[Const.R_Win_Amount]
        self.static_data[Const.S_Win] += result[Const.R_Win_Amount]


        self.static_data[Const.S_Free_Feature_Hit] += 1


        if result[Const.R_Extra_Win] > 0:
            self.static_data[Const.S_Free_Feature_Extra_Win] += result[Const.S_Extra_Win]
            self.static_data[Const.S_Win] += result[Const.S_Extra_Win]

            self.static_data[Const.S_Free_Feature_Extra_Hit] += 1

        if self.game_data[Const.R_Free_Spin_Left] == 0:
            self.game_data[Const.R_Free_Spin_Total] = 0


    def test(self, test_time, total_bet):
        times = 0

        while times < test_time:
            times += 1
            '''进度打印'''
            if times % (test_time / 20) == 0:
                print(str(int(times / test_time * 100)) + ' %')

            self.static_data[Const.S_Bet] += total_bet

            result = Game_Slot.GameSlot(self.game_data).spin(total_bet)
            self.game_data = result[Const.R_Game_Data]

            print(json.dumps(result))

            if Const.R_Free in result.keys() and result[Const.R_Free] == True:
                self.static_data[Const.S_Free_Hit] += 1


            if result[Const.R_Spin_Type] == 0:
                self.base_static(result)

            if result[Const.R_Spin_Type] == 2:
                self.feature_static(result)


            if result[Const.R_Spin_Type] == 1:
                self.free_static(result)

            if result[Const.R_Spin_Type] == 11:
                self.free_feature_static(result)





        return self.static_data


def fun_1(Test_Time, Total_Bet):
    static_data = TestCase().test(Test_Time, Total_Bet)
    return static_data


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    part_time = 100000
    total_bet = 1000

    data = fun_1(part_time, total_bet)

    end_time = datetime.datetime.now()
    print(f"Total RTP：{data[Const.S_Win] / data[Const.S_Bet]}")
    print("==========================")
    print(f"Base RTP：{data[Const.S_Base_Win] / data[Const.S_Bet]}")
    print(f"Base Hit Rate：{data[Const.S_Base_Hit] / part_time}")
    print(f"Base Extra RTP：{data[Const.S_Extra_Win] / data[Const.S_Bet]}")
    print(f"Base Extra Hit：{data[Const.S_Extra_Win_Hit] / part_time}")

    print("==========================")
    print(f"Feature RTP：{data[Const.S_Feature_Win] / data[Const.S_Bet]}")
    print(f"Feature Hit Rate：{data[Const.S_Feature_Win_Time] / data[Const.S_Feature_Hit]}")
    print(f"Feature 倍数：{data[Const.S_Feature_Win] / total_bet / data[Const.S_Feature_Hit]}")
    print(f"Feature 间隔：{part_time / data[Const.S_Feature_Hit]}")
    print(f"Feature Extra RTP：{data[Const.S_Feature_Extra_Win] / data[Const.S_Bet]}")
    print(f"Feature Extra Hit：{data[Const.S_Feature_Extra_Hit] / data[Const.S_Feature_Hit]}")
    print(f"Feature Extra 间隔：{ data[Const.S_Feature_Hit] / data[Const.S_Feature_Extra_Hit]}")


    print("==========================")
    print(f"Free RTP：{data[Const.S_Free_Win] / data[Const.S_Bet]}")
    print(f"Free间隔：{part_time / data[Const.S_Free_Hit]}")
    print(f"Free倍数：{data[Const.S_Free_Win] / data[Const.S_Free_Hit] / total_bet}")
    print(f"Free平均次数：{data[Const.S_FreeSpin] / data[Const.S_Free_Hit]}")
    print(f"Free Extra RTP：{data[Const.S_Free_Extra_Win] / data[Const.S_Bet]}")
    print(f"Free Extra Hit：{data[Const.S_Free_Extra_Hit] / data[Const.S_FreeSpin]}")
    print("==========================")

    print(f"Free Feature RTP：{data[Const.S_Free_Feature_Win] / data[Const.S_Bet]}")
    # print(f"Free Feature Hit Rate：{data[Const.S_Feature_Win_Time] / data[Const.S_Feature_Hit]}")

    print(f"Free Feature 倍数：{data[Const.S_Free_Feature_Win] / total_bet / data[Const.S_Free_Feature_Hit]}")

    print(f"Free Feature 间隔：{data[Const.S_FreeSpin] / data[Const.S_Free_Feature_Hit]}")

    print(f"Free Feature Extra RTP：{data[Const.S_Free_Feature_Extra_Win] / data[Const.S_Bet]}")
    print(f"Free Feature Extra Hit：{data[Const.S_Free_Feature_Extra_Hit] / data[Const.S_Free_Feature_Hit]}")
    print(f"Free Feature Extra 间隔：{ data[Const.S_Free_Feature_Hit] / data[Const.S_Free_Feature_Extra_Hit]}")

    print("==========================")
    print(f"Spend Time：{(end_time - start_time).seconds} s")

