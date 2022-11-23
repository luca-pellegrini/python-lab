# display_function.py
from ezgraphics import GraphicsWindow
from math import *
#from random import *

print()
print("La funzione della variabile x deve rispettare le regole sintattiche")
print("del linguaggio Python e ne può usare le funzioni predefinite")
print("oltre a quelle del modulo math della libreria standard.")
print("Termina il programma scrivendo STOP")
print()

# Dimensioni della finestra grafica
WIDTH = 600
HEIGHT = 600
# Fattore di zoom del grafico
ZOOM = 10 # cioè 10x

# Metto l'origine delle coordinate cartesiane al centro della finestra
X_MIN = (-WIDTH)//2
X_MAX = WIDTH//2
Y_MIN = (-HEIGHT)//2
Y_MAX = HEIGHT//2
"""
Formule di trasformazione da un sist. di rif. cartesiano (x, y)
al sist. di rif. del canvas della finestra (a, b):
a = (WIDTH/2) + x
b = (HEIGHT/2) - y
c.drawPoint(a, b)
"""

while True :
    # Acquisizione dati in input
    print("Scrivi la funzione della variabile x:")
    function = input()
    if function == "STOP" : break
    print()
    print("Funzione inserita: f(x) =", function)

    # Crea la finestra grafica
    win = GraphicsWindow(WIDTH, HEIGHT)
    c = win.canvas()
    # Disegna gli assi cartesiani
    c.setColor("black")
    c.setLineWidth(1)
    c.drawArrow(0, HEIGHT//2, WIDTH, HEIGHT//2) # asse x
    c.drawArrow(WIDTH//2, HEIGHT, WIDTH//2, 0) # asse y

    # Ciclo che visualizza il grafico della funzione
    c.setColor("red")
    for i in range(X_MIN, X_MAX) :
        x = i/ZOOM
        y = eval(function)
        # Coordinate del punto secondo il rif. del canvas
        a = (WIDTH/2) + ZOOM * x
        b = (HEIGHT/2) - ZOOM * y
        if -HEIGHT <= b <= 2*HEIGHT : # disegnare anche dal canvas, ma entro un certo limite
            c.drawPoint(int(a), int(b))
            if i > X_MIN :
                # non è il primo valore: traccio un segmento che lo
                # collega al punto precedente, altrimenti la funzione
                # sembra fatta di punti anziché essere continua
                c.drawLine(aPrev, bPrev, a, b)
        # memorizzo le coordinate per il prossimo segmento
        aPrev = a
        bPrev = b

    win.wait()
    print()
