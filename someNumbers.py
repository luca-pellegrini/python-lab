print ("Programma che svolge operazioni algebriche su alcuni numeri. Quando si è terminato di inserire i numeri si prema invio senza digitare niente")
num=0
somma=0
sommaAssoluti=0
prodotto=1
i=0
media=0
stringNum="0"
while True:
    stringNum=input("Inserisca un numero: ")
    if stringNum!="":
        num=float(stringNum)
        somma+=num
        sommaAssoluti += ((num)**2)**(1/2)
        prodotto*=num
        i+=1
    else:
        break
if i<2:
    print ("ERRORE: bisogna inserire almeno due numeri")
else:
    media=somma/i
    print ("Somma dei numeri:", somma)
    print ("Somma dei valori assoluti dei numeri:", sommaAssoluti)
    print ("Prodotto dei numeri:", prodotto)
    print ("Valore medio dei numeri:", media)
input()
