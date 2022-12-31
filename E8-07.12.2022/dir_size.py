# dir_size.py

"""
Programma che calcola la somma dello spazio occupato dai file
di una cartella e ricorsivamente di tutte le sottocartelle,
usando 'os.path.getsize()'

Analizzando una cartella:
 * si sommano le dimensioni ricevute dalle invocazioni ricorsive sulle sottocartelle
 * poi si aggiungono le dimensioni dei file presenti nella cartella
 * si restituisce il totale
"""

import os
import os.path


def dir_size(path):
    if not isinstance(path, str):
        raise TypeError("argument must be a string")
    total_sum = 0
    names = os.listdir(path)
    if path.endswith(os.sep):
        path = path[:-1]
    if len(names) == 0:
        # Caso base 1: cartella vuota
        return total_sum
    else:
        for name in names:
            full_path = path + os.sep + name
            if os.path.isfile(full_path):
                # Caso base 2: sto analizzando un file
                total_sum += os.path.getsize(full_path)
            elif os.path.isdir(full_path):
                # Caso ricorsivo: sto analizzando una sottocartella
                total_sum += dir_size(full_path)
        return total_sum

if __name__ == "__main__":
    path = input("Partiamo da: ")
    if len(path) == 0:
        path = os.getcwd()
    print()
    print("Dimensione della cartella: %d kB" % (dir_size(path)//1024))
    print()
