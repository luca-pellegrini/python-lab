# reverse_sort.py

## Verifica se una sequenza di stringhe memorizzata in una lista
#  è lessicograficamente ordinata "al contrario"
#  @param List Lista contenente la sequenza di stringhe
#  return Un valore booleano
def check(List) :
    for i in range(len(List)-1) :
        if List[i] < List[i+1] :
            return False
    return True

## Inverte gli elementi di una lista
#  Modifica la lista ricevuta come parametro
def invertList(List) :
    List = List[-1 : -len(List) : -1]

# Acquisizione dati dall'utente
x = [ ]
STOP = ""
print("Termina i dati con una riga vuota:")
while True :
    s = input()
    if s == STOP : break
    x.append(s)

if check(x) :
    y = str(x)
    y1 = y.replace('[', '')
    y2 = y1.replace(']', '')
    print(y2, "è una sequenza ordinata al contrario")
else :
    print("Sequenza non ordinata al contrario")
    x.sort()
    invertList(x)
    print(x)

