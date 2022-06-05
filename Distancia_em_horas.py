import math
distancia_percorrer = int(input('Digite a distância a percorrer'))
km_por_hora = int(input('Digite a velocidade média'))

tempo_viagem = distancia_percorrer // km_por_hora
tempo_viagem1 = distancia_percorrer / km_por_hora
fracao, inteiro = math.modf(tempo_viagem1)
produto_minutos = fracao * 60
frac_final = str(produto_minutos) [0:2]
print(f'Você chegará ao seu destino em', tempo_viagem, 'horas e', frac_final, 'Minutos')
