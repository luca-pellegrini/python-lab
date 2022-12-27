# print_perfect_magic_square.py
from my_input import *

# Acquisizione dato dall'utente
while True :
    n = inputPositiveInteger("")
    if n % 2 == 1 : break
print()

matrix = []
# riempio la matrice di zeri, che durante l'esecuzione dell'algoritmo
# di generazione del quadrato magico significheranno "posizione non
# ancora scritta", perché 0 non è un valore valido nel quadrato
for i in range(n) :
   matrix.append([0]*n)

# Algoritmo suggerito
riga = n-1
colonna = n // 2
for k in range(1, n*n + 1) :
    matrix[riga][colonna] = k
    previousR = riga
    previousC = colonna
    riga += 1
    colonna += 1
    if riga == n : riga = 0
    if colonna == n : colonna = 0
    if matrix[riga][colonna] != 0 :
        riga = previousR
        colonna = previousC
        riga -= 1

# Visualizza la matrice
a = len(str(n*n))
formatStr = "%" + str(a) + "d"
for i in range(n) : # riga
    for j in range(n) : # colonna
        print(formatStr % matrix[i][j], end=" ")
    print()
print()

