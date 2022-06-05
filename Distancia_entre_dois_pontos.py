import math
x1 = int(input('Número'))
x2 = int(input('Número'))
y1 = int(input('Número'))
y2 = int(input('Número'))

plano_cartesiano = (x1 - x2) ** 2 + (y1 - y2) ** 2
raiz = math.sqrt(plano_cartesiano)
if delta >= 10:
    print('longe na saída')
else:
    print('perto')