from random import randint
print ("Giochiamo: dammi due numeri interi positivi, genererò un numero casuale tra essi, e tu dovrai indovinarlo")
a=int(input("Inserisci il limite inferiore: "))
b=int(input("Inserisci il limite superiore: "))
numero=randint(a,b)
#print ("DEBUG numero casuale: ", numero)
i=0
guess=int(input("Indovina il numero: "))
while True:
    i+=1
    if guess != numero:
        if guess < numero:
            guess=int(input("Troppo piccolo, ritenta: "))
        else:
            guess=int(input("Troppo grande, ritenta: "))
    else:
        break
print ("Complimenti! Hai indovinato in",i,"tentativi") 
input()
