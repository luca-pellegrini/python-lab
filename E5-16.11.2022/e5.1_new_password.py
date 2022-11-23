# new_passsword.py

"""
La nuova password:
* deve contenere almeno 8 caratteri
* deve contenere almeno una lettera maiuscola
* deve contenere almeno una lettera minuscola
* deve contenere almeno una cifra numerica
* deve contenere almeno un carattere che non sia una lettera né una cifra
* non deve contenere spazi
* non deve contenere caratteri ripetuti (cioè tutti i caratteri devono essere diversi)

Definisco una funzione per ciascuna regola, che riceve la password e restituisce True se e solo se la regola corrispondente è rispettata.
"""

## Riceve una stringa (la password), e verifica che la sua lunghezza sia almeno di 8 caratteri
#  @param passwd la stringa contenente la password
#  @return True se la lughezza di `passwd` è almeno 8; False altrimenti
#
def pswLength(passwd) :
    return len(passwd) >= 8 # o True o False

## Riceve una stringa (la password), e verifica che contenga almeno una lettera maiuscola
#  @param passwd la stringa contenente la password
#  @return True se `passwd` contiene almeno una lettera maiuscola; False altrimenti
#
def pswLettMaiusc(passwd) :
    b = False
    for c in passwd :
        if c.isupper() :
            b = True
            break
    return b

## Riceve una stringa (la password), e verifica che contenga almeno una lettera minuscola
#  @param passwd la stringa contenente la password
#  @return True se `passwd` contiene almeno una lettera minuscola; False altrimenti
#
def pswLettMinusc(passwd) :
    b = False
    for c in passwd :
        if c.islower() :
            b = True
            break
    return b

## Riceve una stringa (la password), e verifica che contenga almeno una cifra numerica
#  @param passwd la stringa contenente la password
#  @return True se `passwd` contiene almeno una cifra numerica
#
def pswNumber(passwd) :
    b = False
    for c in passwd :
        if c.isdigit() :
            b = True
            break
    return b

## Riceve una stringa (la password), e verifica che contenga almeno un carattere che non è una lettera né una cifra
#  @param passwd la stringa contenente la password
#  @return True se `passwd` rispetta la regola; False altrimenti
#
def pswCarNonAlphaNum(passwd) :
    if passwd.isalnum() : b = False # contiene solo caratteri alfa-numerici
    else : b = True # contiene almeno un carattere che non è una lettera né una cifra
    return b

## Riceve una stringa (la password), e verifica che non contenga spazi
#  @param passwd la stringa contenente la password
#  @return True se `passwd` non contiene spazi; False altrimenti
#
def pswNoSpaces(passwd) :
    b = True
    for c in passwd :
        if c == ' ' :
            b = False
            break
    return b

## Riceve una stringa (la password), e verifica che non contenga due caratteri duplicati
#  @param passwd la stringa contenente la password
#  @return True se `passwd` non contiene caratteri duplicati; False altrimenti
#
def pswNoDuplicates(passwd) :
    for i in range(len(passwd)) :
        for j in range(i + 1, len(passwd)) :
            if passwd[i] == passwd[j] :
                return False
    return True

"""
Definisco una funzione che riceve la password e restituisce True se e solo se la password rispetta tutte le regole sopra definite. Altrimenti, visualizza un messaggio d'errore per ciascuna regola violata, ma senza richiedere una nuova password.
"""

## Riceve una stringa contenente la password, e verifica che rispetti tutte le regole sopra definite
#  @param passwd la stringa contenente la password
#  @return True se `passwd` rispetta tutte le regole; False altrimenti
#
def goodPassword(passwd) :
    b = True
    if not pswLength(passwd) :
        print('Errore: la password deve contenere almeno 8 caratteri')
        b = False
    if not pswLettMaiusc(passwd) :
        print('Errore: la password deve contenere almeno una lettera maiuscola')
        b = False
    if not pswLettMinusc(passwd) :
        print('Errore: la password deve contenere almeno una lettera minuscola')
        b = False
    if not pswNumber(passwd) :
        print('Errore: la password deve contenere almeno una cifra numerica')
        b = False
    if not pswCarNonAlphaNum(passwd) :
        print('Errore: la password deve contenere almeno un carattere non alfanumerico')
        b = False
    if not pswNoSpaces(passwd) :
        print('Errore: la password non deve contenere spazi')
        b = False
    if not pswNoDuplicates(passwd) :
        print('Errore: la password non deve contenere caratteri ripetuti')
        b = False
    #if pswLength(passwd) and pswLettMaiusc(passwd) and pswLettMinusc(passwd) and pswNumber(passwd) and pswCarNonAlphaNum(passwd) and pswNoSpaces(passwd) and pswNoDuplicates(passwd) :
        #b = True
    return b

# Programma principale
# Chiede la password all'utente; ripete la richiesta fino a che l'utente inserisce una password valida
while True :
    s = input('Password: ')
    if goodPassword(s) :
        print('OK')
        break
    print()
    print('Inserire una nuova password')
