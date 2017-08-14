def findprime(num):
    plist = [i for i in range(2,num)]
    p = 0
    while True:
        for i in plist[p+1:]:
            if i % plist[p] == 0:
                plist.remove(i)
        if plist[p] ** 2 >= plist[-1]:
            break
        p += 1
    return plist
print(findprime(120))
    
