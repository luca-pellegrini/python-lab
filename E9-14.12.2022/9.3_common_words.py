# common_words.py
import re
from sys import argv, exit
import ssl; ssl._create_default_https_context = ssl._create_unverified_context

## Legge il testo di un file o pagina web
#  @param url Percorso del file o indirizzo della pagina web
#  @return Stringa contenente il testo del file/pagina web
#
def read_file_or_webpage(url):
    from urllib.request import urlopen    
    if url == "":
        raise ValueError
    elif url.startswith("http://") or url.startswith("https://"):
        webPage = urlopen(url)
        text = str(webPage.read(), "utf-8")
        webPage.close()
    else:
        f = open(url, "r")
        text = f.read()
        f.close()
    return text

# main
if len(argv) != 3:
    exit("Errore: specificare i nomi dei due file")

file1 = argv[1]
file2 = argv[2]
text1 = read_file_or_webpage(file1)
text2 = read_file_or_webpage(file2)

words1 = set(re.split("[^a-zA-Z]+", text1))
words2 = set(re.split("[^a-zA-Z]+", text2))
common = words1.intersection(words2)
for word in sorted(common):
    print(common)

