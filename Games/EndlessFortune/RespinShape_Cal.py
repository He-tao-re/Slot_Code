import Slot_common.Const as Const
import Slot_common.Slots as Slot
import util.Util as Util
import random
import copy


ReelSets = [
    {
        Const.C_ReelName: 'Base_1',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_Wild_Feature: None,
        Const.C_ReelStrip: [
            [[2,10], [2,10], [8,10], [5,10], [5,10], [8,10], [2,10], [4,10], [9,10], [5,10], [6,10], [3,10], [2,10], [8,10], [5,10], [9,10], [3,10], [2,10], [8,10], [5,10], [3,10], [2,10], [7,10], [2,10], [9,10], [8,10], [4,10], [5,10], [3,10], [7,10], [9,10], [2,10], [5,10], [4,10], [5,10], [7,10], [9,10], [1,10], [4,10], [7,10], [3,10], [4,10], [1,10], [8,10], [4,10], [94,10], [6,10], [2,10], [2,10], [3,10], [7,10], [4,10], [4,10], [7,10], [8,10], [4,10], [7,10], [2,10], [3,10], [5,10], [1,10], [90,10], [6,10], [4,10], [6,10], [3,10], [3,10], [6,10], [94,10], [94,10], [94,10], [9,10], [2,10], [6,10], [4,10], [5,10], [3,10], [5,10], [8,10], [9,10], [4,10], [3,10], [4,10], [4,10], [8,10], [94,10], [94,10], [94,10], [7,10], [5,10], [5,10], [5,10], [3,10], [94,10], [8,10], [5,10], [6,10], [3,10], [3,10], [5,10], [5,10], [7,10], [90,10], [9,10], [1,10], [1,10], [6,10], [3,10], [2,10], [4,10], [8,10], [2,10], [1,10], [8,10], [2,10], [4,10], [4,10], [1,10], [6,10], [5,10], [5,10], [5,10], [9,10], [1,10], [1,10], [6,10], [94,10], [94,10], [94,10], [8,10], [5,10], [5,10], [3,10], [2,10], [7,10], [3,10], [2,10], [8,10], [1,10], [1,10], [2,10], [8,10], [4,10], [4,10], [94,10], [94,10], [94,10], [3,10], [2,10], [1,10], [1,10], [4,10], [90,10], [5,10], [6,10], [1,10], [1,10], [4,10], [3,10], [2,10], ],
            [[2,10], [5,10], [8,10], [5,10], [5,10], [8,10], [1,10], [1,10], [94,10], [94,10], [4,10], [4,10], [4,10], [7,10], [2,10], [6,10], [4,10], [5,10], [8,10], [9,10], [2,10], [2,10], [2,10], [3,10], [94,10], [94,10], [3,10], [8,10], [1,10], [0,10], [0,10], [0,10], [3,10], [7,10], [5,10], [4,10], [1,10], [0,10], [5,10], [1,10], [9,10], [1,10], [3,10], [6,10], [9,10], [5,10], [1,10], [6,10], [8,10], [94,10], [1,10], [4,10], [4,10], [5,10], [3,10], [9,10], [8,10], [1,10], [7,10], [9,10], [5,10], [1,10], [3,10], [7,10], [94,10], [94,10], [3,10], [8,10], [6,10], [5,10], [5,10], [6,10], [94,10], [9,10], [5,10], [3,10], [8,10], [0,10], [2,10], [1,10], [5,10], [3,10], [7,10], [1,10], [94,10], [94,10], [2,10], [2,10], [2,10], [6,10], [7,10], [3,10], [3,10], [3,10], [2,10], [7,10], [1,10], [90,10], [7,10], [3,10], [3,10], [5,10], [1,10], [0,10], [0,10], [0,10], [2,10], [3,10], [8,10], [2,10], [6,10], [5,10], [2,10], [3,10], [2,10], [9,10], [5,10], [6,10], [3,10], [1,10], [1,10], [90,10], [7,10], [9,10], [4,10], [2,10], [7,10], [4,10], [5,10], [4,10], [8,10], [2,10], [6,10], [2,10], [4,10], [7,10], [4,10], [3,10], [94,10], [94,10], [5,10], [3,10], [5,10], [8,10], [1,10], [6,10], [2,10], [3,10], [9,10], [94,10], [94,10], [9,10], [4,10], [4,10], [2,10], [90,10], [8,10], [2,10], [2,10], [0,10], [3,10], [3,10], ],
            [[3,10], [4,10], [7,10], [2,10], [2,10], [6,10], [4,10], [1,10], [1,10], [9,10], [2,10], [2,10], [1,10], [7,10], [94,10], [2,10], [8,10], [4,10], [4,10], [1,10], [8,10], [4,10], [7,10], [1,10], [3,10], [90,10], [5,10], [8,10], [2,10], [3,10], [6,10], [2,10], [94,10], [94,10], [6,10], [3,10], [3,10], [3,10], [2,10], [6,10], [9,10], [0,10], [3,10], [5,10], [4,10], [7,10], [1,10], [9,10], [90,10], [7,10], [5,10], [3,10], [6,10], [7,10], [1,10], [3,10], [5,10], [90,10], [3,10], [3,10], [1,10], [9,10], [2,10], [2,10], [8,10], [3,10], [8,10], [2,10], [6,10], [0,10], [1,10], [5,10], [3,10], [1,10], [4,10], [8,10], [2,10], [5,10], [94,10], [94,10], [94,10], [2,10], [5,10], [8,10], [3,10], [1,10], [6,10], [5,10], [0,10], [7,10], [3,10], [2,10], [1,10], [7,10], [2,10], [4,10], [6,10], [3,10], [7,10], [2,10], [1,10], [4,10], [4,10], [8,10], [90,10], [3,10], [3,10], [3,10], [5,10], [5,10], [1,10], [90,10], [9,10], [4,10], [5,10], [5,10], [1,10], [9,10], [5,10], [2,10], [4,10], [9,10], [94,10], [94,10], [94,10], [8,10], [2,10], [5,10], [2,10], [90,10], [5,10], [5,10], [3,10], [0,10], [0,10], [0,10], [2,10], [4,10], [6,10], [2,10], [1,10], [2,10], [6,10], [94,10], [94,10], [94,10], [4,10], [4,10], [1,10], [0,10], [8,10], [4,10], [90,10], [1,10], [4,10], [1,10], [9,10], [5,10], [3,10], [6,10], ],
            [[3,10], [3,10], [5,10], [2,10], [9,10], [4,10], [4,10], [2,10], [90,10], [5,10], [5,10], [4,10], [4,10], [5,10], [5,10], [9,10], [3,10], [3,10], [6,10], [2,10], [2,10], [9,10], [1,10], [1,10], [3,10], [7,10], [2,10], [8,10], [6,10], [5,10], [5,10], [2,10], [9,10], [90,10], [1,10], [9,10], [2,10], [2,10], [7,10], [0,10], [0,10], [0,10], [2,10], [2,10], [90,10], [5,10], [5,10], [7,10], [3,10], [90,10], [5,10], [5,10], [7,10], [8,10], [5,10], [5,10], [94,10], [94,10], [3,10], [4,10], [8,10], [1,10], [2,10], [3,10], [0,10], [5,10], [6,10], [94,10], [4,10], [3,10], [3,10], [2,10], [94,10], [94,10], [6,10], [5,10], [1,10], [6,10], [9,10], [2,10], [1,10], [1,10], [6,10], [2,10], [2,10], [8,10], [1,10], [4,10], [90,10], [9,10], [2,10], [4,10], [4,10], [94,10], [94,10], [5,10], [8,10], [1,10], [6,10], [5,10], [5,10], [0,10], [7,10], [1,10], [1,10], [2,10], [94,10], [94,10], [7,10], [2,10], [8,10], [3,10], [1,10], [0,10], [8,10], [1,10], [1,10], [90,10], [5,10], [5,10], [5,10], [0,10], [7,10], [4,10], [5,10], [7,10], [2,10], [2,10], [7,10], [1,10], [94,10], [94,10], [6,10], [3,10], [3,10], [9,10], [1,10], [9,10], [3,10], [3,10], [8,10], [1,10], [7,10], [90,10], [4,10], [4,10], [4,10], [8,10], [0,10], [2,10], [2,10], [4,10], [94,10], [6,10], [3,10], [6,10], [4,10], [3,10], [2,10], [5,10], [1,10], [4,10], [8,10], [2,10], ],
            [[5,10], [9,10], [2,10], [1,10], [1,10], [5,10], [3,10], [7,10], [4,10], [1,10], [3,10], [8,10], [4,10], [9,10], [2,10], [94,10], [94,10], [94,10], [5,10], [8,10], [2,10], [90,10], [4,10], [7,10], [1,10], [0,10], [7,10], [3,10], [3,10], [7,10], [2,10], [6,10], [1,10], [3,10], [4,10], [4,10], [94,10], [94,10], [94,10], [8,10], [5,10], [4,10], [4,10], [0,10], [0,10], [0,10], [2,10], [4,10], [4,10], [5,10], [4,10], [3,10], [3,10], [3,10], [9,10], [1,10], [90,10], [4,10], [4,10], [1,10], [3,10], [4,10], [9,10], [1,10], [4,10], [90,10], [2,10], [4,10], [3,10], [2,10], [90,10], [3,10], [3,10], [5,10], [5,10], [9,10], [1,10], [5,10], [7,10], [2,10], [5,10], [94,10], [94,10], [94,10], [3,10], [1,10], [8,10], [3,10], [1,10], [1,10], [8,10], [1,10], [0,10], [6,10], [5,10], [6,10], [90,10], [9,10], [2,10], [5,10], [4,10], [8,10], [0,10], [6,10], [2,10], [3,10], [3,10], [3,10], [94,10], [6,10], [2,10], [2,10], [2,10], [0,10], [6,10], [5,10], [4,10], [7,10], [4,10], [5,10], [1,10], [2,10], [8,10], [5,10], [90,10], [2,10], [2,10], [8,10], [5,10], [94,10], [6,10], [1,10], [1,10], [9,10], [2,10], [2,10], [0,10], [9,10], [4,10], [5,10], [90,10], [3,10], [1,10], [8,10], [2,10], [5,10], [3,10], [0,10], [2,10], [1,10], [2,10], [1,10], [5,10], [4,10], [1,10], [4,10], [2,10], [4,10], [1,10], [7,10], ],

        ]
    },
    {
        Const.C_ReelName: 'Base_2',
        Const.C_Mystery: False,
        Const.C_Shuffle: False,
        Const.C_Mystery_Weight: None,
        Const.C_Wild_Feature: None,
        Const.C_ReelStrip: [
            [[2,10], [2,10], [8,10], [5,10], [5,10], [8,10], [2,10], [4,10], [9,10], [5,10], [6,10], [3,10], [2,10], [8,10], [5,10], [9,10], [3,10], [2,10], [8,10], [5,10], [3,10], [2,10], [7,10], [2,10], [9,10], [8,10], [4,10], [5,10], [3,10], [7,10], [9,10], [2,10], [5,10], [4,10], [5,10], [7,10], [9,10], [1,10], [4,10], [7,10], [3,10], [4,10], [1,10], [8,10], [4,10], [94,10], [6,10], [2,10], [2,10], [3,10], [7,10], [4,10], [4,10], [7,10], [8,10], [4,10], [7,10], [2,10], [3,10], [5,10], [1,10], [90,10], [6,10], [4,10], [6,10], [3,10], [3,10], [6,10], [94,10], [94,10], [94,10], [9,10], [2,10], [6,10], [4,10], [5,10], [3,10], [5,10], [8,10], [9,10], [4,10], [3,10], [4,10], [4,10], [8,10], [94,10], [94,10], [94,10], [7,10], [5,10], [5,10], [5,10], [3,10], [94,10], [8,10], [5,10], [6,10], [3,10], [3,10], [5,10], [5,10], [7,10], [90,10], [9,10], [1,10], [1,10], [6,10], [3,10], [2,10], [4,10], [8,10], [2,10], [1,10], [8,10], [2,10], [4,10], [4,10], [1,10], [6,10], [5,10], [5,10], [5,10], [9,10], [1,10], [1,10], [6,10], [94,10], [94,10], [94,10], [8,10], [5,10], [5,10], [3,10], [2,10], [7,10], [3,10], [2,10], [8,10], [1,10], [1,10], [2,10], [8,10], [4,10], [4,10], [94,10], [94,10], [94,10], [3,10], [2,10], [1,10], [1,10], [4,10], [90,10], [5,10], [6,10], [1,10], [1,10], [4,10], [3,10], [2,10], ],
            [[2,10], [5,10], [8,10], [5,10], [5,10], [8,10], [1,10], [1,10], [94,10], [94,10], [4,10], [4,10], [4,10], [7,10], [0,10], [6,10], [4,10], [5,10], [8,10], [9,10], [2,10], [2,10], [2,10], [3,10], [94,10], [94,10], [3,10], [8,10], [1,10], [1,10], [7,10], [3,10], [3,10], [7,10], [5,10], [4,10], [1,10], [8,10], [5,10], [1,10], [9,10], [1,10], [3,10], [6,10], [9,10], [5,10], [1,10], [6,10], [8,10], [94,10], [1,10], [4,10], [4,10], [5,10], [3,10], [9,10], [8,10], [1,10], [7,10], [9,10], [5,10], [1,10], [3,10], [7,10], [94,10], [94,10], [3,10], [8,10], [6,10], [5,10], [5,10], [6,10], [94,10], [9,10], [5,10], [3,10], [8,10], [0,10], [2,10], [1,10], [5,10], [3,10], [7,10], [1,10], [94,10], [94,10], [2,10], [2,10], [2,10], [6,10], [7,10], [3,10], [3,10], [3,10], [2,10], [7,10], [1,10], [90,10], [7,10], [3,10], [3,10], [5,10], [1,10], [0,10], [0,10], [0,10], [2,10], [3,10], [8,10], [2,10], [6,10], [5,10], [2,10], [3,10], [2,10], [9,10], [5,10], [6,10], [3,10], [1,10], [1,10], [90,10], [7,10], [9,10], [4,10], [2,10], [7,10], [4,10], [5,10], [4,10], [8,10], [2,10], [6,10], [2,10], [4,10], [7,10], [4,10], [94,10], [94,10], [94,10], [5,10], [3,10], [5,10], [8,10], [1,10], [6,10], [2,10], [3,10], [9,10], [94,10], [94,10], [94,10], [4,10], [4,10], [2,10], [90,10], [8,10], [2,10], [2,10], [0,10], [3,10], [3,10], ],
            [[3,10], [4,10], [7,10], [2,10], [2,10], [6,10], [4,10], [1,10], [1,10], [9,10], [0,10], [2,10], [1,10], [7,10], [94,10], [2,10], [8,10], [4,10], [4,10], [1,10], [8,10], [4,10], [7,10], [1,10], [3,10], [90,10], [5,10], [8,10], [2,10], [3,10], [6,10], [2,10], [94,10], [94,10], [6,10], [3,10], [3,10], [3,10], [2,10], [6,10], [9,10], [0,10], [3,10], [5,10], [4,10], [7,10], [1,10], [9,10], [90,10], [7,10], [5,10], [3,10], [6,10], [7,10], [1,10], [3,10], [5,10], [90,10], [3,10], [3,10], [1,10], [9,10], [0,10], [0,10], [8,10], [3,10], [8,10], [2,10], [6,10], [0,10], [1,10], [5,10], [3,10], [1,10], [4,10], [8,10], [2,10], [5,10], [9,10], [94,10], [94,10], [2,10], [5,10], [8,10], [3,10], [1,10], [6,10], [5,10], [0,10], [7,10], [3,10], [2,10], [1,10], [7,10], [2,10], [4,10], [6,10], [3,10], [7,10], [2,10], [1,10], [4,10], [4,10], [8,10], [1,10], [3,10], [3,10], [3,10], [5,10], [5,10], [1,10], [5,10], [9,10], [4,10], [5,10], [5,10], [1,10], [9,10], [5,10], [2,10], [4,10], [9,10], [8,10], [94,10], [94,10], [8,10], [2,10], [5,10], [2,10], [90,10], [5,10], [5,10], [3,10], [8,10], [7,10], [0,10], [2,10], [4,10], [6,10], [2,10], [1,10], [2,10], [6,10], [94,10], [94,10], [7,10], [4,10], [4,10], [1,10], [0,10], [8,10], [4,10], [90,10], [1,10], [4,10], [1,10], [9,10], [5,10], [3,10], [6,10], ],
            [[3,10], [3,10], [5,10], [2,10], [9,10], [4,10], [4,10], [2,10], [90,10], [5,10], [5,10], [4,10], [4,10], [5,10], [5,10], [9,10], [3,10], [3,10], [6,10], [2,10], [2,10], [9,10], [1,10], [1,10], [3,10], [7,10], [2,10], [8,10], [6,10], [5,10], [5,10], [2,10], [9,10], [90,10], [1,10], [9,10], [2,10], [2,10], [7,10], [0,10], [0,10], [0,10], [2,10], [2,10], [90,10], [5,10], [5,10], [7,10], [3,10], [90,10], [5,10], [5,10], [7,10], [8,10], [5,10], [5,10], [94,10], [94,10], [3,10], [4,10], [8,10], [1,10], [2,10], [3,10], [0,10], [5,10], [6,10], [94,10], [4,10], [3,10], [3,10], [2,10], [94,10], [94,10], [6,10], [5,10], [1,10], [6,10], [9,10], [2,10], [1,10], [1,10], [6,10], [2,10], [2,10], [8,10], [1,10], [4,10], [90,10], [9,10], [2,10], [4,10], [94,10], [94,10], [94,10], [5,10], [8,10], [1,10], [6,10], [5,10], [5,10], [0,10], [7,10], [1,10], [1,10], [94,10], [94,10], [94,10], [7,10], [2,10], [8,10], [3,10], [1,10], [0,10], [8,10], [1,10], [1,10], [90,10], [5,10], [5,10], [5,10], [0,10], [7,10], [4,10], [5,10], [7,10], [2,10], [2,10], [7,10], [1,10], [94,10], [94,10], [6,10], [3,10], [3,10], [9,10], [1,10], [9,10], [3,10], [3,10], [8,10], [1,10], [7,10], [90,10], [4,10], [4,10], [4,10], [8,10], [0,10], [2,10], [2,10], [4,10], [94,10], [6,10], [3,10], [6,10], [4,10], [3,10], [2,10], [5,10], [1,10], [4,10], [8,10], [2,10], ],
            [[5,10], [9,10], [2,10], [1,10], [1,10], [5,10], [3,10], [7,10], [4,10], [1,10], [3,10], [8,10], [4,10], [9,10], [2,10], [94,10], [94,10], [94,10], [5,10], [8,10], [2,10], [90,10], [4,10], [7,10], [1,10], [0,10], [7,10], [3,10], [3,10], [7,10], [2,10], [6,10], [1,10], [3,10], [4,10], [4,10], [94,10], [94,10], [94,10], [8,10], [5,10], [4,10], [4,10], [0,10], [0,10], [0,10], [2,10], [4,10], [4,10], [5,10], [4,10], [3,10], [3,10], [3,10], [9,10], [1,10], [90,10], [4,10], [4,10], [1,10], [3,10], [4,10], [9,10], [1,10], [4,10], [90,10], [2,10], [4,10], [3,10], [2,10], [90,10], [3,10], [3,10], [5,10], [5,10], [9,10], [1,10], [5,10], [7,10], [2,10], [5,10], [94,10], [94,10], [94,10], [3,10], [1,10], [8,10], [3,10], [1,10], [1,10], [8,10], [1,10], [0,10], [6,10], [5,10], [6,10], [90,10], [9,10], [2,10], [5,10], [4,10], [8,10], [0,10], [6,10], [2,10], [3,10], [3,10], [3,10], [94,10], [6,10], [2,10], [2,10], [2,10], [0,10], [6,10], [5,10], [4,10], [7,10], [4,10], [5,10], [1,10], [2,10], [8,10], [5,10], [90,10], [2,10], [2,10], [8,10], [5,10], [94,10], [6,10], [1,10], [1,10], [9,10], [2,10], [2,10], [0,10], [9,10], [4,10], [5,10], [90,10], [3,10], [1,10], [8,10], [2,10], [5,10], [3,10], [0,10], [2,10], [1,10], [2,10], [1,10], [5,10], [4,10], [1,10], [4,10], [2,10], [4,10], [1,10], [7,10], ],

        ]
    },
]


