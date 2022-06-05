largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

i = 1
while i <= altura:
    if i == 1 or i == altura:
        print(largura*"#")
        i += 1
    elif largura == altura:
        print(*"#", (largura - 3)*" ", "#")
        i += 1
    else: 
        print(*"#", (largura - (altura + 1))*" ", "#")
        i += 1
