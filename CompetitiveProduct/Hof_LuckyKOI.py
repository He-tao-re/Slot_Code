import json
import random
import gevent
import requests
import time
from gevent._fileobjectcommon import FileObjectThread





def run(i):
    # f = open("F:/Data/HuoShi"+str(i),"a+")
    # f_thread = FileObjectThread(f,"a+")
    for j in range(100000):
        try:
            n = 32
            a = "".join(["%s" % random.randint(0, 9) for num in range(0, n)])
            params = f"id={a}&cmd=spin&params=%7B%0A%20%20%20%22bet%22%20%3A%20400%2E0%2C%0A%20%20%20%22fastSpin%22%20%3A%20true%2C%0A%20%20%20%22features%22%20%3A%20null%2C%0A%20%20%20%22gameId%22%20%3A%205059%2C%0A%20%20%20%22lines%22%20%3A%2050%2C%0A%20%20%20%22session%22%20%3A%20%22qAfweGdCCUt0%2D1523740270033982801%22%0A%7D%0A"
            url = "https://fb-lb.houseoffuns.com/onlinecasino/games/handler.ashx"
            session = requests.session()
            content = bytes.decode(session.get(url, params=params, timeout=10).content)

            content_json = json.loads(content)

            # f_thread.write(content + "\n")
            print(j)
            print(content)

            if content_json['result']:

                if 'bonus' in content_json['result']['gameInfo'].keys():
                    if content_json['result']['gameInfo']['bonus']['type'] == "freeSpins":
                        bonusToken = content_json['result']['gameInfo']['bonus']['bonusToken'][13:]
                        freespins = content_json['result']['gameInfo']['bonus']['init']['spinsAmount']

                        print(f"FreeSpin 触发次数：{freespins}")
                        active = True
                        freespin_times = 0
                        while active:
                            try:

                                n = 32
                                a = "".join(["%s" % random.randint(0, 9) for num in range(0, n)])
                                params = f"id={a}&cmd=bonusGame&params=%7B%0A%20%20%20%22bonusToken%22%20%3A%20%22gs%3Ag%2E115%3Ab%3Ak%2E"+bonusToken+"%22%2C%0A%20%20%20%22gameId%22%20%3A%205059%2C%0A%20%20%20%22session%22%20%3A%20%22qAfweGdCCUt0%2D1523740270033982801%22%0A%7D%0A"
                                url = "https://fb-lb.houseoffuns.com/onlinecasino/games/handler.ashx"
                                session = requests.session()
                                free_content = bytes.decode(session.get(url, params=params, timeout=10).content)
                                free_content_json = json.loads(free_content)
                                freespin_times += 1
                                # f_thread.write(free_content + "\n")
                                print(f"FreeSpin 计次：{freespin_times}")
                                print(free_content)
                                spinsCountdown = free_content_json['result']['gameInfo']['bonusGamePlay']['spinsCountdown']
                                if spinsCountdown == 0:
                                    active = False
                            except Exception as e:
                                print(e)
                                continue
            else:
                print(content)
                break
        except Exception as e:
            print(str(e))
            continue
    # f_thread.close()


def gevent_main():
    gevent_list = []
    for i in range(1):
        gevent_list.append(gevent.spawn(run,i))
    gevent.joinall(gevent_list)


if __name__ == '__main__':
    gevent_main()

