# life_random.py
from ezgraphics import GraphicsWindow
from my_input import isFloat, isInteger, inputPositiveInteger
from random import random, randint

def main() :
    # Acquisizione dati dall'utente
    cellSize = inputIntegerGreaterThan("Lunghezza del lato di ciascuna cella (maggiore di 9): ", 9)
    cellePerRiga = cellePerColonna = inputPositiveInteger("Numero celle per ciascuna riga e colonna: ")
    density = inputFloatInInterval("Percentuale di celle occupate (numero nell'intervallo [0, 1]: ", 0, 1)
    # Altri valori che influenzano il disegno (potrebbero essere chiesti all'utente),
    # ma per adesso li inseriamo in variabili (costanti) così il codice è già
    # predisposto al fatto che non siano dei valori predefiniti.
    # Spessore delle linee del reticolo:
    BOARD_LINE_WIDTH = 3 # è meglio che sia dispari per agevolare la simmetria
    # Spessore (percentuale) bordo interno di ciascuna cella:
    INTERNAL_BORDER_PERCENT = 0.2 # deve essere (significativamente) minore di 0.5
    OCCUPIED_COLOR = "red" # colore cellule
    BACKGROUND_COLOR = "green" # colore sfondo
    
    # Calcolo dimensioni della finestra grafica
    WIDTH = BOARD_LINE_WIDTH + (cellSize + BOARD_LINE_WIDTH) * cellePerRiga
    HEIGHT = BOARD_LINE_WIDTH + (cellSize + BOARD_LINE_WIDTH) * cellePerColonna
    INTERNAL_BORDER = cellSize * INTERNAL_BORDER_PERCENT
    
    # Creazione finestra grafica
    win = GraphicsWindow(WIDTH, HEIGHT)
    canvas = win.canvas()
    canvas.setBackground(BACKGROUND_COLOR)
    canvas.setLineWidth(BOARD_LINE_WIDTH)
    
    # Disegna il reticolo
    drawWorld(canvas, cellePerRiga, cellePerColonna, cellSize, BOARD_LINE_WIDTH, WIDTH, HEIGHT)
    canvas.setLineWidth(1) # ripristino spessore, per il bordo delle cellule
    canvas.setFill(OCCUPIED_COLOR)
    
    # Popola il "mondo" e restituisce la densità effettiva
    effectiveDensity = fillWorldWithRandomDensity(canvas, cellePerRiga, cellePerColonna, density, cellSize, BOARD_LINE_WIDTH, INTERNAL_BORDER)
    
    print()
    print("Densità effettiva: %.2f" % effectiveDensity)
    win.wait()


## Disegna il reticolo che definisce il "mondo" in cui avviene la simulazione
#  @param canvas Il pannello della finestra su cui disegnare
#  @param cellePerRiga
#  @param cellePerColonna
#  @param cellSize
#  @param lineWidth Spessore delle linee del reticolo: `BOARD_LINE_WIDTH`
#  @param winWidth Larghezza del canvas: `WIDTH`
#  @param winHeight Altezza del canvas: `HEIGHT`
#
def drawWorld(canvas, cellePerRiga, cellePerColonna, cellSize, lineWidth, winWidth, winHeight) :
    for x in range(cellePerRiga + 1) :
        canvas.drawLine(x * (cellSize + lineWidth) + lineWidth/2 - 1, 0,
                        x * (cellSize + lineWidth) + lineWidth/2 - 1, winHeight - 1)
    for y in range(cellePerColonna + 1) :
        canvas.drawLine(0, y * (cellSize + lineWidth) + lineWidth/2 - 1,
                        winWidth - 1, y * (cellSize + lineWidth) + lineWidth/2 - 1)

## Popola la scacchiera e restituisce la densità effettiva
#  Il valore della densità effettiva deve essere visualizzato
#  (con `print`) dalla funzione principale
#  @param canvas Il pannello della finestra su cui disegnare
#  @param cellePerRiga
#  @param cellePerColonna
#  @param density Valore della densità inserito dall'utente
#  @param cellSize
#  @param lineWidth Spessore delle linee del reticolo: `BOARD_LINE_WIDTH`
#  @param cellBorder Bordo interno di ogni cella, equivale a `INTERNAL_BORDER`
#  @return La densità effettiva delle celle occupate
#
def fillWorldWithRandomDensity(canvas, cellePerRiga, cellePerColonna, density, cellSize, lineWidth, cellBorder) :
    count = 0
    for x in range(cellePerRiga) :
        for y in range(cellePerColonna) :
            if random() < density :
                count += 1
                canvas.drawRect(x * (cellSize + lineWidth) + lineWidth + cellBorder,
                                y * (cellSize + lineWidth) + lineWidth + cellBorder,
                                cellSize - 2 * cellBorder,
                                cellSize - 2 * cellBorder)
    return count / (cellePerRiga * cellePerColonna) # densità effettiva


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

"""
## Genera e restituisce un valore booleano casuale (True o False)
#
def randomBoolean() :
    if randint(0, 1) == 0 : return False
    else : return True
"""

main()
