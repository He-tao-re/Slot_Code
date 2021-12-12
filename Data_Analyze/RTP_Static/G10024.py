import json
import os

import xlwings as xw
import Data_Analyze.common as common
import Data_Analyze.Variable as Variable


game_id = 10024

#排序数据储存文件夹
sort_user_data = '/Users/ht/Documents/Online_Data/Games_Users_Data_2/' + str(game_id)

#分析数据储存文件夹
Analyze_Data_Save = '/Users/ht/Documents/Online_Data/Analyze_Data'

#用户数据列表
users_data = common.file_path(sort_user_data)

#分析数据存放文件
summary_store = '/Users/ht/Documents/Online_Data/Analyze_Data/summary_' + str(game_id) + '.txt'
#文件储存文档
subdivide_data_file = '/Users/ht/Documents/Online_Data/Analyze_Data/subdivide_data_' + str(game_id) + '.xlsx'





#步骤3
def static_data():

    # 删除文件
    try:
        os.remove(summary_store)
    except FileNotFoundError:
        pass


    for user_data in users_data:
        spin_data = open(user_data,'r')

        analyze_data = {
            Variable.All_Spin: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.RTP120: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.RTP110: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.RTP100: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.RTP98: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.RTP96: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.RTP94: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.RTP90: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.RTP85: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.RTP80: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.RTP70: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.NOFEATURE: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.REWARD: {"Spin": 0, "accumulative_bet": 0, "accumulative_win": 0, "accumulative_mul": 0, "Free_hit": 0, "Feature_hit": 0,"RTP": 0},
            Variable.Feature_Hit_RTP: None
        }


        rtpSave = "RTP96"

        for record in spin_data:
            data_dic = json.loads(record.strip())
            # print((json.dumps(data_dic)))

            gameType = data_dic['data']['gameType']

            testModel = data_dic["data"]['attachInfo']['testModel']

            betGold = data_dic["data"]["betGold"]
            winGold = data_dic["data"]["winGold"]

            bet_times = testModel["spinTimes"]

            uid = data_dic["data"]["uid"]

            gameId = data_dic["data"]["gameId"]
            currentGold = data_dic["data"]["gold"]
            createTime = data_dic["data"]["serverTime"]

            if gameType == 0:
                rtpSave = testModel["currentRtp"]
            else:
                pass

            if betGold != 0:
                mul = winGold / betGold
            else:
                mul = 0


            if "rewardId" in testModel.keys():

                if gameType == 0:
                    analyze_data[Variable.REWARD]["Spin"] += 1
                    analyze_data[Variable.REWARD]["accumulative_bet"] += betGold
                    analyze_data[Variable.REWARD]["accumulative_win"] += winGold

                analyze_data[Variable.REWARD]["accumulative_win"] += winGold
                analyze_data[Variable.REWARD]["accumulative_mul"] += winGold / betGold


            else:
                if gameType == 0:
                    rtpType = rtpSave

                    analyze_data[rtpType]["Spin"] += 1
                    analyze_data[rtpType]["accumulative_bet"] += betGold
                    analyze_data[rtpType]["accumulative_win"] += winGold
                    analyze_data[rtpType]["accumulative_mul"] += mul

                    analyze_data[Variable.All_Spin]["Spin"] += 1
                    analyze_data[Variable.All_Spin]["accumulative_bet"] += betGold
                    analyze_data[Variable.All_Spin]["accumulative_win"] += winGold
                    analyze_data[Variable.All_Spin]["accumulative_mul"] += mul




                elif gameType == 1:
                    rtpType = rtpSave
                    mul = winGold / betGold

                    analyze_data[rtpType]["accumulative_win"] += winGold
                    analyze_data[rtpType]["accumulative_mul"] += mul

                    analyze_data[Variable.All_Spin]["accumulative_win"] += winGold
                    analyze_data[Variable.All_Spin]["accumulative_mul"] += mul

                elif gameType == 2:
                    rtpType = rtpSave
                    betGold = data_dic["data"]["betGold"]
                    mul = winGold / betGold

                    analyze_data[rtpType]["accumulative_win"] += winGold
                    analyze_data[rtpType]["accumulative_mul"] += mul

                    analyze_data[Variable.All_Spin]["accumulative_win"] += winGold
                    analyze_data[Variable.All_Spin]["accumulative_mul"] += mul

                elif gameType == 3:
                    rtpType = rtpSave
                    mul = winGold / betGold
                    analyze_data[rtpType]["accumulative_win"] += winGold
                    analyze_data[rtpType]["accumulative_mul"] += mul


                    analyze_data[Variable.All_Spin]["accumulative_win"] += winGold
                    analyze_data[Variable.All_Spin]["accumulative_mul"] += mul

        for k in [Variable.All_Spin, Variable.RTP120, Variable.RTP110, Variable.RTP100, Variable.RTP98, Variable.RTP96, Variable.RTP94, Variable.RTP90, Variable.RTP85, Variable.RTP80, Variable.RTP70, Variable.NOFEATURE, Variable.REWARD]:
            if analyze_data[k]['Spin'] != 0:
                analyze_data[k]['RTP'] = analyze_data[k]['accumulative_mul'] / analyze_data[k]['Spin']
            else:
                analyze_data[k]['RTP'] = 0


        personal_data = {uid: analyze_data}
        analyze_data_json = json.dumps(personal_data)
        file = open(summary_store, 'a+', newline='')
        file.write(analyze_data_json + "\n")
        file.close()

    common.rtp_depart(summary_store,subdivide_data_file)