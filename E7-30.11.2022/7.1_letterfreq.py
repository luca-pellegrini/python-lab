# letterfreq.py
from urllib.request import urlopen
from sys import exit

# Chiede all'utente il nome del file da elaborare
fileName = input("Percorso del file/pagina web: ")
print()

if fileName == "" :
    webPage = urlopen("https://en.wikipedia.org/wiki/Computer_science")
    text = str(webPage.read(), "utf-8")
    webPage.close()
elif fileName.startswith("http://") or fileName.startswith("https://") :
    try :
        webPage = urlopen(fileName)
        text = str(webPage.read(), "utf-8")
    except :
        exit("Errore: pagina web non esistente o non raggiungibile")
    webPage.close()
else :
    try :
        f = open(fileName, "r")
        text = f.read()
    except FileNotFoundError :
        exit("Errore: file non esistente")
    except IsADirectoryError :
        exit("Errore: il percorso fa riferimento a una cartella")
    except UnicodeDecodeError :
        exit("Errore: la codifica del file non è conforme a Unicode.\nQuesto programma può leggere solo file di semplice testo")
    f.close()

# A questo punto, text contiene tutto il testo del file/pagina web
# Converte il testo in minuscolo
text = text.lower()

# Conta il numero di caratteri che sono lettere
letterNum = 0
for i in range(len(text)) :
    if text[i].isalpha() :
        letterNum += 1

ABC = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
frequences = []
for l in ABC :
    frequences.append(text.count(l) / letterNum)

# Visualizza la tabella con le frequenze
print("Tabella delle frequenze:")
for i in range(len(ABC)) :
    string = ABC[i] + " %5.2f%%" % (frequences[i] * 100)
    print(string)
print()
