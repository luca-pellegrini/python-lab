from random import random
from random import randint
while True : # ciclo che contiene tutto il programma
    # Inizializza i parametri
    BIGLIE_INIZ = randint(10, 100) # è una costante nel corso della partita
    print("Il mucchio iniziale contiene", BIGLIE_INIZ, "biglie")
    n_bi = BIGLIE_INIZ # variabile diminuisce nel corso della partita
    # Chi inizia?
    if randint(0, 1) == 0 : 
        turno = 'C'
        print("Inizia il computer")
    else :
        turno = 'U'
        print("Inizia il giocatore umano")
    # Computer stupido o intelligente?
    y = randint(0, 1)
    if y == 0 :
        STUPID_MODE = True  # livello d'intelligenza 0
        print("Computer in modalità stupido")
    else :
        STUPID_MODE = False # livello d'intelligenza 1
        print("Computer in modalità intelligente")
    print()
    # Gioca la partita
    while n_bi > 1 :
        if turno == 'C' : # tocca al computer
            print("Biglie nel mucchio:", n_bi)
            if STUPID_MODE : # computer stupido
                b_sottratte = randint(1, (n_bi//2))
                print("Computer sottrae", b_sottratte, "biglie dal mucchio.")
                n_bi = n_bi - b_sottratte
            else : # computer intelligente
                if n_bi == 2 :
                    b_sottratte = 1
                    print("Computer sottrae", b_sottratte, "biglie dal mucchio.")
                    n_bi = n_bi - b_sottratte # 2-1 = 1
                elif 3 < n_bi < 7 :
                    b_sottratte = n_bi - 3
                    print("Computer sottrae", b_sottratte, "biglie dal mucchio.")
                    n_bi = n_bi - b_sottratte #= n_bi - n_bi -(-3) = 3
                elif 7 < n_bi < 15 :
                    b_sottratte = n_bi - 7
                    print("Computer sottrae", b_sottratte, "biglie dal mucchio.")
                    n_bi = 7
                elif 15 < n_bi < 31 :
                    b_sottratte = n_bi - 15
                    print("Computer sottrae", b_sottratte, "biglie dal mucchio.")
                    n_bi = 15
                elif 31 < n_bi < 63 :
                    b_sottratte = n_bi - 31
                    print("Computer sottrae", b_sottratte, "biglie dal mucchio.")
                    n_bi = 31
                elif 63 < n_bi : # <= BIGLIE_INIZ (al max 100)
                    b_sottratte = n_bi - 63
                    print("Computer sottrae", b_sottratte, "biglie dal mucchio.")
                    n_bi = 63
                else : # n_bi == 3 or n_bi == 7 or n_bi == 15 or n_bi == 31 or n_bi == 63
                    b_sottratte = randint(1, (n_bi//2))
                    print("Computer sottrae", b_sottratte, "biglie dal mucchio.")
                    n_bi = n_bi - b_sottratte
            turno = 'U'
        else : # turno == 'U' -> tocca all'umano
            print("Biglie nel mucchio:", n_bi)
            b_sottratte = int(input("Quante biglie vuoi prendere? "))
            while b_sottratte < 1 or b_sottratte > (n_bi/2) :
                print("Errore: il numero di biglie deve essere compreso tra 1")
                print("e la metà delle biglie presenti nel mucchio!")
                b_sottratte = int(input("Quante biglie vuoi prendere? "))
            n_bi = n_bi - b_sottratte
            turno = 'C'
        print()
    # il ciclo si chiude quando rimane una sola biglia nel mucchio
    # a questo punto, si sa chi ha perso (computer o umano), e quindi chi ha vinto
    # tale informazione viene data dalla variabile 'turno'
    if turno == 'C' :
        print("Congratulazioni: hai vinto!")
    else : # turno == 'U'
        print("Mi dispiace: hai perso!")
        print("Questa volta ha vinto il computer.")
    new_game = input("Vuoi giocare ancora? [S/N]: ")
    while new_game != 'S' and new_game != 'N' :
        print("Errore: rispondi solo con S (sì) o N (no)!")
        new_game = input("Vuoi giocare ancora? [S/N]: ")
    # ora new_game vale solo N o S
    if new_game == 'N' : 
        print("Arrivederci!")
        break # interrompe il programma
    else : # new_game == 'S'
        print()  # Riga vuota
        print("-"*50)