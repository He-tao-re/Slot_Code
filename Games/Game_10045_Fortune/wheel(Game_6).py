import random
import util.Util as Util
import copy

wheel_1 = {
    "A": 100,
    "B": 200,
    "C": 300,
    "D": 400,
    "E": 500,
    "F": 600,
}
wheel_2 = {
    "A": 10,
    "B": 100,
    "C": 30,
    "D": 400,
    "E": 50,
    "F": 600,
}
wheel_3 = {
    "A": 10,
    "B": 20,
    "C": 150,
    "D": 40,
    "E": 500,
    "F": 60,
}

prize_list = {
    "A": 600,
    "B": 300,
    "C": 180,
    "D": 96,
    "E": 60,
    "F": 36,
}

def wheel_game():
    active = True
    award = 0
    prize_get = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
    }

    while active:
        w_1 = Util.randdict(wheel_1)
        w_2 = Util.randdict(wheel_2)
        w_3 = Util.randdict(wheel_3)

        prize_get[w_1] += 1
        prize_get[w_2] += 1
        prize_get[w_3] += 1

        for k,v in prize_get.items():
            if v == 3:
                award += prize_list[k]
                active = False

    return award



if __name__ == '__main__':

    time = 0
    test_time = 100000

    sum_award = 0
    while time <= test_time:
        time += 1
        sum_award += wheel_game()

    print(f"Avg Award：{round(sum_award/test_time,4)}")
