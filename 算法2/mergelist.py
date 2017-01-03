def mergelist(l1,l2,temp):
    if len(l1)==0 or len(l2) == 0:
        temp.extend(l1)
        temp.extend(l2)
        return temp
    else:
        if l1[0]<l2[0]:
            temp.append(l1[0])
            del l1[0]
        else:
            temp.append(l2[0])
            del l2[0]
        return mergelist(l1,l2,temp)