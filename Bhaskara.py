a = int(input())
b = int(input())
c = int(input())

delta = b ** 2 - 4 * a * c

if delta == 0:
    resultado = (-b + d **(1/2))/(2 * a)
    print('a raiz desta equação é', resultado)
else:
    if delta > 0:
        resultado1 = (-b + d ** (1/2)) / (2 * a)
        resultado2 = (-b - d ** (1/2)) / (2 * a)
        if resultado1 < resultado2:
            print(f"as raízes da equação são {resultado1} e {resultado2}")
        else:
            print(f"as raízes da equação são {resultado2} e {resultado1}")
    else:
        print('esta equação não possui raízes reais')