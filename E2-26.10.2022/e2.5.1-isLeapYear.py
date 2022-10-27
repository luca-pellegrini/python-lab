# Versione alternativa di `isLeapYear.py`
# Acquisisci numero intero positivo
anno = int(input("Scrivi il numero corrispondente all'anno: "))

if anno <= 0 :
    print("Errore: solo numeri interi positivi!")
else :
    if anno % 4 == 0 and (anno < 1582 or anno % 100 != 0 or anno % 400 == 0) :
        isLeap = True
    else :  # equivale a: anno % 4 != 0 or (anno >= 1582 and anno % 100 == 0 and anno % 400 != 0)
        isLeap = False
    if isLeap :
        a = " "
    else :  # isLeap == False
        a = " non "
    print("L'anno " + str(anno) + a + "è bisestile")