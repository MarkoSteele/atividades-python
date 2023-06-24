""" Desafio 22 - Receba um nome do usuário, mostre esse nome em maiúsculo
minúsculo, a quantidade de letras e retorne so o primeiro nome """

from time import sleep
delay = 0.5
nome_completo = input('Digite o seu nome completo: ')
print('Analisando o seu nome...')
sleep(delay)
print(f'O seu nome em maiúsculas é {nome_completo.upper()}.')
sleep(delay)
print(f'O seu nome em Minúsculas é {nome_completo.lower()}.')
sleep(delay)
print(f'O seu nome tem ao todo {len(nome_completo)} letras.')
sleep(delay)
primeiro_nome = nome_completo.split(' ')
print(f'O seu primeiro nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras.')


""" Desafio 23 - Receba um valor de 0 até 9999 e mostre o caracter correspondente
a unidade, dezena, centena e milhar """
numero = input('Digite um número: ')
if len(numero) == 4:
    print(f'Unidade: {numero[3]}')
    print(f'Dezena: {numero[2]}')
    print(f'Centena: {numero[1]}')
    print(f'Milhar: {numero[0]}')
elif len(numero) == 3:
    print(f'Unidade: {numero[2]}')
    print(f'Dezena: {numero[1]}')
    print(f'Centena: {numero[0]}')
    print(f'Milhar: Não existe')
elif len(numero) == 2:
    print(f'Unidade: {numero[1]}')
    print(f'Dezena: {numero[0]}')
    print(f'Centena: Não existe')
    print(f'Milhar: Não existe')
elif len(numero) == 1:
    print(f'Unidade: {numero[0]}')
    print(f'Dezena: Não existe')
    print(f'Centena: Não existe')
    print(f'Milhar: Não existe')
else:
    print('Número não suportado, digite um número até 4 casas')



""" Desafio 24 -  receba do usuário uma cidade e diga se ela começa ou não
com 'Sant'"""

# lower para facilitar a verificação
#strip para evitar erros por causa de espaço
cidade = input('Digite uma cidade: ').lower().strip() 
if cidade.find('sant') == -1:
    print('Falso')
else:
    print('Verdadeiro')




""" Desafio 25 -  Crie um programa e leia o nome de uma pessoa e diga se ela tem 'Silva no nome'"""

nome = input('Digite o seu nome completo: ').lower().strip()
if 'silva' in nome:
    print('Este nome possui Silva no sobrenome')
else:
    print('Este nome não possui Silva no sobrenome')