# tictactoe.py
from my_input import *

print("TIC-TAC-TOE!")
print()

# Inizializzazione variabili
s = ['.'] * (3*3) # scacchiera
turno = 1 # inizia il giocatore 1

# Gioca la partita
while True :
    # Visualizza la scacchiera
    print(s[0] + s[1] + s[2])
    print(s[3] + s[4] + s[5])
    print(s[6] + s[7] + s[8])
    print()
    print("Tocca al giocatore %d" % turno)
    while True : # contrassegna una casella valida
        print("Quale casella vuoi contrassegnare?")
        x = inputInteger("Riga (dall'alto): ")
        y = inputInteger("Colonna (da sinistra): ")
        if x < 0 or x > 2 or y < 0 or y > 2 :
            print("Errore: coordinate non valide!")
        elif s[3*x + y] != '.' :
            print("Errore: casella già occupata")
        else :
            if turno == 1 : s[3*x + y] = 'X'
            elif turno == 2 : s[3*x + y] = 'O'
            break 
        print()
        print(s[0] + s[1] + s[2])
        print(s[3] + s[4] + s[5])
        print(s[6] + s[7] + s[8])
        print()
    print()
    # Verifica se uno dei due giocatori ha vinto
    # o se la partita è finita in pareggio
    if ((s[0] == s[3] == s[6] == 'X') or
        (s[0] == s[3] == s[6] == 'O') or
        (s[1] == s[4] == s[7] == 'X') or
        (s[1] == s[4] == s[7] == 'O') or
        (s[2] == s[5] == s[8] == 'X') or
        (s[2] == s[5] == s[8] == 'O') or
        (s[0] == s[1] == s[2] == 'X') or
        (s[0] == s[1] == s[2] == 'O') or
        (s[3] == s[4] == s[5] == 'X') or
        (s[3] == s[4] == s[5] == 'O') or
        (s[6] == s[7] == s[8] == 'X') or
        (s[6] == s[7] == s[8] == 'O') or
        (s[0] == s[4] == s[8] == 'X') or
        (s[0] == s[4] == s[8] == 'O') or
        (s[2] == s[4] == s[6] == 'X') or
        (s[2] == s[4] == s[6] == 'O')) :
        winner = turno
        break
    elif '.' not in s : # tutte le caselle occupate
        winner = 0 # parità
        break
    if turno == 1 :
        turno = 2
    elif turno == 2 :
        turno = 1

# Visualizza la scacchiera
print(s[0] + s[1] + s[2])
print(s[3] + s[4] + s[5])
print(s[6] + s[7] + s[8])
print()
if winner == 0 :
    print("Partita terminata: nessuno ha vinto.")
else :
    print("Ha vinto il giocatore %d" % winner)

