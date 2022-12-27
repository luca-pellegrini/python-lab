# Acquisisce le due stringhe in input
print('Scrivi la prima stringa:')
s1 = input()
print('Scrivi la seconda stringa:')
s2 = input()

# Inizializza variabile Substring
Substring = False

# Verifica se s2 è sottostringa di s1
if s2 == '' :
    Substring = True
elif s1 == s2 : # len(s1) = len(s2)
    Substring = True
elif len(s1) < len(s2) :
    Substring = False # se s1 è più corta di s2, è ovvio che s2 non può essere una sua sottostringa
else : # quindi len(s1) > len(s2) > 0. Il caso s1 == '' (len(s1) = 0) è escluso
    x = 0 # indice di inizio della ricerca in s1
    while x <= len(s1) - len(s2) : # se len(s1) = 0, non inizia il ciclo, quindi Substring rimane False
        y = x
        while y < x + len(s2) :
            if s1[y] == s2[y-x] :
                Substring = True
            else :
                Substring = False # appena trovo una coppia di caratteri che non corrispondo,
                # interrompo questo ciclo (relativo a un particolare valore di x)
                break
            y += 1
        if Substring : break # ho trovato la sottostringa?
        x += 1 # se no, passo al prossimo indice di inizio

# Visualizza risultato
print()
if Substring :
    print('"%s"' % s2, 'è una sottostringa di', '"%s"' % s1)
else :
    print('"%s"' % s2, 'NON è una sottostringa di', '"%s"' % s1)
