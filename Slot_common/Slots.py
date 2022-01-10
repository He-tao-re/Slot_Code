import random

import Slot_common.Const as Const
import util.Util as Util


'''处理reel，转换'''
class DealReel(object):

    def ReelStrip(self, ReelSet):
        for reel in ReelSet:
            dealreel = []
            strip = reel[Const.C_ReelStrip]
            for singalreel in strip:
                dealreel.append(self.DealSingalReel(singalreel))
            reel[Const.R_Dealed_ReelStrip] = dealreel
        return ReelSet


    def DealSingalReel(self, singalreel):
        Symbol_List = []
        Weight_List = []
        accumulate_weight = 0
        for i in singalreel:
            accumulate_weight += i[1]
            Symbol_List.append(i[0])
            Weight_List.append(accumulate_weight)
        return {Const.R_Symbol_List: Symbol_List, Const.R_Weight_List: Weight_List}


'''get 卷轴随机结果'''
class GetReel(object):
    def __init__(self, ReelSet, shape):
        self.reelset = ReelSet
        self.dealreel = ReelSet[Const.R_Dealed_ReelStrip]
        self.shape = shape

    def GetPos(self):
        pos = []
        for singalreel in self.dealreel:
            weight_list = singalreel[Const.R_Weight_List]
            pos_id = 0
            ra = random.randint(0, weight_list[-1])
            for i in weight_list:
                if i < ra:
                    pos_id += 1
                else:
                    break
            pos.append(pos_id)
        return pos

    def get_reel(self):
        pos = self.GetPos()
        reel = []

        for reel_idx in range(len(pos)):
            long_reel = self.dealreel[reel_idx][Const.R_Symbol_List] + self.dealreel[reel_idx][Const.R_Symbol_List][0: self.shape[0]]
            reel.append(long_reel[pos[reel_idx]:pos[reel_idx] + self.shape[reel_idx]])

        if self.reelset[Const.C_Mystery] is not False:
            mystery_change = Util.randdict(self.reelset[Const.C_Mystery_Weight])
            for x in range(len(reel)):
                for y in range(len(reel[x])):
                    if reel[x][y] == self.reelset[Const.C_Mystery]:
                        reel[x][y] = mystery_change
        if self.reelset[Const.C_Shuffle] is True:
            random.shuffle(reel)
        return reel

    def getdouble_reel(self):
        pos = self.GetPos()

        bonus_reel_stripes = self.reelset[Const.C_Bonus_Reel]

        reel = []
        bonus_reel = []

        for reel_idx in range(len(pos)):
            long_reel = self.dealreel[reel_idx][Const.R_Symbol_List] + self.dealreel[reel_idx][Const.R_Symbol_List][0: self.shape[0]]
            long_bonus_reel = bonus_reel_stripes[reel_idx] + bonus_reel_stripes[reel_idx][0: self.shape[0]]
            reel.append(long_reel[pos[reel_idx]:pos[reel_idx] + self.shape[0]])
            bonus_reel.append(long_bonus_reel[pos[reel_idx]:pos[reel_idx] + self.shape[0]])

        if self.reelset[Const.C_Mystery] is not False:
            mystery_change = Util.randdict(self.reelset[Const.C_Mystery_Weight])
            for x in range(len(reel)):
                for y in range(len(reel[x])):
                    if reel[x][y] == self.reelset[Const.C_Mystery]:
                        reel[x][y] = mystery_change
        return reel,bonus_reel


    def get_big_234_symReel(self, shape):
        pos = self.GetPos()
        reel = []

        for reel_idx in range(len(pos)):
            if reel_idx == 0:
                long_reel = self.dealreel[reel_idx][Const.R_Symbol_List] + self.dealreel[reel_idx][Const.R_Symbol_List][0: self.shape[0]]
                reel.append(long_reel[pos[reel_idx]:pos[reel_idx] + shape[0]])
            elif reel_idx == 1:
                long_reel = self.dealreel[reel_idx][Const.R_Symbol_List] + self.dealreel[reel_idx][Const.R_Symbol_List][0: self.shape[0]]
                big_sym = long_reel[pos[reel_idx]]
                reel.append([big_sym, big_sym, big_sym, big_sym])
                reel.append([big_sym, big_sym, big_sym, big_sym])
                reel.append([big_sym, big_sym, big_sym, big_sym])
            elif reel_idx == 2:
                long_reel = self.dealreel[reel_idx][Const.R_Symbol_List] + self.dealreel[reel_idx][Const.R_Symbol_List][0: self.shape[0]]
                reel.append(long_reel[pos[reel_idx]:pos[reel_idx] + shape[2]])

        return reel

    def Get_234_X3_SymReel(self):
        pos = self.GetPos()
        reel = []
        for reel_idx in range(len(pos)):
            if reel_idx == 0:
                long_reel = self.dealreel[reel_idx][Const.R_Symbol_List] + self.dealreel[reel_idx][Const.R_Symbol_List][0: 9]
                reel.append(long_reel[pos[reel_idx]:pos[reel_idx] + 9])
            elif reel_idx == 1:
                long_reel = self.dealreel[reel_idx][Const.R_Symbol_List] + self.dealreel[reel_idx][Const.R_Symbol_List][0: 3]
                big_sym_1 = long_reel[pos[reel_idx]]
                big_sym_2 = long_reel[pos[reel_idx] + 1]
                big_sym_3 = long_reel[pos[reel_idx] + 2]

                reel.append([big_sym_1, big_sym_1, big_sym_1, big_sym_2, big_sym_2, big_sym_2, big_sym_3, big_sym_3, big_sym_3])
                reel.append([big_sym_1, big_sym_1, big_sym_1, big_sym_2, big_sym_2, big_sym_2, big_sym_3, big_sym_3, big_sym_3])
                reel.append([big_sym_1, big_sym_1, big_sym_1, big_sym_2, big_sym_2, big_sym_2, big_sym_3, big_sym_3, big_sym_3])
            elif reel_idx == 2:
                long_reel = self.dealreel[reel_idx][Const.R_Symbol_List] + self.dealreel[reel_idx][Const.R_Symbol_List][0: 9]
                reel.append(long_reel[pos[reel_idx]:pos[reel_idx] + 9])

        return reel



