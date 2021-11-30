import util.Util as Util
import csv

Symbol_List = {
        "Wild": [3, 8, 7, 6, 8],
        "H1": [5, 7, 6, 8, 10],
        "H2": [8, 6, 7, 9, 10],
        "H3": [6, 8, 10, 9, 8],
        "H4": [10, 6, 8, 10, 9],
        "H5": [9, 10, 6, 12, 10],
        "L1": [12, 11, 10, 8, 7],
        "L2": [15, 12, 9, 8, 9],
        "L3": [11, 8, 12, 10, 11],
        "L4": [10, 12, 10, 10, 9],
        "L5": [9, 8, 9, 8, 9],
        "L6": [8, 9, 11, 7, 10],

}

def create_reel():
    filename = open('reels.csv','w',encoding='utf-8',newline="")
    csv_writer = csv.writer(filename)
    col = 5
    Symbol_List_Reverse = {}
    for i in range(col):
        Symbol_List_Reverse[i] = {}
        for k,v in Symbol_List.items():
            Symbol_List_Reverse[i][k] = v[i]

    reel_long = []
    for j in range(col):
        reel_long.append(sum(Symbol_List_Reverse[j].values()))

    long_max = max(reel_long)

    while long_max > 0:
        long_max -= 1
        row = []
        for x in range(col):
            if sum(Symbol_List_Reverse[x].values()) == 0:
                row.append("")
            else:
                sym = Util.randdict(Symbol_List_Reverse[x])
                Symbol_List_Reverse[x][sym] -= 1
                row.append(sym)
        csv_writer.writerow(row)
    filename.close()


if __name__ == "__main__":
    create_reel()

