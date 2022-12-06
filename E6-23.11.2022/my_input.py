## @package my_input.py
# Funzioni utili per l'acquisizione e validazione di dati in input.

# Tutte le funzioni di tipo `is...` non devono avere alcuna
# interazione con l'utente (né in input né in output).

# Riceve una stringa `s`
# Restituisce True se e solo se la stringa `s` non è vuota
# e contiene un numero intero decimale, che può avere: zero
# o più spazi iniziali, un eventuale segno meno, una o più
# cifre decimali (da 0 a 9), zero o più spazi finali
# (es. non ci può essere uno spazio tra il segno meno e
# la prima cifra del numero)
def isInteger(s) :
    atLeastOneDigit = False
    if s == "" : return False # stringa vuota
    i = 0
    while i < len(s) : # spazi iniziali?
        if s[i] != ' ' :
            break
        i += 1 # il valore finale di i corrisponde al primo carattere della stringa che NON è uno spazio (eventualmente zero)
    if i < len(s) and s[i] == '-' : # segno meno?
        i += 1
    while i < len(s) : # cifre decimali?
        if not s[i].isdigit() :
            break
        atLeastOneDigit = True
        i += 1
    while i < len(s) : # spazi finali?
        if s[i] != ' ' :
            break
        i += 1    
    # se i == len(s) vuol dire che sono riuscito a scandire tutta la stringa rispettando il formato,
    # devo solo controllare che ci sia almeno una cifra numerica (potrebbero essere tutti spazi)
    return i == len(s) and atLeastOneDigit

    """Mia soluzione precedente
    atLeastOneDigit = False
    if s == "" : return False # stringa vuota
    countMinus = 0
    for i in range(len(s)) :
        if s[i] == "." : # sarebbe un numero frazionario
            return False
        elif not s[i].isdigit() and s[i] != " " and s[i] != "-" :
            return False
        if s[i].isdigit() : atLeastOneDigit = True
        if s[i] == "-" : countMinus += 1
    if countMinus > 1 : return False
    j = 0
    while j < len(s) - 1 :
        if s[j] == "-" and s[j+1] == " " : # non ci può essere uno spazio tra il segno meno e le cifre del numero
            return False
        j += 1
    k = 0
    while k < len(s) - 2 :
        if (s[k].isdigit() and s[k+1] == " " and s[k+2].isdigit()) or (s[k].isdigit() and s[k+1] == " " and s[k+2] == "-") :
            return False
        k += 1
    return atLeastOneDigit
    """

# Riceve una stringa `s`
# Restituisce True se e solo se la stringa `s` contiene
# un numero decimale in virgola mobile (float)
def isFloat(s) :
    atLeastOneDigit = False
    if s == "" : return False # stringa vuota
    i = 0
    while i < len(s) : # spazi iniziali?
        if s[i] != ' ' :
            break
        i += 1
        # il valore finale di i corrisponde al primo
        # carattere della stringa che NON è uno spazio
        # (eventualmente zero)
    if i < len(s) and s[i] == '-' : # segno meno?
        i += 1
    while i < len(s) : # cifre decimali?
        if not s[i].isdigit() :
            break
        atLeastOneDigit = True
        i += 1
    if i < len(s) and s[i] == '.' : # carattere "punto"?
        i += 1
    while i < len(s) : # cifre decimali dopo il punto?
        if not s[i].isdigit() :
            break
        atLeastOneDigit = True
        i += 1
    if i < len(s) and (s[i] == "e" or s[i] == "E") : # lettera "e" ?
        validPower = False
        i += 1
    if i < len(s) and s[i] == '-' : # segno meno all'esponente?
        i += 1
    while i < len(s) : # cifre decimali all'esponente?
        if not s[i].isdigit() :
            break
        validPower = True
        i += 1
    while i < len(s) : # spazi finali?
        if s[i] != ' ' :
            break
        i += 1    
    # se i == len(s) vuol dire che sono riuscito a scandire
    # tutta la stringa rispettando il formato, devo solo
    # controllare che ci sia almeno una cifra numerica
    # nella base e una nell'esponente, se presente
    return i == len(s) and atLeastOneDigit

