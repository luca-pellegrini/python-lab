# Inizializza le variabili
palindrome = True

# Chiede all'utente una stringa
s = input("Inserire una stringa: ")

# Controlla i caratteri di s per determinare se è palindroma
i = 0 # contatore del ciclo
while i < (len(s))/2 :
    if s[i] != s[-1-i] :
        palindrome = False
        break # basta che una sola coppia di caratteri
        # non coincida per rendere s non palindroma
    i += 1
print()
if palindrome :
    print("La stringa è palindroma")
else :
    print("La stringa non è palindroma")