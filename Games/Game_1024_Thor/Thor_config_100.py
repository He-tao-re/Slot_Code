import Slot_common.Const as Const
import Slot_common.LinesConfig as Line

Const.C_Shape = [4,5,4,5,4]
Const.C_Free_Shape = [4,5,4,5,4]

Const.C_BetLine = 100

Base_Reel_Choose = {0: 100}


Wild = 0
WS = 1
H1 = 2
H2 = 3
M1 = 4
M2 = 5
M3 = 6
M4 = 7
L1 = 8
L2 = 9
L3 = 10
L4 = 11

Scatter = 90

Wilds = [Wild]


Const.C_Wild_Sub = [WS, H1, H2, M1, M2, M3, M4, L1, L2, L3, L4]
Const.C_LineSym = [Wild, WS, H1, H2, M1, M2, M3, M4, L1, L2, L3, L4]

Const.C_ReelSets = [
    {
        Const.C_ReelName: 'base',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_ReelStrip: [
[[10,10],[6,10],[5,10],[2,10],[9,10],[7,10],[2,10],[6,10],[2,10],[4,10],[4,10],[9,10],[11,10],[5,10],[8,10],[1,10],[6,10],[9,10],[8,10],[5,10],[5,10],[3,10],[4,10],[4,10],[9,10],[6,10],[6,10],[8,10],[5,10],[6,10],[10,10],[4,10],[6,10],[3,10],[4,10],[8,10],[1,10],[1,10],[10,10],[3,10],[9,10],[90,10],[10,10],[11,10],[7,10],[4,10],[10,10],[2,10],[10,10],[6,10],[5,10],[7,10],[9,10],[90,10],[10,10],[7,10],[8,10],[7,10],[3,10],[4,10],[3,10],[10,10],[4,10],[6,10],[8,10],[2,10],[4,10],[5,10],[11,10],[9,10],[90,10],[10,10],[10,10],[4,10],[5,10],[9,10],[11,10],[11,10],[7,10],[9,10],[7,10],[5,10],[3,10],[10,10],[7,10],[10,10],[11,10],[10,10],[90,10],[6,10],[6,10],[8,10],[11,10],[3,10],[8,10],[8,10],[7,10],[10,10],[8,10],[10,10],[10,10],[1,10],[5,10],[9,10],[11,10],[7,10],[11,10],[8,10],[9,10],[9,10],[4,10],[6,10],[3,10],[7,10],[9,10],[7,10],[5,10],[5,10],[9,10],[8,10],[7,10],[11,10],[3,10],[6,10],[10,10],[11,10],[8,10],[11,10],[1,10],[9,10],[11,10],[4,10],[9,10],[9,10],[11,10],[7,10],[5,10],[11,10],[6,10],[4,10],[11,10],[2,10],[8,10],[9,10],[2,10],[2,10],[8,10],[9,10],[5,10],[1,10],[8,10],[5,10],[10,10],[9,10],[10,10],[4,10],[7,10],[10,10],[6,10],[5,10],[2,10],[9,10],[7,10],[2,10],[6,10],[2,10],[4,10],[6,10],[9,10],[11,10],[5,10],[8,10],[11,10],[6,10],[9,10],[8,10],[5,10],[5,10],[3,10],[4,10],[4,10],[9,10],[6,10],[6,10],[8,10],[5,10],[6,10],[10,10],[4,10],[6,10],[3,10],[4,10],[8,10],[3,10],[3,10],[10,10],[3,10],[9,10],[90,10],[10,10],[11,10],[7,10],[4,10],[10,10],[2,10],[10,10],[6,10],[5,10],[7,10],[9,10],[8,10],[10,10],[7,10],[8,10],[7,10],[3,10],[4,10],[3,10],[10,10],[4,10],[6,10],[8,10],[2,10],[4,10],[5,10],[11,10],[9,10],[9,10],[10,10],[10,10],[4,10],[5,10],[9,10],[11,10],[11,10],[7,10],[9,10],[7,10],[5,10],[3,10],[10,10],[7,10],[10,10],[11,10],[10,10],[4,10],[6,10],[6,10],[8,10],[11,10],[3,10],[8,10],[8,10],[7,10],[10,10],[8,10],[10,10],[10,10],[5,10],[5,10],[9,10],[11,10],[7,10],[11,10],[8,10],[9,10],[9,10],[4,10],[6,10],[3,10],[7,10],[9,10],[7,10],[5,10],[5,10],[9,10],[8,10],[7,10],[11,10],[3,10],[6,10],[10,10],[11,10],[8,10],[90,10],[9,10],[9,10],[11,10],[4,10],[9,10],[9,10],[11,10],[7,10],[5,10],[11,10],[6,10],[4,10],[11,10],[2,10],[8,10],[9,10],[2,10],[2,10],[8,10],[9,10],[5,10],[5,10],[8,10],[5,10],[10,10],[9,10],[10,10],[4,10],[7,10]],
[[10,10],[9,10],[7,10],[2,10],[7,10],[4,10],[1,10],[9,10],[9,10],[11,10],[4,10],[11,10],[3,10],[6,10],[11,10],[10,10],[11,10],[8,10],[1,10],[11,10],[2,10],[8,10],[10,10],[11,10],[4,10],[4,10],[10,10],[11,10],[11,10],[11,10],[90,10],[9,10],[9,10],[8,10],[10,10],[5,10],[7,10],[8,10],[8,10],[9,10],[11,10],[7,10],[5,10],[7,10],[1,10],[11,10],[1,10],[5,10],[2,10],[5,10],[2,10],[10,10],[6,10],[3,10],[7,10],[3,10],[8,10],[9,10],[9,10],[10,10],[5,10],[6,10],[10,10],[8,10],[11,10],[9,10],[1,10],[8,10],[8,10],[6,10],[5,10],[4,10],[9,10],[10,10],[5,10],[9,10],[9,10],[10,10],[9,10],[7,10],[11,10],[3,10],[10,10],[5,10],[6,10],[10,10],[11,10],[8,10],[3,10],[7,10],[4,10],[6,10],[8,10],[10,10],[7,10],[3,10],[10,10],[10,10],[7,10],[10,10],[2,10],[2,10],[8,10],[6,10],[10,10],[2,10],[11,10],[5,10],[4,10],[6,10],[8,10],[5,10],[6,10],[4,10],[6,10],[3,10],[6,10],[8,10],[90,10],[11,10],[3,10],[6,10],[10,10],[3,10],[11,10],[9,10],[11,10],[10,10],[4,10],[3,10],[7,10],[7,10],[9,10],[9,10],[4,10],[7,10],[7,10],[8,10],[8,10],[11,10],[90,10],[8,10],[10,10],[9,10],[7,10],[2,10],[7,10],[4,10],[1,10],[9,10],[9,10],[11,10],[4,10],[11,10],[3,10],[6,10],[11,10],[10,10],[90,10],[8,10],[2,10],[2,10],[2,10],[8,10],[10,10],[11,10],[4,10],[4,10],[10,10],[11,10],[11,10],[11,10],[90,10],[9,10],[9,10],[8,10],[10,10],[5,10],[7,10],[8,10],[8,10],[9,10],[11,10],[7,10],[5,10],[7,10],[10,10],[11,10],[4,10],[5,10],[2,10],[5,10],[2,10],[10,10],[6,10],[3,10],[7,10],[3,10],[8,10],[9,10],[9,10],[10,10],[5,10],[6,10],[10,10],[8,10],[11,10],[9,10],[9,10],[8,10],[8,10],[6,10],[5,10],[4,10],[9,10],[10,10],[5,10],[9,10],[9,10],[10,10],[9,10],[7,10],[11,10],[3,10],[10,10],[5,10],[6,10],[10,10],[11,10],[8,10],[3,10],[7,10],[4,10],[6,10],[8,10],[10,10],[7,10],[3,10],[10,10],[10,10],[7,10],[10,10],[2,10],[2,10],[8,10],[6,10],[10,10],[2,10],[11,10],[5,10],[4,10],[6,10],[8,10],[5,10],[6,10],[4,10],[6,10],[3,10],[6,10],[8,10],[90,10],[11,10],[3,10],[6,10],[10,10],[3,10],[11,10],[9,10],[11,10],[10,10],[4,10],[3,10],[7,10],[7,10],[9,10],[9,10],[4,10],[7,10],[7,10],[8,10],[90,10],[11,10],[8,10],[8,10]],
[[9,10],[10,10],[8,10],[10,10],[10,10],[4,10],[10,10],[8,10],[5,10],[11,10],[2,10],[1,10],[1,10],[7,10],[11,10],[4,10],[8,10],[2,10],[5,10],[9,10],[11,10],[90,10],[7,10],[11,10],[9,10],[4,10],[8,10],[2,10],[5,10],[11,10],[90,10],[9,10],[4,10],[9,10],[8,10],[6,10],[8,10],[2,10],[3,10],[2,10],[5,10],[6,10],[6,10],[4,10],[7,10],[10,10],[9,10],[6,10],[3,10],[4,10],[10,10],[6,10],[3,10],[11,10],[90,10],[8,10],[3,10],[10,10],[10,10],[3,10],[11,10],[9,10],[90,10],[8,10],[2,10],[10,10],[8,10],[6,10],[10,10],[7,10],[10,10],[10,10],[90,10],[11,10],[4,10],[6,10],[3,10],[8,10],[4,10],[8,10],[6,10],[9,10],[11,10],[7,10],[8,10],[9,10],[1,10],[8,10],[10,10],[1,10],[5,10],[11,10],[9,10],[3,10],[11,10],[5,10],[5,10],[6,10],[11,10],[8,10],[6,10],[9,10],[5,10],[7,10],[10,10],[7,10],[2,10],[7,10],[11,10],[11,10],[6,10],[5,10],[1,10],[2,10],[6,10],[11,10],[2,10],[2,10],[10,10],[4,10],[2,10],[10,10],[11,10],[4,10],[11,10],[11,10],[10,10],[9,10],[2,10],[5,10],[6,10],[7,10],[8,10],[3,10],[1,10],[10,10],[8,10],[4,10],[4,10],[4,10],[10,10],[6,10],[8,10],[4,10],[4,10],[9,10],[8,10],[5,10],[6,10],[9,10],[5,10],[4,10],[4,10],[9,10],[10,10],[8,10],[10,10],[10,10],[4,10],[10,10],[8,10],[5,10],[11,10],[2,10],[2,10],[2,10],[7,10],[11,10],[4,10],[8,10],[2,10],[5,10],[9,10],[11,10],[9,10],[7,10],[11,10],[9,10],[4,10],[8,10],[2,10],[5,10],[11,10],[90,10],[9,10],[4,10],[9,10],[8,10],[6,10],[8,10],[2,10],[3,10],[2,10],[5,10],[6,10],[6,10],[4,10],[7,10],[10,10],[9,10],[6,10],[3,10],[4,10],[10,10],[6,10],[3,10],[11,10],[7,10],[8,10],[3,10],[10,10],[10,10],[3,10],[11,10],[9,10],[9,10],[8,10],[2,10],[10,10],[8,10],[6,10],[10,10],[7,10],[10,10],[10,10],[10,10],[11,10],[4,10],[6,10],[3,10],[8,10],[4,10],[8,10],[6,10],[9,10],[11,10],[7,10],[8,10],[9,10],[4,10],[8,10],[10,10],[8,10],[5,10],[11,10],[9,10],[3,10],[11,10],[5,10],[5,10],[6,10],[11,10],[8,10],[6,10],[9,10],[5,10],[7,10],[10,10],[7,10],[2,10],[7,10],[11,10],[11,10],[6,10],[5,10],[7,10],[2,10],[6,10],[11,10],[2,10],[2,10],[10,10],[4,10],[2,10],[10,10],[11,10],[4,10],[11,10],[11,10],[10,10],[9,10],[2,10],[5,10],[6,10],[7,10],[8,10],[3,10],[3,10],[10,10],[8,10],[4,10],[4,10],[4,10],[10,10],[6,10],[8,10],[4,10],[4,10],[9,10],[8,10],[5,10],[6,10],[9,10],[5,10],[4,10],[4,10]],
[[9,10],[5,10],[5,10],[8,10],[6,10],[9,10],[5,10],[7,10],[6,10],[6,10],[7,10],[6,10],[6,10],[9,10],[11,10],[8,10],[90,10],[9,10],[9,10],[10,10],[5,10],[5,10],[11,10],[7,10],[5,10],[9,10],[3,10],[2,10],[11,10],[3,10],[10,10],[10,10],[6,10],[8,10],[3,10],[7,10],[4,10],[7,10],[10,10],[7,10],[6,10],[9,10],[10,10],[4,10],[10,10],[8,10],[5,10],[10,10],[4,10],[6,10],[8,10],[5,10],[11,10],[4,10],[1,10],[9,10],[1,10],[7,10],[2,10],[9,10],[10,10],[2,10],[3,10],[6,10],[2,10],[5,10],[11,10],[6,10],[6,10],[9,10],[4,10],[3,10],[2,10],[3,10],[7,10],[8,10],[10,10],[10,10],[3,10],[11,10],[11,10],[11,10],[8,10],[6,10],[6,10],[5,10],[8,10],[11,10],[11,10],[8,10],[4,10],[1,10],[1,10],[6,10],[8,10],[10,10],[2,10],[9,10],[8,10],[3,10],[7,10],[11,10],[5,10],[8,10],[9,10],[10,10],[4,10],[6,10],[7,10],[9,10],[7,10],[3,10],[11,10],[5,10],[11,10],[6,10],[11,10],[4,10],[5,10],[11,10],[10,10],[9,10],[4,10],[7,10],[4,10],[10,10],[11,10],[11,10],[90,10],[8,10],[9,10],[5,10],[8,10],[2,10],[4,10],[4,10],[9,10],[9,10],[11,10],[5,10],[3,10],[8,10],[9,10],[6,10],[8,10],[9,10],[2,10],[9,10],[5,10],[5,10],[8,10],[6,10],[9,10],[5,10],[7,10],[8,10],[8,10],[7,10],[6,10],[6,10],[9,10],[11,10],[8,10],[90,10],[9,10],[9,10],[10,10],[5,10],[5,10],[11,10],[7,10],[5,10],[9,10],[3,10],[2,10],[11,10],[3,10],[10,10],[10,10],[6,10],[8,10],[3,10],[7,10],[4,10],[7,10],[10,10],[7,10],[6,10],[9,10],[10,10],[4,10],[10,10],[8,10],[5,10],[10,10],[4,10],[6,10],[8,10],[5,10],[11,10],[4,10],[4,10],[9,10],[6,10],[7,10],[2,10],[9,10],[10,10],[2,10],[3,10],[6,10],[2,10],[5,10],[11,10],[6,10],[6,10],[9,10],[4,10],[3,10],[2,10],[3,10],[7,10],[8,10],[90,10],[10,10],[3,10],[11,10],[11,10],[11,10],[8,10],[6,10],[6,10],[5,10],[8,10],[11,10],[11,10],[8,10],[4,10],[1,10],[1,10],[6,10],[8,10],[10,10],[2,10],[9,10],[8,10],[3,10],[7,10],[11,10],[5,10],[8,10],[9,10],[10,10],[4,10],[6,10],[7,10],[9,10],[7,10],[3,10],[11,10],[5,10],[11,10],[6,10],[11,10],[4,10],[5,10],[11,10],[90,10],[9,10],[4,10],[7,10],[4,10],[10,10],[11,10],[90,10],[10,10],[8,10],[9,10],[5,10],[8,10],[2,10],[4,10],[4,10],[9,10],[9,10],[11,10],[5,10],[3,10],[8,10],[9,10],[6,10],[8,10],[9,10],[2,10]],
[[5,10],[7,10],[6,10],[6,10],[5,10],[5,10],[5,10],[7,10],[8,10],[1,10],[5,10],[1,10],[11,10],[11,10],[3,10],[9,10],[90,10],[10,10],[5,10],[3,10],[6,10],[2,10],[2,10],[7,10],[10,10],[3,10],[6,10],[10,10],[8,10],[8,10],[3,10],[5,10],[4,10],[9,10],[10,10],[9,10],[4,10],[7,10],[8,10],[10,10],[4,10],[10,10],[4,10],[7,10],[9,10],[5,10],[8,10],[11,10],[5,10],[2,10],[9,10],[90,10],[8,10],[9,10],[5,10],[3,10],[7,10],[7,10],[3,10],[11,10],[7,10],[2,10],[8,10],[4,10],[3,10],[3,10],[10,10],[9,10],[2,10],[7,10],[4,10],[11,10],[10,10],[11,10],[2,10],[5,10],[7,10],[3,10],[2,10],[11,10],[10,10],[11,10],[2,10],[6,10],[9,10],[10,10],[90,10],[11,10],[11,10],[2,10],[3,10],[7,10],[7,10],[9,10],[8,10],[11,10],[6,10],[8,10],[2,10],[6,10],[8,10],[3,10],[11,10],[6,10],[5,10],[6,10],[7,10],[7,10],[6,10],[1,10],[4,10],[8,10],[8,10],[2,10],[11,10],[3,10],[7,10],[3,10],[9,10],[5,10],[9,10],[11,10],[7,10],[1,10],[11,10],[5,10],[6,10],[9,10],[10,10],[2,10],[90,10],[10,10],[10,10],[5,10],[4,10],[4,10],[1,10],[2,10],[9,10],[9,10],[7,10],[2,10],[9,10],[6,10],[10,10],[10,10],[4,10],[10,10],[7,10],[10,10],[5,10],[7,10],[6,10],[6,10],[5,10],[5,10],[5,10],[7,10],[8,10],[2,10],[5,10],[1,10],[11,10],[11,10],[3,10],[9,10],[90,10],[10,10],[5,10],[3,10],[6,10],[2,10],[2,10],[7,10],[10,10],[3,10],[6,10],[10,10],[8,10],[8,10],[3,10],[5,10],[4,10],[9,10],[10,10],[9,10],[4,10],[7,10],[8,10],[8,10],[4,10],[10,10],[4,10],[7,10],[9,10],[5,10],[8,10],[11,10],[5,10],[2,10],[9,10],[90,10],[8,10],[9,10],[5,10],[3,10],[7,10],[7,10],[3,10],[11,10],[7,10],[2,10],[8,10],[4,10],[3,10],[3,10],[90,10],[9,10],[2,10],[7,10],[4,10],[11,10],[10,10],[11,10],[2,10],[5,10],[7,10],[3,10],[2,10],[11,10],[10,10],[11,10],[2,10],[6,10],[9,10],[10,10],[8,10],[11,10],[11,10],[2,10],[3,10],[7,10],[7,10],[9,10],[8,10],[11,10],[6,10],[8,10],[2,10],[6,10],[8,10],[3,10],[11,10],[6,10],[5,10],[6,10],[7,10],[7,10],[6,10],[8,10],[4,10],[8,10],[8,10],[2,10],[11,10],[3,10],[7,10],[3,10],[9,10],[5,10],[9,10],[11,10],[7,10],[7,10],[11,10],[5,10],[6,10],[9,10],[10,10],[2,10],[10,10],[10,10],[10,10],[5,10],[4,10],[4,10],[8,10],[2,10],[9,10],[9,10],[7,10],[2,10],[9,10],[6,10],[10,10],[10,10],[4,10],[10,10],[7,10],[10,10]]

        ]
    },
    {
        Const.C_ReelName: 'free',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_ReelStrip: [
[[10,10],[6,10],[5,10],[2,10],[9,10],[7,10],[2,10],[6,10],[2,10],[4,10],[4,10],[9,10],[1,10],[5,10],[8,10],[11,10],[6,10],[9,10],[8,10],[5,10],[5,10],[3,10],[4,10],[4,10],[9,10],[6,10],[6,10],[8,10],[5,10],[6,10],[10,10],[4,10],[6,10],[3,10],[1,10],[1,10],[8,10],[3,10],[10,10],[3,10],[9,10],[90,10],[10,10],[11,10],[7,10],[4,10],[10,10],[2,10],[10,10],[6,10],[5,10],[7,10],[9,10],[90,10],[10,10],[7,10],[8,10],[7,10],[3,10],[4,10],[3,10],[10,10],[4,10],[6,10],[8,10],[2,10],[4,10],[5,10],[11,10],[9,10],[90,10],[10,10],[10,10],[4,10],[5,10],[9,10],[11,10],[11,10],[7,10],[9,10],[7,10],[5,10],[3,10],[10,10],[7,10],[10,10],[11,10],[10,10],[90,10],[6,10],[6,10],[8,10],[11,10],[3,10],[8,10],[8,10],[7,10],[10,10],[8,10],[10,10],[10,10],[1,10],[5,10],[9,10],[11,10],[7,10],[11,10],[8,10],[9,10],[9,10],[4,10],[6,10],[3,10],[7,10],[9,10],[7,10],[5,10],[5,10],[9,10],[8,10],[7,10],[11,10],[3,10],[6,10],[10,10],[11,10],[8,10],[1,10],[1,10],[9,10],[11,10],[4,10],[9,10],[9,10],[11,10],[7,10],[5,10],[11,10],[6,10],[4,10],[11,10],[2,10],[8,10],[9,10],[2,10],[2,10],[8,10],[9,10],[5,10],[1,10],[8,10],[5,10],[10,10],[9,10],[10,10],[4,10],[7,10],[10,10],[6,10],[5,10],[2,10],[9,10],[7,10],[2,10],[6,10],[2,10],[4,10],[6,10],[9,10],[11,10],[5,10],[8,10],[11,10],[6,10],[9,10],[8,10],[5,10],[5,10],[3,10],[4,10],[4,10],[9,10],[6,10],[6,10],[8,10],[5,10],[6,10],[10,10],[4,10],[6,10],[3,10],[4,10],[8,10],[3,10],[3,10],[10,10],[3,10],[9,10],[90,10],[10,10],[11,10],[7,10],[4,10],[10,10],[2,10],[10,10],[6,10],[5,10],[7,10],[9,10],[8,10],[10,10],[7,10],[8,10],[7,10],[3,10],[4,10],[3,10],[10,10],[4,10],[6,10],[8,10],[2,10],[4,10],[5,10],[11,10],[9,10],[9,10],[10,10],[10,10],[4,10],[5,10],[9,10],[11,10],[11,10],[7,10],[9,10],[7,10],[5,10],[3,10],[10,10],[7,10],[10,10],[11,10],[10,10],[4,10],[6,10],[6,10],[8,10],[11,10],[3,10],[8,10],[8,10],[7,10],[10,10],[8,10],[10,10],[10,10],[5,10],[5,10],[9,10],[11,10],[7,10],[11,10],[8,10],[9,10],[9,10],[4,10],[6,10],[3,10],[7,10],[9,10],[7,10],[5,10],[5,10],[9,10],[8,10],[7,10],[11,10],[3,10],[6,10],[10,10],[11,10],[8,10],[90,10],[9,10],[9,10],[11,10],[4,10],[9,10],[9,10],[11,10],[7,10],[5,10],[11,10],[6,10],[4,10],[11,10],[2,10],[8,10],[9,10],[2,10],[2,10],[8,10],[9,10],[5,10],[5,10],[8,10],[5,10],[10,10],[9,10],[10,10],[4,10],[7,10]],
[[10,10],[9,10],[7,10],[2,10],[7,10],[4,10],[1,10],[9,10],[9,10],[11,10],[4,10],[11,10],[3,10],[6,10],[11,10],[10,10],[11,10],[8,10],[8,10],[11,10],[2,10],[8,10],[10,10],[11,10],[4,10],[4,10],[10,10],[11,10],[11,10],[11,10],[2,10],[2,10],[9,10],[1,10],[1,10],[5,10],[7,10],[8,10],[4,10],[9,10],[11,10],[7,10],[5,10],[7,10],[10,10],[11,10],[4,10],[5,10],[2,10],[5,10],[2,10],[10,10],[6,10],[3,10],[7,10],[3,10],[8,10],[9,10],[9,10],[10,10],[5,10],[6,10],[10,10],[8,10],[11,10],[9,10],[1,10],[1,10],[8,10],[6,10],[5,10],[4,10],[9,10],[10,10],[5,10],[9,10],[9,10],[10,10],[9,10],[7,10],[11,10],[3,10],[10,10],[5,10],[6,10],[10,10],[11,10],[8,10],[3,10],[7,10],[4,10],[6,10],[8,10],[10,10],[7,10],[3,10],[10,10],[10,10],[7,10],[10,10],[1,10],[2,10],[8,10],[6,10],[10,10],[2,10],[11,10],[5,10],[4,10],[6,10],[8,10],[5,10],[6,10],[4,10],[6,10],[3,10],[6,10],[8,10],[90,10],[11,10],[3,10],[6,10],[10,10],[3,10],[11,10],[9,10],[11,10],[10,10],[4,10],[3,10],[7,10],[7,10],[9,10],[9,10],[4,10],[7,10],[7,10],[8,10],[8,10],[11,10],[90,10],[8,10],[10,10],[9,10],[7,10],[2,10],[7,10],[4,10],[1,10],[9,10],[9,10],[11,10],[4,10],[11,10],[3,10],[6,10],[11,10],[10,10],[8,10],[8,10],[2,10],[2,10],[2,10],[8,10],[10,10],[11,10],[4,10],[4,10],[10,10],[11,10],[11,10],[11,10],[90,10],[9,10],[9,10],[8,10],[10,10],[5,10],[7,10],[8,10],[8,10],[9,10],[11,10],[7,10],[5,10],[7,10],[10,10],[11,10],[4,10],[5,10],[2,10],[5,10],[2,10],[10,10],[6,10],[3,10],[7,10],[3,10],[8,10],[9,10],[9,10],[10,10],[5,10],[6,10],[10,10],[8,10],[11,10],[9,10],[9,10],[8,10],[8,10],[6,10],[5,10],[4,10],[9,10],[10,10],[5,10],[9,10],[9,10],[10,10],[9,10],[7,10],[11,10],[3,10],[10,10],[5,10],[6,10],[10,10],[11,10],[8,10],[3,10],[7,10],[4,10],[6,10],[8,10],[10,10],[7,10],[3,10],[10,10],[10,10],[7,10],[10,10],[2,10],[2,10],[8,10],[6,10],[10,10],[2,10],[11,10],[5,10],[4,10],[6,10],[8,10],[5,10],[6,10],[4,10],[6,10],[3,10],[6,10],[8,10],[90,10],[11,10],[3,10],[6,10],[10,10],[3,10],[11,10],[9,10],[11,10],[10,10],[4,10],[3,10],[7,10],[7,10],[9,10],[9,10],[4,10],[7,10],[7,10],[8,10],[90,10],[11,10],[8,10],[8,10]],
[[9,10],[10,10],[8,10],[10,10],[10,10],[4,10],[10,10],[8,10],[5,10],[11,10],[2,10],[1,10],[1,10],[7,10],[11,10],[4,10],[8,10],[2,10],[5,10],[9,10],[11,10],[90,10],[7,10],[11,10],[9,10],[4,10],[8,10],[2,10],[5,10],[11,10],[90,10],[9,10],[4,10],[9,10],[1,10],[1,10],[8,10],[2,10],[3,10],[2,10],[5,10],[6,10],[6,10],[4,10],[7,10],[10,10],[9,10],[6,10],[3,10],[4,10],[10,10],[6,10],[3,10],[11,10],[90,10],[8,10],[3,10],[10,10],[10,10],[3,10],[11,10],[9,10],[90,10],[8,10],[2,10],[10,10],[8,10],[6,10],[10,10],[7,10],[10,10],[10,10],[90,10],[11,10],[4,10],[6,10],[3,10],[8,10],[4,10],[8,10],[6,10],[9,10],[11,10],[7,10],[8,10],[9,10],[4,10],[8,10],[10,10],[8,10],[5,10],[11,10],[9,10],[3,10],[11,10],[5,10],[5,10],[6,10],[11,10],[8,10],[6,10],[9,10],[5,10],[7,10],[10,10],[7,10],[2,10],[7,10],[11,10],[11,10],[6,10],[5,10],[7,10],[2,10],[6,10],[11,10],[1,10],[1,10],[10,10],[4,10],[2,10],[10,10],[11,10],[4,10],[11,10],[11,10],[10,10],[9,10],[2,10],[5,10],[6,10],[7,10],[8,10],[3,10],[1,10],[10,10],[8,10],[4,10],[4,10],[4,10],[10,10],[6,10],[8,10],[4,10],[4,10],[9,10],[8,10],[5,10],[6,10],[9,10],[5,10],[4,10],[4,10],[9,10],[10,10],[8,10],[10,10],[10,10],[4,10],[10,10],[8,10],[5,10],[11,10],[2,10],[2,10],[2,10],[7,10],[11,10],[4,10],[8,10],[2,10],[5,10],[9,10],[11,10],[9,10],[7,10],[11,10],[9,10],[4,10],[8,10],[2,10],[5,10],[11,10],[90,10],[9,10],[4,10],[9,10],[8,10],[6,10],[8,10],[2,10],[3,10],[2,10],[5,10],[6,10],[6,10],[4,10],[7,10],[10,10],[9,10],[6,10],[3,10],[4,10],[10,10],[6,10],[3,10],[11,10],[7,10],[8,10],[3,10],[10,10],[10,10],[3,10],[11,10],[9,10],[9,10],[8,10],[2,10],[10,10],[8,10],[6,10],[10,10],[7,10],[10,10],[10,10],[10,10],[11,10],[4,10],[6,10],[3,10],[8,10],[4,10],[8,10],[6,10],[9,10],[11,10],[7,10],[8,10],[9,10],[4,10],[8,10],[10,10],[8,10],[5,10],[11,10],[9,10],[3,10],[11,10],[5,10],[5,10],[6,10],[11,10],[8,10],[6,10],[9,10],[5,10],[7,10],[10,10],[7,10],[2,10],[7,10],[11,10],[11,10],[6,10],[5,10],[7,10],[2,10],[6,10],[11,10],[2,10],[2,10],[10,10],[4,10],[2,10],[10,10],[11,10],[4,10],[11,10],[11,10],[10,10],[9,10],[2,10],[5,10],[6,10],[7,10],[8,10],[3,10],[3,10],[10,10],[8,10],[4,10],[4,10],[4,10],[10,10],[6,10],[8,10],[4,10],[4,10],[9,10],[8,10],[5,10],[6,10],[9,10],[5,10],[4,10],[4,10]],
[[9,10],[5,10],[5,10],[8,10],[6,10],[9,10],[5,10],[7,10],[6,10],[6,10],[7,10],[6,10],[6,10],[9,10],[11,10],[8,10],[90,10],[9,10],[9,10],[10,10],[10,10],[5,10],[11,10],[7,10],[5,10],[9,10],[3,10],[2,10],[11,10],[3,10],[10,10],[10,10],[6,10],[8,10],[3,10],[7,10],[4,10],[7,10],[10,10],[7,10],[6,10],[9,10],[10,10],[4,10],[10,10],[8,10],[5,10],[10,10],[4,10],[6,10],[8,10],[5,10],[11,10],[1,10],[1,10],[9,10],[6,10],[7,10],[2,10],[9,10],[10,10],[2,10],[3,10],[6,10],[2,10],[5,10],[11,10],[6,10],[6,10],[9,10],[4,10],[3,10],[2,10],[3,10],[7,10],[8,10],[10,10],[10,10],[3,10],[11,10],[1,10],[11,10],[8,10],[6,10],[6,10],[5,10],[8,10],[11,10],[11,10],[8,10],[4,10],[4,10],[6,10],[6,10],[8,10],[1,10],[1,10],[9,10],[8,10],[3,10],[7,10],[11,10],[5,10],[8,10],[9,10],[10,10],[4,10],[6,10],[7,10],[9,10],[7,10],[3,10],[11,10],[5,10],[11,10],[6,10],[11,10],[4,10],[5,10],[11,10],[10,10],[9,10],[4,10],[7,10],[4,10],[10,10],[11,10],[11,10],[90,10],[8,10],[9,10],[5,10],[8,10],[2,10],[4,10],[4,10],[9,10],[9,10],[11,10],[5,10],[3,10],[8,10],[9,10],[6,10],[8,10],[9,10],[2,10],[9,10],[5,10],[5,10],[8,10],[6,10],[9,10],[5,10],[7,10],[8,10],[8,10],[7,10],[6,10],[6,10],[9,10],[11,10],[8,10],[90,10],[9,10],[9,10],[10,10],[5,10],[5,10],[11,10],[7,10],[5,10],[9,10],[3,10],[2,10],[11,10],[3,10],[10,10],[10,10],[6,10],[8,10],[3,10],[7,10],[4,10],[7,10],[10,10],[7,10],[6,10],[9,10],[10,10],[4,10],[10,10],[8,10],[5,10],[10,10],[4,10],[6,10],[8,10],[5,10],[11,10],[4,10],[4,10],[9,10],[6,10],[7,10],[2,10],[9,10],[10,10],[2,10],[3,10],[6,10],[2,10],[5,10],[11,10],[6,10],[6,10],[9,10],[4,10],[3,10],[2,10],[3,10],[7,10],[8,10],[8,10],[10,10],[3,10],[11,10],[11,10],[11,10],[8,10],[6,10],[6,10],[5,10],[8,10],[11,10],[11,10],[8,10],[4,10],[1,10],[1,10],[6,10],[8,10],[10,10],[2,10],[9,10],[8,10],[3,10],[7,10],[11,10],[5,10],[8,10],[9,10],[10,10],[4,10],[6,10],[7,10],[9,10],[7,10],[3,10],[11,10],[5,10],[11,10],[6,10],[11,10],[4,10],[5,10],[11,10],[90,10],[9,10],[4,10],[7,10],[4,10],[10,10],[11,10],[90,10],[10,10],[8,10],[9,10],[5,10],[8,10],[2,10],[4,10],[4,10],[9,10],[9,10],[11,10],[5,10],[3,10],[8,10],[9,10],[6,10],[8,10],[9,10],[2,10]],
[[5,10],[7,10],[6,10],[6,10],[5,10],[5,10],[5,10],[7,10],[8,10],[2,10],[5,10],[5,10],[11,10],[11,10],[3,10],[9,10],[90,10],[10,10],[5,10],[3,10],[6,10],[2,10],[2,10],[7,10],[10,10],[3,10],[6,10],[10,10],[8,10],[1,10],[3,10],[5,10],[4,10],[9,10],[10,10],[9,10],[4,10],[7,10],[8,10],[10,10],[4,10],[10,10],[4,10],[7,10],[9,10],[5,10],[8,10],[11,10],[5,10],[2,10],[9,10],[90,10],[8,10],[9,10],[5,10],[3,10],[7,10],[7,10],[3,10],[11,10],[7,10],[2,10],[8,10],[4,10],[3,10],[3,10],[10,10],[9,10],[2,10],[7,10],[4,10],[11,10],[10,10],[1,10],[2,10],[5,10],[7,10],[3,10],[2,10],[11,10],[10,10],[11,10],[2,10],[6,10],[9,10],[10,10],[90,10],[11,10],[11,10],[2,10],[3,10],[7,10],[7,10],[9,10],[8,10],[11,10],[6,10],[8,10],[2,10],[6,10],[8,10],[3,10],[11,10],[6,10],[5,10],[6,10],[7,10],[7,10],[6,10],[1,10],[1,10],[8,10],[8,10],[2,10],[11,10],[3,10],[7,10],[3,10],[9,10],[5,10],[9,10],[11,10],[1,10],[1,10],[11,10],[5,10],[6,10],[9,10],[10,10],[2,10],[90,10],[10,10],[10,10],[5,10],[4,10],[4,10],[2,10],[2,10],[9,10],[9,10],[7,10],[2,10],[9,10],[6,10],[10,10],[10,10],[4,10],[10,10],[7,10],[10,10],[5,10],[7,10],[6,10],[6,10],[5,10],[5,10],[5,10],[7,10],[8,10],[2,10],[5,10],[1,10],[11,10],[11,10],[3,10],[9,10],[90,10],[10,10],[5,10],[3,10],[6,10],[2,10],[2,10],[7,10],[10,10],[3,10],[6,10],[10,10],[8,10],[8,10],[3,10],[5,10],[4,10],[9,10],[10,10],[9,10],[4,10],[7,10],[8,10],[8,10],[4,10],[10,10],[4,10],[7,10],[9,10],[5,10],[8,10],[11,10],[5,10],[2,10],[9,10],[90,10],[8,10],[9,10],[5,10],[3,10],[7,10],[7,10],[3,10],[11,10],[7,10],[2,10],[8,10],[4,10],[3,10],[3,10],[90,10],[9,10],[2,10],[7,10],[4,10],[11,10],[10,10],[11,10],[2,10],[5,10],[7,10],[3,10],[2,10],[11,10],[10,10],[11,10],[2,10],[6,10],[9,10],[10,10],[8,10],[11,10],[11,10],[2,10],[3,10],[7,10],[7,10],[9,10],[8,10],[11,10],[6,10],[8,10],[2,10],[6,10],[8,10],[3,10],[11,10],[6,10],[5,10],[6,10],[7,10],[7,10],[6,10],[8,10],[4,10],[8,10],[8,10],[2,10],[11,10],[3,10],[7,10],[3,10],[9,10],[5,10],[9,10],[11,10],[7,10],[7,10],[11,10],[5,10],[6,10],[9,10],[10,10],[2,10],[10,10],[10,10],[10,10],[5,10],[4,10],[4,10],[8,10],[2,10],[9,10],[9,10],[7,10],[2,10],[9,10],[6,10],[10,10],[10,10],[4,10],[10,10],[7,10],[10,10]]

        ]
    },
    {
        Const.C_ReelName: 'super free',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_ReelStrip: [
[[10,10],[6,10],[5,10],[2,10],[9,10],[7,10],[2,10],[6,10],[2,10],[4,10],[4,10],[9,10],[11,10],[5,10],[8,10],[1,10],[1,10],[9,10],[8,10],[5,10],[5,10],[3,10],[4,10],[4,10],[9,10],[6,10],[6,10],[8,10],[5,10],[6,10],[10,10],[4,10],[6,10],[3,10],[4,10],[8,10],[8,10],[3,10],[10,10],[3,10],[9,10],[10,10],[11,10],[7,10],[4,10],[10,10],[2,10],[10,10],[6,10],[5,10],[7,10],[9,10],[10,10],[7,10],[8,10],[7,10],[3,10],[4,10],[3,10],[10,10],[4,10],[6,10],[8,10],[2,10],[4,10],[5,10],[11,10],[9,10],[10,10],[10,10],[4,10],[5,10],[9,10],[11,10],[11,10],[7,10],[9,10],[7,10],[5,10],[3,10],[10,10],[7,10],[10,10],[11,10],[10,10],[6,10],[6,10],[8,10],[11,10],[3,10],[8,10],[8,10],[7,10],[10,10],[8,10],[10,10],[10,10],[1,10],[5,10],[9,10],[11,10],[7,10],[11,10],[8,10],[9,10],[9,10],[4,10],[6,10],[3,10],[7,10],[9,10],[7,10],[5,10],[5,10],[9,10],[8,10],[7,10],[11,10],[3,10],[6,10],[10,10],[11,10],[8,10],[11,10],[1,10],[9,10],[11,10],[4,10],[9,10],[9,10],[11,10],[7,10],[5,10],[11,10],[6,10],[4,10],[11,10],[2,10],[8,10],[9,10],[2,10],[2,10],[8,10],[9,10],[5,10],[1,10],[8,10],[5,10],[10,10],[9,10],[10,10],[4,10],[7,10],[10,10],[6,10],[5,10],[2,10],[9,10],[7,10],[2,10],[6,10],[2,10],[4,10],[6,10],[9,10],[11,10],[5,10],[8,10],[11,10],[6,10],[9,10],[8,10],[5,10],[5,10],[3,10],[4,10],[4,10],[9,10],[6,10],[6,10],[8,10],[5,10],[6,10],[10,10],[4,10],[6,10],[3,10],[4,10],[8,10],[3,10],[3,10],[10,10],[3,10],[9,10],[10,10],[11,10],[7,10],[4,10],[10,10],[2,10],[10,10],[6,10],[5,10],[7,10],[9,10],[8,10],[10,10],[7,10],[8,10],[7,10],[3,10],[4,10],[3,10],[10,10],[4,10],[6,10],[8,10],[2,10],[4,10],[5,10],[11,10],[9,10],[9,10],[10,10],[10,10],[4,10],[5,10],[9,10],[11,10],[11,10],[7,10],[9,10],[7,10],[5,10],[3,10],[10,10],[7,10],[10,10],[11,10],[10,10],[4,10],[6,10],[6,10],[8,10],[11,10],[3,10],[8,10],[8,10],[7,10],[10,10],[8,10],[10,10],[10,10],[5,10],[5,10],[9,10],[11,10],[7,10],[11,10],[8,10],[9,10],[9,10],[4,10],[6,10],[3,10],[7,10],[9,10],[7,10],[5,10],[5,10],[9,10],[8,10],[7,10],[11,10],[3,10],[6,10],[10,10],[11,10],[8,10],[9,10],[9,10],[11,10],[4,10],[9,10],[9,10],[11,10],[7,10],[5,10],[11,10],[6,10],[4,10],[11,10],[2,10],[8,10],[9,10],[2,10],[2,10],[8,10],[9,10],[5,10],[5,10],[8,10],[5,10],[10,10],[9,10],[10,10],[4,10],[7,10]],
[[10,10],[9,10],[7,10],[2,10],[7,10],[4,10],[1,10],[9,10],[9,10],[11,10],[4,10],[11,10],[3,10],[6,10],[11,10],[10,10],[11,10],[8,10],[8,10],[11,10],[2,10],[8,10],[10,10],[11,10],[4,10],[4,10],[10,10],[11,10],[11,10],[11,10],[2,10],[2,10],[9,10],[8,10],[10,10],[5,10],[7,10],[8,10],[4,10],[9,10],[11,10],[7,10],[5,10],[7,10],[10,10],[11,10],[4,10],[5,10],[2,10],[5,10],[2,10],[10,10],[6,10],[3,10],[7,10],[3,10],[8,10],[9,10],[9,10],[10,10],[5,10],[6,10],[10,10],[8,10],[11,10],[9,10],[9,10],[8,10],[8,10],[6,10],[5,10],[4,10],[9,10],[10,10],[5,10],[9,10],[9,10],[10,10],[9,10],[7,10],[11,10],[3,10],[10,10],[5,10],[6,10],[10,10],[11,10],[8,10],[3,10],[7,10],[4,10],[6,10],[8,10],[10,10],[7,10],[3,10],[10,10],[10,10],[7,10],[10,10],[1,10],[2,10],[8,10],[6,10],[10,10],[2,10],[11,10],[5,10],[4,10],[6,10],[8,10],[5,10],[6,10],[4,10],[6,10],[3,10],[6,10],[8,10],[11,10],[3,10],[6,10],[10,10],[3,10],[11,10],[9,10],[11,10],[10,10],[4,10],[3,10],[7,10],[7,10],[9,10],[9,10],[4,10],[7,10],[7,10],[8,10],[8,10],[11,10],[8,10],[10,10],[9,10],[7,10],[2,10],[7,10],[4,10],[1,10],[9,10],[9,10],[11,10],[4,10],[11,10],[3,10],[6,10],[11,10],[10,10],[8,10],[2,10],[2,10],[2,10],[8,10],[10,10],[11,10],[4,10],[4,10],[10,10],[11,10],[11,10],[11,10],[9,10],[9,10],[8,10],[10,10],[5,10],[7,10],[8,10],[8,10],[9,10],[11,10],[7,10],[5,10],[7,10],[10,10],[11,10],[4,10],[5,10],[2,10],[5,10],[2,10],[10,10],[6,10],[3,10],[7,10],[3,10],[8,10],[9,10],[9,10],[10,10],[5,10],[6,10],[10,10],[8,10],[11,10],[9,10],[9,10],[8,10],[8,10],[6,10],[5,10],[4,10],[9,10],[10,10],[5,10],[9,10],[9,10],[10,10],[9,10],[7,10],[11,10],[3,10],[10,10],[5,10],[6,10],[10,10],[11,10],[8,10],[3,10],[7,10],[4,10],[6,10],[8,10],[10,10],[7,10],[3,10],[10,10],[10,10],[7,10],[10,10],[2,10],[2,10],[8,10],[6,10],[10,10],[2,10],[11,10],[5,10],[4,10],[6,10],[8,10],[5,10],[6,10],[4,10],[6,10],[3,10],[6,10],[8,10],[11,10],[3,10],[6,10],[10,10],[3,10],[11,10],[9,10],[11,10],[10,10],[4,10],[3,10],[7,10],[7,10],[9,10],[9,10],[4,10],[7,10],[7,10],[8,10],[11,10],[8,10],[8,10]],
[[9,10],[10,10],[8,10],[10,10],[10,10],[4,10],[10,10],[8,10],[5,10],[11,10],[2,10],[1,10],[1,10],[7,10],[11,10],[4,10],[8,10],[2,10],[5,10],[9,10],[11,10],[7,10],[11,10],[9,10],[4,10],[8,10],[2,10],[5,10],[11,10],[9,10],[4,10],[9,10],[8,10],[6,10],[8,10],[2,10],[3,10],[2,10],[5,10],[6,10],[6,10],[4,10],[7,10],[10,10],[9,10],[6,10],[3,10],[4,10],[10,10],[6,10],[3,10],[11,10],[8,10],[3,10],[10,10],[10,10],[3,10],[11,10],[9,10],[8,10],[2,10],[10,10],[8,10],[6,10],[10,10],[7,10],[10,10],[10,10],[11,10],[4,10],[6,10],[3,10],[8,10],[4,10],[8,10],[6,10],[9,10],[11,10],[7,10],[8,10],[9,10],[4,10],[8,10],[10,10],[8,10],[5,10],[11,10],[9,10],[3,10],[11,10],[5,10],[5,10],[6,10],[11,10],[8,10],[6,10],[9,10],[5,10],[7,10],[10,10],[7,10],[2,10],[7,10],[11,10],[11,10],[6,10],[5,10],[7,10],[2,10],[6,10],[11,10],[2,10],[2,10],[10,10],[4,10],[2,10],[10,10],[11,10],[4,10],[11,10],[11,10],[10,10],[9,10],[2,10],[5,10],[6,10],[7,10],[8,10],[3,10],[1,10],[10,10],[8,10],[4,10],[4,10],[4,10],[10,10],[6,10],[8,10],[4,10],[4,10],[9,10],[8,10],[5,10],[6,10],[9,10],[5,10],[4,10],[4,10],[9,10],[10,10],[8,10],[10,10],[10,10],[4,10],[10,10],[8,10],[5,10],[11,10],[2,10],[2,10],[2,10],[7,10],[11,10],[4,10],[8,10],[2,10],[5,10],[9,10],[11,10],[9,10],[7,10],[11,10],[9,10],[4,10],[8,10],[2,10],[5,10],[11,10],[9,10],[4,10],[9,10],[8,10],[6,10],[8,10],[2,10],[3,10],[2,10],[5,10],[6,10],[6,10],[4,10],[7,10],[10,10],[9,10],[6,10],[3,10],[4,10],[10,10],[6,10],[3,10],[11,10],[7,10],[8,10],[3,10],[10,10],[10,10],[3,10],[11,10],[9,10],[9,10],[8,10],[2,10],[10,10],[8,10],[6,10],[10,10],[7,10],[10,10],[10,10],[10,10],[11,10],[4,10],[6,10],[3,10],[8,10],[4,10],[8,10],[6,10],[9,10],[11,10],[7,10],[8,10],[9,10],[4,10],[8,10],[10,10],[8,10],[5,10],[11,10],[9,10],[3,10],[11,10],[5,10],[5,10],[6,10],[11,10],[8,10],[6,10],[9,10],[5,10],[7,10],[10,10],[7,10],[2,10],[7,10],[11,10],[11,10],[6,10],[5,10],[7,10],[2,10],[6,10],[11,10],[2,10],[2,10],[10,10],[4,10],[2,10],[10,10],[11,10],[4,10],[11,10],[11,10],[10,10],[9,10],[2,10],[5,10],[6,10],[7,10],[8,10],[3,10],[3,10],[10,10],[8,10],[4,10],[4,10],[4,10],[10,10],[6,10],[8,10],[4,10],[4,10],[9,10],[8,10],[5,10],[6,10],[9,10],[5,10],[4,10],[4,10]],
[[9,10],[5,10],[5,10],[8,10],[6,10],[9,10],[5,10],[7,10],[6,10],[6,10],[7,10],[6,10],[6,10],[9,10],[11,10],[8,10],[1,10],[1,10],[10,10],[10,10],[5,10],[11,10],[7,10],[5,10],[9,10],[3,10],[2,10],[11,10],[3,10],[10,10],[10,10],[6,10],[8,10],[3,10],[7,10],[4,10],[7,10],[10,10],[7,10],[6,10],[9,10],[10,10],[4,10],[10,10],[8,10],[5,10],[10,10],[4,10],[6,10],[8,10],[5,10],[11,10],[4,10],[1,10],[9,10],[6,10],[7,10],[2,10],[9,10],[10,10],[2,10],[3,10],[6,10],[2,10],[5,10],[11,10],[6,10],[6,10],[9,10],[4,10],[3,10],[2,10],[3,10],[7,10],[8,10],[10,10],[10,10],[3,10],[11,10],[11,10],[11,10],[8,10],[6,10],[6,10],[5,10],[8,10],[11,10],[11,10],[8,10],[4,10],[4,10],[6,10],[6,10],[8,10],[10,10],[2,10],[9,10],[8,10],[3,10],[7,10],[11,10],[5,10],[8,10],[9,10],[10,10],[4,10],[6,10],[7,10],[9,10],[7,10],[3,10],[11,10],[5,10],[11,10],[6,10],[11,10],[4,10],[5,10],[11,10],[10,10],[9,10],[4,10],[7,10],[4,10],[10,10],[11,10],[11,10],[8,10],[9,10],[5,10],[8,10],[2,10],[4,10],[4,10],[9,10],[9,10],[11,10],[5,10],[3,10],[8,10],[9,10],[6,10],[8,10],[9,10],[2,10],[9,10],[5,10],[5,10],[8,10],[6,10],[9,10],[5,10],[7,10],[8,10],[8,10],[7,10],[6,10],[6,10],[9,10],[11,10],[8,10],[9,10],[9,10],[10,10],[5,10],[5,10],[11,10],[7,10],[5,10],[9,10],[3,10],[2,10],[11,10],[3,10],[10,10],[10,10],[6,10],[8,10],[3,10],[7,10],[4,10],[7,10],[10,10],[7,10],[6,10],[9,10],[10,10],[4,10],[10,10],[8,10],[5,10],[10,10],[4,10],[6,10],[8,10],[5,10],[11,10],[4,10],[4,10],[9,10],[6,10],[7,10],[2,10],[9,10],[10,10],[2,10],[3,10],[6,10],[2,10],[5,10],[11,10],[6,10],[6,10],[9,10],[4,10],[3,10],[2,10],[3,10],[7,10],[8,10],[10,10],[3,10],[11,10],[11,10],[11,10],[8,10],[6,10],[6,10],[5,10],[8,10],[11,10],[11,10],[8,10],[4,10],[1,10],[1,10],[6,10],[8,10],[10,10],[2,10],[9,10],[8,10],[3,10],[7,10],[11,10],[5,10],[8,10],[9,10],[10,10],[4,10],[6,10],[7,10],[9,10],[7,10],[3,10],[11,10],[5,10],[11,10],[6,10],[11,10],[4,10],[5,10],[11,10],[9,10],[4,10],[7,10],[4,10],[10,10],[11,10],[10,10],[8,10],[9,10],[5,10],[8,10],[2,10],[4,10],[4,10],[9,10],[9,10],[11,10],[5,10],[3,10],[8,10],[9,10],[6,10],[8,10],[9,10],[2,10]],
[[5,10],[7,10],[6,10],[6,10],[5,10],[5,10],[5,10],[7,10],[8,10],[2,10],[5,10],[5,10],[11,10],[11,10],[1,10],[1,10],[10,10],[5,10],[3,10],[6,10],[2,10],[2,10],[7,10],[10,10],[3,10],[6,10],[10,10],[8,10],[8,10],[3,10],[5,10],[4,10],[9,10],[10,10],[9,10],[4,10],[7,10],[8,10],[10,10],[4,10],[10,10],[4,10],[7,10],[9,10],[5,10],[8,10],[11,10],[5,10],[2,10],[9,10],[8,10],[9,10],[5,10],[3,10],[7,10],[7,10],[3,10],[11,10],[7,10],[2,10],[8,10],[4,10],[3,10],[3,10],[10,10],[9,10],[2,10],[7,10],[4,10],[11,10],[10,10],[11,10],[2,10],[5,10],[7,10],[3,10],[2,10],[11,10],[10,10],[11,10],[2,10],[6,10],[9,10],[10,10],[11,10],[11,10],[2,10],[3,10],[7,10],[7,10],[9,10],[8,10],[11,10],[6,10],[8,10],[2,10],[6,10],[8,10],[3,10],[11,10],[6,10],[5,10],[6,10],[7,10],[7,10],[6,10],[1,10],[4,10],[8,10],[8,10],[2,10],[11,10],[3,10],[7,10],[3,10],[9,10],[5,10],[9,10],[11,10],[7,10],[1,10],[11,10],[5,10],[6,10],[9,10],[10,10],[2,10],[10,10],[10,10],[5,10],[4,10],[4,10],[2,10],[2,10],[9,10],[9,10],[7,10],[2,10],[9,10],[6,10],[10,10],[10,10],[4,10],[10,10],[7,10],[10,10],[5,10],[7,10],[6,10],[6,10],[5,10],[5,10],[5,10],[7,10],[8,10],[2,10],[5,10],[1,10],[11,10],[11,10],[3,10],[9,10],[10,10],[5,10],[3,10],[6,10],[2,10],[2,10],[7,10],[10,10],[3,10],[6,10],[10,10],[8,10],[8,10],[3,10],[5,10],[4,10],[9,10],[10,10],[9,10],[4,10],[7,10],[8,10],[8,10],[4,10],[10,10],[4,10],[7,10],[9,10],[5,10],[8,10],[11,10],[5,10],[2,10],[9,10],[8,10],[9,10],[5,10],[3,10],[7,10],[7,10],[3,10],[11,10],[7,10],[2,10],[8,10],[4,10],[3,10],[3,10],[9,10],[2,10],[7,10],[4,10],[11,10],[10,10],[11,10],[2,10],[5,10],[7,10],[3,10],[2,10],[11,10],[10,10],[11,10],[2,10],[6,10],[9,10],[10,10],[8,10],[11,10],[11,10],[2,10],[3,10],[7,10],[7,10],[9,10],[8,10],[11,10],[6,10],[8,10],[2,10],[6,10],[8,10],[3,10],[11,10],[6,10],[5,10],[6,10],[7,10],[7,10],[6,10],[8,10],[4,10],[8,10],[8,10],[2,10],[11,10],[3,10],[7,10],[3,10],[9,10],[5,10],[9,10],[11,10],[7,10],[7,10],[11,10],[5,10],[6,10],[9,10],[10,10],[2,10],[10,10],[10,10],[10,10],[5,10],[4,10],[4,10],[8,10],[2,10],[9,10],[9,10],[7,10],[2,10],[9,10],[6,10],[10,10],[10,10],[4,10],[10,10],[7,10],[10,10]]

        ]
    }
]


