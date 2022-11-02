print ("Programma che calcola il massimo comun divisore tre due numeri interi positivi")
primo=int(input("Inserisca il primo numero: "))
secondo=int(input("Inserisca il secondo numero: "))
if primo<=0 or secondo <=0:
    print ("ERRORE: entrambi i numeri devono essere interi positivi")
else:
    if primo>secondo:
        m=primo
        n=secondo
    else:
        m=secondo
        n=primo
    while m%n!=0:
        a=m
        m=n
        n=a%n
    print("Il massimo comun divisore e':", n)
input()
        
            
