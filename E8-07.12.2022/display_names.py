# display_names.py

"""
Programma che naviga in modo ricorsivo il file system
a partire da una directory assegnata

Per _navigazione ricorsiva_ si intende che, per ogni cartella presente nella directory assegnata, il programma deve:
 1. visualizzare il nome completo di tutti i file,
 2. visualizzare il nome completo di tutte le cartelle,
 3. "entrare" in tutte le cartelle e ripetere i punti 1, 2 e 3

Il nome dei file andrà preceduto dal carattere "F", il nome delle cartelle andrà preceduto dal carattere "D".
"""

import os
import os.path


## Visualizza, ricorivamente, il contenuto di una cartella
#  @param dir (una stringa) cartella da cui iniziare la navigazione ricorsiva
#
def display_names(path):
    names = os.listdir(path)
    if path.endswith(os.sep):
        path = path[:-1] # tronca l'ultimo carattere
    if len(names) == 0:
        # Caso base 1: cartella vuota
        return
    else:
        for name in names:
            full_path = path + os.sep + name # concatenazione di stringhe
            if os.path.isfile(full_path):
                # Caso base 2: sto analizzando un file
                print("F " + full_path)
            elif os.path.isdir(full_path):
                # Caso ricorsivo: sto analizzando una cartella
                print("D " + full_path)
                display_names(full_path)

directory = input("Partiamo da: ")
if len(directory) == 0:
    directory = os.getcwd()
display_names(directory)
