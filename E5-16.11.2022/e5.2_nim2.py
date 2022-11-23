# nim2.py
#from random import random
from random import randint

def main() :
    new_game = True
    while new_game : # ciclo che contiene il programma principale
        print()
        print("GIOCO DI NIM - v2")
        # Inizializza i parametri
        BIGLIE_INIZ = randint(10, 100) # è una costante nel corso della partita
        print("Il mucchio iniziale contiene", BIGLIE_INIZ, "biglie")
        n_bi = BIGLIE_INIZ # variabile diminuisce nel corso della partita
        # Chi inizia?
        if randomBoolean() :
            print("Inizia il computer")
            turno = 'C'
        else :
            print("Inizia il giocatore umano")
            turno = 'U'
    
        # Computer stupido o intelligente?
        INTELL_MODE = randomBoolean()
        if INTELL_MODE :
            print("Computer in modalità intelligente")
        else :
            print("Computer in modalità stupido")            
        print()
    
        # Gioca la partita
        while n_bi > 1 :
            if turno == 'C' : # tocca al computer
                print("Biglie nel mucchio:", n_bi)
                b_prese = takeComputerBalls(INTELL_MODE, n_bi)
                print("Computer sottrae", b_prese, "biglie dal mucchio.")
                n_bi -= b_prese
                turno = 'U'
            else : # turno == 'U' -> tocca all'umano
                b_prese = askUserBalls(n_bi)
                n_bi -= b_prese
                turno = 'C'
            print()
        # il ciclo si chiude quando rimane una sola biglia nel mucchio
        # a questo punto, si sa chi ha perso (computer o umano), e quindi chi ha vinto: tale informazione viene data dalla variabile 'turno'
        if turno == 'C' :
            print("Congratulazioni: hai vinto!")
        else : # turno == 'U'
            print("Mi dispiace: hai perso!")
            print("Questa volta ha vinto il computer.")
    
        new_game = playAgain() # True o False
        if not new_game :
            print("Arrivederci!")
            #break # interrompe il programma
        else : # new_game = True -> gioca ancora
            print()  # Riga vuota
            print("-"*50)


## askUserBalls: Visualizza il numero di biglie presenti nel mucchio (n_bi), e chiede all'utente quante ne vuole prendere (b_prese)
#  Ripete la domanda finché non viene indicata una quantità che rispetti le regole del gioco
#  @param n_bi numero di biglie presenti nel mucchio
#  @return b_prese
#
def askUserBalls(n_bi) :
    print("Biglie nel mucchio:", n_bi)
    while True :
        b_prese = int(input("Quante biglie vuoi prendere? "))
        if 1 <= b_prese <= (n_bi/2) :
            break
        else : # b_prese < 1 or b_prese > (n_bi/2)
            print("Errore: il numero di biglie deve essere compreso tra 1")
            print("e la metà delle biglie presenti nel mucchio!")
    return b_prese

## takeComputerBalls: Calcola e restituisce il numero di biglie prese dal computer (b_prese)
#  sulla base del numero di biglie presenti nel mucchio (n_bi) e sul livello di intelligenza del computer.
#  Computer gioca in maniera intelligente se e solo se INTELL_MODE vale True
#  @param INTELL_MODE vale True se computer in modalità intelligente; False se stupido
#  @param n_bi numero di biglie presenti nel mucchio
#  @return b_prese
#
def takeComputerBalls(INTELL_MODE, n_bi) :
    if INTELL_MODE : # computer intelligente
        if n_bi == 2 :
            b_prese = 1
            #print("Computer sottrae", b_prese, "biglie dal mucchio.")
            #n_bi = 1
        elif 3 < n_bi < 7 :
            b_prese = n_bi - 3
            #print("Computer sottrae", b_prese, "biglie dal mucchio.")
            #n_bi = 3
        elif 7 < n_bi < 15 :
            b_prese = n_bi - 7
            #print("Computer sottrae", b_prese, "biglie dal mucchio.")
            #n_bi = 7
        elif 15 < n_bi < 31 :
            b_prese = n_bi - 15
            #print("Computer sottrae", b_prese, "biglie dal mucchio.")
            #n_bi = 15
        elif 31 < n_bi < 63 :
            b_prese = n_bi - 31
            #print("Computer sottrae", b_prese, "biglie dal mucchio.")
            #n_bi = 31
        elif 63 < n_bi : # <= BIGLIE_INIZ (al max 100)
            b_prese = n_bi - 63
            #print("Computer sottrae", b_prese, "biglie dal mucchio.")
            #n_bi = 63
        else : # n_bi == 3 or n_bi == 7 or n_bi == 15 or n_bi == 31 or n_bi == 63
            b_prese = randint(1, (n_bi//2))
            #print("Computer sottrae", b_prese, "biglie dal mucchio.")
            #n_bi = n_bi - b_prese
    else : # computer stupido
        b_prese = randint(1, (n_bi//2))
        #print("Computer sottrae", b_prese, "biglie dal mucchio.")
        #n_bi = n_bi - b_prese
    return b_prese

## playAgain: Restituisce il valore True se e solo se l'utente vuole fare un'altra partita
#
def playAgain() :
    while True :
        Str = input("Vuoi giocare ancora? [S/N]: ")
        if Str == 'S' or Str == 's' :
            return True
        elif Str == 'N' or Str == 'n' :
            return False
        else :
            print("Errore: rispondi solo con S (sì) o N (no)!")

## randomBoolean: Genera e restituisce un valore booleano casuale (True o False)
#
def randomBoolean() :
    if randint(0, 1) == 0 : return False
    else : return True

# Esecuzione del programma
main()