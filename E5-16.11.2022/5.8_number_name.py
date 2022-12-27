# number_name.py

from my_input import *

## Restituisce il nome dell'unità
#  Usata solo all'interno di altre funzioni di seguito definite
#  @param num Numero intero da analizzare
#  @return Stringa
#
def nomeUnita(num) :
    c_unita = num % 10
    if c_unita == 0 : return ''
    elif c_unita == 1 : return 'uno'
    elif c_unita == 2 : return 'due'
    elif c_unita == 3 : return 'tre'
    elif c_unita == 4 : return 'quattro'
    elif c_unita == 5 : return 'cinque'
    elif c_unita == 6 : return 'sei'
    elif c_unita == 7 : return 'sette'
    elif c_unita == 8 : return 'otto'
    elif c_unita == 9 : return 'nove'

## Restituisce il nome di decina + unità
#  Tiene conto anche del caso particolare dei numeri da 10 a 19
#
def nomeDecineUnita(num) :
    num_mod100 = num % 100
    c_unita = num % 10
    c_decine = (num // 10) % 10
    s = '' # stringa da restituire
    if c_decine == 0 : s += nomeUnita(num)
    elif c_decine == 1 :
        if num_mod100 == 10 : s += 'dieci'
        elif num_mod100 == 11 : s += 'undici'
        elif num_mod100 == 12 : s += 'dodici'
        elif num_mod100 == 13 : s += 'tredici'
        elif num_mod100 == 14 : s += 'quattordici'
        elif num_mod100 == 15 : s += 'quindici'
        elif num_mod100 == 16 : s += 'sedici'
        elif num_mod100 == 17 : s += 'diciassette'
        elif num_mod100 == 18 : s += 'diciotto'
        elif num_mod100 == 19 : s += 'diciannove'
    elif c_decine == 2 : # venti
        s += 'vent'
        if c_unita != 1 and c_unita != 8 : s += 'i'
        s += nomeUnita(num)
    elif c_decine == 3 : # trenta
        s += 'trent'
        if c_unita != 1 and c_unita != 8 : s += 'a'
        s += nomeUnita(num)
    elif c_decine == 4 : # quaranta
        s += 'quarant'
        if c_unita != 1 and c_unita != 8 : s += 'a'
        s += nomeUnita(num)
    elif c_decine == 5 : # cinquanta
        s += 'cinquant'
        if c_unita != 1 and c_unita != 8 : s += 'a'
        s += nomeUnita(num)
    elif c_decine == 6 : # sessanta
        s += 'sessant'
        if c_unita != 1 and c_unita != 8 : s += 'a'
        s += nomeUnita(num)
    elif c_decine == 7 : # settanta
        s += 'settant'
        if c_unita != 1 and c_unita != 8 : s += 'a'
        s += nomeUnita(num)
    elif c_decine == 8 : # ottanta
        s += 'ottant'
        if c_unita != 1 and c_unita != 8 : s += 'a'
        s += nomeUnita(num)
    elif c_decine == 9 : # novanta
        s += 'novant'
        if c_unita != 1 and c_unita != 8 : s += 'a'
        s += nomeUnita(num)
    return s

def nomeCentinaiaDecineUnita(num) :
    c_cent = (num // 100) % 10
    s = ''
    if c_cent > 1 :
        s += nomeUnita(c_cent)
    if c_cent > 0 :
        s += 'cento'
    s += nomeDecineUnita(num)
    print("DEBUG:", s)
    return s

def nomeCentDecUnitMigliaia(num) :
    s = nomeCentinaiaDecineUnita(num // 1000)
    if num // 1000 > 1 : s += 'mila'
    if num // 1000 == 1 : s = s.replace('uno', 'mille')
    print("DEBUG:", s)
    return s


# Acquisizione dato in input
while True :
    num = inputInteger("Scrivi un numero intero positivo, minore di un milione: ")
    if 0 < num < 1000000 : break

# Visualizza
outputStr = nomeCentDecUnitMigliaia(num) + nomeCentinaiaDecineUnita(num)
print(outputStr)
