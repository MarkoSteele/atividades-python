
import random

numero_aleatorio = random.randint(0, 5)
numero_fornecido = int(input('Digite um número: '))

if numero_aleatorio == numero_fornecido:
    print('Acertou')
else:
    print('Errou')
