n = int(input("Digite um número inteiro: "))
i = n - 1

while i > 0:
    if i == 1:
        print('primo')
        break
    elif n % i == 0:
        print('não primo')
        break
    else:
        i -= 1