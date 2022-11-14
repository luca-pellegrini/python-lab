# Acquisisce le due stringhe in input
print('Scrivi la prima stringa:')
s1 = input()
print('Scrivi la seconda stringa:')
s2 = input()

# Inizializza variabili Subseq e FoundCar
Subseq = False
Found = 0

# Verifica se s2 è sottosequenza di s1
if s2 == '' :
    Subseq = True
elif s1 == s2 : # len(s1) = len(s2)
    Subseq = True
elif len(s1) < len(s2) : # se s1 è più corta di s2, è ovvio che s2 non può essere una sua sottosequenza
    Subseq = False
else : # quindi len(s1) > len(s2) > 0. Il caso s1 == '' (len(s1) = 0) è escluso
    i = 0 # indice dei caratteri di s2
    x = 0 # indice di inizio della ricerca in s1
    while i < len(s2) : # cerco i caratteri di s2, uno alla volta
        #print('DEBUG: i =', i)
        y = x
        while y < len(s1) :
            #print('DEBUG: y =', y)
            if s1[y] == s2[i] :
                Found += 1
                #print('DEBUG: trovato', str(Found) + '° carattere di s2')
                x = y + 1
                break
            y += 1
        i += 1
    if Found == len(s2) : Subseq = True

# Visualizza risultato
print()
if Subseq :
    print('"%s"' % s2, 'è una sottosequenza di', '"%s"' % s1)
else :
    print('"%s"' % s2, 'NON è una sottosequenza di', '"%s"' % s1)
