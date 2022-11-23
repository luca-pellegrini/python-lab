# Acquisisci numero intero positivo
decNumber = int(input('Scrivi un numero intero positivo (minore di 4000): '))
while decNumber <= 0 or decNumber >= 4000 :
    print('Errore: devi scrivere un numero intero positivo (e minore di 4000)! Riprova')
    decNumber = int(input('Scrivi un numero intero positivo: '))

# Calcola le cifre di migliaia, centinaia, decine e unita' del numero
migl_dec = decNumber // 1000  # cifra migliaia num decimale
cent_dec = (decNumber % 1000) // 100  # cifra centinaia num decimale
deci_dec = (decNumber % 100) // 10  # cifra decine num decimale
unit_dec = decNumber % 10  # cifra unità num decimale

romanNumber = ''

# Conversione delle cifre da decimali a romane
# Migliaia
if migl_dec == 1 :
    romanNumber += 'M'
elif migl_dec == 2 :
    romanNumber += 'MM'
elif migl_dec == 3 :
    romanNumber += 'MMM'

# Centinaia
if cent_dec == 1 :
    romanNumber += 'C'
elif cent_dec == 2 :
    romanNumber += 'CC'
elif cent_dec == 3:
    romanNumber += 'CCC'
elif cent_dec == 4:
    romanNumber += 'CD'
elif cent_dec == 5:
    romanNumber += 'D'
elif cent_dec == 6:
    romanNumber += 'DC'
elif cent_dec == 7:
    romanNumber += 'DCC'
elif cent_dec == 8:
    romanNumber += 'DCCC'
elif cent_dec == 9:
    romanNumber += 'CM'

# Decine
if deci_dec == 1 :
    romanNumber += 'X'
elif deci_dec == 2:
    romanNumber += 'XX'
elif deci_dec == 3:
    romanNumber += 'XXX'
elif deci_dec == 4:
    romanNumber += 'XL'
elif deci_dec == 5:
    romanNumber += 'L'
elif deci_dec == 6:
    romanNumber += 'LX'
elif deci_dec == 7:
    romanNumber += 'LXX'
elif deci_dec == 8:
    romanNumber += 'LXXX'
elif deci_dec == 9:
    romanNumber += 'XC'

# Unità
if unit_dec == 1 :
    romanNumber += 'I'
elif unit_dec == 2:
    romanNumber += 'II'
elif unit_dec == 3:
    romanNumber += 'III'
elif unit_dec == 4:
    romanNumber += 'IV'
elif unit_dec == 5:
    romanNumber += 'V'
elif unit_dec == 6:
    romanNumber += 'VI'
elif unit_dec == 7:
    romanNumber += 'VII'
elif unit_dec == 8:
    romanNumber += 'VIII'
elif unit_dec == 9:
    romanNumber += 'IX'

# Visualizza il numero romano
print('Numero romano:', romanNumber)
