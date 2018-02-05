#!/home/absintio/VIDEO\ CORSO\ PYTHON/ESERCIZI/STRINGHE/ESPARTE1/Es.SLICING/
#@Python3.6 -U ABsintio -F SLICING.py -v GCC 7.2.0

tmp = '######### {esercizio} #########'.format(esercizio = 'ESERCIZIO 1')
tmp1 = '######### {esercizio} #########'.format(esercizio = 'ESERCIZIO 2')
tmp2 = '######### {esercizio} #########'.format(esercizio = 'ESERCIZIO 3')
tmp3 = '######### {esercizio} #########'.format(esercizio = 'ESERCIZIO 4')
tmp4 = '######### {esercizio} #########'.format(esercizio = 'ESERCIZIO 5')

#SOLUZIONE ESERCIZI STRINGHE
#SLICING #######################################################################

"""
            ESERCIZIO 1

"""

print(tmp)
stringa = 'Festa'
print(stringa[:3]) ; print(stringa[1:4]) ; print(stringa[2:5] + '\n')


"""
            ESERCIZIO 2

"""

print(tmp1)
stringa1 = 'fes'
stringa2 = 'est'
stringa3 = 'sta'
concatenazione = stringa1[:-1] + stringa2[-2:] + stringa3[-1]
print(concatenazione + '\n')


"""
            ESERCIZIO 3

"""

print(tmp2)
stringa = '123video456corso789python'
lunghezza = len(stringa)
s1 = stringa[:(-lunghezza+3)]
s2 = stringa[8:(-lunghezza+11)]
s3 = stringa[16:(-lunghezza+19)]
result = s1+s2+s3
print(result)
s4 = result[4] ; s5 = result[8]
indice5 = 4 ; indice9 = 8
if s4 == stringa[2*indice5+2] and s5 == stringa[2*indice9+2]:
    print(True)
else:
    print(str(False) + '\n')


"""
            ESERCIZIO 4

"""

print(tmp3)
stringa = '123video456corso789python'
lunghezza = len(stringa)
s1 = stringa[-lunghezza:3]
s2 = stringa[(-lunghezza+8):11]
s3 = stringa[(-lunghezza+16):19]
result = s1+s2+s3
print(result)
s4 = result[4]; s5 = result[8]
indice5 = 4 ; indice9 = 8
if s4 == stringa[2*indice5+2] or s5 == stringa[2*indice9+2]:
    print(str(True)+'\n')
else:
    print(False)


"""
            ESERCIZIO 5

"""

print(tmp4)
stringa = 'sequenza'
seq1 = stringa[:3]
seq2 = stringa[3:6]
seq3 = stringa[6:]
lun1 = len(seq1) ; lun2 = len(seq2) ; lun3 = len(seq3)
if lun1 == lun2 and lun2 == lun3 and lun1 == lun3:
    print(True)
else:
    print(str(False)+'\n')
