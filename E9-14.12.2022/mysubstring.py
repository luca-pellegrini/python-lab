# mysubstring.py (modulo)


## Genera tutte le possibili sottostringhe di una stringa data
#  @param s La stringa di partenza
#  @return Una lista con tutte le possibili sottostringhe
#
def get_all_substrings(s):
    if not isinstance(s, str):
        raise TypeError("argument must be a string")
    substrings = list()
    substrings.append("")
    # per ogni possibile lunghezza n di sottostringa
    for n in range(1, len(s)+1):
        # per ogni possibile posizione iniziale i
        i = 0
        while (i+n) <= len(s):
            substrings.append(s[i:i+n])
            i += 1
    return substrings
"""
Versione alternativa che restituisce lista senza duplicati:
def get_all_substrings(s):
    if not isinstance(s, str):
        raise TypeError("argument must be of type string")
    substrings = list()
    for n in range(len(s)+1):
        temp = set()
        i = 0
        while (i+n) <= len(s):
            temp.add(s[i:i+n])
            i += 1
        # qui l'insieme temp non contiene sottostr. duplicate
        for elem in temp:
            substrings.append(elem)
    return substrings
"""

## Calcola il numero di tutte le possibili sottostringhe
#  di una stringa data, senza generarle
#  @param s La stringa di partenza
#
def num_substrings(s):
    if not isinstance(s, str):
        raise TypeError("argument must be a string")
    n = len(s)
    return 1 + (n * (n+1)) // 2

## Verifica se le stringhe contenute in una lista sono tutte diverse
#  @param ss Lista di stringhe
#  @return True se e solo se le stringhe sono tutte diverse
#
def are_unique(ss):
    if not isinstance(ss, list):
        raise TypeError("argument must be of type list")
    for i in range(len(ss)):
        for j in range(i+1, len(ss)):
            if ss[i] == ss[j]: return False
    return True

## Verifica se le stringhe contenute in una lista
#  sono disposte in ordine di lunghezza crescente
#  @param ss Lista di stringhe
#  @return True se la condizione è vera
#
def is_sorted_by_increasing_length(ss):
    if not isinstance(ss, list):
        raise TypeError("argument must be of type list")
    for i in range(len(ss) - 1):
        if len(ss[i]) > len(ss[i+1]): return False
    return True

## Verifica se le stringhe contenute in una lista
#  sono disposte in ordine di lunghezza decrescente
#  @param ss Lista di stringhe
#  @return True se la condizione è vera
#
def is_sorted_by_decreasing_length(ss):
    if not isinstance(ss, list):
        raise TypeError("argument must be of type list")
    for i in range(len(ss) - 1):
        if len(ss[i]) < len(ss[i+1]): return False
    return True

## Verifica se le stringhe contenute in una lista
#  sono disposte secondo l'ordinamento lessicografico
#  @param ss Lista di stringhe
#  @return True se la condizione è vera
#
def is_forward_sorted(ss):
    if not isinstance(ss, list):
        raise TypeError("argument must be of type list")
    for i in range(len(ss) - 1):
        if ss[i] > ss[i+1]: return False
    return True

## Verifica se le stringhe contenute in una lista
#  sono disposte secondo l'ordinamento lessicografico inverso
#  @param ss Lista di stringhe
#  @return True se la condizione è vera
#
def is_backward_sorted(ss):
    if not isinstance(ss, list):
        raise TypeError("argument must be of type list")
    for i in range(len(ss) - 1):
        if ss[i] < ss[i+1]: return False
    return True

## Uguale a is_forward_sorted(ss)
#
def is_sorted(ss):
    return is_forward_sorted(ss)

## Verifica se una stringa è sottostringa di un'altra
#  @param s1 Possibile sottostringa
#  @param s2 Stringa che potrebbe contenere s1
#  @return True se s1 è sottostringa di s2
#
def is_substring(s1, s2):
    if not (isinstance(s1, str) and isinstance(s2, str)):
        raise TypeError("both arguments must be strings")
    return (s1 in s2)

## Verifica se una stringa è sottosequenza di un'altra stringa
#  @param s1 Possibile sottosequenza
#  @param s2 Stringa che potrebbe contenere s1
#  @return True se s1 è sottosequenza di s2
#
def is_subsequence(s1, s2):
    if not (isinstance(s1, str) and isinstance(s2, str)):
        raise TypeError("both arguments must be strings")
    if (s1 == "" or s1 == s2):
        return True
    elif len(s1) > len(s2):
        return False
    else: # 0 < len(s1) <= len(s2)
        found = 0
        x = 0 # indice di inizio della ricerca in s2
        for char in s1: # cerco i caratteri di s1, uno alla volta
            i = x
            while i < len(s2):
                if s2[i] == char:
                    found += 1
                    x = i + 1
                    break
                i += 1
        return (found == len(s1))

## Genera tutte le possibili sottosequenze di una stringa
#  @param s La stringa da cui estrarre le sottosequenze
#  @return Lista contenente tutte le sottosequenze
#
def get_all_subsequences(s):
    if not isinstance(s, str):
        raise TypeError("argument must be a string")
    n = len(s)
    subseqs = list()
    for i in range(2**n):
        i_bin = decimal_to_binary(i, n)
        sub = ""
        for j in range(n):
            if i_bin[j] == "1":
                sub += s[j]
        subseqs.append(sub)
    return subseqs

## Converte un numero intero decimale in un numero in base 2
#  @param num Numero intero in base 10
#  @param min_lenght Minima lunghezza in bit del numero restituito 
#  (aggiunge zeri iniziali se necessario)
#  @return Stringa contenente il numero in base 2
#
def decimal_to_binary(num, min_lenght):
    if not (isinstance(num, int) and isinstance(min_lenght, int)):
        raise TypeError("both arguments must be of type int")
    quoziente = num
    bin = ""
    while quoziente > 0:
        resto = quoziente % 2
        quoziente = quoziente // 2
        bin = str(resto) + bin
    if len(bin) < min_lenght:
        for k in range(min_lenght - len(bin)):
            bin = "0" + bin
    return bin

## Calcola il numero di tutte le possibili sottosequenze
#  di una stringa data, senza generarle
#  @param s La stringa di partenza
#
def num_subsequences(s):
    return 2**(len(s))

