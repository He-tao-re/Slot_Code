# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:40:02 2019

@author: HT
"""

wheel_number = [i for i in range(16)]
wheel_strcal = ['=' for i in range(16)]

calresult = dict(map(lambda x, y: [x, y], wheel_number, wheel_strcal))

reel_1 = ['AI5', 'AI4', 'AI3', 'AI2']
reel_2 = ['AJ5', 'AJ4', 'AJ3', 'AJ2']
reel_3 = ['AK5', 'AK4', 'AK3', 'AK2']
reel_4 = ['AL5', 'AL4', 'AL3', 'AL2']
reel_5 = ['AM5', 'AM4', 'AM3', 'AM2']


for r1 in range(4):
    for r2 in range(4):
        for r3 in range(4):
            for r4 in range(4):
                for r5 in range(4):

                    wnumber = r1 + r2 + r3 + r4 + r5
                    equation = reel_1[r1] + '*' + reel_2[r2] + '*' + reel_3[r3] + '*' + reel_4[r4] + '*' + reel_5[r5] +'+'
                    calresult[wnumber] = calresult[wnumber] + equation
for k, v in calresult.items():
    k = 15 - k
    print(calresult[k][:-1])
