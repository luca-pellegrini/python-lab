# life_random.py
from ezgraphics import GraphicsWindow
from my_input import isFloat, isInteger, inputPositiveInteger
from random import random, randint

def main() :
    # Acquisizione dati dall'utente
    LATO_CELLA = inputIntegerGreaterThan("Lunghezza del lato di ciascuna cella (maggiore di 9): ", 9)
    NUM_CELLE = inputPositiveInteger("Numero celle per ciascuna riga e colonna")
    PERC_CELLE_OCCUP = inputFloatInInterval("Percentuale di celle occupate (un numero reale nell'intervallo [0, 1]: ", 0, 1)
    #
    # 
    #
    print("Ricordati di finire la funzione main!")
    # alla fine del programma: win.wait()


# Chiede all'utente di inserire un numero, visualizzando `message`
# Restituisce il numero inserito solo se è un numero intero ed è maggiore del parametro `n`
# Utilizza la funzione `isInteger`
def inputIntegerGreaterThan(message, n) :
    while True :
        s = input(message)
        if isInteger(s) :
            x = int(s)
            if x > n : return x

# Chiede all'utente di inserire un numero, visualizzando `message`
# Restituisce il numero inserito solo se è un numero frazionario (float) e appartiene all'intervallo [a, b]
# Utilizza la funzione `isFloat`
def inputFloatInInterval(message, a, b) :
    while True :
        s = input(message)
        if isFloat(s) :
            x = float(s)
            if a <= x <= b : return x 

## Genera e restituisce un valore booleano casuale (True o False)
#
def randomBoolean() :
    if randint(0, 1) == 0 : return False
    else : return True

## Disegna la scacchiera che definisce il "mondo" in cui avviene la simulazione
#
def drawWorld() :
    #
    print("Ricordadi di finire drawWorld!")

## Popola la scacchiera e restituisce la densità effettiva
#  Il valore della densità effettiva deve essere visualizzato (con `print`) dalla funzione principale
#
def fillWorldWithRandomDensity() :
    #
    print("Ricordati di finire fillWorldWithRandomDensity!")