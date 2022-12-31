# find_file.py

"""
IL programma:
 * chiede all'utente una stringa da cercare
 * chiede all'utente il nome di una cartella del file system (percorso assoluto o relativo) da cui iniziare la ricerca;
 se l'utente fornisce la stringa vuota, la cartella sarà quella in cui il programma viene eseguito ('current working directory')
 * visualizza il percorso completo (cartella + nome del file) di tutti i file il cui nome contiene la stringa da cercare
"""

import os
import os.path


## Cerca tutti i file il cuni nome contiene una data stringa
#  @param query La stringa che deve essere contenuta nei nomi dei file
#  @param path La cartella da cui iniziare la ricerca
#
def find_file(query, path):
    if not isinstance(query, str) or not isinstance(path, str):
        raise TypeError("both arguments must be strings")
    #
    names = os.listdir(path)
    if path.endswith(os.sep):
        path = path[:-1] # tronca l'ultimo carattere
    if len(names) == 0:
        # Caso base 1: cartella vuota
        return
    else:
        for name in names:
            full_path = path + os.sep + name
            if os.path.isfile(full_path):
                # Caso base 2: sto analizzando un file
                if query in name:
                    print(full_path)
            elif os.path.isdir(full_path):
                # Caso ricorsivo: sto analizzando una cartella
                find_file(query, full_path)

# Acquisizione dati dall'utente
query = input("Stringa da cercare: ")
path = input("Cartella da cui iniziare la ricerca: ")
if len(path) == 0:
    path = os.getcwd()
print()

find_file(query, path)
print()
