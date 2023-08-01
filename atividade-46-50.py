""" atividade 46  
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
indo de 10 até 0, com uma pausa de 1 segundo entre eles
"""
from time import sleep
delay = 1

def count_reg(num):
    while num >= 0:
        print(num)
        sleep(delay)
        num -= 1
        if num == 0:
            print("Estouro dos fogos de artifício")
            break
count_reg(10)


""" atividade 47 
Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre
1 e 50
"""
def identifica_par():
    for numero in range(1,51):
        if numero % 2 == 0:
            print(numero)
identifica_par()




""" atividade 48 
Faça um programa que calcule a soma entre todos os numeros impares que são multiplos
de 3 e que se encontram no intervalo de 1 até 500
"""
def identifica_impar():
    for numero in range(1, 501):
        if numero % 3 == 0:
            print(numero)
identifica_impar()


""" atividade 49 
Refaça o desafio 09 mostrando uma tabuada so que agora utilizando um laço for
"""
numero = int(input('Digite um número para saber a sua tabuada: '))
def calculadora(num):
    for i in range(0, 11):
        print(f'{num} x {i} = {i * num}')
calculadora(numero)



""" atividade 50 
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem
pares. se o valor digitado for impar, desconsidere-o
"""

num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))
num3 = int(input("Digite o número 3: "))
num4 = int(input("Digite o número 4: "))
num5 = int(input("Digite o número 5: "))
num6 = int(input("Digite o número 6: "))
numeros = [num1, num2, num3, num4, num5, num6]
def somando_lista():
    total = 0
    for num in numeros:
        if num % 2 == 0:
            total += num
    print(total)
somando_lista()