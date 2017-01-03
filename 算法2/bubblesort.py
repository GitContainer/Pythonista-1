l = [5,6,0,-1,3,-6,12,1]

def bubblesort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
print(bubblesort(l))
# 没什么坑，注意 j 要减 去 i, i要减去 1