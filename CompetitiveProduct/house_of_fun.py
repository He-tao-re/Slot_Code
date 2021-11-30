
import json
import random
import gevent
import requests
import time

from gevent._fileobjectcommon import FileObjectThread


def run(i):
    f = open("C:/Users/Betta/Desktop/Competitive_Data/"+str(i),"a+")
    f_thread = FileObjectThread(f,"a+")
    for j in range(500):
        try:
            n = 32
            a = "".join(["%s" % random.randint(0, 9) for num in range(0, n)])
            params = f"id={a}&cmd=spin&params=%7B%0A%20%20%20%22bet%22%20%3A%20200%2E0%2C%0A%20%20%20%22fastSpin%22%20%3A%20true%2C%0A%20%20%20%22features%22%20%3A%20null%2C%0A%20%20%20%22gameId%22%20%3A%2077%2C%0A%20%20%20%22lines%22%20%3A%2050%2C%0A%20%20%20%22session%22%20%3A%20%22g72qhI6loI6F%2D1423464964199634262%22%0A%7D%0A"
            url = "https://fb-lb.houseoffuns.com/onlinecasino/games/handler.ashx"
            session = requests.session()
            content = bytes.decode(session.get(url, params=params,timeout=10).content)

            # print(content)
            content_json = json.loads(content)
            if content_json['result']:

                time.sleep(1)
                print(content)
                f_thread.write(content+"\n")
                print("house_of_fun_" + str(i) + "第" + str(j) + "条")
            else:
                print(content)
                break
        except Exception as e:
            print(str(e))
            continue
    f_thread.close()


def run_test(i):
    for j in range(500):
        print("第" + str(i) + "个任务第" + str(j) + "。")
        gevent.sleep(1)


def gevent_main():
    gevent_list = []
    for i in range(1):
        gevent_list.append(gevent.spawn(run, i))
    gevent.joinall(gevent_list)


if __name__ == '__main__':

    gevent_main()



