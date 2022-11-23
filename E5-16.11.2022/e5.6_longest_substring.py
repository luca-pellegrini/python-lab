# longest_substring.py

print()
# Acquisisce le due stringhe in input
print('Scrivi la prima stringa:')
s1 = input()
print('Scrivi la seconda stringa:')
s2 = input()

# Inizializza variabile Substring
Substring = ''
#prevSubstring = ''

# Cerca sottostringa comune tra s1 e s2
if s1 == '' or s2 == '' :
    Substring = ''
else :
    i = 0
    while i < len(s1) :
        k = len(s1)
        while k > i :
            x = 0
            while x < len(s2) :
                y = len(s2)
                while y > x :
                    if s1[i:k] == s2[x:y] :
                        s = s1[i:k]
                        if len(s) > len(Substring) :
                            Substring = s
                            #print("DEBUG:", Substring)
                    y -= 1
                x += 1
            k -= 1
        i += 1
print()

"""
if s1[i:k] == s2[x:y] :
    s = s1[i:k]
    if len(s) > len(Substring) :
        Substring = s
"""

print("Sottostringa comune:", Substring)