import datetime

def date_list(title,date_1, date_2):
    f_list = []

    date_begin = datetime.datetime(date_1[0], date_1[1], date_1[2])
    date_end = datetime.datetime(date_2[0], date_2[1], date_2[2])

    active = True
    while active:
        f_name = f"{title}_{date_begin.year}_{date_begin.month}_{date_begin.day}"
        f_list.append(f_name)

        if date_begin == date_end:
            active = False
        date_begin += datetime.timedelta(hours=24)

    return f_list