ReelSet_Weight = {0: 66,
                  1: 34}


Bonus = 94

high_pro = 0.2
low_pro = 0.16

high_pro_num = 3

respin_time = 5


ReelSet = Slot.DealReel().ReelStrip(ReelSets)


class Test(object):
    def __init__(self, test_time):

        self.shape_count = {'3X5': 0, '3X4': 0, '2X5': 0, '3X3': 0, '2X4': 0, '3X2': 0, '2X3': 0, '2X2': 0, "3X1": 0, '2X1': 0, "1X1": 0}
        self.test_time = test_time
        self.feature_hit = 0


    def test(self):

        time = 0
        while time < self.test_time:
            time += 1
            '''进度打印'''
            if time % (self.test_time / 20) == 0:
                print(str(int(time / self.test_time * 100)) + ' %')

            idx = Util.randdict(ReelSet_Weight)
            reel = Slot.GetReel(ReelSet[idx], [3,5]).get_reel()

            bonus_num = 0
            for x in range(5):
                for y in range(3):
                    if reel[x][y] == Bonus:
                        bonus_num += 1
            if bonus_num >= 6:
                self.feature_hit += 1
                shape_list = Respin(reel,high_pro,low_pro,high_pro_num).respin_game()
                for shape, num in shape_list.items():
                    self.shape_count[shape] += len(num)

        feature_interval = self.test_time / self.feature_hit

        print('feature触发间隔' + str(feature_interval))
        for shape, num in self.shape_count.items():
            average_num = num / self.feature_hit
            print(shape, average_num)

