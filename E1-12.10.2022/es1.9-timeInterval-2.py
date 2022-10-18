# Fork di es1.9-timeInterval.py

# Chiedi all'utente due orari
o1 = int(input("Inserire il primo orario (es. 0930): "))
o2 = int(input("Inserire il secondo orario (successivo al primo): "))

min1 = o1%100
ore1 = o1//100
min2 = o2%100
ore2 = o2//100

o1_in_min = ore1*60 + min1
o2_in_min = ore2*60 + min2

delta_in_min = o2_in_min - o1_in_min
"""
Se delta_in_min < 0, io vorrei avere il valore: (minuti in 24h) + delta_in_min
Tuttavia, non posso ancora usare l'enunciato if in questo esercizio.
Mi serve un'operazione matematica che possa ottenere lo stesso risultato, e allo stesso tempo lasciare inalterato il valore delta_in_min nel caso sia già positivo
"""

# (60*24) = 1440 minuti in un giorno di 24h
delta2 = (delta_in_min + 1440)%(1440)
"""
delta2 è sempre il più piccolo valore positivo tale che delta2 è uguale a delta_in_min modulo 1440
Vale sempre delta_in_min < 1440

Se delta_in_min > 0, allora (delta_in_min + 1440)%(1440) = delta_in_min
Se delta_in_min < 0, allora (delta_in_min + 1440)%(1440) = 1440 + delta_in_min; e quindi 0 < delta2 < 1440
"""

deltaMin = delta2 %60
deltaOre = delta2 //60

# Visualizza
print("Tempo trascorso:", deltaOre, "ore e", deltaMin, "minuti")
