l = [7, 3, 0, 4, 3, 4, 2, 9, 4, 6, 3, 9, 4, 3]


def buddle_soft(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j+1],l[j]=l[j],l[j+1]
    return l


print(buddle_soft(l))
