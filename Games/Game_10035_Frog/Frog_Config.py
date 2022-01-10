import Slot_common.Const as Const
import Slot_common.LinesConfig as Lines


Const.C_Shape = [3, 3, 3, 3, 3]
Const.C_BetLine = 50
Const.C_PayLine = Lines.LINE_50_3X5_TYPE1


Base_Reel_Choose = {0:500, 1:0}
Const.C_Base_ReelSets = [
    {
        Const.C_ReelName: 'Base_1',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_ReelStrip: [
[[2,10],[7,10],[0,10],[4,10],[10,10],[11,10],[1,10],[5,10],[6,10],[8,10],[4,10],[4,10],[4,10],[9,10],[90,10],[8,10],[5,10],[5,10],[2,10],[9,10],[7,10],[3,10],[3,10],[4,10],[5,10],[7,10],[9,10],[5,10],[4,10],[9,10],[3,10],[9,10],[7,10],[2,10],[2,10],[2,10],[9,10],[7,10],[1,10],[1,10],[10,10],[90,10],[5,10],[10,10],[4,10],[7,10],[3,10],[3,10],[3,10],[11,10],[2,10],[8,10],[4,10],[7,10],[6,10],[2,10],[2,10],[8,10],[9,10],[0,10],[4,10],[6,10],[3,10],[3,10],[6,10],[6,10],[1,10],[8,10],[10,10],[2,10],[0,10],[6,10],[7,10],[1,10],[11,10],[0,10],[11,10],[5,10],[1,10],[1,10],[11,10],[3,10],[7,10],[0,10],[7,10],[9,10],[2,10],[4,10],[10,10],[3,10],[8,10],[4,10],[10,10],[5,10],[4,10],[8,10],[90,10],[6,10],[4,10],[9,10],[0,10],[9,10],[7,10],[90,10],[10,10],[3,10],[10,10],[9,10],[0,10],[9,10],[7,10],[1,10],[10,10],[3,10],[10,10],[1,10],[5,10],[6,10],[8,10],[4,10]],
[[2,10],[8,10],[11,10],[0,10],[10,10],[8,10],[5,10],[5,10],[4,10],[4,10],[7,10],[90,10],[6,10],[1,10],[1,10],[7,10],[3,10],[3,10],[8,10],[8,10],[90,10],[6,10],[4,10],[4,10],[9,10],[3,10],[5,10],[4,10],[11,10],[4,10],[9,10],[0,10],[6,10],[1,10],[2,10],[3,10],[10,10],[7,10],[5,10],[5,10],[9,10],[0,10],[9,10],[10,10],[3,10],[2,10],[2,10],[11,10],[0,10],[1,10],[1,10],[1,10],[6,10],[10,10],[0,10],[10,10],[9,10],[5,10],[5,10],[5,10],[6,10],[1,10],[9,10],[0,10],[6,10],[1,10],[10,10],[3,10],[11,10],[0,10],[10,10],[2,10],[2,10],[2,10],[6,10],[5,10],[0,10],[11,10],[5,10],[2,10],[2,10],[9,10],[90,10],[7,10],[4,10],[4,10],[7,10],[8,10],[0,10],[8,10],[1,10],[5,10],[5,10],[7,10],[6,10],[3,10],[11,10],[90,10],[9,10],[1,10],[4,10],[8,10],[3,10],[0,10],[11,10],[2,10],[11,10],[1,10],[4,10],[8,10],[3,10],[0,10],[11,10],[2,10],[11,10],[5,10],[5,10],[4,10],[4,10],[7,10]],
[[11,10],[3,10],[3,10],[3,10],[9,10],[11,10],[0,10],[7,10],[4,10],[4,10],[3,10],[3,10],[10,10],[9,10],[5,10],[3,10],[7,10],[0,10],[6,10],[5,10],[5,10],[2,10],[2,10],[2,10],[7,10],[11,10],[0,10],[8,10],[1,10],[1,10],[3,10],[10,10],[4,10],[4,10],[1,10],[9,10],[7,10],[8,10],[3,10],[3,10],[2,10],[11,10],[3,10],[5,10],[2,10],[9,10],[0,10],[8,10],[1,10],[11,10],[5,10],[8,10],[0,10],[11,10],[1,10],[6,10],[3,10],[8,10],[2,10],[7,10],[0,10],[3,10],[2,10],[6,10],[8,10],[0,10],[4,10],[6,10],[90,10],[3,10],[6,10],[4,10],[11,10],[90,10],[10,10],[5,10],[8,10],[1,10],[0,10],[6,10],[7,10],[90,10],[10,10],[1,10],[3,10],[3,10],[4,10],[11,10],[10,10],[2,10],[11,10],[4,10],[4,10],[6,10],[3,10],[4,10],[7,10],[2,10],[2,10],[6,10],[4,10],[9,10],[90,10],[6,10],[8,10],[5,10],[0,10],[6,10],[4,10],[9,10],[3,10],[6,10],[8,10],[5,10],[7,10],[0,10],[7,10],[4,10],[4,10],[3,10]],
[[7,10],[5,10],[5,10],[3,10],[9,10],[10,10],[1,10],[1,10],[1,10],[6,10],[8,10],[4,10],[5,10],[0,10],[10,10],[8,10],[4,10],[5,10],[7,10],[1,10],[1,10],[6,10],[6,10],[0,10],[8,10],[9,10],[3,10],[2,10],[11,10],[90,10],[11,10],[2,10],[9,10],[0,10],[11,10],[9,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[9,10],[10,10],[2,10],[5,10],[3,10],[6,10],[90,10],[7,10],[4,10],[4,10],[4,10],[6,10],[7,10],[0,10],[5,10],[8,10],[1,10],[5,10],[4,10],[8,10],[9,10],[2,10],[2,10],[5,10],[5,10],[11,10],[6,10],[0,10],[7,10],[1,10],[4,10],[4,10],[0,10],[7,10],[8,10],[5,10],[5,10],[4,10],[4,10],[9,10],[5,10],[2,10],[3,10],[9,10],[90,10],[11,10],[8,10],[2,10],[2,10],[10,10],[0,10],[3,10],[2,10],[6,10],[90,10],[8,10],[8,10],[2,10],[2,10],[9,10],[9,10],[5,10],[5,10],[7,10],[8,10],[2,10],[2,10],[9,10],[9,10],[5,10],[5,10],[7,10],[8,10],[1,10],[1,10],[1,10],[6,10],[8,10]],
[[5,10],[3,10],[3,10],[10,10],[10,10],[4,10],[4,10],[11,10],[10,10],[1,10],[1,10],[1,10],[6,10],[5,10],[3,10],[10,10],[1,10],[1,10],[9,10],[6,10],[5,10],[90,10],[6,10],[3,10],[2,10],[7,10],[8,10],[3,10],[0,10],[8,10],[9,10],[4,10],[4,10],[8,10],[1,10],[1,10],[2,10],[8,10],[8,10],[0,10],[11,10],[6,10],[1,10],[4,10],[10,10],[5,10],[9,10],[0,10],[5,10],[5,10],[3,10],[9,10],[8,10],[3,10],[0,10],[9,10],[11,10],[5,10],[11,10],[4,10],[8,10],[0,10],[11,10],[4,10],[2,10],[10,10],[0,10],[3,10],[8,10],[2,10],[11,10],[90,10],[9,10],[8,10],[5,10],[11,10],[1,10],[6,10],[90,10],[2,10],[9,10],[5,10],[4,10],[6,10],[4,10],[1,10],[7,10],[0,10],[10,10],[3,10],[5,10],[8,10],[9,10],[0,10],[2,10],[7,10],[4,10],[7,10],[11,10],[4,10],[1,10],[11,10],[6,10],[4,10],[2,10],[2,10],[8,10],[4,10],[1,10],[11,10],[6,10],[3,10],[3,10],[7,10],[8,10],[90,10],[11,10],[10,10],[1,10],[1,10]],
        ]
    },
    {
        Const.C_ReelName: 'Free_1',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_ReelStrip: [
[[2,10],[2,10],[4,10],[1,10],[5,10],[4,10],[4,10],[4,10],[3,10],[5,10],[5,10],[2,10],[3,10],[3,10],[4,10],[5,10],[5,10],[4,10],[3,10],[2,10],[2,10],[2,10],[4,10],[4,10],[90,10],[5,10],[4,10],[3,10],[3,10],[3,10],[2,10],[4,10],[2,10],[2,10],[4,10],[4,10],[3,10],[3,10],[1,10],[2,10],[2,10],[1,10],[4,10],[5,10],[2,10],[1,10],[1,10],[5,10],[2,10],[4,10],[3,10],[4,10],[5,10],[4,10],[5,10],[4,10],[0,10],[2,10],[3,10],[5,10],[5,10],[3,10],[1,10],[5,10],[4,10]],
[[2,10],[2,10],[5,10],[5,10],[4,10],[4,10],[2,10],[1,10],[1,10],[3,10],[3,10],[90,10],[4,10],[4,10],[3,10],[5,10],[4,10],[4,10],[5,10],[1,10],[2,10],[3,10],[5,10],[5,10],[3,10],[3,10],[2,10],[2,10],[1,10],[1,10],[1,10],[0,10],[5,10],[5,10],[5,10],[1,10],[4,10],[5,10],[3,10],[3,10],[2,10],[2,10],[2,10],[5,10],[2,10],[5,10],[2,10],[2,10],[3,10],[4,10],[4,10],[3,10],[1,10],[5,10],[5,10],[3,10],[2,10],[1,10],[4,10],[3,10],[3,10],[2,10],[1,10],[4,10],[3,10],[0,10],[2,10],[5,10],[5,10],[4,10],[4,10]],
[[3,10],[3,10],[3,10],[2,10],[4,10],[4,10],[3,10],[3,10],[5,10],[3,10],[4,10],[5,10],[5,10],[2,10],[2,10],[5,10],[5,10],[1,10],[1,10],[3,10],[4,10],[4,10],[1,10],[1,10],[3,10],[3,10],[2,10],[3,10],[5,10],[2,10],[5,10],[1,10],[5,10],[5,10],[1,10],[3,10],[2,10],[5,10],[3,10],[2,10],[2,10],[4,10],[90,10],[3,10],[4,10],[4,10],[5,10],[1,10],[0,10],[1,10],[1,10],[3,10],[3,10],[4,10],[2,10],[4,10],[4,10],[3,10],[4,10],[2,10],[2,10],[4,10],[4,10],[5,10],[4,10],[3,10],[5,10],[0,10],[4,10],[4,10],[3,10]],
[[5,10],[5,10],[3,10],[1,10],[1,10],[1,10],[2,10],[5,10],[4,10],[4,10],[5,10],[1,10],[1,10],[3,10],[3,10],[2,10],[90,10],[2,10],[4,10],[4,10],[2,10],[2,10],[3,10],[3,10],[3,10],[2,10],[5,10],[3,10],[2,10],[4,10],[4,10],[4,10],[5,10],[5,10],[1,10],[5,10],[4,10],[2,10],[2,10],[5,10],[5,10],[1,10],[1,10],[4,10],[4,10],[4,10],[5,10],[5,10],[4,10],[4,10],[5,10],[2,10],[3,10],[1,10],[2,10],[2,10],[0,10],[3,10],[4,10],[5,10],[2,10],[2,10],[5,10],[5,10],[2,10],[2,10],[5,10],[5,10],[1,10],[1,10],[1,10]],
[[5,10],[3,10],[3,10],[4,10],[4,10],[1,10],[1,10],[1,10],[5,10],[3,10],[1,10],[1,10],[5,10],[3,10],[3,10],[2,10],[3,10],[3,10],[4,10],[4,10],[1,10],[1,10],[2,10],[1,10],[1,10],[4,10],[3,10],[3,10],[5,10],[5,10],[3,10],[3,10],[5,10],[5,10],[4,10],[3,10],[4,10],[2,10],[4,10],[3,10],[2,10],[5,10],[5,10],[1,10],[1,10],[2,10],[5,10],[4,10],[4,10],[1,10],[0,10],[3,10],[5,10],[0,10],[2,10],[4,10],[4,10],[1,10],[4,10],[2,10],[2,10],[4,10],[1,10],[3,10],[3,10],[90,10],[1,10],[1,10]],
        ]
    },
]


Wild = 0
H1 = 1
H2 = 2
H3 = 3
H4 = 4
H5 = 5
L1 = 6
L2 = 7
L3 = 8
L4 = 9
L5 = 10
L6 = 11

M_Wild = 100

#Jackpot
Grand = 1000
Major = 500
Minor = 20
Mini = 5



Scatter = 90
Wilds = [Wild,M_Wild]

Const.C_Wild_Sub = [H1,H2,H3,H4,H5,L1,L2,L3,L4,L5,L6]
Const.C_LineSym = [Wild,M_Wild,H1,H2,H3,H4,H5,L1,L2,L3,L4,L5,L6]

Scatter_Mul = [[7,1],[6,5],[5,10],[4,20],[3,40],[2,100],[1,200]]
Wild_Dance = {0:1,1:3,2:8,3:15,4:20,5:1,6:2,7:3,8:10,9:0,10:1,11:3,12:8,13:15,14:20}

Const.C_Paytable = {
    Wild:[0,10,25,150,400],
    H1:[0,0,20,100,200],
    H2:[0,0,15,25,100],
    H3:[0,0,10,20,80],
    H4:[0,0,5,15,60],
    H5:[0,0,5,10,40],
    L1:[0,0,2,5,15],
    L2:[0,0,2,5,15],
    L3:[0,0,2,5,15],
    L4:[0,0,2,5,15],
    L5:[0,0,2,5,15],
    L6:[0,0,2,5,15],

    Scatter: [0,0,5,8,16]

}
