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

deltaMin = delta_in_min %60
deltaOre = delta_in_min //60

# Visualizza
print("Tempo trascorso:", deltaOre, "ore e", deltaMin, "minuti")
