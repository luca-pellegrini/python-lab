# file_compare.py
from sys import argv

f1 = open(argv[1], "r")
text1 = f1.read()
f2 = open(argv[2], "r")
text2 = f2.read()
f1.close()
f2.close()

if text1 == text2 :
    pass
else :
    print("I file sono diversi")
