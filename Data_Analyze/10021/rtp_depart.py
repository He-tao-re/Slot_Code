import os
import csv
import json

import Data_Analyze.common as common
import Data_Analyze.Variable as Variable


#步骤4




summary_store = 'F:/Online_Data/Analyze_Data/summary_10021.txt'
user_data_file = open(summary_store, 'r', newline='')

#文件储存文档
subdivide_data_doc = 'F:/Online_Data/Analyze_Data/subdivide_data_10021'



try:
    os.mkdir(subdivide_data_doc)
except FileExistsError:
    file_list = common.file_path(subdivide_data_doc)
    for file in file_list:
        os.remove(file)


rtp_list = [Variable.RTP120, Variable.RTP110, Variable.RTP100, Variable.RTP98, Variable.RTP96, Variable.RTP94, Variable.RTP90, Variable.RTP85, Variable.RTP80, Variable.RTP70, Variable.NOFEATURE, Variable.REWARD]

for rtpType in rtp_list:
    file_path = subdivide_data_doc + '/' + rtpType + '.csv'
    with open(file_path,'w',newline="") as file:
        writer = csv.writer(file)

        csv_head = ["uid","spinTimes","累计bet","累计win","累计倍数","rtp"]
        writer.writerow(csv_head)

for user_data in user_data_file:
    user_data_dic = json.loads(user_data)

    for rtpType in rtp_list:
        file_path = subdivide_data_doc + '/' + rtpType + '.csv'
        with open(file_path,'a+',newline="") as file:
            writer = csv.writer(file)

            uid = list(user_data_dic.keys())[0]
            spinTimes = user_data_dic[uid][rtpType]["Spin"]
            accBet = user_data_dic[uid][rtpType]['accumulative_bet']
            accWin = user_data_dic[uid][rtpType]['accumulative_win']
            accMul = user_data_dic[uid][rtpType]['accumulative_mul']
            rtp = user_data_dic[uid][rtpType]['RTP']
            writer.writerow([uid,spinTimes,accBet,accWin,accMul,rtp])


user_data_file.close()