Free_Spins = {
    3: 8,
    4: 20,
    5: 50
}


Const.C_Game_Set = {
    "random_add_pro": [0.18,0.12,0.1,0.08,0.06,0.06,0.04,0.04,0.02,0.02,0.01,0.01,0.008,0.008,0.005,0.005,0.003,0.003,0.002,0.002,0.001,0,0],
    "add_num": [[6,20],[5,50],[4,150],[3,300],[2,200],[1,100]],

    "free_add_WS":[[10,5],[9,10],[8,20],[7,80],[6,150],[5,250],[4,500],[3,400],[2,200]],

    "super_free_add_WS":[[10,5],[9,10],[8,40],[7,60],[6,120],[5,150],[4,400],[3,300],[2,200]],

    "super_free_shape": [
        [{1, 2, 9, 12, 19, 20}, 120],
        [{0, 3, 9, 12, 18, 21}, 130],
        [{1, 2, 5, 6, 7, 14, 15, 16, 19, 20}, 5],
        [{5, 7, 14, 16}, 130],
        [{0, 3, 6, 10, 11, 15, 18, 21}, 50],
        [{1, 2, 4, 8, 10, 11, 13, 17, 19, 20}, 60],
        [{9, 10, 11, 12}, 130],
        [{0, 3, 5, 6, 7, 14, 15, 16, 18, 21}, 10],
        [{4, 5, 6, 7, 8, 13, 14, 15, 16, 17}, 60],
        [{0, 3, 6, 9, 12, 15, 18, 21}, 80],
        [{1, 2, 4, 8, 13, 17, 19, 20}, 130],
        [{5, 7, 10, 11, 14, 16}, 30],
        [{0, 4, 9, 13, 18, 3, 8, 12, 17, 21}, 30],
        [{0, 3, 10, 11, 18, 21}, 130],
        [{1, 2, 10, 11, 19, 20}, 60]

    ]
}

Const.C_Paytable = {
    Wild: [0, 0, 60, 120, 300],
    WS: [0, 0, 60, 120, 300],
    H1: [0, 0, 40, 80, 200],
    H2: [0, 0, 30, 60, 150],
    M1: [0, 0, 20, 40, 100],
    M2: [0, 0, 20, 40, 100],
    M3: [0, 0, 15, 30, 80],
    M4: [0, 0, 15, 30, 80],
    L1: [0, 0, 10, 20, 60],
    L2: [0, 0, 10, 20, 40],
    L3: [0, 0, 10, 20, 40],
    L4: [0, 0, 10, 20, 40],
    Scatter: [0,0,0,0,0]
}

Const.C_PayLine = Line.LINE_50_45454_TYPE1

Const.C_Free_PayLine = Line.LINE_50_45454_TYPE1

