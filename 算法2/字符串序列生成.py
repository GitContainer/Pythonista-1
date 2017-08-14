def genereate(s):
    if s == '':
        return ''
    elif len(s) == 1:
        return s
    else:
        s = s + ' '
        out = []
        flag = 1
        for i in range(len(s)-1):
            p = s[i]
            q = s[i+1]
            if p == q:
                flag += 1
            else:
                if flag >1:
                    out.append(p+str(flag))
                else:
                    out.append(p)
                flag = 1

        return ''.join(out)

l = genereate('caabaab')
# output ca2ba2b
print(l)
                
