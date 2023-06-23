""" Desafio 16 - crie um programa que leia um número real qualquer e mostre a sua versão
inteira"""

numero = float(input('Digite um valor real: '))
numero_int = int(numero)
print(f'O valor digitado foi {numero}, e o seu número inteiro é: {numero_int}')


""" Desafio 17 - Faça um programa que leia o comprimento dos catetos oposto e adjacente,
mostre o valor da hipotenusa"""

co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
h = ((co ** 2) + (ca ** 2)) ** 0.5
print(f'O valor da hipotenusa é {h}')

""" Desafio 18 - Faça um programa que receba um angulo qualquer e mostre na tela o valor do seno,
cosseno e da tangente deste angulo"""
import math

pi = 3.14159265358979323846
angulo = float(input('Digite um angulo qualquer: '))
rad = angulo * pi / 180
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print(f'O ângulo digitado foi {angulo}, o valor do seu seno é {seno:.4f}, do seu cosseno é {cosseno:.4f} e da sua tangente é {tangente:.4f}')


""" Desafio 19 - Receba o valor de 4 alunos e crie um programa que fara um sorteio entre eles"""

import random
pessoa1 = input('Digite o nome do primeiro aluno: ')
pessoa2 = input('Digite o nome do segundo aluno: ')
pessoa3 = input('Digite o nome do terceiro aluno: ')
pessoa4 = input('Digite o nome do quarto aluno: ')

alunos = [pessoa1, pessoa2, pessoa3, pessoa4]
print(f'O aluno escolhido foi {random.choice(alunos)}')



""" Desafio 20 - pegando do exemplo anterior, mostre-os em uma ordem entre os 4 alunos 
(dentro de um array)"""

import random
pessoa1 = input('Digite o nome do primeiro aluno: ')
pessoa2 = input('Digite o nome do segundo aluno: ')
pessoa3 = input('Digite o nome do terceiro aluno: ')
pessoa4 = input('Digite o nome do quarto aluno: ')

alunos = [pessoa1, pessoa2, pessoa3, pessoa4]
random.shuffle(alunos)
print(alunos)