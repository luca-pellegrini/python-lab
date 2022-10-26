# Chiedi due numeri (float) all'utente
num1 = float(input("Primo numero? "))
num2 = float(input("Secondo numero? "))

# Somma
sum = num1 + num2
print("Somma:", sum)

# Prodotto
product = num1 * num2
print("Prodotto:", product)

# Valore medio
media = (num1 + num2) / 2
print("Valore medio:", media)

areEqual = False  # variabile usata di seguito

# Valore minimo e massimo
if num1 > num2 :
    print("Valore massimo:", num1)
    print("Valore minimo:", num2)
elif num1 < num2 :
    print("Valore massimo:", num2)
    print("Valore minimo:", num1)
else :
    print('I due numeri hanno lo stesso valore')
    areEqual = True

# Valore assoluto della differenza
if areEqual :
    print('Differenza (in valore assoluto) = 0')
else :
    absDiff = abs(num1 - num2)
    print('Differenza (in valore assoluto):', absDiff)
