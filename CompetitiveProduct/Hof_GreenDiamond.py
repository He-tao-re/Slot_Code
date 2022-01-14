import json
import random
import gevent
import requests



def run(i):

    for j in range(100000):
        try:
            n = 32
            a = "".join(["%s" % random.randint(0, 9) for num in range(0, n)])
            params = f"id={a}&cmd=spin&params=%7B%0A%20%20%20%22bet%22%20%3A%20400%2E0%2C%0A%20%20%20%22features%22%20%3A%20null%2C%0A%20%20%20%22gameId%22%20%3A%20149%2C%0A%20%20%20%22lines%22%20%3A%205%2C%0A%20%20%20%22session%22%20%3A%20%22TxGUFcGEgKCD%2D6872398120464242002%22%0A%7D%0A"
            url = "https://fb-lb.houseoffuns.com/onlinecasino/games/handler.ashx"
            session = requests.session()
            content = bytes.decode(session.get(url, params=params, timeout=10).content)

            content_json = json.loads(content)
            # print(content)

            if content_json['result']:
                balance = content_json["result"]["gameInfo"]["common"]["balance"]
                print(j,'\t',f'{int(balance):,d}')
            else:
                print(content)
                break
        except Exception as e:
            print(str(e))
            continue


def gevent_main():
    gevent_list = []
    for i in range(1):
        gevent_list.append(gevent.spawn(run,i))
    gevent.joinall(gevent_list)


if __name__ == '__main__':
    gevent_main()

