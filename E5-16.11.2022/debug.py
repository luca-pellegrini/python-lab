from my_input import *

while True :
    x = input()
    if x == "STOP" : break
    print("isInteger:", isInteger(x))
print()

while True :
    y = input()
    if y == "STOP" : break
    print("isFloat:", isFloat(y))
print()

n1 = inputInteger("Numero intero: ")
print(n1)
n2 = inputFloat("Numero frazionario: ")
print(n2)
b = inputYesNo("Rispondi [S/N]: ", "S", "N")