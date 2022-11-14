from sys import exit

# Chiede all'utente i valori massimi di base e esponente (numeri interi positivi)
baseMax = int(input("Valore massimo della base: "))
espMax = int(input("Valore massimo dell'esponente: "))

if baseMax < 1 or espMax < 1 :
    exit("Errore: i valori devono essere interi positivi!")

"""
# Calcolo l'estremo in basso a destra della tabella (baseMax**espMax)
# che determina la larghezza x di ogni colonna della tabella
estremo = baseMax ** espMax
#print("DEBUG:", str(baseMax) + "^" + str(espMax), "=", estremo)
x = len(str(estremo))
#print("DEBUG: larghezza =", x)
S = "%" + str(x) + "d" # S = "%4d" se len(str(estremo))=4
"""

# Costruisco la tabella, una riga alla volta, una potenza alla volta
base = 1
while base <= baseMax :
    esp = 1
    while esp <= espMax :
        # calcolo la lunghezza del massimo numero in questa colonna
        maxValue = baseMax ** esp
        x = len(str(maxValue))
        S = "%" + str(x) + "d" # S = "%xd"
        print(S % (base ** esp), end=" ")
        esp += 1
    print()
    base += 1

