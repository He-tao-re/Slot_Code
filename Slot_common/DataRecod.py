import csv
import time
import datetime

def create_csv(game):
    date = datetime.date.today()
    str_date = str(date)
    t = time.time()
    path = 'C:/Users/Betta/Desktop/GameData/'
    filename = game + '-' + str_date + '-' + str(round(t) % 10000) + str('.csv')
    path_filename = path + filename
    return path_filename


def write_csv(file_name, data):
    print(file_name)
    with open(file_name, 'a+', newline="") as file:
        csv_write = csv.writer(file)
        csv_write.writerow(data)
