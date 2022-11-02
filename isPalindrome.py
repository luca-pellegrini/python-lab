print("Programma che stabilisce se una stringa e' palindromo")
stringa=input("Inserisca la stringa: ")
caratteri=len(stringa)
i=0
while caratteri-1-i>=0:
    #print ("DEBUG",caratteri-1-i)
    if stringa[i]==stringa[caratteri-1-i]:
        i+=1
    else:
        break
if i==caratteri:
    print ("La stringa e' un palindromo")
else :
    print ("La stringa non e' un palindromo")
input()
