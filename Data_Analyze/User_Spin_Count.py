
User_Spin_Count = {

}


def add_data(uid,game_id,spin_time):
    if uid in User_Spin_Count.keys():
        User_Spin_Count[uid][game_id] = spin_time


    else:
        User_Spin_Count[uid] = {}
        User_Spin_Count[uid][game_id] = spin_time

