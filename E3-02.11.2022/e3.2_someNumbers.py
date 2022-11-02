# Inizializza le variabili
STOP = ''
n = 0 # numero di numeri inseriti dall'utente: contatore del ciclo
somma = 0
absSomma = 0 # somma dei valori assoluti
prodotto = 1

print('Termina la sequenza di numeri con una riga vuota')

# Inserimento dati dell'utente
while True :
    inputStr = input()
    if inputStr == STOP :
        break
    else :
        n += 1
        somma += float(inputStr)
        absSomma += abs(float(inputStr))
        prodotto = prodotto * float(inputStr)

# Se il numero di dati inseriti e' minore di 2, visualizza un messaggio di errore
# altrimenti visualizza le variabili elaborate
if n < 2 :
    print('Errore: devi inserire almeno due numeri. Riprova')
else :
    print('Somma:', somma)
    print('Somma dei valori assoluti:', absSomma)
    print('Prodotto:', prodotto)
    print('Valore medio:', somma/n)

