# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:40:02 2019

@author: Acer
"""
wheel_number = [i for i in range(25)]
wheel_strcal = ['=' for i in range(25)]

calresult = dict(map(lambda x, y: [x, y], wheel_number, wheel_strcal))

reel_1 = ['AS6', 'AS5', 'AS4', 'AS3', 'AS2']
reel_2 = ['AT6', 'AT5', 'AT4', 'AT3', 'AT2']
reel_3 = ['AU6', 'AU5', 'AU4', 'AU3', 'AU2']
reel_4 = ['AV6', 'AV5', 'AV4', 'AV3', 'AV2']
reel_5 = ['AW6', 'AW5', 'AW4', 'AW3', 'AW2']
reel_6 = ['AX6', 'AX5', 'AX4', 'AX3', 'AX2']

for r1 in range(5):
    for r2 in range(5):
        for r3 in range(5):
            for r4 in range(5):
                for r5 in range(5):
                    for r6 in range(5):
                        wnumber = r1 + r2 + r3 + r4 + r5 + r6
                        equation = reel_1[r1] + '*' + reel_2[r2] + '*' + reel_3[r3] + '*' + reel_4[r4] + '*' + reel_5[
                            r5] + '*' + reel_6[r6] + '+'
                        calresult[wnumber] = calresult[wnumber] + equation

for k, v in calresult.items():
    k = 24 - k
    print(calresult[k][:-1])







