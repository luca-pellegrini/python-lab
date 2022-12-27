# eratostene.py
from my_input import *

# Acquisizione dati dall'utente
print("Questo programma utilizza il Crivello di Eratostene")
print("per cercare i numeri primi minori di un certo valore massimo.")
MAX = inputPositiveInteger("Valore massimo (num. intero positivo): ")

# Iniziallizzazione lista
x = [True] * MAX
# per costruzione, len(x) = MAX
x[0] = False # 0 non è un numero primo
if MAX > 1 :
    x[1] = False # 1 non è un numero primo

# Cerca i numeri primi
for i in range(2, MAX) : # si considera ciascun numero intero maggiore di uno
    if x[i] == True :
        for k in range(i + 1, MAX) :
            if k % i == 0 :
                x[k] = False

# Visualizza il risultato
print()
if True in x :
    print("Numeri primi minori di %d:" % MAX)
    for j in range(MAX) :
        if x[j] == True : print(j, end=" ")
    print()
else :
    print("Non ci sono numeri primi")

