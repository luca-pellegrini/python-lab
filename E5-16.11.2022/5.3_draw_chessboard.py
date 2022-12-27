# draw_chessboard.py
from ezgraphics import *
"""
Programma per disegnare in una finestra una scacchiera 8x8, con quadrati alternativamente bianchi e neri, con il quadroato in alto a sinistra bianco.
Prima di iniziare a disegnare, chiede all'utente la lunghezza del lato di ciascuna casella della scacchiera, misurata in pixel: valore inserito deve essere numero intero maggiore di 5 (ripetere la richiesta finché condizione non è soddisfatta).
"""

# Inizializzazione variabile N_CASELLE
## Indica la dimensione (numero di caselle per lato) della scacchiera desiderata. In questo caso una 8x8
N_CASELLE = 8

# Acquisizione dati in input
## Chiede all'utente lunghezza del lato di ogni casella (variabile L)
while True :
    print("Lughezza (in pixel) del lato di ogni casella")
    readStr = input("(Numero intero maggiore di 5): ")
    if readStr.isdigit() :
        L = int(readStr)
        if L > 5 : break
        else : 
            print("Errore: numero inserito non è maggiore di 5!")
            print()
    else :
        print("Errore: valore inserito non è un numero intero!")
        print()

# Calcola dimensioni della scacchiera (e della finestra che dovrà contenerla)
SIZE = N_CASELLE * L

# Creazione finestra grafica e canvas
window = GraphicsWindow(width=SIZE, height=SIZE)
c = window.canvas() # canvas della finestra appena creata

# Disegna caselle della scacchiera
for i in range(N_CASELLE) : # sull'asse y
    for k in range(N_CASELLE) : # sull'asse x
        if (i + k) % 2 == 0 :
            c.setColor("white") # bianco
        else :
            c.setColor("black") # nero
        c.drawRect(k*L, i*L, L, L)

window.wait() # La finestra rimane aperta finché l'utente non la chiude manualmente
