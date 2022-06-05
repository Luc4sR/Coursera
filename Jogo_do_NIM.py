def computador_escolhe_jogada(n,m):
    computadorRemove = 1
    while computadorRemove != m:
        if (n - computadorRemove) % (m+1)== 0:
            return computadorRemove
        else:
            computadorRemove += 1
    return computadorRemove

def usuario_escolhe_jogada(n,m):
    op_errada = False
    while not op_errada:
        pecas_retirar= int(input("Quantas peças você vai tirar? "))
        if pecas_retirar > m or pecas_retirar < 1:
            print("\nOops! Jogada inválida! Tente de novo.\n")
            op_errada = False
        else:
            op_errada = True    
    return pecas_retirar

def partida():
    pecas_validas = False
    while not pecas_validas:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if m > n:
            print("\nOops! Número de peças a retirar inválido! Tente de novo.\n")
        else:
            pecas_validas = True
    vezDoPC = False
    if n % (m+1) == 0:
        print()
        print("Voce começa!")
    else:
        print()
        print("Computador começa!")
        vezDoPC = True
    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', computadorRemove, 'peças')
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
                return 2
            vezDoPC = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jogadorRemove, 'peças')
            if n == 0:
                print('Fim do jogo! Voce ganhou!')
                return 1
            vezDoPC = True
        if n ==1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()
                
def campeonato():
    pontuacao = usuario_pontos = computador_pontos = 0
    i = 1
    while i <= 3:
        print(f"**** Rodada {i} ****\n")
        pontuacao = partida()
        if pontuacao == 1:
            usuario_pontos += 1
        elif pontuacao == 2:
            computador_pontos += 1
        i+= 1
   
    print("**** Final do campeonato! ****/n")
    print(f"Placar: Você {usuario_pontos} X {computador_pontos} Computador")


print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
escolha = int(input())
if escolha == 1:
    print("Voce escolheu uma partida!\n")
    partida()
elif escolha ==2:
    print("Voce escolheu um campeonato!\n")
    campeonato()
else:
    print("\nOops! Jogada inválida! Tente de novo.\n")
