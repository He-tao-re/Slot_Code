import Slot_common.Const as Const
import Slot_common.LinesConfig as Lines

Const.C_Shape = [8, 8, 8, 8, 8]

Const.C_BetLine = 60

base_reels = {0: 100}
free_reels = {1: 100}


Const.C_ReelSets = [
    {
        Const.C_ReelName: 'Base',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_ReelStrip: [
            [[7,10],[7,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[7,10],[7,10],[3,10],[3,10],[3,10],[3,10],[7,10],[7,10],[9,10],[9,10],[90,10],[90,10],[90,10],[6,10],[6,10],[2,10],[2,10],[2,10],[2,10],[9,10],[9,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[7,10],[7,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[8,10],[8,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[7,10],[7,10],[7,10],[7,10],[3,10],[3,10],[3,10],[3,10],[3,10],[3,10],[8,10],[8,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[7,10],[7,10],[7,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[2,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[7,10],[7,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[8,10],[8,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[3,10],[3,10],[3,10],[3,10],[3,10],[3,10],[8,10],[8,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[2,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[9,10],[9,10],[9,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[2,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[5,10],[5,10],[8,10],[8,10],[6,10],[6,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[8,10],[8,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[3,10],[3,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[7,10]],
            [[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[8,10],[8,10],[8,10],[4,10],[4,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[9,10],[9,10],[1,10],[1,10],[8,10],[8,10],[2,10],[2,10],[2,10],[2,10],[5,10],[5,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[3,10],[3,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[2,10],[2,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[0,10],[0,10],[0,10],[0,10],[7,10],[7,10],[6,10],[6,10],[1,10],[1,10],[7,10],[7,10],[2,10],[2,10],[8,10],[8,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[7,10],[7,10],[8,10],[8,10],[8,10],[4,10],[4,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[9,10],[9,10],[8,10],[8,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[5,10],[5,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[0,10],[0,10],[6,10],[6,10],[7,10],[7,10],[3,10],[3,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[2,10],[2,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[0,10],[0,10],[9,10],[9,10],[7,10],[7,10],[6,10],[6,10],[1,10],[1,10],[7,10],[7,10],[2,10],[2,10],[8,10],[8,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10]],
            [[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[7,10],[7,10],[7,10],[2,10],[2,10],[2,10],[3,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[3,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[6,10],[6,10],[4,10],[4,10],[7,10],[7,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[1,10],[1,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[3,10],[3,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[1,10],[1,10],[1,10],[1,10],[5,10],[5,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[0,10],[0,10],[0,10],[0,10],[8,10],[8,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[7,10],[7,10],[7,10],[2,10],[2,10],[2,10],[3,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[3,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[6,10],[6,10],[4,10],[4,10],[7,10],[7,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[1,10],[1,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[3,10],[3,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[1,10],[1,10],[1,10],[1,10],[5,10],[5,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[0,10],[0,10],[9,10],[9,10],[8,10],[8,10],[4,10],[4,10],[0,10],[0,10],[6,10],[6,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10]],
            [[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[9,10],[9,10],[9,10],[4,10],[4,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[6,10],[6,10],[1,10],[1,10],[1,10],[1,10],[5,10],[5,10],[5,10],[5,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[1,10],[1,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[3,10],[3,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[0,10],[0,10],[0,10],[0,10],[7,10],[7,10],[5,10],[5,10],[6,10],[6,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[9,10],[9,10],[9,10],[4,10],[4,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[6,10],[6,10],[1,10],[1,10],[1,10],[1,10],[5,10],[5,10],[5,10],[5,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[1,10],[1,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[0,10],[0,10],[3,10],[3,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[0,10],[0,10],[7,10],[7,10],[5,10],[5,10],[6,10],[6,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10]],
            [[3,10],[3,10],[3,10],[3,10],[6,10],[6,10],[6,10],[2,10],[2,10],[2,10],[2,10],[4,10],[4,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[6,10],[6,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[1,10],[1,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[1,10],[1,10],[1,10],[1,10],[7,10],[7,10],[7,10],[5,10],[5,10],[8,10],[8,10],[8,10],[9,10],[9,10],[0,10],[0,10],[0,10],[0,10],[6,10],[6,10],[2,10],[2,10],[8,10],[8,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[6,10],[6,10],[6,10],[2,10],[2,10],[2,10],[2,10],[4,10],[4,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[6,10],[6,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[1,10],[1,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[1,10],[1,10],[1,10],[1,10],[7,10],[7,10],[7,10],[5,10],[5,10],[0,10],[0,10],[8,10],[8,10],[8,10],[9,10],[9,10],[6,10],[6,10],[2,10],[2,10],[0,10],[0,10],[8,10],[8,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10]],

        ]
    },
    {
        Const.C_ReelName: 'Base',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_ReelStrip: [
            [[7,10],[7,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[7,10],[7,10],[3,10],[3,10],[3,10],[3,10],[7,10],[7,10],[9,10],[9,10],[90,10],[90,10],[90,10],[6,10],[6,10],[2,10],[2,10],[2,10],[2,10],[9,10],[9,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[7,10],[7,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[8,10],[8,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[7,10],[7,10],[7,10],[7,10],[3,10],[3,10],[3,10],[3,10],[3,10],[3,10],[8,10],[8,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[7,10],[7,10],[7,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[2,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[7,10],[7,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[8,10],[8,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[3,10],[3,10],[3,10],[3,10],[3,10],[3,10],[8,10],[8,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[2,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[9,10],[9,10],[9,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[2,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[5,10],[5,10],[8,10],[8,10],[6,10],[6,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[8,10],[8,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[3,10],[3,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[7,10]],
            [[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[0,10],[0,10],[8,10],[4,10],[4,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[9,10],[9,10],[0,10],[0,10],[0,10],[0,10],[9,10],[9,10],[8,10],[8,10],[2,10],[2,10],[2,10],[2,10],[5,10],[5,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[1,10],[1,10],[7,10],[7,10],[3,10],[3,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[2,10],[2,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[0,10],[0,10],[0,10],[0,10],[7,10],[7,10],[6,10],[6,10],[1,10],[1,10],[7,10],[7,10],[2,10],[2,10],[8,10],[8,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[8,10],[8,10],[8,10],[4,10],[4,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[9,10],[9,10],[0,10],[0,10],[0,10],[0,10],[9,10],[9,10],[8,10],[8,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[5,10],[5,10],[5,10],[5,10],[4,10],[4,10],[4,10],[4,10],[0,10],[0,10],[6,10],[6,10],[7,10],[7,10],[3,10],[3,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[2,10],[2,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[0,10],[0,10],[9,10],[9,10],[7,10],[7,10],[6,10],[6,10],[1,10],[1,10],[7,10],[7,10],[2,10],[2,10],[8,10],[8,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10]],
            [[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[0,10],[0,10],[7,10],[2,10],[2,10],[2,10],[3,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[3,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[6,10],[6,10],[4,10],[4,10],[7,10],[7,10],[2,10],[2,10],[2,10],[2,10],[0,10],[0,10],[0,10],[0,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[3,10],[3,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[1,10],[1,10],[1,10],[1,10],[5,10],[5,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[0,10],[0,10],[0,10],[0,10],[8,10],[8,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[7,10],[7,10],[7,10],[2,10],[2,10],[2,10],[3,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[3,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[6,10],[6,10],[4,10],[4,10],[7,10],[7,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[1,10],[1,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[3,10],[3,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[1,10],[1,10],[1,10],[1,10],[5,10],[5,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[0,10],[0,10],[9,10],[9,10],[8,10],[8,10],[4,10],[4,10],[0,10],[0,10],[6,10],[6,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10]],
            [[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[0,10],[0,10],[9,10],[4,10],[4,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[6,10],[6,10],[1,10],[1,10],[1,10],[1,10],[5,10],[5,10],[5,10],[5,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[0,10],[0,10],[0,10],[0,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[3,10],[3,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[0,10],[0,10],[0,10],[0,10],[7,10],[7,10],[5,10],[5,10],[6,10],[6,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[9,10],[9,10],[9,10],[4,10],[4,10],[9,10],[9,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[6,10],[6,10],[0,10],[0,10],[0,10],[0,10],[5,10],[5,10],[5,10],[5,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[1,10],[1,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[0,10],[0,10],[3,10],[3,10],[4,10],[4,10],[4,10],[4,10],[8,10],[8,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[8,10],[8,10],[9,10],[9,10],[0,10],[0,10],[7,10],[7,10],[5,10],[5,10],[6,10],[6,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10]],
            [[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[0,10],[0,10],[2,10],[2,10],[2,10],[4,10],[4,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[6,10],[6,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[0,10],[0,10],[0,10],[0,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[1,10],[1,10],[1,10],[1,10],[7,10],[7,10],[7,10],[5,10],[5,10],[8,10],[8,10],[8,10],[9,10],[9,10],[0,10],[0,10],[0,10],[0,10],[6,10],[6,10],[2,10],[2,10],[8,10],[8,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[0,10],[0,10],[6,10],[2,10],[2,10],[2,10],[2,10],[4,10],[4,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[1,10],[2,10],[2,10],[2,10],[3,10],[3,10],[3,10],[3,10],[5,10],[5,10],[5,10],[5,10],[6,10],[6,10],[3,10],[3,10],[2,10],[2,10],[2,10],[2,10],[1,10],[1,10],[1,10],[1,10],[4,10],[4,10],[4,10],[4,10],[6,10],[6,10],[7,10],[7,10],[5,10],[5,10],[5,10],[5,10],[1,10],[1,10],[1,10],[1,10],[7,10],[7,10],[7,10],[5,10],[5,10],[0,10],[0,10],[8,10],[8,10],[8,10],[9,10],[9,10],[6,10],[6,10],[2,10],[2,10],[0,10],[0,10],[8,10],[8,10],[7,10],[7,10],[2,10],[2,10],[3,10],[3,10],[90,10],[90,10],[90,10],[4,10],[4,10],[4,10],[4,10],[9,10],[9,10],[9,10],[2,10],[2,10]],

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
Scatter = 90
Respin_Blank = 100

Wilds = [Wild]
Const.C_Wild_Sub = [H1,H2,H3,H4,H5,L1,L2,L3,L4,L5,L6]
Const.C_LineSym = [Wild,H1,H2,H3,H4,H5,L1,L2,L3,L4,L5,L6]

Grand = Const.C_Grand
Mega = Const.C_Mega
Major = Const.C_Major
Minor = Const.C_Minor
Mini = Const.C_Mini

Const.C_Game_Set = {
    "SC_Freespin": [[1, 150], [2, 80], [3, 20]],

    "Respin_Pro_Set_Choose": [[0,6500],[1,2000],[2,1000],[3,500]],
    "Respin_Pro_Set": [
        [
            [
                [[1,1],[0.4,6]],[[1,1],[0.4,4]],[[0.8,1],[0.35,4]],[[0.6,1],[0.35,4]],[[0,0],[0.35,4]],[[0,0],[0.3,4]],[[0,0],[0.25,4]],[[0,0],[0.15,3]]
            ],
            0.05
        ],
        [
            [
                [[1,1],[0.4,6]],[[1,1],[0.4,4]],[[0.8,1],[0.35,4]],[[0.6,1],[0.35,4]],[[0,0],[0.35,4]],[[0,0],[0.3,4]],[[0,0],[0.25,4]],[[0,0],[0.15,3]]
            ],
            0.15
        ],
        [
            [
                [[1,1],[0.5,6]],[[1,1],[0.5,6]],[[0.8,1],[0.4,4]],[[0.6,1],[0.4,4]],[[0,0],[0.4,4]],[[0,0],[0.35,4]],[[0,0],[0.3,4]],[[0,0],[0.3,3]]
            ],
            0.05
        ],
        [
            [
                [[1,1],[0.5,6]],[[1,1],[0.5,6]],[[0.8,1],[0.4,4]],[[0.6,1],[0.4,4]],[[0,0],[0.4,4]],[[0,0],[0.35,4]],[[0,0],[0.3,4]],[[0,0],[0.3,3]]
            ],
            0.15
        ]
    ],
    "Power_UP_Pool": [201,201,202,202,203,204],
    "Surpass_Power_Up": 204,
    "203_pick_num": [[10,2],[9,8],[8,15],[7,40],[6,100],[5,250],[4,400]],
    "203_prize": [[300,50],[240,100],[200,150],[180,180],[150,300],[120,500],[100,600],[80,800],[60,1000],[50,1200],[40,1500],[30,2000],[20,1620]],
    "204_Weight_1": [[Grand,1],[12,1000],[5,1000],[Mini,1200],[8,1500],[Minor,300],[30,200],[8,1200],[Mega,10],[15,500],[5,1000],[Mini,1200],[2,200],[8,1500],[Major,20],[5,1000],[Minor,300],[12,800]],
    "204_Weight_2": [[Grand,1],[12,450],[5,1500],[Minor,300],[12,450],[Major,50],[30,200],[Mini,600],[8,800],[2,1000],[Mega,10],[15,400],[5,1500],[Mini,600],[2,1000],[Minor,300],[5,1500],[8,800]],
}

Const.C_Jackpot_Set = {
    Grand: 2000,
    Mega: 500,
    Major: 100,
    Minor: 20,
    Mini: 10
}


Base_Respin_H1 = 8
Free_Respin_H1 = 6









Const.C_Paytable = {
    H1: [0, 0, 15, 30, 150],
    H2: [0, 0, 10, 20, 100],
    H3: [0, 0, 10, 20, 100],
    H4: [0, 0, 10, 20, 100],
    H5: [0, 0, 10, 20, 100],
    L1: [0, 0, 6, 12, 60],
    L2: [0, 0, 6, 12, 60],
    L3: [0, 0, 6, 12, 60],
    L4: [0, 0, 6, 12, 60],
    Scatter: [0, 0, 2, 5, 10]
}

Const.C_PayLine = Lines.LINE_60_5X8_TYPE1
Payline_70 = Lines.LINE_70_5X8_TYPE1
Payline_80 = Lines.LINE_80_5X8_TYPE1