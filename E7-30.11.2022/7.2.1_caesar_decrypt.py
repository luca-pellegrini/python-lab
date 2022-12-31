# caesar_decrypt.py
from sys import argv, exit
from urllib.request import urlopen

# Definisco una funzione
## Sostituisce una lettera con un altra, secondo le regole del cifrario di Cesare
#  Sostituisce solo i caratteri che sono lettere, maiuscole o minuscole
#  I caratteri che non sono lettere, vengo restituiti identici
#  @param PARAM numero intero
#  @param c carattere da sostituire (se è una lettera)
#  @return la lettera sostituita (o il carattere non sostituito, se non era una lettera)
def changeLetter(PARAM, c) :
    if len(c) != 1 :
        raise TypeError("parametro c deve essere un carattere. Ricevuta una stringa di lunghezza %d" % len(c))
    # ipotesi semplice: PARAM è già un numero intero positivo, minore di 26
    # Codici numerici Unicode che ci servono    
    # ord('A') = 65
    # ord('Z') = 90
    # ord('a') = 97
    # ord('z') = 122
    # lettere maiuscole 65-90; minuscole 97-122
    i = ord(c)
    if 65 <= i <= 90 : # lettere maiuscole
        c = chr((((i-65) + PARAM) % 26) + 65)
    elif 97 <= i <= 122 : # lettere minuscole
        c = chr((((i-97) + PARAM) % 26) + 97)
    return c

PARAM = 3 # di default

# Acquisisce i dati dall'utente tramite argomenti sulla command line
if len(argv) == 1 :
    exit("Errore: nessun file fornito come argomento")
elif len(argv) == 2 : # un solo argomento sulla command line
    fileName = argv[1]
else : # almeno due argomenti sulla command line
    fileName = argv[1]
    if int(argv[2]) > 0 :
        PARAM = int(argv[2]) % 26

# Legge il file/pagina web richiesto dall'utente
if fileName.startswith("http://") or fileName.startswith("https://") :
    try :
        webPage = urlopen(fileName)
        text = str(webPage.read(), "utf-8")
    except :
        exit("Errore: pagina web non esistente o non raggiungibile")
    webPage.close()
else :
    try :
        f  = open(fileName, "r")
        text = f.read()
    except FileNotFoundError :
        exit("Errore: file non esistente")
    except IsADirectoryError :
        exit("Errore: il percorso fa riferimento a una cartella")
    except UnicodeDecodeError :
        exit("Errore: la codifica del file non è conforme a Unicode.\nQuesto programma può leggere solo file di semplice testo")
    f.close()

# Crea il testo cifrato da visualizzare in output
outStr = ""
for i in range(len(text)) :
    outStr = outStr + changeLetter(-PARAM, text[i])
print(outStr, end="")
