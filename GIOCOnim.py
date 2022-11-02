#gioco di Nim
from random import randint
continuare=True
vincitore=0
a=0
while continuare==True:
    #print ("DEBUG corpo del gioco")
    print()
    print ("GIOCO DI NIM")
    numero=randint(10,100)
    print ("Numero iniziale di biglie:", numero)
    giocatore=randint(1,2)
    if randint(1,100)%2==0:
        #print ("DEBUG il computer e' intelligente")
        computerFurbo=True
    else:
        #print ("DEBUG il computer e' stupido")
        computerFurbo=False
    while numero>0:
        if giocatore==1:
            a=numero #variabile che ho aggiunto in seguito per calcolare quante biglie toglie il computer
            if numero==1:
                vincitore=2
                break
            giocatore=2 #al prossimo turno tocca all'utente
            if not computerFurbo:
                numero=numero-randint(1,numero//2)
            else:
                if numero==2:
                    numero=1
                elif 3<numero<7:
                    numero=3
                elif 7<numero<15:
                    numero=7
                elif 15<numero<31:
                    numero=15
                elif 31<numero<63:
                    numero=31
                elif numero>63:
                    numero=63
                else:
                    numero=numero-randint(1,numero//2)
            print ("Tocca a me, sottraggo",a-numero,"biglie")
            print ("Numero biglie:", numero)
        toglie=0
        if numero==1:
            vincitore=1
            break
        while toglie<1 or toglie>numero//2:
            toglie=int(input("Tocca a te, quante biglie vuoi sottrarre? "))
        numero=numero-toglie
        giocatore=1 #al prossimo turno tocca al computer
        print ("Numero biglie:", numero)
    if vincitore==1:
        print("Questa volta hai perso, ritenta!")
    elif vincitore==2:
        print ("Complimenti, hai vinto!")
    while True:
        giocare=input("Vuoi giocare ancora? Rispondi S o N ")
        if giocare=="N" or giocare=="S":
            if giocare=="N":
                continuare=False
            break
input()        
