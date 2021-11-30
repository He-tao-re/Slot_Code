import Slot_common.Const as Const
import datetime
import Games.Game_10035_Frog.Frog_Slot as Game_Slot


class TestCase(object):
    def __init__(self):

        self.self_data = {

        }
        self.static_data = {
            Const.S_Bet: 0,
            Const.S_Base_Win: 0,
            Const.S_Base_Hit: 0,
            Const.S_Base_Sym_Win: 0,

            Const.S_Free_Hit: 0,
            Const.S_Free_Win: 0,
            Const.S_FreeSpin: 0,

        }



    def test(self, test_time, total_bet):
        times = 0

        while times < test_time:
            times += 1
            '''进度打印'''
            if times % (test_time / 20) == 0:
                print(str(int(times / test_time * 100)) + ' %')
            self.static_data[Const.S_Bet] += total_bet

            result = Game_Slot.GameSlot(self.self_data).paidspin(total_bet)
            self.self_data = result[Const.R_Self_Data]

            if Const.R_Free in result.keys():
                free_end = max(result[Const.R_Free].keys())
                self.static_data[Const.S_FreeSpin] += free_end
                self.static_data[Const.S_Free_Hit] += 1
                self.static_data[Const.S_Free_Win] += result[Const.R_Free_Win_Amount]

            self.static_data[Const.S_Base_Win] += result[Const.R_Win_Amount]


            if result[Const.R_Win_Amount] > 0:
                self.static_data[Const.S_Base_Hit] += 1




        return self.static_data

def fun_1(Test_Time,Total_Bet):

    static_data = TestCase().test(Test_Time, Total_Bet)

    return static_data


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    part_time = 1000000
    total_bet = 1000
    data = fun_1(part_time,total_bet)

    end_time = datetime.datetime.now()
    print(f"Total RTP：{(data[Const.S_Base_Win] + data[Const.S_Free_Win])/data[Const.S_Bet]}")
    print(f"Hit Rate：{data[Const.S_Base_Hit] / part_time}")

    print("==========================")
    print(f"Free RTP：{data[Const.S_Free_Win]/data[Const.S_Bet]}")
    print(f"Free间隔：{part_time/data[Const.S_Free_Hit]}")
    print(f"Free倍数：{data[Const.S_Free_Win]/data[Const.S_Free_Hit]/total_bet}")

    print("==========================")
    print(f"Spend Time：{(end_time-start_time).seconds} s")

