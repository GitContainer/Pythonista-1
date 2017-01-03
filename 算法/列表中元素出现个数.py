def v_sort(l):
    s = {}
    for date in l:
        if date in s:
            s[date] += 1
        else:
            s[date] = 1

    print(s)

l=[2015,2016,2015,2017,2012,2012,2015,2017,2012,]

if __name__ == '__main__':
    v_sort(l)