""" Exercício 51
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão
 """
num1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite o valor da razão da PA: '))
pa = []

def gerando_pa(n,r):
    pa.insert(0, n)
    for i in range(1,11):
        n += r
        pa.insert(i, n)
    print(pa)
gerando_pa(num1, razao)




""" Exercício 52
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

 """


entrada = int(input('Digite um número para saber se ele é primo: '))
def verifica_primo(i):
    resultado = 0
    for n in range(1, i + 1):
        if i % n == 0:
            print(f'\033[1;31m{n}' + '\033[0;0m')
            resultado += 1
    if resultado == 2:
        print(f'O número {entrada} é primo.')    
verifica_primo(entrada)


""" Exercício 53
Crie um programa que leia uma frase qualquer e diga se ela é considerada um palindromo,
desconsidere os espaços
 """
palavra = input('Digite uma palavra: ').replace(" ", "").lower()
palavra_invertida = palavra[::-1]
if palavra_invertida == palavra:
    print(f'A palavra {palavra} é sim um palíndromo')





""" Exercício 54
Crie um programa que leia o ano de nascimento de 6 pessoas, no final mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são de maior
"""

from datetime import datetime

data_atual = datetime.today()
ano_atual = data_atual.year

ano1 = int(input('Digite o ano de nascimento da primeira pessoa: '))
ano2 = int(input('Digite o ano de nascimento da segunda pessoa: '))
ano3 = int(input('Digite o ano de nascimento da terceira pessoa: '))
ano4 = int(input('Digite o ano de nascimento da quarta pessoa: '))
ano5 = int(input('Digite o ano de nascimento da quinta pessoa: '))
ano6 = int(input('Digite o ano de nascimento da sexta pessoa: '))

anos = [ano1, ano2, ano3, ano4, ano5, ano6]

for ano in anos:
    if ano_atual - ano >= 18:
        print(f'A pessoa que nasceu em {ano} é de maior.')
    else:
        print(f'A pessoa que nasceu em {ano} não é de maior.')

""" Exercício 55
Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e
menor peso lido
"""
peso1 = int(input('Digite o peso da primeira pessoa: '))
peso2 = int(input('Digite o peso da segunda pessoa: '))
peso3 = int(input('Digite o peso da terceira pessoa: '))
peso4 = int(input('Digite o peso da quarta pessoa: '))
peso5 = int(input('Digite o ano da quinta pessoa: '))

peso = [peso1, peso2, peso3, peso4, peso5]

menor_peso = min(peso)
maior_peso = max(peso)
print(f'Esse é o menor {menor_peso}')
print(f'Esse é o maior {maior_peso}')