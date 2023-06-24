""" Desafio 26 - Receba uma frase do usuário, mostre
Quantas vezes aparece a letra "A", em que posição ele aparece a primeira vez
em que posição ela aparece na ultima vez"""

""" frase = input('Digite uma frase: ').upper()
print(f'A letra "A" aparece {frase.count("A")}')
print(f'A primeira vez que a letra "A" aparece em {frase.find("A")+1}')
print(f'A ultima vez que a letra "A" aparece em {frase.rfind("A")+1}')
 """


""" Desafio 27 - Receba o nome completo do usuário e mostre separadamente
o primeiro nome e o último nome"""

""" nome_completo = input('Digite o seu nome completo: ')
nome_separado = nome_completo.split(' ')
print(f'Este é o seu primeiro nome: {nome_separado[0]}')
print(f'Este é o seu primeiro nome: {nome_separado[-1]}')
 """


""" Desafio 28 -  Escreva um programa que vai gerar um número entre 0 a 5, e pça
para o usuário adivinhar o número, mostre se o usuário ganhou ou perdeu"""

""" 
import random

numero_aleatorio = random.randint(0, 5)
numero_fornecido = int(input('Digite um número: '))

if numero_aleatorio == numero_fornecido:
    print('Acertou')
else:
    print('Errou')
 """


""" Desafio 29 -  Escreva um programa que leia a velocidade de um carro e se
ele ultrapassar 80km/h, mostre a mensagem dizendo que ele foi multado e
faça o calculo de 7 reais por km acima do permitido"""
""" 
velocidade = 90  # pode ser uma entrada do usuário também, porém teria que converter para int
velocidade_limite = 80

if velocidade <= velocidade_limite:
    print('O carro não foi multado')
else:
    valor_multa = velocidade - 70
    multa = valor_multa * 7
    print(f'O motorista foi multado e o valor a pagar é {multa}')
 """





""" Desafio 30 -  Crie um programa que leia um número inteiro e informe
se ele é ímpar ou par"""

# utilizei também um try/except para evitar erros para o usuário
try:
    valor = int(input('Digite um número inteiro para descobrir se ele é ímpar ou par: '))
    resto = valor % 2

    if resto == 0: 
        print(f'O valor digitado ({valor}) é par')
    else:
        print(f'O valor digitado ({valor}) é ímpar')
except:
    print('Valor digitado é inválido')
