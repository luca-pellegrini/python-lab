from random import randint

# Inizializza le variabili
while True :
    a = int(input("Primo numero: "))
    if a < 0 : print("Deve essere un numero intero positivo")
    else : break
while True :
    b = int(input("Secondo numero, maggiore del primo: "))
    if b < 0 : print("Deve essere un numero intero positivo")
    elif b <= a : print("Il secondo numero deve essere maggiore del primo")
    else : break
i = 0 # numero di tentativi

# Genera numero intero casuale compreso in [a, b]
magic_num = randint(a, b)

# Chiede al giocatore di indovinare il numero magico
print("Indovina il numero magico (casuale), compreso tra", a, "e", b)
while True :
    num = int(input())
    i += 1
    if num == magic_num :
        print("Congratulazioni: hai indovinato il numero magico!")
        print("Numero di tentativi:", i)
        break
    elif num > magic_num : print("Troppo grande!")
    else : print("Troppo piccolo!")