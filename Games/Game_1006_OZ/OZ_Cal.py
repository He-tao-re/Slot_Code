import random
import datetime

pro = [1/40, 3/160, 1/40]

pro_s = [1,1,1]

s_use = 0.03


collect = [0, 0, 0]

r1 = 0
r2 = 0
r3 = 0
r12 = 0
r13 = 0
r23 = 0
r123 = 0

time = 0
test_time = 20000000
start_time = datetime.datetime.now()
while time < test_time:
    time += 1

    if collect[0] == 2 and collect[1] == 2 and collect[2] == 2:
        sra = random.random()
        if sra < s_use:
            collect[0] += 1
            collect[1] += 1
            collect[2] += 1
        else:
            for i in range(3):
                ra = random.random()
                if ra <= pro[i]:
                    collect[i] += 1

    elif collect[0] == 2 and collect[1] == 2:
        sra = random.random()
        if sra < s_use:
            collect[0] += 1
            collect[1] += 1
        else:
            for i in range(3):
                ra = random.random()
                if ra <= pro[i]:
                    collect[i] += 1

    elif collect[0] == 2 and collect[2] == 2:
        sra = random.random()
        if sra < s_use:
            collect[0] += 1
            collect[2] += 1
        else:
            for i in range(3):
                ra = random.random()
                if ra <= pro[i]:
                    collect[i] += 1

    elif collect[1] == 2 and collect[2] == 2:
        sra = random.random()
        if sra < s_use:
            collect[1] += 1
            collect[2] += 1
        else:
            for i in range(3):
                ra = random.random()
                if ra <= pro[i]:
                    collect[i] += 1

    else:
        for i in range(3):
            ra = random.random()
            if ra <= pro[i]:
                collect[i] += 1


    if collect[0] == 3 and collect[1] == 3 and collect[2] == 3:
        r123 += 1
        collect[0] = 0
        collect[1] = 0
        collect[2] = 0

    if collect[0] == 3 and collect[1] == 3:
        r12 += 1
        collect[0] = 0
        collect[1] = 0

    if collect[0] == 3 and collect[2] == 3:
        r13 += 1
        collect[0] = 0
        collect[2] = 0

    if collect[1] == 3 and collect[2] == 3:
        r23 += 1
        collect[1] = 0
        collect[2] = 0

    if collect[0] == 3:
        r1 += 1
        collect[0] = 0

    if collect[1] == 3:
        r2 += 1
        collect[1] = 0

    if collect[2] == 3:
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
