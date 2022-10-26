# Chiedi all'utente un numero dispari (intero)
num1 = int(input('Scrivi un numero dispari (intero): '))

# Un numero e' pari se e solo se il num % 2 = 0 
# (il resto della divisione per 2 del numero stesso e' 0)
# (in altre parole, se e solo se e' un multiplo di 2)
resto1 = num1 % 2  # resto della divisione per 2

if resto1 == 1 :
    print('Complimenti! Il numero', num1, 'è dispari')
else :
    print('Errore: devi inserire un numero dispari! Riprova')
    num2 = int(input('Scrivi un numero dispari: '))
    resto2 = num2 % 2
    if resto2 == 1 :
        print('Complimenti! Il numero', num2, 'è dispari')
    else :
        print('Ripassa il concetto di numero dispari, ti saluto.')
