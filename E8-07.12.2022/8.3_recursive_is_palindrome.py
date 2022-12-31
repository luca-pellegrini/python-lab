# recursive_is_palindrome.py

def main() :
    s = input("Una stringa: ")
    print()
    # Visualizza risultato
    print(s, end=" ")
    if not isPalindrome(s) :
        print("NON", end=" ")
    print("è un palindromo")

def isPalindrome(s) :
    if len(s) <= 1 :
        return True
    #print("Ricorsione...")
    return (s[0] == s[-1]) and isPalindrome(s[1:-1])

main()
