from math import sqrt

i = int(input('Scrivi un numero intero: '))
isPrime = True # in modo che i=1 risulti primo
k = 2 # contatore del ciclo seguente
while k < i : # considero solo k t.c. 1 < k < i
    #print('DEBUG: ingresso nel ciclo')
    if i % k == 0 : # controllo se i è divisibile per k
        isPrime = False # se si', allora i NON è primo
        break
    k += 1
if isPrime : print(i, 'è un numero primo')
else : print(i, 'non è un numero primo')