class Respin(object):
    def __init__(self, reel, high_pro, pro, high_pro_num):
        self.reel = reel
        self.high_pro = high_pro
        self.pro = pro
        self.high_pro_num = high_pro_num

        self.all_pos = {}
        self.bonus_pos = []
        self.blank_pos = {}

    def deal_reel(self):
        for x in range(5):
            for y in range(3):
                idx = x + y * 5

                if self.reel[x][y] == Bonus:
                    self.bonus_pos.append(idx)
                    self.all_pos[idx] = Bonus
                else:
                    self.blank_pos[idx] = low_pro
                    self.all_pos[idx] = None

    def distribute_pro(self):
        if len(self.blank_pos) >= 3:
            special_pos = random.sample(self.blank_pos.keys(), high_pro_num)
        else:
            special_pos = self.blank_pos.keys()

        for idx in special_pos:
            self.blank_pos[idx] = high_pro

    def respin_game(self):
        self.deal_reel()
        self.distribute_pro()

        times = copy.deepcopy(respin_time)

        while times > 0:
            times -= 1
            for idx in self.all_pos.keys():
                if self.all_pos[idx] != Bonus:
                    ra = random.random()
                    if ra < self.blank_pos[idx]:
                        self.all_pos[idx] = Bonus
                        self.bonus_pos.append(idx)


        shape_list = self.get_shape()

        # print(self.all_pos)
        # print(self.bonus_pos)
        # print(self.blank_pos)
        # print(shape_list)
        # print('\n')

        return shape_list

    def get_shape(self):
        shape_list = {'3X5': [], '3X4': [], '2X5': [], '3X3': [], '2X4': [], '3X2': [], '2X3': [], '2X2': [], "3X1": [], '2X1': [], "1X1": []}

        shape_3X5 = [{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14}]
        shape_3X4 = [{0,1,2,3,5,6,7,8,10,11,12,13},{1,2,3,4,6,7,8,9,11,12,13,14}]
        shape_2X5 = [{0,1,2,3,4,5,6,7,8,9},{5,6,7,8,9,10,11,12,13,14}]
        shape_3X3 = [{0,1,2,5,6,7,10,11,12},{1,2,3,6,7,8,11,12,13},{2,3,4,7,8,9,12,13,14}]
        shape_2X4 = [{0,1,2,3,5,6,7,8},{1,2,3,4,6,7,8,9},{5,6,7,8,10,11,12,13},{6,7,8,9,11,12,13,14}]
        shape_3X2 = [{0,1,5,6,10,11},{1,2,6,7,11,12},{2,3,7,8,12,13},{3,4,8,9,13,14}]
        shape_2X3 = [{0,1,2,5,6,7},{1,2,3,6,7,8},{2,3,4,7,8,9},{5,6,7,10,11,12},{6,7,8,11,12,13},{7,8,9,12,13,14}]
        shape_2X2 = [{0,1,5,6},{1,2,6,7},{2,3,7,8},{3,4,8,9},{5,6,10,11},{6,7,11,12},{7,8,12,13},{8,9,13,14}]
        shape_3X1 = [{0,5,10},{1,6,11},{2,7,12},{3,8,13},{4,9,14}]
        shape_2X1 = [{0,5},{5,10},{1,6},{6,11},{2,7},{7,12},{3,8},{8,13},{4,9},{9,14}]
        shape_1X1 = [{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}]

        bonus_list = copy.deepcopy(self.bonus_pos)
        bonus_list = set(bonus_list)

        for shape_combo in shape_3X5:
            if shape_combo <= bonus_list:
                shape_list['3X5'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        for shape_combo in shape_3X4:
            if shape_combo <= bonus_list:
                shape_list['3X4'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        for shape_combo in shape_2X5:
            if shape_combo <= bonus_list:
                shape_list['2X5'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        for shape_combo in shape_3X3:
            if shape_combo <= bonus_list:
                shape_list['3X3'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        for shape_combo in shape_2X4:
            if shape_combo <= bonus_list:
                shape_list['2X4'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        for shape_combo in shape_3X2:
            if shape_combo <= bonus_list:
                shape_list['3X2'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        for shape_combo in shape_2X3:
            if shape_combo <= bonus_list:
                shape_list['2X3'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        for shape_combo in shape_2X2:
            if shape_combo <= bonus_list:
                shape_list['2X2'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        for shape_combo in shape_3X1:
            if shape_combo <= bonus_list:
                shape_list['3X1'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        for shape_combo in shape_2X1:
            if shape_combo <= bonus_list:
                shape_list['2X1'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        for shape_combo in shape_1X1:
            if shape_combo <= bonus_list:
                shape_list['1X1'].append(shape_combo)
                for idx in shape_combo:
                    bonus_list.remove(idx)

        if len(bonus_list) > 0:
            print("False")

        return shape_list


