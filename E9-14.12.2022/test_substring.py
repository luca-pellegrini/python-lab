# test_substring.py
# Collaudo del modulo mysubstring

from mysubstring import *

## Inverte il contenuto di una lista
#
def reverse(lst):
    n = len(lst)
    for i in range(n // 2):
        temp = lst[i]
        lst[i] = lst[n-1 -i]
        lst[n-1 -i] = temp

# main
print("Collaudo del modulo mysubstring\n")
for s in ["", "a", "ab", "abc", "abcdefghilm"]:
    print("Stringa: " + s)
    ss = get_all_substrings(s)
    len1 = num_substrings(s)
    len2 = len(ss)
    print("Lunghezza prevista:", len1)
    print("Lunghezza effettiva:", len2)
    if len1 != len2:
        print("ERRORE: le due lunghezze non coincidono")
    if not are_unique(ss):
        print("ERRORE: la lista contiene duplicati")
    ss.sort()
    if not is_forward_sorted(ss):
        print("ERRORE: la lista non è correttamente ordinata")
    reverse(ss)
    if not is_backward_sorted(ss):
        print("ERRORE: la lista non è ordinata al contrario")
    print()

for s in ["", "a", "ab", "abc", "abcdefghilm"]:
    ...
