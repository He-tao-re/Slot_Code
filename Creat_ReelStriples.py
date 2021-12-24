import util.Util as Util
import csv

Symbol_List = {
        "S1": [5    ,7  ,5  ,4  ,7  ],
        "S2": [5    ,7  ,5  ,6  ,10 ],
        "S3": [10   ,7  ,5  ,6  ,10 ],
        "B1": [13   ,4  ,15 ,6  ,12 ],
        "B2": [5    ,12 ,5  ,12 ,8  ],
        "L1": [10   ,13 ,5  ,14 ,4  ],
        "L2": [7    ,12 ,15 ,7  ,13 ],
        "L3": [13   ,6  ,13 ,13 ,4  ],

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

