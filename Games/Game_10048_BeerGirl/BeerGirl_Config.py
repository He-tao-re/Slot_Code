import Slot_common.Const as Const


Const.C_Shape = [3, 3, 3, 3, 3]
Const.C_BetLine = 60


Base_Reel_Choose = {0:500, 1:0}
Const.C_Base_ReelSets = [
    {
        Const.C_ReelName: 'Base_1',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_ReelStrip: [
[[2,10],[7,10],[5,10],[4,10],[10,10],[11,10],[1,10],[5,10],[6,10],[8,10],[4,10],[4,10],[4,10],[9,10],[2,10],[8,10],[5,10],[5,10],[2,10],[9,10],[7,10],[3,10],[3,10],[4,10],[5,10],[7,10],[9,10],[5,10],[4,10],[9,10],[3,10],[9,10],[7,10],[2,10],[2,10],[2,10],[9,10],[7,10],[1,10],[1,10],[10,10],[90,10],[5,10],[10,10],[4,10],[7,10],[3,10],[3,10],[3,10],[11,10],[2,10],[8,10],[4,10],[7,10],[6,10],[2,10],[2,10],[8,10],[9,10],[4,10],[4,10],[6,10],[3,10],[3,10],[6,10],[6,10],[1,10],[8,10],[10,10],[2,10],[2,10],[6,10],[7,10],[1,10],[11,10],[4,10],[11,10],[5,10],[1,10],[1,10],[11,10],[1,10],[7,10],[3,10],[7,10],[9,10],[2,10],[4,10],[10,10],[3,10],[8,10],[4,10],[10,10],[5,10],[4,10],[8,10],[90,10],[6,10],[4,10],[9,10],[3,10],[9,10],[7,10],[90,10],[10,10],[3,10],[10,10],[9,10],[5,10],[9,10],[7,10],[1,10],[10,10],[3,10],[10,10],[1,10],[5,10],[6,10],[8,10],[4,10]],
[[2,10],[8,10],[11,10],[0,10],[10,10],[8,10],[5,10],[5,10],[4,10],[4,10],[7,10],[90,10],[6,10],[1,10],[1,10],[7,10],[0,10],[3,10],[8,10],[8,10],[90,10],[6,10],[4,10],[4,10],[9,10],[3,10],[5,10],[4,10],[11,10],[4,10],[9,10],[0,10],[6,10],[1,10],[2,10],[3,10],[10,10],[7,10],[5,10],[5,10],[9,10],[0,10],[9,10],[10,10],[3,10],[2,10],[2,10],[11,10],[0,10],[1,10],[1,10],[1,10],[6,10],[10,10],[0,10],[10,10],[9,10],[5,10],[5,10],[5,10],[6,10],[1,10],[9,10],[0,10],[6,10],[1,10],[10,10],[3,10],[11,10],[0,10],[10,10],[2,10],[2,10],[2,10],[6,10],[5,10],[0,10],[11,10],[5,10],[2,10],[2,10],[9,10],[90,10],[7,10],[4,10],[4,10],[7,10],[8,10],[0,10],[8,10],[1,10],[5,10],[5,10],[7,10],[6,10],[3,10],[11,10],[90,10],[9,10],[1,10],[4,10],[8,10],[3,10],[0,10],[11,10],[2,10],[11,10],[1,10],[4,10],[8,10],[3,10],[0,10],[11,10],[2,10],[11,10],[5,10],[5,10],[4,10],[4,10],[7,10]],
[[11,10],[3,10],[3,10],[3,10],[9,10],[11,10],[0,10],[7,10],[4,10],[90,10],[3,10],[3,10],[10,10],[9,10],[0,10],[3,10],[7,10],[0,10],[6,10],[5,10],[5,10],[2,10],[2,10],[2,10],[7,10],[11,10],[0,10],[8,10],[1,10],[1,10],[3,10],[10,10],[4,10],[4,10],[1,10],[9,10],[90,10],[8,10],[3,10],[3,10],[2,10],[11,10],[3,10],[5,10],[2,10],[9,10],[0,10],[8,10],[1,10],[11,10],[5,10],[8,10],[0,10],[11,10],[1,10],[6,10],[3,10],[8,10],[2,10],[7,10],[0,10],[3,10],[2,10],[6,10],[8,10],[0,10],[4,10],[6,10],[90,10],[3,10],[6,10],[4,10],[11,10],[90,10],[10,10],[5,10],[8,10],[1,10],[0,10],[6,10],[7,10],[90,10],[10,10],[1,10],[3,10],[3,10],[4,10],[11,10],[10,10],[2,10],[11,10],[4,10],[4,10],[6,10],[90,10],[4,10],[7,10],[2,10],[2,10],[6,10],[4,10],[9,10],[90,10],[6,10],[8,10],[5,10],[0,10],[6,10],[4,10],[9,10],[3,10],[6,10],[8,10],[5,10],[7,10],[0,10],[7,10],[4,10],[4,10],[3,10]],
[[7,10],[5,10],[5,10],[3,10],[9,10],[10,10],[1,10],[1,10],[1,10],[6,10],[8,10],[4,10],[5,10],[0,10],[10,10],[8,10],[4,10],[5,10],[7,10],[1,10],[1,10],[6,10],[6,10],[0,10],[8,10],[9,10],[3,10],[2,10],[11,10],[7,10],[11,10],[2,10],[9,10],[0,10],[11,10],[9,10],[2,10],[2,10],[2,10],[0,10],[3,10],[3,10],[9,10],[10,10],[0,10],[5,10],[3,10],[6,10],[90,10],[7,10],[4,10],[4,10],[4,10],[6,10],[7,10],[0,10],[5,10],[8,10],[1,10],[5,10],[4,10],[8,10],[9,10],[0,10],[2,10],[5,10],[5,10],[11,10],[6,10],[0,10],[7,10],[1,10],[4,10],[4,10],[0,10],[7,10],[8,10],[5,10],[5,10],[4,10],[0,10],[9,10],[5,10],[2,10],[3,10],[9,10],[90,10],[11,10],[8,10],[2,10],[2,10],[10,10],[0,10],[3,10],[2,10],[6,10],[90,10],[8,10],[8,10],[2,10],[2,10],[9,10],[9,10],[5,10],[5,10],[7,10],[8,10],[2,10],[2,10],[9,10],[9,10],[5,10],[5,10],[7,10],[8,10],[1,10],[1,10],[1,10],[6,10],[8,10]],
[[5,10],[3,10],[3,10],[10,10],[10,10],[4,10],[4,10],[11,10],[10,10],[1,10],[1,10],[1,10],[6,10],[5,10],[3,10],[10,10],[1,10],[1,10],[9,10],[6,10],[5,10],[90,10],[6,10],[3,10],[2,10],[7,10],[8,10],[3,10],[7,10],[8,10],[9,10],[4,10],[4,10],[8,10],[1,10],[1,10],[2,10],[8,10],[8,10],[2,10],[11,10],[6,10],[1,10],[4,10],[10,10],[5,10],[9,10],[7,10],[5,10],[5,10],[3,10],[9,10],[8,10],[3,10],[6,10],[9,10],[11,10],[5,10],[11,10],[4,10],[8,10],[7,10],[11,10],[4,10],[2,10],[10,10],[7,10],[3,10],[8,10],[2,10],[11,10],[90,10],[9,10],[8,10],[5,10],[11,10],[1,10],[6,10],[90,10],[2,10],[9,10],[5,10],[4,10],[6,10],[4,10],[1,10],[7,10],[6,10],[10,10],[3,10],[5,10],[8,10],[9,10],[7,10],[2,10],[7,10],[4,10],[7,10],[11,10],[4,10],[1,10],[11,10],[6,10],[4,10],[2,10],[2,10],[8,10],[4,10],[1,10],[11,10],[6,10],[3,10],[3,10],[7,10],[8,10],[90,10],[11,10],[10,10],[1,10],[1,10]]
        ]
    },
    {
        Const.C_ReelName: 'Free_1',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_ReelStrip: [
[[2,10],[7,10],[5,10],[4,10],[10,10],[11,10],[1,10],[5,10],[6,10],[8,10],[7,10],[4,10],[4,10],[9,10],[6,10],[8,10],[5,10],[5,10],[2,10],[9,10],[7,10],[3,10],[3,10],[4,10],[5,10],[7,10],[9,10],[5,10],[4,10],[9,10],[3,10],[9,10],[7,10],[2,10],[2,10],[2,10],[9,10],[7,10],[1,10],[1,10],[10,10],[90,10],[5,10],[10,10],[4,10],[7,10],[3,10],[3,10],[3,10],[11,10],[2,10],[8,10],[4,10],[7,10],[6,10],[2,10],[2,10],[8,10],[9,10],[4,10],[4,10],[6,10],[3,10],[3,10],[6,10],[6,10],[1,10],[8,10],[10,10],[2,10],[2,10],[6,10],[7,10],[1,10],[11,10],[90,10],[11,10],[5,10],[1,10],[1,10],[11,10],[1,10],[7,10],[3,10],[7,10],[9,10],[2,10],[4,10],[10,10],[3,10],[8,10],[4,10],[10,10],[90,10],[4,10],[8,10],[90,10],[6,10],[4,10],[9,10],[3,10],[9,10],[7,10],[90,10],[10,10],[3,10],[10,10],[9,10],[5,10],[9,10],[7,10],[1,10],[10,10],[3,10],[10,10],[1,10],[5,10],[6,10],[8,10],[4,10]],
[[2,10],[8,10],[11,10],[2,10],[10,10],[8,10],[5,10],[5,10],[4,10],[4,10],[7,10],[7,10],[6,10],[1,10],[1,10],[7,10],[3,10],[3,10],[8,10],[8,10],[1,10],[6,10],[4,10],[4,10],[9,10],[3,10],[5,10],[4,10],[11,10],[4,10],[9,10],[90,10],[6,10],[1,10],[2,10],[3,10],[10,10],[7,10],[5,10],[5,10],[9,10],[2,10],[9,10],[10,10],[3,10],[2,10],[2,10],[11,10],[90,10],[1,10],[1,10],[1,10],[6,10],[10,10],[0,10],[10,10],[9,10],[5,10],[5,10],[5,10],[6,10],[1,10],[9,10],[7,10],[6,10],[1,10],[10,10],[3,10],[11,10],[0,10],[10,10],[2,10],[2,10],[2,10],[6,10],[5,10],[0,10],[11,10],[5,10],[2,10],[2,10],[9,10],[90,10],[7,10],[4,10],[4,10],[7,10],[8,10],[90,10],[8,10],[1,10],[5,10],[5,10],[7,10],[6,10],[3,10],[11,10],[90,10],[9,10],[1,10],[4,10],[8,10],[3,10],[7,10],[11,10],[2,10],[11,10],[1,10],[4,10],[8,10],[3,10],[90,10],[11,10],[2,10],[11,10],[5,10],[5,10],[4,10],[4,10],[7,10]],
[[11,10],[3,10],[3,10],[3,10],[9,10],[11,10],[3,10],[7,10],[4,10],[4,10],[3,10],[3,10],[10,10],[9,10],[5,10],[3,10],[7,10],[7,10],[6,10],[5,10],[5,10],[2,10],[2,10],[2,10],[7,10],[11,10],[90,10],[8,10],[1,10],[1,10],[3,10],[10,10],[4,10],[4,10],[1,10],[9,10],[90,10],[8,10],[3,10],[3,10],[2,10],[11,10],[3,10],[5,10],[2,10],[9,10],[6,10],[8,10],[1,10],[11,10],[5,10],[8,10],[7,10],[11,10],[1,10],[6,10],[3,10],[8,10],[2,10],[7,10],[0,10],[3,10],[2,10],[6,10],[8,10],[7,10],[4,10],[6,10],[90,10],[3,10],[6,10],[4,10],[11,10],[90,10],[10,10],[5,10],[8,10],[1,10],[7,10],[6,10],[7,10],[90,10],[10,10],[1,10],[3,10],[3,10],[4,10],[11,10],[10,10],[2,10],[11,10],[4,10],[4,10],[6,10],[3,10],[4,10],[7,10],[2,10],[2,10],[6,10],[4,10],[9,10],[7,10],[6,10],[8,10],[5,10],[0,10],[6,10],[4,10],[9,10],[3,10],[6,10],[8,10],[5,10],[7,10],[0,10],[7,10],[4,10],[4,10],[3,10]],
[[7,10],[5,10],[5,10],[3,10],[9,10],[10,10],[1,10],[1,10],[1,10],[6,10],[8,10],[4,10],[5,10],[90,10],[10,10],[8,10],[4,10],[5,10],[7,10],[1,10],[1,10],[6,10],[6,10],[0,10],[8,10],[9,10],[3,10],[2,10],[11,10],[7,10],[11,10],[2,10],[9,10],[90,10],[11,10],[9,10],[2,10],[2,10],[2,10],[3,10],[3,10],[90,10],[9,10],[10,10],[2,10],[5,10],[3,10],[6,10],[6,10],[7,10],[4,10],[4,10],[4,10],[6,10],[7,10],[90,10],[5,10],[8,10],[1,10],[5,10],[4,10],[8,10],[9,10],[2,10],[2,10],[5,10],[5,10],[11,10],[6,10],[0,10],[7,10],[1,10],[4,10],[4,10],[0,10],[7,10],[8,10],[5,10],[5,10],[4,10],[4,10],[9,10],[5,10],[2,10],[3,10],[9,10],[90,10],[11,10],[8,10],[2,10],[2,10],[10,10],[7,10],[3,10],[2,10],[6,10],[90,10],[8,10],[8,10],[2,10],[2,10],[9,10],[9,10],[5,10],[5,10],[7,10],[8,10],[2,10],[2,10],[9,10],[9,10],[5,10],[5,10],[7,10],[8,10],[1,10],[1,10],[1,10],[6,10],[8,10]],
[[5,10],[3,10],[3,10],[10,10],[10,10],[4,10],[4,10],[6,10],[10,10],[1,10],[1,10],[1,10],[6,10],[5,10],[3,10],[10,10],[1,10],[1,10],[9,10],[6,10],[5,10],[6,10],[6,10],[3,10],[2,10],[7,10],[8,10],[3,10],[7,10],[8,10],[9,10],[4,10],[4,10],[8,10],[1,10],[1,10],[2,10],[8,10],[8,10],[2,10],[11,10],[6,10],[1,10],[90,10],[10,10],[5,10],[9,10],[7,10],[5,10],[5,10],[3,10],[9,10],[8,10],[3,10],[6,10],[9,10],[11,10],[5,10],[11,10],[90,10],[8,10],[7,10],[11,10],[4,10],[2,10],[10,10],[7,10],[3,10],[8,10],[2,10],[11,10],[90,10],[9,10],[8,10],[5,10],[11,10],[1,10],[6,10],[90,10],[2,10],[9,10],[5,10],[4,10],[6,10],[4,10],[1,10],[7,10],[6,10],[10,10],[3,10],[5,10],[8,10],[9,10],[7,10],[2,10],[7,10],[4,10],[7,10],[11,10],[4,10],[1,10],[11,10],[6,10],[4,10],[2,10],[2,10],[8,10],[4,10],[1,10],[11,10],[6,10],[3,10],[3,10],[7,10],[8,10],[90,10],[11,10],[10,10],[1,10],[1,10]]
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


#Jackpot
Grand = 2000
Major = 500
Minor = 50
Mini = 10



Scatter = 90
Wilds = [Wild]

Const.C_Wild_Sub = [H1,H2,H3,H4,H5,L1,L2,L3,L4,L5,L6]
Const.C_LineSym = [Wild,H1,H2,H3,H4,H5,L1,L2,L3,L4,L5,L6]

Scatter_Collect_Prize = [
    [[Minor,100],[15,500],[12,1200],[Mini,2000],[8,4000],[6,6000],[5,8000],[4,10000],[3,68200]],
    [[Major,1],[Minor,20],[15,100],[12,200],[Mini,400],[8,1000],[6,1200],[5,2080]],
    [[Grand,1],[Major,20],[Minor,200],[15,500],[12,1000],[Mini,1500],[8,1800],[6,2000],[5,2979]],
]

Const.C_Paytable = {
    H1:[0,0,50,100,300],
    H2:[0,0,25,50,200],
    H3:[0,0,30,40,125],
    H4:[0,0,15,30,100],
    H5:[0,0,10,15,60],
    L1:[0,0,5,10,25],
    L2:[0,0,5,10,25],
    L3:[0,0,5,10,25],
    L4:[0,0,5,10,25],
    L5:[0,0,5,10,25],
    L6:[0,0,5,10,25],

    Scatter: [0,0,0,0,0]

}