'''处理reel结果，获得线上赢钱'''
class StandardLineEvaluator(object):
    def __init__(self, totalbet, spinreel, payline, paytable, betLine, wild_sub, linesym, wilds, wild):

        self.totalbet = totalbet
        self.spinreel = spinreel

        self.paytable = paytable
        self.payline = payline

        self.wildsub = wild_sub

        self.linesym = linesym
        self.wilds = wilds
        self.wild = wild
        self.betLine = betLine

        self.linebet = totalbet / betLine


    def GetAllLine(self):
        line_id = 0
        line_result = []
        for line in self.payline:
            col = 0
            line_combo = []
            line_pos = []

            for row in line:
                line_combo.append(self.spinreel[col][row])
                line_pos.append([col, row])
                col += 1
            line_result.append({Const.R_Line_Id: line_id, Const.R_Line_Combo: line_combo, Const.R_Line_Pos: line_pos})
            line_id += 1
        return line_result


    def evaluateLine(self, oneline):
        line_combo = oneline[Const.R_Line_Combo]
        sym_long = 0
        wild_long = 0
        kind = line_combo[0]
        line_mul = 0
        long = 0

        if line_combo[0] in self.linesym:
            if line_combo[0] in self.wildsub:
                for x in range(len(line_combo)):
                    if line_combo[x] == line_combo[0] or line_combo[x] in self.wilds:
                        sym_long += 1
                    else:
                        break

                kind = line_combo[0]
                line_mul = self.paytable[kind][sym_long-1]
                long = sym_long

            elif line_combo[0] in self.wilds:
                for x in range(len(line_combo)):
                    if line_combo[x] in self.wilds:
                        wild_long += 1
                    else:
                        break

                if wild_long < len(line_combo):

                    normal_sym = line_combo[wild_long]

                    if normal_sym in self.linesym:
                        for x in range(len(line_combo)):
                            if line_combo[x] == line_combo[wild_long] or line_combo[x] in self.wilds:
                                sym_long += 1
                            else:
                                break

                        if self.paytable[normal_sym][sym_long-1] >= self.paytable[self.wild][wild_long-1]:
                            line_mul = self.paytable[normal_sym][sym_long-1]
                            long = sym_long
                            kind = normal_sym
                        else:
                            line_mul = self.paytable[self.wild][wild_long-1]
                            long = wild_long
                            kind = self.wild
                    else:
                        line_mul = self.paytable[self.wild][wild_long-1]
                        long = wild_long
                        kind = self.wild
                else:
                    line_mul = self.paytable[self.wild][wild_long - 1]
                    long = wild_long
                    kind = self.wild

        oneline[Const.R_Line_Kind] = kind
        oneline[Const.R_Line_Mul] = line_mul
        oneline[Const.R_Line_Win] = line_mul * self.linebet
        oneline[Const.R_Line_Pos] = oneline[Const.R_Line_Pos][:long]
        oneline[Const.R_Line_Long] = long


        return oneline

    def evaluate(self):
        line_result = {}
        line_ifo = self.GetAllLine()
        line_result[Const.R_Line] = []
        winAmount = 0
        for singalline in line_ifo:
            oneline = self.evaluateLine(singalline)
            if oneline[Const.R_Line_Win] > 0:
                winAmount += oneline[Const.R_Line_Win]
                line_result[Const.R_Line].append(oneline)
        line_result[Const.R_Line_WinAmount] = winAmount
        line_result[Const.R_Win_Amount] = winAmount
        return line_result


    def mul_wild_evaluate(self,m_wild,wild_mul):
        line_result = {}
        line_ifo = self.GetAllLine()
        line_result[Const.R_Line] = []
        winAmount = 0
        for singalline in line_ifo:
            oneline = self.evaluateLine(singalline)
            if oneline[Const.R_Line_Win] > 0:

                if m_wild in oneline[Const.R_Line_Combo][:oneline[Const.R_Line_Long]]:

                    oneline[Const.R_Line_Mul] *= wild_mul
                    oneline[Const.R_Line_Win] *= wild_mul

                winAmount += oneline[Const.R_Line_Win]
                line_result[Const.R_Line].append(oneline)
        line_result[Const.R_Line_WinAmount] = winAmount
        line_result[Const.R_Win_Amount] = winAmount
        return line_result



