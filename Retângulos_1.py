lado = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

linha = 0
coluna = 0

while linha < altura:
    while coluna < lado:
        print("#", end="")
        coluna += 1
    print()
    linha += 1
    coluna = 0
