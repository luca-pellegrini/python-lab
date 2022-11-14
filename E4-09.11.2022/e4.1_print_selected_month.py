# print_selected_month.py
# Chiede all'utente un numero intero compreso tra 1 e 12
while True :
    n = int(input("Inserisci il numero del mese (1-12): "))
    if 1 <= n <= 12 : break
    else : print("Errore: numero non valido!")

# len("settembre") = 9
Stringa = "%-9s%-9s%-9s%-9s%-9s%-9s%-9s%-9s%-9s%-9s%-9s%-9s" % ("Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre")
#print('DEBUG: Stringa =', Stringa)

# Visualizza mese
print(Stringa[(n-1)*9 : n*9])