class WayLineEvaluator(object):
    def __init__(self, Paytable, Wild_Sub, LineSym, Wilds, Wild, totalbet, line_num, spinreel):
        self.spinreel = spinreel
        self.Wild = Wild
        self.Wilds = Wilds
        self.LineSym = LineSym
        self.Paytable = Paytable
        self.Wild_Sub = Wild_Sub
        self.total_bet = totalbet
        self.line_bet = totalbet / line_num



    def Symbol_Count(self):
        symbol_count = []

        for sym in self.Wild_Sub:
            sym_pos = []
            num_count = [0,0,0,0,0,0]
            long = 0


            for col_idx in range(len(self.spinreel)):

                equal_sym_num = 0
                equal_sym_pos = []

                for row_idx in range(len(self.spinreel[col_idx])):
                    if self.spinreel[col_idx][row_idx] in self.Wilds or self.spinreel[col_idx][row_idx] == sym:
                        equal_sym_num += 1
                        equal_sym_pos.append(row_idx)


                num_count[col_idx] = equal_sym_num
                sym_pos.append(equal_sym_pos)

            for i in num_count:
                if i != 0:
                    long += 1
                else:break



            symbol_count.append(
                {
                    Const.R_Line_Pos: sym_pos,
                    Const.R_Number_Count: num_count,
                    Const.R_Line_Kind: sym,
                    Const.R_Line_Long: long,
                })


        return symbol_count

    def evaluate(self):
        sym_count = self.Symbol_Count()
        line_result = []
        win_amount = 0

        for v in sym_count:
            kind = v[Const.R_Line_Kind]
            long = v[Const.R_Line_Long]
            if long >= 1:
                basic_mul = self.Paytable[kind][long - 1]

                if basic_mul == 0:
                    pass

                else:
                    mul = basic_mul
                    for num in v[Const.R_Number_Count][:long]:
                        mul = mul * num

                    v[Const.R_Sym_Basic_Mul] = basic_mul
                    v[Const.R_Sym_Mul] = mul
                    v[Const.R_Sym_Win] = mul * self.line_bet

                    win_amount += mul * self.line_bet
                    line_result.append(v)

        return line_result, win_amount


    def Symbol_Count_S(self):
        symbol_count = []

        head_sym_set = set(self.spinreel[0])

        for head_sym in head_sym_set:
            if head_sym in self.LineSym:
                sym_pos = []
                num_count = []
                for x in range(len(self.spinreel)):

                    if head_sym in self.spinreel[x] or self.Wild in self.spinreel[x]:
                        sym_num = 0
                        for y in range(len(self.spinreel[x])):
                            idx = x + y * 5
                            if self.spinreel[x][y] == head_sym or self.spinreel[x][y] in self.Wilds:
                                sym_pos.append(idx)
                                sym_num += 1

                        num_count.append(sym_num)
                    else:
                        break
                symbol_count.append(
                     {Const.R_Line_Pos: sym_pos,
                      Const.R_Number_Count: num_count,
                      Const.R_Line_Kind: head_sym,
                      Const.R_Line_Long: len(num_count)})

            else:
                pass
        return symbol_count


    def evaluate_wild_mul(self, wild_data):
        sym_count = self.Symbol_Count_S()
        line_result = []
        win_amount = 0
        for v in sym_count:
            kind = v[Const.R_Line_Kind]
            long = v[Const.R_Line_Long]
            basic_mul = self.Paytable[kind][long - 1]

            if basic_mul == 0:
                pass

            else:
                mul = basic_mul
                for num in v[Const.R_Number_Count]:
                    mul = mul * num

                for wild_idx in wild_data.keys():
                    if wild_idx in v[Const.R_Line_Pos]:
                        mul = mul * wild_data[wild_idx]

                v[Const.R_Line_Mul] = mul
                v[Const.R_Line_Win] = mul * self.line_bet
                win_amount += mul * self.line_bet
                line_result.append(v)

        return line_result, win_amount