# Tutte le funzioni di tipo `input...` devono chiedere
# ripetutamente il dato all'utente finché questo non
# rispetta le specifiche della funzione, visualizzando
# di nuovo il messaggio `message` (senza messaggi d'errore)

## Visualizza il messaggio in `message`, e restituisce True o False a seconda della risposta dell'utente (sì o no)
#  Ignora la differenza tra maiuscole e minuscole
#  @param message Stringa contenente il messaggio da visualizzare per l'utente (una domanda a cui possa rispondere "sì" o "no")
#  @param yes Stringa che deve essere scritta dall'utente, affinché la funzione restituisca `True`
#  @param no Stringa che deve essere scritta dall'utente, affinché la funzione restituisca `False`
#  @return `True` se l'utente scrive la stringa in `yes`, False se scrive la stringa in `no`
def inputYesNo(message, yes, no) :
    while True :
        s = input(message)
        if s.lower() == yes.lower() :
            return True
        elif s.lower() == no.lower() :
            return False

# Chiede all'utente di inserire una stringa
# Restituisce la stringa solo se inizia con la stringa `startString`
# Se `startString` è la stringa vuota, restituisce la prima stringa inserita dall'utente
def inputStringStartingWith(message, startString) :
    while True :
        s = input(message)
        if s[:len(startString)] == startString :
            return s

# Chiede all'utente di inserire una stringa
# Restituisce la stringa solo se termina con la stringa `endString`
# Se `endString` è la stringa vuota, restituisce la prima stringa inserita dall'utente
def inputStringEndingWith(message, endString) :
    while True :
        s = input(message)
        if s[-len(endString):] == endString :
            return s

# Chiede all'utente di inserire una stringa
# Restituisce la stringa solo se contiene la stringa `substring`
# Se `substring` è la stringa vuota, restituisce la prima stringa inserita dall'utente
def inputStringContaining(message, substring) :
    while True :
        s = input(message)
        if substring == '' or s == substring :
            return s
        elif len(s) > len(substring) :
            x = 0
            while x < len(s) :
                if s[x:x + len(substring)] == substring :
                    return s
                x += 1

# Chiede all'utente di inserire un numero
# Restituisce il numero inserito solo se è un numero intero
# Utilizza la funzione `isInteger`
def inputInteger(message) :
    while True :
        s = input(message)
        if isInteger(s) :
            return int(s)

# Chiede all'utente di inserire un numero
# Restituisce il numero inserito solo se è un numero intero positivo
# Utilizza la funzione `inputInteger`
def inputPositiveInteger(message) :
    while True:
        num = inputInteger(message)
        if num > 0 :
            return num

# Chiede all'utente di inserire un numero
# Restituisce il numero inserito solo se è un numero intero negativo
# Utilizza la funzione `inputInteger`
def inputNegativeInteger(message) :
    while True :
        num = inputInteger(message)
        if num < 0 :
            return num

# Chiede all'utente di inserire un numero
# Restituisce il numero inserito solo se è un numero intero non positivo (<= 0)
# Utilizza la funzione `inputInteger`
def inputNonPositiveInteger(message) :
    while True :
        num = inputInteger(message)
        if num <= 0 :
            return num

# Chiede all'utente di inserire un numero
# Restituisce il numero inserito solo se è un numero intero non negativo (>= 0)
# Utilizza la funzione `inputInteger`
def inputNonNegativeInteger(message) :
    while True :
        num = inputInteger(message)
        if num >= 0 :
            return num

# Chiede all'utente di inserire un numero
# Restituisce il numero inserito solo se è un numero frazionario (float)
# Utilizza la funzione `isFloat`
def inputFloat(message) :
    while True :
        s = input(message)
        if isFloat(s) :
            return float(s)
