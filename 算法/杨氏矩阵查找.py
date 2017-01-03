def find(l,x):
    rows = len(1) -1
    cols = len(len[0])-1
    row = 0
    col = cols
    while col>0 and row<=rows:
        value = l[row][cols]
        if value == x:
            return True
        elif value > x:
            col = col-1
        elif value < x:
            row = row+1
    return True
