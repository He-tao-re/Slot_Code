import random


class GetProgress(object):
    def __init__(self, p1, p2, p3):
        self.p1_1 = p1[0]
        self.p2_1 = p2[0]
        self.p3_1 = p3[0]
        self.p1_2 = p1[1]
        self.p2_2 = p2[1]
        self.p3_2 = p3[1]

        self.reel_1_C = 0
        self.reel_2_C = 0
        self.reel_3_C = 0

    def reel_1(self):
        rand_num_1 = random.random()
        if self.reel_1_C == 0:

            p_1 = self.p1_1
        else:
            p_1 = self.p1_2
        self.reel_1_C += 1

        if rand_num_1 < p_1:
            return "A_1"
        else:
            return "B_1"

    def reel_2(self):
        rand_num_2 = random.random()

        if self.reel_2_C == 0:
            p_2 = self.p2_1
        else:
            p_2 = self.p2_2
        self.reel_2_C += 1

        if rand_num_2 < p_2:
            return "A_2"
        else:
            return "B_2"

    def reel_3(self):
        rand_num_3 = random.random()

        if self.reel_3_C == 0:
            p_3 = self.p3_1
        else:
            p_3 = self.p3_2
        self.reel_3_C += 1

        if rand_num_3 < p_3:
            return "A_3"
        else:
            return "B_3"

    def game_progress(self):
        active = True
        reel = 1

        progress_List = []
        while active:
            if reel == 1:
                r_1 = self.reel_1()
                if r_1 == "B_1":
                    reel = 2
                else:
                    reel = 1
                    active = False

                progress_List.append(r_1)

            elif reel == 2:
                r_2 = self.reel_2()
                if r_2 == "B_2":
                    reel = 3
                else:
                    reel = 1

                progress_List.append(r_2)

            elif reel == 3:
                r_3 = self.reel_3()
                if r_3 == "B_3":
                    reel = 3
                else:
                    reel = 2

                progress_List.append(r_3)

        return progress_List


if __name__ == '__main__':
    data_count = {
        "A_1": 0,
        "B_1": 0,
        "A_2": 0,
        "B_2": 0,
        "A_3": 0,
        "B_3": 0,
    }
    test_time = 10000000
    time = 0
    while time < test_time:
        time += 1

        '''进度打印'''
        if time % (test_time / 10) == 0:
            print(str(int(time / test_time * 100)) + ' %')
        progress_list = GetProgress([0.985,0.7],[0.5,0.6],[0.5,0.7]).game_progress()
        if len(progress_list) > 1:
            for r in progress_list:
                data_count[r] += 1

    for k,v in data_count.items():
        print(f"Kind:{k} \t {v/test_time}")

    for k,v in data_count.items():
        print(f"Kind:{k} \t {round(v/data_count['A_1'],6)}")
