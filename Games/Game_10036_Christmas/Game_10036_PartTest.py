import Slot_common.Const as Const
import datetime
import Games.Game_10036_Christmas.Christmas_PartTest_Slot as Game_Slot



class TestCase(object):
    def __init__(self):

        self.self_data = {
            Const.R_Collect_Data:{
                Const.R_Collect_Progress: 0,
                
            }
        }
        self.static_data = {
            Const.S_Bet: 0,
            Const.S_Base_Win: 0,
            Const.S_Base_Hit: 0,
            Const.S_Base_Sym_Win: 0,

            Const.S_Free_Hit: 0,
            Const.S_Free_Win: 0,
            Const.S_FreeSpin: 0,

            Const.R_Collect_Data: 0,
            Const.S_Jackpot_Hit: {
                Const.C_Grand: 0,
                Const.C_Major: 0,
                Const.C_Minor: 0,
                Const.C_Mini: 0
            },
            Const.S_Jackpot_Win: 0

        }



    def test(self, test_time, total_bet, kind, reel_idx):
        times = 0

        while times < test_time:
            times += 1
            # '''进度打印'''
            # if times % (test_time / 20) == 0:
            #     print(str(int(times / test_time * Game_10039_Macau)) + ' %')
            self.static_data[Const.S_Bet] += total_bet

            result = Game_Slot.GameSlot(self.self_data).paidspin(total_bet,kind,reel_idx)
            self.self_data = result[Const.R_Self_Data]

            if Const.R_Free in result.keys():
                self.static_data[Const.S_Free_Hit] += 1

            self.static_data[Const.S_Base_Win] += result[Const.R_Win_Amount]


            if result[Const.R_Win_Amount] > 0:
                self.static_data[Const.S_Base_Hit] += 1

            if result[Const.R_Jackpot_Hit] is not None:
                jackpot_kind = result[Const.R_Jackpot_Hit]
                self.static_data[Const.S_Jackpot_Hit][jackpot_kind] += 1
                self.static_data[Const.S_Jackpot_Win] += result[Const.R_Jackpot_Win]

            self.static_data[Const.R_Collect_Data] += result[Const.R_Collect_Data]


            # print(result)
        return self.static_data

def fun_1(Test_Time,Total_Bet,kind,reel_idx):

    static_data = TestCase().test(Test_Time, Total_Bet,kind,reel_idx)
    return static_data


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    part_time = 5000000
    total_bet = 1000

    summary = []
    #[['base', 0], ['base', 1], ['free', 2], ['free', 3], ['free', 4], ['free', 5], ['Super', 6],['Super', 7], ['Super', 8]]
    #  base         free         wheel free  2X Wheel     3X wheel        Super       4X Super     5X Super
    for reel_kind in [['free', 2]]:

        kind = reel_kind[0]
        reel_idx = reel_kind[1]

        data = fun_1(part_time,total_bet,kind,reel_idx)

        end_time = datetime.datetime.now()

        print(reel_kind)


        print(f"Total RTP：{(data[Const.S_Base_Win] + data[Const.S_Free_Win])/data[Const.S_Bet]}")
        print("==========================")
        print(f"Base RTP：{data[Const.S_Base_Win] / data[Const.S_Bet]}")

        print(f"Base Hit Rate：{data[Const.S_Base_Hit] / part_time}")

        print("==========================")
        try:
            print(f"Free RTP：{data[Const.S_Free_Win]/data[Const.S_Bet]}")
            print(f"Free间隔：{part_time/data[Const.S_Free_Hit]}")
            print(f"Free倍数：{data[Const.S_Free_Win]/data[Const.S_Free_Hit]/total_bet}")
            print(f"Free平均次数：{data[Const.S_FreeSpin]/data[Const.S_Free_Hit]}")
        except ZeroDivisionError:
            pass

        try:
            print(f"Jackpot RTP: {data[Const.S_Jackpot_Win]/data[Const.S_Bet]}")
            print(f"Jackpot Hit: {data[Const.S_Jackpot_Hit]}")
        except ZeroDivisionError:
            pass

        print("==========================")
        print(f"Spend Time：{(end_time-start_time).seconds} s")

        summary.append([data[Const.S_Base_Win] / data[Const.S_Bet], data[Const.S_Jackpot_Win]/data[Const.S_Bet], data[Const.R_Collect_Data] / part_time,reel_kind])

    for i in summary:
        print(f"{i[0]} \t {i[1]} \t {i[2]} \t\t {i[3]}")