# Chiede all'utente un numero
num = int(input("Scrivi un numero intero maggiore di 1: "))
while num <= 1 :
    num = int(input("Errore: scrivi un numero maggiore di uno: "))
print()

print("I suoi fattori primi sono:", end=" ")
i = 2
while i <= num :
    while num % i == 0 :
        print(i, end=" ")
        num = num // i
    i += 1
print()
