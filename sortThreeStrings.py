#programma che mette tre stringhe in ordine lessicografico
prima=input("Inserisca prima stringa: ")
seconda=input("Inserisca seconda stringa: ")
terza=input("Inserisca terza stringa: ")
if prima>=seconda:
    if seconda>=terza:
        minima=terza
        mid=seconda
        massima=prima
    else:
        if terza>=prima:
            minima=seconda
            mid=prima
            massima=terza
        else:
            minima=seconda
            mid=terza
            massima=prima
else:
    if prima>=terza:
        minima=terza
        mid=prima
        massima=seconda
    else:
        if terza>=seconda:
            minima=prima
            mid=seconda
            massima=terza
        else:
            minima=prima
            mid=terza
            massima=seconda
print ("Le stringhe in ordine crescente sono: ")
print (minima)
print (mid)
print (massima)
input()
