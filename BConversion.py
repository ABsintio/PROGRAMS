''' Binary Convertion
    The function convert the number from base 10 to 2. 
    The range where the numbers can be rapresented goes
    from -128 (-2^(7)) to 127 (2^(7)-1)'''

from math import modf

#Define the conv_bin(D) function for the conversion of the number
def conv_bin(D):
    d = 2
    l = list(modf(D/d))
    if not l[0] == 0.0:
        l[0]=1
    else:
        l[0]=0
    lst = []
    lst.append(l[0])
    N = l[1]
    n = 1
    while n > 0:
        if len(lst) > 7:
            break
        C = N
        l = list(modf(C/d))
        if not l[0] == 0.0:
            l[0] = 1
        else:
            l[0]=0
        N = l[1]
        lst.append(l[0])
    lst.reverse()
    num_b = ''
    for x in lst[0:9]:
        num_b += x
    If D > 0:
        print('il numero è: ', num_b)
    elif D < 0:
        i = -1
        z = lst
        for i in range(8):
            if z[i]==0:
                z[i]=1
            elif z[i]==1:
                z[i]=0
        n = len(z)-1
        for i in range(8):
            if z[n-i]==1:
                z[n-i]=0
            elif z[n-i]==0:
                z[n-i]=1
                break
        num_b_ca2 = ''
        for x in z[0:9]:
            num_b_ca2 += x
        print('Il numero in Ca2 è: ', num_b_ca2)
