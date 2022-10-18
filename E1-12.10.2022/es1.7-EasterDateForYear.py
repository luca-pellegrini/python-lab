# Seguiamo l'algoritmo di Gauss
y = int(input("Inserisci l'anno per cui vuoi calcolare la domenica di Pasqua: "))
a = y % 19	#a resto
b = y // 100	#b quoziente
c = y % 100		#c resto
d = b // 4	#d quoziente
e = b % 4 	#e resto
g = (8*b+13) // 25	#g quoziente
h = (19*a+b-d-g+15) % 30	#h resto
j = c // 4	#j quoziente
k = c % 4	#k resto
m = (a+11*h) // 319	#m quoziente
r = (2*e+2*j-k-h+m+32) % 7
n = (h-m+r+90) // 25
p = (h-m+r+n+19) % 32

print("Pasqua:", p, "/", n, "/", y)
