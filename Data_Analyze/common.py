import os
import json
import Data_Analyze.Variable as Variable
import xlwings as xw


def file_path(file_dir):
    files_path = []
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件

        for file in files:
            files_path.append(root + '/' + file)

        # print(files_path)
    return files_path


def sort_data(original_file_name,sort_file_name):
    #文档路径 + 储存路径
    user_game_data = open(original_file_name, 'r', newline='')

    data_save = {}
    time_list = []


    for line in user_game_data:
        spin_data = json.loads(line)
        uid = spin_data["data"]['uid']
        create_Time = spin_data['data']['serverTime']
        time_list.append(create_Time)
        data_save[create_Time] = line

    time_list.sort()

    sort_file = open(sort_file_name, 'a+', newline='')

    for time_point in time_list:
        sort_file.write(data_save[time_point])

    sort_file.close()

def excel_analysis_data(sht):
    sht.range('n1').value = ['玩家spin分布数据', '玩家分布', '占比']
    sht.range('n3').value = ['[0]', '=COUNTIF(B:B,0)', '=O3/SUM($O$3:$O$8)']
    sht.range('n4').value = ['(0,10]', '=COUNTIFS(B:B,">0",B:B,"<=10")', '=O4/SUM($O$3:$O$8)']
    sht.range('n5').value = ['(10,50]', '=COUNTIFS(B:B,">10",B:B,"<=50")', '=O5/SUM($O$3:$O$8)']
    sht.range('n6').value = ['(50,100]', '=COUNTIFS(B:B,">50",B:B,"<=100")', '=O6/SUM($O$3:$O$8)']
    sht.range('n7').value = ['(100,500]', '=COUNTIFS(B:B,">100",B:B,"<=500")', '=O7/SUM($O$3:$O$8)']
    sht.range('n8').value = ['(500,max]', '=COUNTIF(B:B,">500")', '=O8/SUM($O$3:$O$8)']
    sht.range('n9').value = []
    sht.range('n10').value = ['人均spin', '=AVERAGE(B:B)']
    sht.range('n11').value = ['人均spin（Spin >= 100）', '=AVERAGEIF(B:B,">=100",B:B)']
    sht.range('n12').value = ['深度体验率','=P7+P8']
    sht.range('n13').value = []
    sht.range('n14').value = ['玩家RTP分布数据(区间)','玩家分布','占比']
    sht.range('n15').value = ['(0,0.3]','=COUNTIFS(F:F,">=0",F:F,"<=0.3")','=O15/SUM($O$15:$O$27)']
    sht.range('n16').value = ['(0.3,0.4]','=COUNTIFS(F:F,">0.3",F:F,"<=0.4")','=O16/SUM($O$15:$O$27)']
    sht.range('n17').value = ['(0.4,0.5]','=COUNTIFS(F:F,">0.4",F:F,"<=0.5")','=O17/SUM($O$15:$O$27)']
    sht.range('n18').value = ['(0.5,0.6]','=COUNTIFS(F:F,">0.5",F:F,"<=0.6")','=O18/SUM($O$15:$O$27)']
    sht.range('n19').value = ['(0.6,0.7]','=COUNTIFS(F:F,">0.6",F:F,"<=0.7")','=O19/SUM($O$15:$O$27)']
    sht.range('n20').value = ['(0.7,0.8]','=COUNTIFS(F:F,">0.7",F:F,"<=0.8")','=O20/SUM($O$15:$O$27)']
    sht.range('n21').value = ['(0.8,0.9]','=COUNTIFS(F:F,">0.8",F:F,"<=0.9")','=O21/SUM($O$15:$O$27)']
    sht.range('n22').value = ['(0.9,1]','=COUNTIFS(F:F,">0.9",F:F,"<=1")','=O22/SUM($O$15:$O$27)']
    sht.range('n23').value = ['(1,1.1]','=COUNTIFS(F:F,">1",F:F,"<=1.1")','=O23/SUM($O$15:$O$27)']
    sht.range('n24').value = ['(1.1,1.2]','=COUNTIFS(F:F,">1.1",F:F,"<=1.2")','=O24/SUM($O$15:$O$27)']
    sht.range('n25').value = ['(1.2,1.5]','=COUNTIFS(F:F,">1.2",F:F,"<=1.5")','=O25/SUM($O$15:$O$27)']
    sht.range('n26').value = ['(1.5,2]','=COUNTIFS(F:F,">1.5",F:F,"<=2")','=O26/SUM($O$15:$O$27)']
    sht.range('n27').value = ['(2,max]','=COUNTIF(F:F,">2")','=O27/SUM($O$15:$O$27)']
    sht.range('n28').value = []
    sht.range('n29').value = ['人均RTP','=AVERAGE(F:F)']
    sht.range('n30').value = ['关卡RTP','=SUM(E:E)/SUM(B:B)']
    sht.range('n31').value = []
    sht.range('n32').value = ['玩家RTP分布（Spin >= 100)','玩家分布','占比']
    sht.range('n33').value = ['(0,0.3]','=COUNTIFS(B:B,">=100",F:F,"<=0.3")','=O33/SUM($O$33:$O$45)']
    sht.range('n34').value = ['(0.3,0.4]','=COUNTIFS(B:B,">=100",F:F,">0.3",F:F,"<=0.4")','=O34/SUM($O$33:$O$45)']
    sht.range('n35').value = ['(0.4,0.5]','=COUNTIFS(B:B,">=100",F:F,">0.4",F:F,"<=0.5")','=O35/SUM($O$33:$O$45)']
    sht.range('n36').value = ['(0.5,0.6]','=COUNTIFS(B:B,">=100",F:F,">0.5",F:F,"<=0.6")','=O36/SUM($O$33:$O$45)']
    sht.range('n37').value = ['(0.6,0.7]','=COUNTIFS(B:B,">=100",F:F,">0.6",F:F,"<=0.7")','=O37/SUM($O$33:$O$45)']
    sht.range('n38').value = ['(0.7,0.8]','=COUNTIFS(B:B,">=100",F:F,">0.7",F:F,"<=0.8")','=O38/SUM($O$33:$O$45)']
    sht.range('n39').value = ['(0.8,0.9]','=COUNTIFS(B:B,">=100",F:F,">0.8",F:F,"<=0.9")','=O39/SUM($O$33:$O$45)']
    sht.range('n40').value = ['(0.9,1]','=COUNTIFS(B:B,">=100",F:F,">0.9",F:F,"<=1.0")','=O40/SUM($O$33:$O$45)']
    sht.range('n41').value = ['(1,1.1]','=COUNTIFS(B:B,">=100",F:F,">1.0",F:F,"<=1.1")','=O41/SUM($O$33:$O$45)']
    sht.range('n42').value = ['(1.1,1.2]','=COUNTIFS(B:B,">=100",F:F,">1.1",F:F,"<=1.2")','=O42/SUM($O$33:$O$45)']
    sht.range('n43').value = ['(1.2,1.5]','=COUNTIFS(B:B,">=100",F:F,">1.2",F:F,"<=1.5")','=O43/SUM($O$33:$O$45)']
    sht.range('n44').value = ['(1.5,2]','=COUNTIFS(B:B,">=100",F:F,">1.5",F:F,"<=2.0")','=O44/SUM($O$33:$O$45)']
    sht.range('n45').value = ['(2,max]','=COUNTIFS(B:B,">=100",F:F,">2")','=O45/SUM($O$33:$O$45)']
    sht.range('n46').value = []
    sht.range('n47').value = ['人均RTP','=SUMIF(B:B,">=100",F:F)/COUNTIF(B:B,">=100")']
    sht.range('n48').value = []
    sht.range('n49').value = []
    sht.range('n50').value = ['累计Spin次数','=SUM(B:B)']
    sht.range('n51').value = ['Spin人数','=COUNT(B:B)']

