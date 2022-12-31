# string_permutations.py

from math import factorial

def recursive_permutations(s):
    if not isinstance(s, str):
        raise TypeError("argument must be a string")
    #
    perm_list = list()
    if len(s) == 0:
        # Caso base 1: stringa vuota
        return perm_list
    elif len(s) == 1:
        # Caso base 2: stringa di un solo carattere
        perm_list.append(s)
        return perm_list
    else:
        c = s[0]
        sub = s[1:]
        #print("c =", c)
        #print("sub =", sub)
        ss = recursive_permutations(sub)
        #print("DEBUG:", ss)
        for e in ss:
            for i in range(len(s)):
                temp = e[:i] + c + e[i:]
                perm_list.append(temp)
        return perm_list


def iterative_permutations(s):
    if not isinstance(s, str):
        raise TypeError("argument must be a string")
    #
    if len(s) == 0:
        # Caso base 1: stringa vuota
        return []
    elif len(s) == 1:
        # Caso base 2: stringa di un solo carattere
        return [s]
    # Il numero delle permutazioni di s è (len(s))!
    count = factorial(len(s))
    # c è la lista ordinata dei caratteri presentii nella stringa s
    c = list(s)
    c.sort()
    # Preparo la lista delle permutazioni, che verrà riempita e restituita
    perm_list = list()
    # La prima permutazione è quella con i caratteri ordinati
    ss = "".join(c)
    perm_list.append(ss)
    # Genero tutte le altre permutazioni, che sono (count - 1)
    for k in range(count-1):
        # Procedo a ritroso in c, partendo dal penultimo elemento e
        # cercando il primo elemento che è minore dell'elemento che lo segue
        i = len(s) - 2
        while i >= 0:
            if c[i] < c[i+1]:
                # c[i] è il primo elemento (a partire dalla fine)
                # che è minore dell'elemento che lo segue nella lista c
                #
                # Ripartendo a ritroso in c, cerco il primo elemento
                # che è maggiore di c[i]
                j = len(s) - 1
                while c[j] < c[i]:
                    j -= 1
                # Scambio c[i] con c[j]
                temp = c[i]
                c[i] = c[j]
                c[j] = temp
                # Inverto la porzione della lista c compresa tra
                # la posizione i (esclusa) e la fine della lista
                # (se tale porzione è vuota, il ciclo non fa niente)
                i += 1
                j = len(s) - 1
                while i < j:
                    temp = c[i]
                    c[i] = c[j]
                    c[j] = temp
                    i += 1
                    j -= 1
                # La lista c contiene una nuova permutazione di s,
                # dopodiché interrompo il ciclo interno e genero
                # una nuova permutazione ripetendo la ricerca
                ss = "".join(c)
                perm_list.append(ss)
                break
            else:
                i -= 1
    return perm_list


## Controlla se una stringa contiene caratteri duplicati
#  @param s La stringa da controllare
#  @return True se la stringa contiene almeno una coppia di caratteri duplicati; False altrimenti
def has_duplicates(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return True
    return False


if __name__ == "__main__":
    while True:
        s = input("Stringa (senza caratteri duplicati): ")
        if not has_duplicates(s):
            break
    print()
    iter_list = iterative_permutations(s)
    iter_list.sort()
    recur_list = recursive_permutations(s)
    recur_list.sort()
    if iter_list != recur_list:
        print("Errore")
    else:
        print("Permutazioni:")
        print(recur_list)
