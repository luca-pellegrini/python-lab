# number_name.py

from my_input import *

## Restituisce il nome dell'unità
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
    if c_decine == 0 : return nomeUnita(num)
    elif c_decine == 1 :
        if num_mod100 == 10 : return 'dieci'
        elif num_mod100 == 11 : return 'undici'
        elif num_mod100 == 12 : return 'dodici'
        elif num_mod100 == 13 : return 'tredici'
        elif num_mod100 == 14 : return 'quattordici'
        elif num_mod100 == 15 : return 'quindici'
        elif num_mod100 == 16 : return 'sedici'
        elif num_mod100 == 17 : return 'diciassette'
        elif num_mod100 == 18 : return 'diciotto'
        elif num_mod100 == 19 : return 'diciannove'
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

def nomeCentinaia(num) :
    c_cent = (num // 100) % 10
    s = ''
    if c_cent > 0 :
        s += 'cento'
        if c_cent > 1 :
            s += nomeUnita(c_cent)
    return s


# Acquisizione dato in input
while True :
    num = inputInteger("Scrivi un numero intero positivo, minore di un milione: ")
    if 0 < num < 1000000 : break


