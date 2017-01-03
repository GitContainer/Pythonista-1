l = [1,2,3,4,5,6,7,8,9]
#    0 1 2 3 4 5 6 7

def binarysearch(l,x):
    left, right = 0, len(l)-1
    while left <= right:
        mid = (left+right)//2
        if l[mid]<x:
            left = mid+1
        elif l[mid]>x:
            right = mid-1
        else:
            return mid
    return False
print(binarysearch(l,8))

#注意加 1 和 减 1 否则在剩两个数的时候会陷入死循环
