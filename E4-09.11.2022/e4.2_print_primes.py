from math import sqrt

# Chiedi valore massimo all'utente
maxValue = int(input('Scrivi un numero intero maggiore di uno: '))
while maxValue <= 1 :
    maxValue = int(input('Errore: scrivi un numero maggiore di uno: '))
print()

# Cicli annidati
print('I numeri primi sono:')
i = 1
while i <= maxValue : # ciclo che analizza ogni numero i <= maxValue per vedere se è primo
    # uso parte del codice di `is_prime.py`
    isPrime = True # in modo che i=1 risulti primo
    k = 2 # contatore del ciclo seguente
    while k < i : # considero solo k t.c. 1 < k < i
        if i % k == 0 : # controllo se i è divisibile per k
            isPrime = False # se sì, allora i NON è primo
            break
        k += 1
    if isPrime : print(i) # visualizzo i solo se è primo
    i += 1
