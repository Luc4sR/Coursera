def Primo(n):
    i = n - 1
    while i > 0:
        if i == 1:
            return True
        elif n % i == 0:
            return False
        else:
            i -= 1

def maior_primo(x):
    while x > 0:
        if Primo(x) == True:
            return x
        else:
            x -= 1
    print(x)
