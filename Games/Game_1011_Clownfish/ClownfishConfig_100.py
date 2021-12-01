import Slot_common.Const as Const
import Slot_common.LinesConfig as Lines

Const.C_Shape = [4, 4, 4, 4, 4]
Const.C_BetLine = 100
Const.C_PayLine = Lines.LINE_50_4X5_TYPE1

Wild = 0
M1 = 1
M2 = 2
M3 = 3
M4 = 4
L1 = 5
L2 = 6
L3 = 7
L4 = 8

BN = 94
Pick = 91
Scatter = 90
Wilds = [Wild]

Const.C_Base_ReelSets = [
    {
        Const.C_ReelName: 'Base_1',
        Const.C_Mystery: 92,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: {M1: 120, M2: 120, M3: 180, M4: 180, L1: 100, L2: 100, L3: 100, L4: 100},
        Const.C_ReelStrip: [
[[1,10],[1,10],[1,10],[1,10],[94,10],[94,10],[5,10],[5,10],[1,10],[1,10],[8,10],[8,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[94,10],[2,10],[2,10],[2,10],[2,10],[6,10],[6,10],[6,10],[6,10],[91,10],[3,10],[3,10],[3,10],[3,10],[94,10],[7,10],[7,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[7,10],[7,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[5,10],[6,10],[5,10],[4,10],[4,10],[3,10],[3,10],[7,10],[8,10],[90,10],[7,10],[2,10],[2,10],[1,10],[1,10],[5,10],[94,10],[7,10],[7,10],[7,10],[4,10],[6,10],[3,10],[5,10],[5,10],[91,10],[2,10],[2,10],[2,10],[2,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[8,10],[8,10],[6,10],[4,10],[4,10],[4,10],[4,10],[94,10],[6,10],[6,10],[90,10],[7,10],[92,10],[92,10],[92,10],[92,10],[8,10],[90,10],[5,10],[8,10],[5,10],[3,10],[3,10],[3,10],[3,10],[92,10],[92,10],[92,10],[92,10],[6,10],[94,10],[5,10],[6,10],[2,10],[2,10],[2,10],[2,10],[8,10],[8,10],[90,10],[7,10],[7,10],[4,10],[4,10],[4,10],[3,10],[3,10],[3,10],[91,10],[8,10],[6,10],[7,10],[94,10],[2,10],[2,10],[2,10],[2,10]],
[[1,10],[1,10],[1,10],[1,10],[94,10],[94,10],[5,10],[5,10],[1,10],[1,10],[8,10],[8,10],[94,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[8,10],[2,10],[2,10],[2,10],[2,10],[6,10],[6,10],[6,10],[6,10],[90,10],[3,10],[3,10],[3,10],[3,10],[94,10],[7,10],[7,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[7,10],[7,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[5,10],[90,10],[5,10],[4,10],[4,10],[3,10],[3,10],[7,10],[8,10],[90,10],[7,10],[2,10],[2,10],[1,10],[1,10],[5,10],[5,10],[94,10],[7,10],[7,10],[4,10],[6,10],[91,10],[1,10],[5,10],[5,10],[2,10],[2,10],[2,10],[94,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[8,10],[8,10],[6,10],[91,10],[4,10],[4,10],[4,10],[94,10],[4,10],[6,10],[6,10],[7,10],[92,10],[92,10],[92,10],[92,10],[8,10],[5,10],[8,10],[5,10],[90,10],[3,10],[3,10],[3,10],[3,10],[92,10],[92,10],[92,10],[92,10],[6,10],[5,10],[6,10],[91,10],[2,10],[2,10],[2,10],[2,10],[8,10],[94,10],[8,10],[7,10],[7,10],[4,10],[4,10],[4,10],[3,10],[3,10],[3,10],[91,10],[8,10],[6,10],[7,10],[2,10],[2,10],[2,10],[2,10]],
[[1,10],[1,10],[1,10],[1,10],[94,10],[94,10],[5,10],[5,10],[1,10],[1,10],[8,10],[8,10],[94,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[94,10],[2,10],[2,10],[2,10],[2,10],[6,10],[6,10],[6,10],[6,10],[90,10],[3,10],[3,10],[3,10],[3,10],[94,10],[7,10],[7,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[7,10],[7,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[5,10],[6,10],[5,10],[4,10],[4,10],[3,10],[3,10],[7,10],[8,10],[90,10],[7,10],[2,10],[2,10],[1,10],[1,10],[5,10],[5,10],[94,10],[7,10],[7,10],[4,10],[6,10],[90,10],[3,10],[5,10],[5,10],[2,10],[2,10],[2,10],[94,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[91,10],[8,10],[8,10],[6,10],[4,10],[4,10],[4,10],[94,10],[4,10],[6,10],[6,10],[7,10],[92,10],[92,10],[92,10],[92,10],[8,10],[5,10],[90,10],[8,10],[5,10],[3,10],[3,10],[3,10],[3,10],[92,10],[92,10],[92,10],[92,10],[6,10],[5,10],[91,10],[6,10],[2,10],[2,10],[2,10],[2,10],[8,10],[94,10],[8,10],[7,10],[7,10],[4,10],[4,10],[4,10],[3,10],[3,10],[3,10],[91,10],[8,10],[6,10],[7,10],[2,10],[2,10],[2,10],[2,10]],
[[1,10],[1,10],[1,10],[1,10],[94,10],[94,10],[5,10],[5,10],[1,10],[1,10],[8,10],[8,10],[94,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[8,10],[2,10],[2,10],[2,10],[2,10],[6,10],[6,10],[6,10],[6,10],[90,10],[3,10],[3,10],[3,10],[3,10],[94,10],[7,10],[7,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[7,10],[7,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[5,10],[6,10],[5,10],[4,10],[4,10],[3,10],[3,10],[7,10],[8,10],[90,10],[7,10],[2,10],[2,10],[1,10],[1,10],[5,10],[5,10],[94,10],[7,10],[7,10],[4,10],[6,10],[91,10],[2,10],[5,10],[5,10],[2,10],[2,10],[2,10],[94,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[8,10],[91,10],[8,10],[6,10],[4,10],[4,10],[4,10],[94,10],[4,10],[6,10],[6,10],[7,10],[92,10],[92,10],[92,10],[92,10],[8,10],[5,10],[8,10],[5,10],[90,10],[3,10],[3,10],[3,10],[3,10],[92,10],[92,10],[92,10],[92,10],[6,10],[91,10],[5,10],[6,10],[2,10],[2,10],[2,10],[2,10],[8,10],[94,10],[8,10],[7,10],[7,10],[4,10],[4,10],[4,10],[3,10],[3,10],[3,10],[91,10],[8,10],[6,10],[7,10],[2,10],[2,10],[2,10],[2,10]],
[[1,10],[1,10],[1,10],[1,10],[94,10],[94,10],[5,10],[5,10],[1,10],[1,10],[8,10],[8,10],[94,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[94,10],[2,10],[2,10],[2,10],[2,10],[6,10],[6,10],[6,10],[6,10],[90,10],[3,10],[3,10],[3,10],[3,10],[94,10],[7,10],[7,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[7,10],[7,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[5,10],[6,10],[90,10],[4,10],[4,10],[3,10],[3,10],[7,10],[8,10],[90,10],[7,10],[2,10],[2,10],[1,10],[1,10],[5,10],[5,10],[94,10],[7,10],[7,10],[4,10],[6,10],[91,10],[3,10],[5,10],[5,10],[2,10],[2,10],[2,10],[94,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[8,10],[91,10],[8,10],[6,10],[4,10],[4,10],[4,10],[94,10],[4,10],[6,10],[6,10],[7,10],[92,10],[92,10],[92,10],[92,10],[8,10],[5,10],[8,10],[5,10],[90,10],[3,10],[3,10],[3,10],[3,10],[92,10],[92,10],[92,10],[92,10],[91,10],[6,10],[5,10],[6,10],[2,10],[2,10],[2,10],[2,10],[8,10],[94,10],[8,10],[7,10],[7,10],[4,10],[4,10],[4,10],[3,10],[3,10],[3,10],[91,10],[8,10],[6,10],[7,10],[2,10],[2,10],[2,10],[2,10]]

        ]
    }
]

Const.C_Free_ReelSets = [
    {
        Const.C_ReelName: 'Free_1',
        Const.C_Mystery: 92,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: {M1: 120, M2: 120, M3: 180, M4: 180, L1: 100, L2: 100, L3: 100, L4: 100},
        Const.C_ReelStrip: [
[[1,10],[1,10],[1,10],[1,10],[92,10],[92,10],[92,10],[92,10],[5,10],[5,10],[5,10],[94,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[8,10],[92,10],[92,10],[94,10],[2,10],[2,10],[6,10],[6,10],[6,10],[94,10],[94,10],[3,10],[3,10],[3,10],[3,10],[7,10],[7,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[7,10],[7,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[5,10],[6,10],[94,10],[4,10],[4,10],[3,10],[3,10],[8,10],[8,10],[7,10],[94,10],[2,10],[2,10],[1,10],[1,10],[5,10],[94,10],[94,10],[6,10],[6,10],[7,10],[7,10],[4,10],[6,10],[3,10],[5,10],[94,10],[94,10],[2,10],[2,10],[2,10],[2,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[8,10],[8,10],[6,10],[4,10],[94,10],[94,10],[4,10],[94,10],[6,10],[6,10],[90,10],[7,10],[92,10],[92,10],[92,10],[92,10],[8,10],[5,10],[5,10],[8,10],[94,10],[3,10],[3,10],[3,10],[3,10],[92,10],[92,10],[92,10],[92,10],[6,10],[1,10],[1,10],[5,10],[6,10],[2,10],[2,10],[2,10],[2,10],[8,10],[8,10],[7,10],[7,10],[94,10],[4,10],[4,10],[4,10],[3,10],[3,10],[3,10],[94,10],[8,10],[6,10],[7,10],[2,10],[2,10],[2,10],[2,10]],
[[1,10],[1,10],[1,10],[1,10],[92,10],[92,10],[92,10],[92,10],[5,10],[5,10],[5,10],[94,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[8,10],[92,10],[92,10],[94,10],[2,10],[2,10],[6,10],[6,10],[6,10],[94,10],[94,10],[3,10],[3,10],[3,10],[3,10],[7,10],[7,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[7,10],[7,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[94,10],[94,10],[5,10],[4,10],[4,10],[3,10],[3,10],[8,10],[8,10],[7,10],[94,10],[2,10],[2,10],[1,10],[1,10],[5,10],[94,10],[94,10],[6,10],[6,10],[7,10],[7,10],[4,10],[6,10],[6,10],[6,10],[5,10],[5,10],[2,10],[2,10],[2,10],[2,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[8,10],[94,10],[94,10],[4,10],[4,10],[4,10],[94,10],[4,10],[6,10],[6,10],[7,10],[92,10],[92,10],[92,10],[92,10],[8,10],[5,10],[8,10],[5,10],[94,10],[3,10],[3,10],[3,10],[3,10],[92,10],[92,10],[92,10],[92,10],[6,10],[6,10],[6,10],[6,10],[2,10],[2,10],[2,10],[2,10],[8,10],[92,10],[92,10],[8,10],[94,10],[7,10],[4,10],[4,10],[90,10],[3,10],[3,10],[3,10],[94,10],[8,10],[6,10],[7,10],[2,10],[2,10],[2,10],[2,10]],
[[1,10],[1,10],[1,10],[1,10],[92,10],[92,10],[92,10],[92,10],[5,10],[5,10],[5,10],[94,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[8,10],[92,10],[92,10],[94,10],[2,10],[2,10],[6,10],[6,10],[6,10],[94,10],[94,10],[3,10],[3,10],[3,10],[3,10],[7,10],[7,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[7,10],[7,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[5,10],[94,10],[94,10],[4,10],[4,10],[3,10],[3,10],[8,10],[8,10],[7,10],[94,10],[2,10],[2,10],[1,10],[1,10],[5,10],[94,10],[94,10],[6,10],[6,10],[7,10],[7,10],[4,10],[6,10],[6,10],[6,10],[5,10],[5,10],[2,10],[2,10],[2,10],[2,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[8,10],[94,10],[94,10],[4,10],[4,10],[4,10],[94,10],[4,10],[94,10],[6,10],[7,10],[92,10],[92,10],[92,10],[92,10],[8,10],[5,10],[5,10],[6,10],[94,10],[3,10],[3,10],[3,10],[3,10],[92,10],[92,10],[92,10],[92,10],[3,10],[3,10],[6,10],[6,10],[2,10],[2,10],[2,10],[2,10],[8,10],[92,10],[92,10],[8,10],[94,10],[7,10],[4,10],[4,10],[90,10],[3,10],[3,10],[3,10],[94,10],[8,10],[6,10],[7,10],[2,10],[2,10],[2,10],[2,10]],
[[1,10],[1,10],[1,10],[1,10],[92,10],[92,10],[92,10],[92,10],[5,10],[5,10],[5,10],[94,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[8,10],[92,10],[92,10],[94,10],[2,10],[2,10],[6,10],[6,10],[6,10],[94,10],[94,10],[3,10],[3,10],[3,10],[3,10],[7,10],[7,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[7,10],[7,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[94,10],[94,10],[5,10],[4,10],[4,10],[3,10],[3,10],[8,10],[8,10],[7,10],[94,10],[2,10],[2,10],[1,10],[1,10],[5,10],[94,10],[94,10],[6,10],[6,10],[7,10],[7,10],[94,10],[6,10],[6,10],[6,10],[5,10],[5,10],[2,10],[2,10],[2,10],[2,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[94,10],[8,10],[94,10],[4,10],[4,10],[4,10],[94,10],[4,10],[6,10],[6,10],[7,10],[92,10],[92,10],[92,10],[92,10],[8,10],[8,10],[8,10],[5,10],[94,10],[3,10],[3,10],[3,10],[3,10],[92,10],[92,10],[92,10],[92,10],[6,10],[6,10],[5,10],[5,10],[2,10],[2,10],[2,10],[2,10],[8,10],[92,10],[92,10],[8,10],[94,10],[7,10],[4,10],[4,10],[90,10],[3,10],[3,10],[3,10],[94,10],[8,10],[6,10],[7,10],[2,10],[2,10],[2,10],[2,10]],
[[1,10],[1,10],[1,10],[1,10],[92,10],[92,10],[92,10],[92,10],[5,10],[5,10],[5,10],[94,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[8,10],[92,10],[92,10],[94,10],[2,10],[2,10],[6,10],[6,10],[6,10],[94,10],[94,10],[3,10],[3,10],[3,10],[3,10],[7,10],[7,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[7,10],[7,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[5,10],[94,10],[94,10],[4,10],[4,10],[3,10],[3,10],[8,10],[8,10],[7,10],[94,10],[2,10],[2,10],[1,10],[1,10],[5,10],[94,10],[94,10],[6,10],[6,10],[7,10],[7,10],[4,10],[94,10],[94,10],[3,10],[5,10],[5,10],[2,10],[2,10],[2,10],[2,10],[92,10],[92,10],[92,10],[92,10],[92,10],[92,10],[1,10],[1,10],[1,10],[1,10],[94,10],[94,10],[8,10],[94,10],[4,10],[4,10],[4,10],[94,10],[4,10],[94,10],[6,10],[7,10],[92,10],[92,10],[92,10],[92,10],[8,10],[5,10],[8,10],[5,10],[90,10],[3,10],[3,10],[3,10],[3,10],[92,10],[92,10],[92,10],[92,10],[6,10],[6,10],[5,10],[6,10],[2,10],[2,10],[2,10],[2,10],[8,10],[92,10],[92,10],[8,10],[7,10],[94,10],[4,10],[4,10],[4,10],[3,10],[3,10],[3,10],[94,10],[8,10],[94,10],[7,10],[2,10],[2,10],[2,10],[2,10]]

        ]
    }
]



Const.C_Wild_Sub = [M1, M2, M3, M4, L1, L2, L3, L4]
Const.C_LineSym = [M1, M2, M3, M4, L1, L2, L3, L4, Wild]

Const.C_Paytable = {
    M1: [0, 0, 5, 15, 50],
    M2: [0, 0, 5, 15, 50],
    M3: [0, 0, 3, 10, 25],
    M4: [0, 0, 3, 10, 25],
    L1: [0, 0, 1, 5, 15],
    L2: [0, 0, 1, 5, 15],
    L3: [0, 0, 1, 5, 15],
    L4: [0, 0, 1, 5, 15],
    Scatter: [0, 0, 0, 0, 0]
}

Const.C_Free_Paytable = {
    M1: [0, 0, 5, 15, 50],
    M2: [0, 0, 5, 15, 50],
    M3: [0, 0, 3, 10, 25],
    M4: [0, 0, 3, 10, 25],
    L1: [0, 0, 1, 5, 15],
    L2: [0, 0, 1, 5, 15],
    L3: [0, 0, 1, 5, 15],
    L4: [0, 0, 1, 5, 15],
    Scatter: [0, 0, 0, 0, 0]
}

Const.C_Trigger_FreeSpins = {
    3: 10,
    4: 15,
    5: 25
}
Const.C_Re_Trigger_FreeSpins = {
    2: 5,
    3: 10,
    4: 15,
    5: 25
}
Base_Bubble = {
    Const.R_Bottom_Bubble_Kind: {5: 10, 4: 70, 3: 120, 2: 200, 1: 400, None: 9200},
    Const.R_Bottom_Bubble_Local: {
        1: {20: 50, 21: 50, 22: 50, 23: 50, 24: 50},
        2: {26: 50, 27: 50, 28: 50, 29: 50},
        3: {32: 50, 33: 50, 34: 50},
        4: {38: 50, 39: 50},
        5: {44: 50}
    },

    Const.R_Random_Bubble_Hit: {
        0:   0.10,
        1:   0.08,
        2:   0.06,
        3:   0.05,
        4:   0.05,
        5:   0.04,
        6:   0.04,
        7:   0.03,
        8:   0.02,
        9:   0.01,
        10:  0.01,
        11:  0.0001,


    },
    Const.R_Bubble_Num: {8: 1, 7: 3, 6: 8, 5: 10, 4: 20, 3: 40, 2: 80, 1: 150},
    Const.R_Random_Bubble_Kind: {5: 10, 4: 90, 3: 200, 2: 700, 1: 9000},

    Const.R_Bubble_Prize: {
        1: {
            0: 1,
            1: 8,
            2: 100,
            3: 350,
            4: 200,
            5: 300,
            6: 450,
            7: 600,
            8: 650,
            9: 750,
            10:780,
            11:800,
            12:850,
            13:1200,
            14:1500,
            15:2000,
            16:4461,
        },
        2: {
            0: 0,
            1: 5,
            2: 100,
            3: 300,
            4: 150,
            5: 250,
            6: 500,
            7: 700,
            8: 800,
            9: 900,
            10:920,
            11:940,
            12:950,
            13:1200,
            14:1500,
            15:2000,
            16:3785,
        },
        3: {
            0: 0,
            1: 0,
            2: 80,
            3: 100,
            4: 120,
            5: 220,
            6: 300,
            7: 700,
            8: 800,
            9: 900,
            10:920,
            11:950,
            12:1000,
            13:1300,
            14:1500,
            15:2500,
            16:3610,
        },
        4: {
            0: 0,
            1: 0,
            2: 50,
            3: 100,
            4: 120,
            5: 220,
            6: 300,
            7: 700,
            8: 800,
            9: 900,
            10:920,
            11:950,
            12:1240,
            13:2200,
            14:2500,
            15:4000,
            16:0,
        },
        5: {
            0: 0,
            1: 0,
            2: 50,
            3: 80,
            4: 100,
            5: 150,
            6: 400,
            7: 600,
            8: 800,
            9: 1000,
            10:1200,
            11:1400,
            12:1720,
            13:2000,
            14:2500,
            15:3000,
            16:0,
        },

    },
    Const.R_Bubble_Local: {
        1: {
            0: 10,	1: 10,	2: 10,	3: 10,	4: 10,
            5: 10,	6: 10,	7: 10,	8: 10,	9: 10,
            10: 5,	11: 5,	12: 5,	13: 5,	14: 5,
            15: 5,	16: 5,	17: 5,	18: 5,	19: 5,
        },
        2: {
            1: 10,	2: 10,	3: 10,	4: 10,
            6: 10,	7: 10,	8: 10,	9: 10,
            11: 10,	12: 10,	13: 10,	14: 10,
            16: 5,	17: 5,	18: 5,	19: 5,
            21: 5,	22: 5,	23: 5,	24: 5,
        },
        3: {
            2: 2,	3: 2,	4: 2,
            7: 10,	8: 10,	9: 10,
            12: 10,	13: 10,	14: 10,
            17: 5,	18: 5,	19: 5,
            22: 5,	23: 5,	24: 5,
            27: 5,	28: 5,	29: 5,
        },
        4: {
            3: 2,	4: 2,
            8: 10,	9: 10,
            13: 10,	14: 10,
            18: 5,	19: 5,
            23: 5,	24: 5,
            28: 5,	29: 5,
            33: 5,	34: 5,
        },
        5: {
            4: 2,
            9: 10,
            14: 10,
            19: 10,
            24: 5,
            29: 5,
            34: 5,
            39: 5,
        }

    }
}


Free_Bubble = {
    Const.R_Free_Original_Bubble: {5: 500, 4: 3000, 3: 6500},

    Const.R_Bottom_Bubble_Kind: {5: 10, 4: 50, 3: 90, 2: 450, 1: 800, None: 8600},
    Const.R_Bottom_Bubble_Local: {
        1: {20: 50, 21: 50, 22: 50, 23: 50, 24: 50},
        2: {26: 50, 27: 50, 28: 50, 29: 50},
        3: {32: 50, 33: 50, 34: 50},
        4: {38: 50, 39: 50},
        5: {44: 50}
    },

    Const.R_Random_Bubble_Hit: {
        0:     0.20,
        1:     0.12,
        2:     0.10,
        3:     0.08,
        4:     0.06,
        5:     0.05,
        6:     0.04,
        7:     0.03,
        8:     0.03,
        9:     0.02,
        10:    0.01,
        11:   0.0001,


    },
    Const.R_Bubble_Num: {8: 1, 7: 5, 6: 15, 5: 20, 4: 30, 3: 50, 2: 80, 1: 100},
    Const.R_Random_Bubble_Kind: {5: 20, 4: 90, 3: 300, 2: 1000, 1: 8600},

    Const.R_Bubble_Prize: {
        1: {
            0: 1,
            1: 8,
            2: 200,
            3: 750,
            4: 250,
            5: 350,
            6: 480,
            7: 550,
            8: 620,
            9: 650,
            10:780,
            11:800,
            12:850,
            13:900,
            14:1500,
            15:2500,
            16:3811,
        },
        2: {
            0: 0,
            1: 5,
            2: 200,
            3: 750,
            4: 250,
            5: 350,
            6: 480,
            7: 550,
            8: 620,
            9: 650,
            10:780,
            11:800,
            12:850,
            13:900,
            14:1500,
            15:2500,
            16:3815,
        },
        3: {
            0: 0,
            1: 0,
            2: 100,
            3: 750,
            4: 150,
            5: 350,
            6: 480,
            7: 550,
            8: 620,
            9: 650,
            10:780,
            11:800,
            12:850,
            13:900,
            14:1500,
            15:2500,
            16:4020,
        },
        4: {
            0: 0,
            1: 0,
            2: 50,
            3: 750,
            4: 100,
            5: 350,
            6: 500,
            7: 800,
            8: 1500,
            9: 1800,
            10:2150,
            11:3000,
            12:4000,
            13:0,
            14:0,
            15:0,
            16:0,
        },
        5: {
            0: 0,
            1: 0,
            2: 50,
            3: 750,
            4: 100,
            5: 350,
            6: 500,
            7: 800,
            8: 1500,
            9: 1800,
            10:2150,
            11:3000,
            12:4000,
            13:0,
            14:0,
            15:0,
            16:0,
        },

    },
    Const.R_Bubble_Local: {
        1: {
            0: 10,	1: 10,	2: 10,	3: 10,	4: 10,
            5: 10,	6: 10,	7: 10,	8: 10,	9: 10,
            10: 10,	11: 10,	12: 10,	13: 10,	14: 10,
            15: 10,	16: 10,	17: 10,	18: 10,	19: 10,
        },
        2: {
            1: 10,	2: 10,	3: 10,	4: 10,
            6: 10,	7: 10,	8: 10,	9: 10,
            11: 10,	12: 10,	13: 10,	14: 10,
            16: 10,	17: 10,	18: 10,	19: 10,
            21: 10,	22: 10,	23: 10,	24: 10,
        },
        3: {
            2: 2,	3: 2,	4: 2,
            7: 10,	8: 10,	9: 10,
            12: 10,	13: 10,	14: 10,
            17: 10,	18: 10,	19: 10,
            22: 10,	23: 10,	24: 10,
            27: 10,	28: 10,	29: 10,
        },
        4: {
            3: 2,	4: 2,
            8: 10,	9: 10,
            13: 10,	14: 10,
            18: 10,	19: 10,
            23: 10,	24: 10,
            28: 10,	29: 10,
            33: 10,	34: 10,
        },
        5: {
            4: 2,
            9: 10,
            14: 10,
            19: 10,
            24: 10,
            29: 10,
            34: 10,
            39: 10,
        }

    }
}

Super_Free_Bubble = {
    Const.R_Free_Original_Bubble: {5: 3000, 4: 7000, 3: 0},

    Const.R_Bottom_Bubble_Kind: {5:50, 4: 150, 3: 500, 2: 1000, 1: 300, None: 8000},
    Const.R_Bottom_Bubble_Local: {
        1: {20: 50, 21: 50, 22: 50, 23: 50, 24: 50},
        2: {26: 50, 27: 50, 28: 50, 29: 50},
        3: {32: 50, 33: 50, 34: 50},
        4: {38: 50, 39: 50},
        5: {44: 50}
    },

    Const.R_Random_Bubble_Hit: {
        0:    0.6000,
        1:    0.5000,
        2:    0.4500,
        3:    0.4000,
        4:    0.3000,
        5:    0.2500,
        6:    0.2000,
        7:    0.0500,
        8:    0.0500,
        9:    0.0300,
        10:   0.0100,
        11:   0.0001,


    },
    Const.R_Bubble_Num: {8: 1, 7: 3, 6: 8, 5: 10, 4: 20, 3: 50, 2: 80, 1: 100},
    Const.R_Random_Bubble_Kind: {5: 10, 4: 90, 3: 200, 2: 1500, 1: 8100},

    Const.R_Bubble_Prize: {
        1: {
            0: 1,
            1: 8,
            2: 200,
            3: 750,
            4: 250,
            5: 350,
            6: 480,
            7: 550,
            8: 620,
            9: 650,
            10:780,
            11:800,
            12:850,
            13:900,
            14:1500,
            15:2500,
            16:3811,
        },
        2: {
            0: 0,
            1: 5,
            2: 200,
            3: 750,
            4: 250,
            5: 350,
            6: 480,
            7: 550,
            8: 620,
            9: 650,
            10:780,
            11:800,
            12:850,
            13:900,
            14:1500,
            15:2500,
            16:3815,
        },
        3: {
            0: 0,
            1: 0,
            2: 100,
            3: 750,
            4: 150,
            5: 350,
            6: 480,
            7: 550,
            8: 620,
            9: 650,
            10:780,
            11:800,
            12:850,
            13:900,
            14:1500,
            15:2500,
            16:4020,
        },
        4: {
            0: 0,
            1: 0,
            2: 50,
            3: 750,
            4: 100,
            5: 350,
            6: 500,
            7: 800,
            8: 1500,
            9: 1800,
            10:2150,
            11:3000,
            12:4000,
            13:0,
            14:0,
            15:0,
            16:0,
        },
        5: {
            0: 0,
            1: 0,
            2: 50,
            3: 750,
            4: 100,
            5: 350,
            6: 500,
            7: 800,
            8: 1500,
            9: 1800,
            10:2150,
            11:3000,
            12:4000,
            13:0,
            14:0,
            15:0,
            16:0,
        },

    },
    Const.R_Bubble_Local: {
        1: {
            0: 10,	1: 10,	2: 10,	3: 10,	4: 10,
            5: 10,	6: 10,	7: 10,	8: 10,	9: 10,
            10: 10,	11: 10,	12: 10,	13: 10,	14: 10,
            15: 10,	16: 10,	17: 10,	18: 10,	19: 10,
        },
        2: {
            1: 10,	2: 10,	3: 10,	4: 10,
            6: 10,	7: 10,	8: 10,	9: 10,
            11: 10,	12: 10,	13: 10,	14: 10,
            16: 10,	17: 10,	18: 10,	19: 10,
            21: 10,	22: 10,	23: 10,	24: 10,
        },
        3: {
            2: 2,	3: 2,	4: 2,
            7: 10,	8: 10,	9: 10,
            12: 10,	13: 10,	14: 10,
            17: 10,	18: 10,	19: 10,
            22: 10,	23: 10,	24: 10,
            27: 10,	28: 10,	29: 10,
        },
        4: {
            3: 2,	4: 2,
            8: 10,	9: 10,
            13: 10,	14: 10,
            18: 10,	19: 10,
            23: 10,	24: 10,
            28: 10,	29: 10,
            33: 10,	34: 10,
        },
        5: {
            4: 2,
            9: 10,
            14: 10,
            19: 10,
            24: 10,
            29: 10,
            34: 10,
            39: 10,
        }

    }
}

Const.C_Jackpot_Set = {
    "Grand": 1000,
    "Major": 500,
    "Minor": 20,
    "Mini": 5
}
Const.R_Bubble_Prize_Kind = {0: "Grand", 1: "Major", 2: "Minor", 3: "Mini", 4: 20, 5: 15, 6: 12, 7: 10, 8: 8, 9: 6,
                             10: 5, 11: 4, 12: 3, 13: 2.5, 14: 2, 15: 1.5, 16: 1}