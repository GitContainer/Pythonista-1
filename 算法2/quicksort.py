l = [5,6,0,-1,3,-6,12,1]

def quicksort(l):
    if len(l) <= 1:
        return l
    else:
        center= l[0]
        less = quicksort([n for n in l[1:] if n < center])
        more = quicksort([n for n in l[1:] if n >= center])
        return less + [center] + more
print(quicksort(l))
#三个坑
# len
# 递归外面要加括号，使其成为列表
# 要对l 进行切片，跳过第一个
