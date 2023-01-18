# spellcheck.py
import re
from urllib.request import urlopen
#from sys import exit

# Chiede all'utente il file di cui verificare l'ortografia
filename1 = input("File/pagina web da verificare: ")
# e il file contenente il dizionario
filename2 = input("Dizionario (file con una parola per riga): ")
print()

## Legge il testo di un file o pagina web
#  @param url Indirizzo del file o pagina web da leggere
#  @param default Pagina web da leggere se 'url' è la stringa vuota
#  @return Stringa contenente il testo del file/pagina web
#
def read_file_or_webpage(url, default):
    if url == "":
        webPage = urlopen(default)
        text = str(webPage.read(), "utf-8")
        webPage.close()
    elif url.startswith("http://") or url.startswith("https://"):
        webPage = urlopen(url)
        text = str(webPage.read(), "utf-8")
        webPage.close()
    else:
        f = open(url, "r")
        text = f.read()
        f.close()
    return text

# Legge i due file e li converte in minuscolo
text_to_check = read_file_or_webpage(filename1, "https://en.wikipedia.org/wiki/Computer_science")
text_with_words = read_file_or_webpage(filename2, "https://users.cs.duke.edu/~ola/ap/linuxwords")

# Elabora text_with_words (Genera insieme con le parole valide)
temp = text_with_words.split("\n")
d = set()
for val in temp:
    val = val.strip()
    word = val.lower()
    d.add(word)
# ora d contiene l'insieme di tutte le parole valide

# Elabora text_to_check
temp1 = re.split("[^a-z]", text_to_check.lower())
temp1.sort()
temp2 = list()
temp2.append(temp1[0])
for i in range(1, len(temp1)):
    if temp1[i] != temp1[i-1]:
        temp2.append(temp1[i])
for word in temp2:
    if word not in d:
        print(word)
