import json
import os
import csv
import time
import shutil
import xlwings as xw

Game_ID = 10013

"""File"""

Person_File_Site = "F:/Online_Data/Games_Users_Data_2/10013/17673.txt"
Analyze_Data_Site = "C:/Users/shdch/Desktop/17673"


def write_down_excel():


    app = xw.App(visible=True, add_book=False)
    wb = app.books.add()
    sht = wb.sheets.add("data")

    sht.range('a1').value = ["时间", "game_type", "uid", "user_level", "持金", "spinTimes", "rtp_type", "送奖", "bet", "win", "倍数"]

    num = 1

    O_file = open(Person_File_Site,'r', encoding='UTF-8',newline='')
    for spin_data in O_file:

        print(spin_data)

        spin_data = json.loads(spin_data)

        game_type = spin_data["data"]['gameType']
        uid = spin_data["data"]['uid']
        user_level = spin_data["data"]["gradeData"]["level"]
        balance_gold = spin_data["data"]["gold"]

        spin_times = spin_data["data"]["attachInfo"]["testModel"]["spinTimes"]

        if "currentRtp" in spin_data["data"]["attachInfo"]["testModel"].keys():
            rtp_type = spin_data["data"]["attachInfo"]["testModel"]["currentRtp"]
        else:
            rtp_type = ""

        if "rewardId" in spin_data["data"]["attachInfo"]["testModel"].keys():
            reward_type = spin_data["data"]["attachInfo"]["testModel"]["rewardId"]
        else:
            reward_type = ""


        bet = spin_data["data"]['betGold']
        win = spin_data["data"]['winGold']


        """时间格式"""
        timeStamp = float(spin_data['data']['serverTime']/1000)
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)



        num += 1
        cell = 'a' + str(num)
        spin_mul = win / bet

        sht.range(cell).value = [otherStyleTime, game_type, uid, user_level, balance_gold, spin_times, rtp_type, reward_type, bet, win, spin_mul]

    wb.save(Analyze_Data_Site)
    wb.close()



if __name__ == '__main__':
    write_down_excel()