#!/home/absintio/VIDEO\ CORSO\ PYTHON/ESERCIZI/STRINGHE/ESPARTE1Es.UNPACKING
#@Python3.6 -U ABsintio -F SoluzioniUNPACKING.py -v GCC 2.7.0

tmp = '######### {esercizio} #########'.format(esercizio = 'ESERCIZIO 1')
tmp1 = '######### {esercizio} #########'.format(esercizio = 'ESERCIZIO 2')
tmp2 = '######### {esercizio} #########'.format(esercizio = 'ESERCIZIO 3')
tmp3 = '######### {esercizio} #########'.format(esercizio = 'ESERCIZIO 4')
tmp4 = '######### {esercizio} #########'.format(esercizio = 'ESERCIZIO 5')

#SOLUZIONI ESERCIZI STRINGHE 
#UNPACKING #####################################################################

"""
                ESERCIZIO 1

"""

print(tmp)
stringa = 'sequenza'
a0, a1, a2, a3, a4, a5, a6, a7 = stringa[:]
composta = a0+a1+a2+a3+a4+a5+a6+a7
print(composta+'\n')


"""
                ESERCIZIO 2

"""

print(tmp1)
stringa = 'ciao123456'
n1, n2, n3, n4, n5, n6 = stringa[4:]
result = int(n1) + int(n2) + int(n3) + int(n4) + int(n5) + int(n6)
print(str(result)+'\n')


"""
                ESERCIZIO 3

"""

print(tmp2)
stringa = '0123456789'
a0, a1, a2, a3, a4, a5, a6, a7, a8, a9 = stringa[:]
ora1 = a0+a9+':'+a4+a3+':'+a5+a6
ora2 = a1+a0+':'+a2+a7+':'+a5*2
ora3 = a1+a8+':'+a4+a2+':'+a3+a9
print(ora1 + '\n' + ora2 + '\n' + ora3 + '\n')


"""
                ESERCIZIO 4

"""

print(tmp3)
stringa = 'scossa'
a0, a1, a2 = stringa[:(len(stringa)//2)]
a3, a4, a5 = stringa[(len(stringa)//2):]
result1 = a0 + ' ' + a3
result2 = a1 + ' ' + a4
result3 = a2 + ' ' + a5
print(result1 + '\n' + result2 + '\n' + result3 + '\n')

