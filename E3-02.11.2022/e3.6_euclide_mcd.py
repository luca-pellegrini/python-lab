# Inizializza le variabili
while True :
    a = int(input("Primo numero (intero positivo): "))
    if a <= 0 : print("Deve essere un numero intero positivo!")
    else : break
while True :
    b = int(input("Secondo numero (intero positivo): "))
    if b < 0 : print("Deve essere un numero intero positivo!")
    else : break

# Confronta a e b
if a > b :
    m = a
    n = b  # ho m > n
else :
    m = b
    n = a  # ho m > n

# DEBUG
#print("m =", m)
#print("n =", n)

# Algoritmo di Euclide
resto = m % n
while resto != 0 :
    m = n
    n = resto
    resto = m % n

# Visualizza il MCD
print("Il massimo comun divisore è", n)