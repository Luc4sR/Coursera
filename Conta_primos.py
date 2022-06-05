def ePrimo(n):
    i = n - 1
    while i > 0:
        if i == 1:
            return True
            break
        elif (n % i == 0):
            return False
            break
        else:
            i -= 1

def n_primos(x):
    primos = 0
    while x > 0:
        if ePrimo(x) == True:
            primos += 1
            x -= 1
        else:
            x -= 1
    return(primos)