# find_empty_dir.py

"""
Il programma:
 * chiede all'utente il nome di una cartella del file system (percorso assoluto o relativo) da cui iniziare la ricerca;
 se l'utente fornisce la stringa vuota, la cartella sarà quella in cui il programma viene eseguito ('current working directory')
 * visualizza i nomi delle cartelle che non contengono altre cartelle né file (cioè sono cartelle vuote)
"""

import os
import os.path


## Cerca e visualizza le cartelle vuote
#  @param path La cartella da cui iniziare la ricerca
def find_empty_dir(path):
    names = os.listdir(path)
    if path.endswith(os.sep):
        path = path[:-1]
    if len(names) == 0:
        # Caso base: cartella vuota
        print(path)
        return
    else:
        for name in names:
            full_path = path + os.sep + name
            if os.path.isdir(full_path):
                find_empty_dir(full_path)

# Acquisizione dati dall'utente
path = input("Cartella da cui iniziare la ricerca: ")
if len(path) == 0:
    path = os.getcwd()
print()

find_empty_dir(path)
print()