def rtp_depart(summary_store,subdivide_data_file):

    try:
        os.remove(subdivide_data_file)
    except FileNotFoundError:
        pass

    # rtp_list = [Variable.RTP120, Variable.RTP110, Variable.RTP100, Variable.RTP98, Variable.RTP96, Variable.RTP94,
    #             Variable.RTP90, Variable.RTP85, Variable.RTP80, Variable.RTP70, Variable.NOFEATURE, Variable.REWARD, Variable.All_Spin]
    rtp_list = [Variable.All_Spin]

    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False
    app.screen_updating = False

    wb = app.books.add()
    wb.save(path=subdivide_data_file)
    wb.close()
    app.quit()

    wb = app.books.open(subdivide_data_file)

    for rtpType in rtp_list:

        sht = xw.sheets.add(name=rtpType,before=None,after=None)
        sht.range('a1').value = ["uid", "spinTimes", "累计bet", "累计win", "累计倍数", "rtp"]
        num = 1
        user_data_file = open(summary_store, 'r', newline='')

        for user_data in user_data_file:
            user_data_dic = json.loads(user_data)

            num += 1

            cell = 'a' + str(num)

            uid = list(user_data_dic.keys())[0]
            spinTimes = user_data_dic[uid][rtpType]["Spin"]
            accBet = user_data_dic[uid][rtpType]['accumulative_bet']
            accWin = user_data_dic[uid][rtpType]['accumulative_win']
            accMul = user_data_dic[uid][rtpType]['accumulative_mul']
            rtp = user_data_dic[uid][rtpType]['RTP']
            # print(num)

            sht.range(cell).value = [uid, spinTimes, accBet, accWin, accMul, rtp]

        excel_analysis_data(sht)

        user_data_file.close()
    wb.save(path=subdivide_data_file)
    wb.close()
    app.quit()






