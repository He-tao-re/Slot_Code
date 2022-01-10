import json
import os
import shutil
import Data_Analyze.common as common


#步骤1


def depart():
    original_file_list = common.file_path('/Users/ht/Documents/Online_Data/Original_Data')
    '''新建文件夹和删除已有文件夹中的数据，分机台储存数据'''
    try:
        dir_path = "/Users/ht/Documents/Online_Data/Games"
        os.mkdir(dir_path)
    except FileExistsError:
        dir_path = "/Users/ht/Documents/Online_Data/Games"
        file_list = common.file_path(dir_path)
        for file in file_list:
            os.remove(file)
    '''分离 机台/用户 数据'''
    shutil.rmtree("/Users/ht/Documents/Online_Data/Games_Users_Data")
    os.mkdir("/Users/ht/Documents/Online_Data/Games_Users_Data")
    num = 0
    # print(original_file_list)
    for original_file in original_file_list:
        if original_file[-3:] == "log":
            file_object = open(original_file,'r', encoding='UTF-8',newline='')
            for line in file_object:
                # print(line[57:])
                num += 1
                if num % 10000 == 0:
                    print(num)


                dict_data = json.loads(line[57:])


                json_data = json.dumps(dict_data)
                game_id = dict_data["data"]["gameId"]
                uid = dict_data["data"]["uid"]
                # gameType = dict_data['data']['gameType']

                try:
                    dir_path = "/Users/ht/Documents/Online_Data/Games_Users_Data/" + str(game_id)
                    os.mkdir(dir_path)
                except FileExistsError:
                    pass
                file_path = "/Users/ht/Documents/Online_Data/Games_Users_Data/" + str(game_id) + "/" + str(uid) + ".txt"
                file = open(file_path, 'a+', newline='')
                file.write(json_data)
                file.write('\n')
                file.close()

        else:
            pass

