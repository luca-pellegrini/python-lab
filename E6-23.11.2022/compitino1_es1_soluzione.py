# compitino1_esempio1_testo.py
"""
   Primo compitino di Elementi di Informatica e Programmazione - ESEMPIO

   TEMPO A DISPOSIZIONE = 1 ora e mezza (90 minuti)
   
   Il progetto consiste nello sviluppo di alcune funzioni cooperanti tra loro,
   ma la struttura della cooperazione (cioe' dell'interazione tra le funzioni)
   e' gia' delineata.

   Ciascuna funzione e' descritta nel commento che la precede, che a volte
   contiene anche delle prescrizioni o dei divieti da seguire durante la
   scrittura del codice (ad esempio, non si possono usare alcune specifiche funzioni...)
   che valgono soltanto per la funzione a cui si riferisce il commento.
   
   Alcune sezioni di codice sono gia' presenti e non possono essere modificate!
   Le sezioni di codice mancante e da scrivere sono identificate dal commento
   # SCRIVERE QUI 
"""
def main() :
    lst1 = createRandomIntegerList(30, 1, 10)
    lst2 = list(lst1) # duplico la lista
    lst1.sort()
    removeFromSortedList(lst1)
    removeFromUnsortedList(lst2)
    if areEquals(lst1, lst2) :
        print("Collaudo riuscito (ma non significa che non ci siano errori...)")
    else :
        print("Collaudo non riuscito")
# SCRIVERE QUI
    #print()
    #L = createRandomIntegerList(10, 1, 20)
    #print(L)
    """
    Qui si possono inserire altri eventuali collaudi (ma non e' necessario)
    """
# fine main
     
"""
La funzione areEquals deve restituire True se e solo se le due liste di numeri ricevute
come parametri hanno lo stesso contenuto, indipendentemente dall'ordinamento degli
elementi (altrimenti, ovviamente, deve restituire False).
Per essere dichiarate uguali, le due liste devono contenere gli stessi
valori, ciascuno con la stessa molteplicita'.
Esempio:  1 2 3 4 4 4 3   e   4 3 4 3 4 2 1  sono uguali.
Esempio:  1 2   e   1 2 2  non sono uguali.
Due liste vuote sono (ovviamente) uguali.
La funzione non puo' modificare, neanche temporaneamente, il contenuto delle liste.
La funzione ovviamente puo' utilizzare le funzioni definite nel seguito del testo
(leggere tutto prima di iniziare a lavorare !!!!)
"""
def areEquals(lst1, lst2) :
    for i in lst1 :
        if (i not in lst2) or (lst1.count(i) != lst2.count(i)) :
            return False
    return True
# fine areEquals

"""
La funzione removeFromUnsortedList deve eliminare dalla lista ricevuta come parametro
tutti e soli gli elementi che sono presenti in essa piu' di due volte,
lasciando soltanto gli elementi che sono presenti una o due volte
(gli elementi che sono presenti due volte dovranno essere presenti
due volte anche alla fine della procedura).
Gli elementi rimasti nella lista dovranno trovarsi nella stessa
posizione relativa che avevano inizialmente (quindi, per semplificare
le cose, e' decisamente preferibile evitare di ordinare la lista).
Non possono essere create altre liste ne' altri contenitori.
Con oggetti di tipo lista, l'unico metodo utilizzabile è remove
(ovviamente si possono usare FUNZIONI che ricevono una lista, come len).
"""
def removeFromUnsortedList(a) :
    """
    Dovendo eliminare elementi dalla lista, suggerisco di non usare un ciclo for...
    """
# SCRIVERE QUI
    i = 0
    while i < len(a) :
        element = a[i]
        j = i
        count = 0
        while j < len(a) :
            if a[j] == element :
                count += 1
            j += 1
        if count > 2 :
            for n in range(count) :
                a.remove(element)
        else :
            i += 1
# fine removeFromUnsortedList
   
"""
La funzione removeFromSortedList deve eliminare dalla lista ricevuta come parametro
tutti e soli gli elementi che sono presenti in essa piu' di due volte,
lasciando soltanto gli elementi che sono presenti una o due volte
(gli elementi che sono presenti due volte dovranno essere presenti
due volte anche alla fine della procedura).
Con oggetti di tipo lista, l'unico metodo utilizzabile è pop
(ovviamente si possono usare FUNZIONI che ricevono una lista, come len).
La lista ricevuta e' ordinata (non c'e' bisogno di verificarlo)
e deve essere ordinata anche al termine della procedura.
Non possono essere create altre liste ne' altri contenitori.
"""
def removeFromSortedList(a) :
    """
    In una lista ordinata, eventuali elementi replicati
    si trovano in posizioni tra loro consecutive.
    """
# SCRIVERE QUI
    i = 0
    while i < len(a) :
        element = a[i]
        n = a.count(element)
        if n > 2 :
            a[i:i + n] = [] # elimino tutti gli elementi duplicati
            # NON faccio avanzare i
        else :
            i += 1
# fine removeFromSortedList

"""
La funzione createRandomIntegerList deve creare e restituire una lista
di lunghezza uguale al valore
del primo parametro ricevuto e contenente numeri interi pseudocasuali
appartenenti all'intervallo [a, b].
"""
from random import randint
def createRandomIntegerList(size, a, b) :
# SCRIVERE QUI
    x = [ ]
    for i in range(size) :
        x.append(randint(a, b))
    return x
# fine createRandomIntegerList
   
main()

