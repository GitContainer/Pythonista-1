l = [7, 3, 0, 4, 3, 4, 2, 9, 4, 6, 3, 9, 4, 3]


def qsort(l):
    if l == []:
        return []
    else:
        center = l[0]
        less = qsort([n for n in l[1:]  if n < center])
        big = qsort([n for n in l[1:] if n >= center])
    return less + [center] + big


print(qsort(l))
