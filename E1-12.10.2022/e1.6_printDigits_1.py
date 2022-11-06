# Chiedi il numero all'utente
num = int(input("Scrivi un numero intero compreso tra 0 e 99999: "))

# Calcola le cifre
d1 = num // 10000 #La prima cifra è il quoziente della divisione num//10000
num = num - d1*10000
d2 = num // 1000
num = num - d2*1000
d3 = num // 100
num = num - d3*100
d4 = num // 10
d5 = num % 10

# Visualizza le singole cifre
print("Le cifre sono:")
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
