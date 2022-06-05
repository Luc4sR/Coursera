
def computador_escolhe_jogada(n,m):
    remove = 1
    while remove != m:
        if (n - remove) % (m + 1) == 0:
            return remove
        else:
            remove += 1
            return remove
def usuario_escolhe_jogada(n,m):
    print('**** Rodada 1 ****')
    n = int(input('Quantas peças ?' ))
    m = int(input('Limite de peças por jogada' ))
    if n % m+1 == 0:
        print('Você começa')
    elif n % m+1 > 0:
        print('Computador começa')
        
print('Bem-vindo ao jogo do NIM! Escolha:')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato')
tipo_jogo = int(input())
if tipo_jogo == 1:
    print('Você escolheu uma partida isolada')
elif tipo_jogo == 2:
    print('Você escolheu um campeonato')
else:
    print('Oops! Jogada inválida, escolha 1 ou 2')
