""" Desafio 41 -  É necessário que o programa leia
a idade do usuário, e que mostre a sua categoria de
acordo com a idade
até 9 = Mirim
até 14 = Infantil
até 19 = Junior
até 25 = Sênior
acima de 25 = Master
"""
idade = int(input('Digite a sua idade para saber a sua categoria: '))
if idade <= 9:
    print('A sua categoria é mirim')
elif idade <= 14:
    print('A sua categoria é Infantil')
elif idade <= 19:
    print('A sua categoria é Junior')
elif idade <= 25:
    print('A sua categoria é Sênior')
else:
    print('A sua categoria é Master')



""" Desafio 43 -  Desenvolva um programa que leia o peso e a altura de uma pessoa e faça
o Calculo do seu IMC e mostre o status de acordo com a tabela:
Abaixo de 18.5: abaixo do peso
entre 18.5 e 25: peso ideal
entre 25 e 30: sobrepeso
entre 30 e 40: Obesidade
acima de 40: Obesidade móbida
"""
peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')


""" Desafio 44 -  Elabore um programa que deva calcular o valor a ser pago de um produto
que será considerado o seu preço normal e a condição de pagamento:
A vista(dinheiro/cheque): desconto de 10%
A vista(cartão): 5% de desconto
em Até x2: preço normal
3x ou mais vezes: 20% de juros
"""
from time import sleep
delay = 0.5
high_delay = 1

produto = float(input('Digite o valor do produto: R$'))
forma_pagamento = ['1. à vista (dinheiro/cheque)', '2. à vista (cartão)', '3. parcelando em até x2', '4. parcelando x3 ou mais vezes']
for modo in forma_pagamento:
    print(modo)
    sleep(delay)
forma_escolhida = input('Digite a forma de pagamento desejada: ')
sleep(high_delay)
if forma_escolhida == '1':
    valor_produto = produto * 0.9 
    print(f'O valor a ser pago será de R${valor_produto}')
elif forma_escolhida == '2':
    valor_produto = produto * 0.95
    print(f'O valor a ser pago será de R${valor_produto}')
elif forma_escolhida == '3':
    valor_produto = produto
    print(f'O valor a ser pago será de R${valor_produto}')
elif forma_escolhida == '4':
    valor_produto = produto * 1.2
    print(f'O valor a ser pago será de R${valor_produto}')


""" Desafio 45 -  Crie um programa que faça o computador jogar Jokenpô com você:"""
import random

opcoes = ['1. Pedra', '2. Papel', '3. Tesoura']
escolha_maquina = random.choice(opcoes)
print(escolha_maquina)
for opcao in opcoes:
    print(opcao)
escolha = input('Digite o número da sua opção de escolha: ')
empate = (escolha == '1' and escolha_maquina ==  '1. Pedra') or (escolha == '2' and escolha_maquina ==  '2. Papel') or (escolha == '3' and escolha_maquina ==  '3. Tesoura')
vitoria_usuario = (escolha == '1' and escolha_maquina ==  '3. Tesouro') or (escolha == '2' and escolha_maquina ==  '1. Pedra') or (escolha == '3' and escolha_maquina ==  '2. Papel')
vitoria_maquina = (escolha == '2' and escolha_maquina ==  '3. Tesouro') or (escolha == '3' and escolha_maquina ==  '1. Pedra') or (escolha == '1' and escolha_maquina ==  '2. Papel')
if empate:
    print('Empate!!')
elif vitoria_usuario:
    print('Você ganhou!!')
elif vitoria_maquina:
    print('A maquina ganhou!!')


