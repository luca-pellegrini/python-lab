print ("Programma che calcola la deviazione standard di una serie di numeri. Quando si è terminato di inserire i numeri, si digiti STOP")
stringNum=""
num=0
a=0
b=0
n=0
while True:
    stringNum=input("Inserisca un numero: ")
    if stringNum!="STOP":
        num=float(stringNum)
        b+=num
        a+=num**2
        n+=1
    else:
        break
if n<2:
    print("ERRORE: si devono inserire almeno due numeri")
else:
    d=((a-b*b/n)/(n-1))**(1/2)
    print("Deviazione standard:",d)
input() 
