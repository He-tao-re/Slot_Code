import random


class CollectGame(object):
    def __init__(self):
        self.coin_list = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
        }

        self.tower_list = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            77: 0,
            777: 0,
        }


    def get_coin_random(self):
        for k in self.coin_list.keys():
            x_random = random.random()
            if x_random < 0.53:
                self.coin_list[k] = 1
            else:
                self.coin_list[k] = -1

    def coin_game(self):

        for floor in self.tower_list.keys():

            if len(self.coin_list.keys()) > 0:

                self.get_coin_random()
                coin_list = list(self.coin_list.values())

                self.tower_list[floor] = coin_list.count(1)


                if floor == 777:
                    self.tower_list[floor] = len(coin_list)

                    return self.tower_list


                del_list = []
                for k,v in self.coin_list.items():
                    if v == 1:
                        del_list.append(k)
                for k in del_list:
                    del self.coin_list[k]



            else:
                return self.tower_list

def test():
    time = 0
    test_time = 1000000

    game_win = 0

    while time < test_time:
        time += 1
        result = CollectGame().coin_game()
        print(result)
        mul = 0

        for k,v in result.items():
            mul += k*v
        game_win += mul

    print("平均倍数：{}".format(game_win / test_time))


if __name__ == '__main__':
    test()