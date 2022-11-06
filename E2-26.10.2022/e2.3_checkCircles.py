# Chiedi all'utente i dati
print('La prima circonferenza ha centro in C1 e raggio r1')
x1 = float(input('Coordinata x di C1: '))
y1 = float(input('Coordinata y di C1: '))
r1 = float(input('Raggio r1: '))

while r1 <= 0 :
    print('Errore: il raggio r1 deve essere positivo! Riprova')
    r1 = float(input('Raggio r1: '))

print()
print('La seconda circonferenza ha centro in C2 e raggio r2')
x2 = float(input('Coordinata x di C2: '))
y2 = float(input('Coordinata y di C2: '))
r2 = float(input('Raggio r2: '))

while r2 <= 0 :
    print('Errore: il raggio r2 deve essere positivo! Riprova')
    r2 = float(input('Raggio r2: '))

print()

deltaR = ((x1 - x2)**2 + (y1 - y2)**2)**0.5  # distanza tra C1 e C2, ossia tra i centri delle due circonferenze

# Calcoliamo le varie condizioni
if deltaR == 0 and r1 == r2 :
    print('Le due circonferenze sono coincidenti')
elif deltaR == r1 + r2 :
    print('Le due circonferenze sono tangenti esternamente')
elif deltaR == abs(r1 - r2) :
    print('Le due circonferenze sono tangenti internamente')
elif abs(r1 - r2) < deltaR < r1 + r2 :
    print('Le due circonferenze sono secanti')
elif deltaR == 0 and r1 != r2 :
    print('Le due circonferenze sono concentriche (ma non coincidenti)')
elif deltaR > 0 and (r2 + deltaR < r1 or r1 + deltaR < r2) :
    print('Le due circonferenze sono una interna all\'altra')
else :
    print('Le due circonferenze sono (reciprocamente) esterne')
