# is_perfect_magic_square.py
from sys import exit

## Riceve in input una stringa scritta dall'utente
#  La stringa deve contenere una sequenza di numeri interi positivi.
# Chiede all'utente di inserire una sequenza di numeri interi positivi (separati da almeno uno spazio), visualizzando il messaggio 'message'
#  Restituisce una lista con i numeri inseriti dall'utente
def inputSequenceOfNumbers() :
    s = input()
    i = 0
    row = [ ]
    while i < len(s) :
        # "consuma" eventuali spazi
        while i < len(s) and s[i] == " " : i += 1
        j = i # forse inizia un numero
        while i < len(s) and s[i].isdigit() :
                i += 1 # "consuma" cifre
        if i == j : # non c'erano cifre, non era un numero
            exit("Errore")
        # aggiungo il numero alla fine della riga che sto costruendo
        row.append(int(s[j:i]))
    return row


# Inizializzazione variabili e acquisizione dati dall'utente
matrix = [ ]

riga = inputSequenceOfNumbers()
#print("DEBUG", riga)
N = len(riga) # dimensioni del quadrato
print("DEBUG: n =", N)
matrix.append(riga)
i = 1
while i < N :
    riga = inputSequenceOfNumbers()
    #print("DEBUG", riga)
    matrix.append(riga)
    i += 1
print()

# Verifica che tutte le righe abbiano la stessa lunghezza
for row in matrix :
    if len(row) != N :
        exit("Errore: le righe non hanno tutte la stessa lunghezza")

# Verifica che il quadrato magico contenga tutti e soli i numeri da 1 a n**2 senza ripetizioni
sequence = [ ]
for row in matrix :
    sequence = sequence + row
for n in range(1, N*N + 1) :
    if n not in sequence :
        exit("Manca il numero %d" % n)

# Visualizza la matrice
a = len(str(max(sequence)))
formatStr = "%" + str(a) + "d"
for j in range(N) : # riga
    for k in range(N) : # colonna
        print(formatStr % matrix[j][k], end=" ")
    print()
print()

# Verifica regole del quadrato magico
# Numeri tutti diversi (in realtà l'ho già verificato sopra)
for n in sequence :
    if sequence.count(n) > 1 :
        exit("Il quadrato contiene numeri duplicati, non è un quadrato magico")

# Verifico che la somma di ogni riga, di ogni colonna e delle diagonali abbia lo stesso valore
MAGIC_NUMBER = sum(matrix[0])
# righe
for i in range(1, N) :
    if sum(matrix[i]) != MAGIC_NUMBER :
        exit("La riga %d è sbagliata" % (i+1))
# colonne
for j in range(N) : # colonna
    columnSum = 0
    for k in range(N) : # riga
        columnSum += matrix[k][j]
    if columnSum != MAGIC_NUMBER :
        exit("La colonna %d è sbagliata" % (i+1))
# diagonali principali
tempSum = 0
for i in range(N) :
    tempSum += matrix[i][i]
if tempSum != MAGIC_NUMBER :
    exit("La diagonale dall'angolo superiore sinistro è sbagliata")
tempSum = 0
for i in range(N) :
   tempSum += matrix[i][N - i - 1]
if tempSum != MAGIC_NUMBER :
   exit("La diagonale dall'angolo superiore destro è sbagliata")

# Se il programma arriva qui, allora il quadrato e+è valido
print("OK: è un quatrado magico perfetto")

