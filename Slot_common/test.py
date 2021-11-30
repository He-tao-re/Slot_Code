import time
import datetime

fileName = "test"
t = time.time()

# this the format for showing
format = "type is: %-30s , value is: %s "

# show the time
print(format % (str(type(t)), str(t)))

dateWithTime = datetime.datetime.now()
# check the type of dateWithTime
print(format % (str(type(dateWithTime)), str(dateWithTime)))

# get the date only
# date = datetime.datetime.date(dateWithTime)
# print(format %(str(type(date)),str(date)))

# another way of getting date
date = datetime.date.today()
print(format % (str(type(date)), str(date)))

# change the type of date
strDate = str(date)
print(format % (str(type(strDate)), str(strDate)))

# add the date and time in file name
fileName = fileName + '-' + strDate + '-' + str(round(t) % 10000)
print(format % (str(type(fileName)), str(fileName)))
