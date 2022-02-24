import random
import util.Util as Util
import copy
pool = [6,5,4,3,2,1,6,5,4,3,2,1,6,5,4,3,2,1]

award_table = {
    6: [48, 96, 192],
    5: [24, 48, 96],
    4: [18, 36, 72],
    3: [18, 36, 60],
    2: [12, 24],
    1: [6, 12],
}


def pick_pool():
    c_pool = copy.deepcopy(pool)
    random.shuffle(pool)
    pick_list = []
    get_all_1 = False
    get_all_2 = False

    pick_time = 5
    while pick_time > 0:
        pick_time -= 1

        pick = c_pool.pop()

        pick_list.append(pick)

        if get_all_1 is False and pick_list.count(1) == 3:
            pick_time += 2
            get_all_1 = True
        if get_all_2 is False and pick_list.count(2) == 3:
            pick_time += 2
            get_all_2 = True
    return pick_list

def get_award():
    pick_list = pick_pool()

    c_Award_table = copy.deepcopy(award_table)
    award = 0

    for i in range(1,7):
        num = pick_list.count(i)
        award += sum(c_Award_table[i][:num])
    return award



if __name__ == '__main__':

    time = 0
    test_time = 100000

    sum_award = 0
    while time <= test_time:
        time += 1
        sum_award += get_award()

    print(f"Avg Award：{round(sum_award/test_time,4)}")
