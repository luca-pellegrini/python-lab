# Inizializza le variabili
STOP = 'STOP'
n = 0 # numero di valori inseriti dall'utente: contatore del ciclo
B = 0 # somma di tutti i valori
A = 0 # somma dei quadrati di tutti i valori

print('Termina la sequenza di numeri scrivendo STOP')

# Inserimento dati dell'utente
while True :
    s = input()
    if s == STOP :
        break
    else :
        n += 1
        B += float(s)
        A += (float(s))**2

# Se n < 2, visualizza un messaggio d'errore
# altrimenti, calcola e visualizza 
if n < 2 :
    print('Errore: devi inserire almeno due numeri. Riprova')
else :
    D = ((A - B*B/n)/(n-1))**(0.5)
    print('Deviazione standard:', D)
