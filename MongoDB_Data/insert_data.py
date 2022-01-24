import json
import os
import shutil
import time,datetime
import pytz
import pymongo
import Data_Analyze.common as common


#步骤1
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Spin_Data"]
dblist = myclient.list_database_names()

def insert_data():
    original_file_list = common.file_path('/Volumes/From_HT/PrepareToMongo')
    '''新建文件夹和删除已有文件夹中的数据，分机台储存数据'''
    collections_list = set()
    num = 0
    # print(original_file_list)

    utc = pytz.timezone('America/Los_Angeles')
    for original_filePath in original_file_list:
        file_name = original_filePath.replace('/Volumes/From_HT/PrepareToMongo/',"")
        if file_name[-3:] == "log" and file_name[0] != ".":
            print(file_name)
            file_object = open(original_filePath,'r', encoding='UTF-8',newline='')
            for line in file_object:
                # print(line[57:])
                num += 1
                if num % 10000 == 0:
                    print(num)

                dict_data = json.loads(line[57:])['data']
                game_id = dict_data["gameId"]
                uid = dict_data["uid"]
                serve_time = dict_data["serverTime"]
                spin_time = datetime.datetime.fromtimestamp(serve_time / 1000)
                los_time = spin_time.astimezone(tz=utc)

                collect_name = f"data_{los_time.year}_{los_time.month}_{los_time.day}"
                mycol = mydb[collect_name]

                mycol.insert_one(dict_data)

                collections_list.add(collect_name)

    for collect_name in collections_list:
        mycol = mydb[collect_name]
        # 创建索引
        mycol.create_index('{"gameId":1,"uid":1,"serverTime":1}')