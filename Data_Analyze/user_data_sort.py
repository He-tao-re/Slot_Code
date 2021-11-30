import os
import shutil

import Data_Analyze.common as common

""""
对分类后的用户数据排序
sort_file_list中为排好序的（机台-用户数据）
"""

#未排序用户数据文件夹
original_dir_list = 'F:/Online_Data/Games_Users_Data/'
#排序用户数据文件夹
sort_file_list = 'F:/Online_Data/Games_Users_Data_2/'


#机台文件夹列表
Games_List = os.listdir(original_dir_list)

def time_data():
    for game_id in Games_List:
        '''新建文件夹和删除已有文件夹中的数据，分机台储存数据'''

        #原始文件名列表
        original_file_list = os.listdir(original_dir_list + game_id)



        #新文件路径
        sort_file_dir_path = sort_file_list + game_id
        #删除
        try:
            shutil.rmtree(sort_file_dir_path)
        except FileNotFoundError:
            pass
        #新建
        os.mkdir(sort_file_dir_path)

        for file_name in original_file_list:
            original_file_path = original_dir_list + game_id + '/' + file_name
            sort_file_name = sort_file_list + game_id + '/'  + file_name

            common.sort_data(original_file_path, sort_file_name)