# Chiede all'utente le tre stringhe
s1 = input('Prima stringa: ')
s2 = input('Seconda stringa: ')
s3 = input('Terza stringa: ')

# Inizializza variabili min, mid, max (ordine lessicografico crescente)
min = ''
mid = ''
max = ''

# Confronta le stringhe
if s1 < s2 :
    if s2 < s3 :
        min = s1
        mid = s2
        max = s3
    else :
        if s1 < s3 :
            min = s1
            mid = s3
            max = s2
        else :
            min = s3
            mid = s1
            max = s2
else :
    if s1 < s3 :
        min = s2
        mid = s1
        max = s3
    else :
        if s2 < s3 :
            min = s2
            mid = s3
            max = s1
        else :
            min = s3
            mid = s2
            max = s1

# Visualizza
print("Le stringhe in ordine crescente sono:")
print(min)
print(mid)
print(max)
