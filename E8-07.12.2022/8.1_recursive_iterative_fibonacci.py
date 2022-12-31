# recursive_iterative_fibonacci.py
from time import perf_counter

def main() :
    while True :
        try :
            n = int(input("Un numero intero positivo: "))
            break
        except ValueError :
            pass
    print()

    beginTime = perf_counter()
    f1 = iterativeFib(n)
    endTime = perf_counter()
    deltaTime1 = endTime - beginTime

    beginTime = perf_counter()
    f2 = recursiveFib(n)
    endTime = perf_counter()
    deltaTime2 = endTime - beginTime

    if f1 == f2 :
        print("Fib( %d ) =" % n, f1)
    else :
        print("Errore: i due numeri calcolati sono diversi")

    print("Tempo impiegato da iterativeFib = %e s" % deltaTime1)
    print("Tempo impiegato da recursiveFib = %e s" % deltaTime2)

def iterativeFib(n) :
    if n < 2 :
        return n
    fib0 = 0
    fib1 = 1
    for i in range(2, n+1) :
        newFib = fib0 + fib1
        fib0 = fib1
        fib1 = newFib
    return fib1

def recursiveFib(n) :
    if n < 2 :
        return n
    return recursiveFib(n-2) + recursiveFib(n-1)

main()
