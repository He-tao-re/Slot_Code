import csv
import os
import json

import Data_Analyze.common as common
import Data_Analyze.Variable as Variable



#步骤5




summary_store = 'F:/Online_Data/Analyze_Data/summary_10021.txt'
user_data_file = open(summary_store, 'r', newline='')

#文件储存文档
subdivide_data_doc = 'F:/Online_Data/Analyze_Data/subdivide_data_10021'

summary_file_path = subdivide_data_doc + '/' + 'AllRTP.csv'


rtp_list = [Variable.RTP120, Variable.RTP110, Variable.RTP100, Variable.RTP98, Variable.RTP96, Variable.RTP94, Variable.RTP90, Variable.RTP85, Variable.RTP80, Variable.RTP70, Variable.NOFEATURE, Variable.REWARD]


with open(summary_file_path,'w',newline="") as file:
    writer = csv.writer(file)

    csv_head = ["uid", "spinTimes", "累计bet", "累计win", "累计倍数", "", "AwardSpins", "AwardBet", "AwardWin", "AwardMul", "RTP_A", "RTP_NA"]
    writer.writerow(csv_head)

    for user_data in user_data_file:
        user_data_dic = json.loads(user_data)

        uid = list(user_data_dic.keys())[0]
        spinTimes = 0
        accBet = 0
        accWin = 0
        accMul = 0
        for rtpType in rtp_list:

            spinTimes += user_data_dic[uid][rtpType]["Spin"]
            accBet += user_data_dic[uid][rtpType]['accumulative_bet']
            accWin += user_data_dic[uid][rtpType]['accumulative_win']
            accMul += user_data_dic[uid][rtpType]['accumulative_mul']

        awardSpins = user_data_dic[uid][Variable.REWARD]['Spin']
        awardBet = user_data_dic[uid][Variable.REWARD]['accumulative_bet']
        awardWin = user_data_dic[uid][Variable.REWARD]['accumulative_win']
        awardMul = user_data_dic[uid][Variable.REWARD]['accumulative_mul']


        writer.writerow([uid,spinTimes,accBet,accWin,accMul,"",awardSpins,awardBet,awardWin,awardMul])


