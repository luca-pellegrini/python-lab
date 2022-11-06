# Acquisisci un numero scritto secondo il sistema di numerazione romano
print("Sono supportati solo numeri romani")
print("il cui corrispondente numero decimale è < 4000")
romanStr = input("Scrivi un numero romano: ")

"""
Il programma conta il n° di ricorrenze di ogni lettera I, V, X, L, C, D, M
nella scrittura romana del numero inserito (romanStr)
Ad ogni lettera è associato un valore numerico: 1, 5, 10, 50, 100, 500, 1000
Definiamo una variabile decNumber (inizialmente = 0), che sarà il risultato
della conversione di romanStr.
Si aumenta decNumber per ogni lettera presente nella sua scritta romana, 
secondo i rispettivi valori associati a ogni lettera.
I = +1
V = +5
X = +10
etc. etc.
Infine, si sottrae a decNumber un certo valore numerico, determinato dal
n° di ricorrenze di stringhe di tipo: IV, IX, XL, XC, CD, CM
IV, IX = -1
XL, XC = -10
CD, CM = -100
"""

# Conta il n° di ricorrenze di ogni lettera I, V, X, L, C, D, M
numI = romanStr.count('I')
numV = romanStr.count('V')
numX = romanStr.count('X')
numL = romanStr.count('L')
numC = romanStr.count('C')
numD = romanStr.count('D')
numM = romanStr.count('M')

decNumber = numI + numV*5 + numX*10 + numL*50 + numC*100 + numD*500 + numM*1000
print("Somma parziale:", decNumber) #DEBUG

# Conta il n° di ricorrenze di stringhe di tipo: IV, IX, XL, XC, CD, CM
numIV = romanStr.count('IV')
numIX = romanStr.count('IX')
numXL = romanStr.count('XL')
numXC = romanStr.count('XC')
numCD = romanStr.count('CD')
numCM = romanStr.count('CM')

decNumber = decNumber - (numIV + numIX)*2 - (numXL + numXC)*20 - (numCD + numCM)*200

# Visualizza decNumber
print("Numero decimale:", decNumber)