# Acquisisci numero intero positivo
num = int(input('Scrivi un numero intero positivo (minore di 4000): '))
while num <= 0 or num >= 4000 :
    print('Errore: devi scrivere un numero intero positivo (e minore di 4000)! Riprova')
    num = int(input('Scrivi un numero intero positivo: '))

# Calcola le cifre di migliaia, centinaia, decine e unita' del numero
m = num // 1000
c = (num % 1000) // 100
d = (num % 100) // 10
u = num % 10


