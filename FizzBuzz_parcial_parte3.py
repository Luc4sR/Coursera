numero = int(input('Qual o número? '))

if numero % 3 == 0 and numero % 5 == 0:
  print('FizzBuzz')
else:
  print(numero)