# Acquisisci numero intero positivo
anno = int(input("Scrivi il numero corrispondente all'anno: "))
if anno <= 0 :
    print("Errore: devi inserire un numero intero positivo!")
else :
    isLeap = False  # in generale, un anno non è bisestile
    if anno % 4 == 0 : # divisibile per 4
        isLeap = True  # bisestile
        if anno > 1582 :  # per gli anni > 1582 valgono le seguenti eccezioni
            if anno % 100 == 0 : # divisibile per 100
                isLeap = False
                if anno % 400 == 0 : # divisibile per 400
                    isLeap = True
    if isLeap :
        print("L'anno", anno, "è bisestile")
    else :
        print("L'anno", anno, "non è bisestile")
