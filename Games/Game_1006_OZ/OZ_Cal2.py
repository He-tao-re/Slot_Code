import random
import datetime

pro = [6/53, 15/214, 12/107]

collect = [0, 0, 0]

r1 = 0
r2 = 0
r3 = 0
r12 = 0
r13 = 0
r23 = 0
r123 = 0

time = 0
test_time = 50000000
start_time = datetime.datetime.now()
while time < test_time:
    time += 1


    for i in range(3):
        ra = random.random()
        if ra <= pro[i]:
            collect[i] += 1

    if collect[0] == 1 and collect[1] == 1 and collect[2] == 1:
        r123 += 1
        collect[0] = 0
        collect[1] = 0
        collect[2] = 0

    if collect[0] == 1 and collect[1] == 1:
        r12 += 1
        collect[0] = 0
        collect[1] = 0

    if collect[0] == 1 and collect[2] == 1:
        r13 += 1
        collect[0] = 0
        collect[2] = 0

    if collect[1] == 1 and collect[2] == 1:
        r23 += 1
        collect[1] = 0
        collect[2] = 0

    if collect[0] == 1:
        r1 += 1
        collect[0] = 0


    if collect[1] == 1:
        r2 += 1
        collect[1] = 0

    if collect[2] == 1:
        r3 += 1
        collect[2] = 0
end_time = datetime.datetime.now()

print(test_time/r1)
print(test_time/r2)
print(test_time/r3)
print(test_time/r12)
print(test_time/r13)
print(test_time/r23)
print(test_time/r123)
print((end_time-start_time).seconds)
