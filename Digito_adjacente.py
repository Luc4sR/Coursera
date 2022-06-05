n = int(input("Digite um número inteiro: "))
condicao = True

while condicao:
    x = n%10
    x1 = n//10
    x2 = x1%10
    if n <= 10:
        print('não')
        condicao = False
    elif n > 10 and x == x2:
        print('sim')
        condicao = False
    else:
        n = n//10