from sys import exit

print("Questo programma legge una riga di testo, e la visualizza priva di")
print("eventuali caratteri duplicati")
print("Scrivi di seguito una riga di testo")

S = input()
if S == "" :
    exit("Errore: la riga di testo non può essere vuota!")
outS = S[0]
i = 1
while i < len(S) :
    if S[i] != S[i-1] :
        outS += S[i]
    i += 1
print()
print("Risultato:")
print(outS)
