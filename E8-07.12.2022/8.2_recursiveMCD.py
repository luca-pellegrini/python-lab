# recursiveMCD.py

def main() :
    # Acquisizione dati dall'utente
    while True :
        try :
            n1 = int(input("Primo numero intero positivo: "))
            break
        except ValueError :
            pass
    while True :
        try :
            n2 = int(input("Secondo numero intero positivo: "))
            break
        except ValueError :
            pass
    print()
    # Visualizza MCD
    print("M.C.D. di %d e %d vale: %d" % (n1, n2, MCD(n1, n2)))
    #print(MCD(max(n1, n2), min(n1, n2)))

def MCD(m, n) :
    if m % n == 0 :
        return n
    else :
        return MCD(n, m % n)

main()
