import random
import util.Util as Util
import copy


award_pool = {
    1: 600,
    2: 180,
    3: 180,
    4: 60,
    5: 60,
    6: 30,
    7: 30,
    8: 30,
    9: 15,
    10: 15,
    11: 15,
    12: 15,
    }

weight_pool = {
    1: 10,
    2: 50,
    3: 50,
    4: 200,
    5: 200,
    6: 500,
    7: 500,
    8: 500,
    9: 1000,
    10: 1000,
    11: 1000,
    12: 1000,
    }


def pick_pool():
    w_pool = copy.deepcopy(weight_pool)
    a_pool = copy.deepcopy(award_pool)


    pick_time = 3
    pick_more = 0

    award = 0

    while pick_time > 0:
        pick_time -= 1

        pick_key = Util.randdict(w_pool)
        award += a_pool[pick_key]
        del w_pool[pick_key]

        rand_num = random.random()

        if rand_num < 0.1 and pick_more < 3:
            pick_time += 1
            pick_more += 1

    return award


if __name__ == '__main__':

    time = 0
    test_time = 1000000

    sum_award = 0
    while time <= test_time:
        time += 1
        sum_award += pick_pool()

    print(f"Avg Award：{round(sum_award/test_time,4)}")
