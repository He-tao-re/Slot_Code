import Data_Analyze.game_data_depart as depart_funimport Data_Analyze.user_data_sort as sort_dataimport Data_Analyze.RTP_Summary as RTP_summaryimport Data_Analyze.common as commonimport datetimeimport osif __name__ == '__main__':    start_time = datetime.datetime.now()    Sub_Data = True    Sum_Data = True    '''分离数据'''    depart_fun.depart()    '''用户机台数据按时间重新排序'''    sort_data.time_data()    RTP_summary.rtp_data(Sub_Data,Sum_Data)    #    # RTP_summary.test_rtp_data(Sub_Data,Sum_Data)    RTP_summary.final_data(True)    end_time = datetime.datetime.now()    print(f'消耗时间：{(end_time-start_time).seconds} s')