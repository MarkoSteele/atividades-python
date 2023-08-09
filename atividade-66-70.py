from time import sleep
delay = 1
""" Atividade 67  Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido qaudno o número solicitado for negativo
"""
num_in = int(input('Digite um número para saber a tabuada dele: '))
def calculadora(num):
    if num > 0:
        for i in range(1, 11):
            resultado = i * num
            print(f'{i} x {num} = {resultado}')
    else:
        print('Valor não suportado, a calculadora será encerrada, obrigado!')
calculadora(num_in)


""" Atividade 68 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas no final do jogo:
"""
import random


def jogo_impar_par():
    vitorias = 0
    condicao =  True
    while condicao:
        opcao = input('Você quer impar ou par? ').strip().lower()
        numero = int(input('Digite um número: '))
        numero_maquina = random.randint(1, 100)
        resultado = numero + numero_maquina
        if opcao == 'impar' or opcao == 'ímpar':
            if resultado % 2 == 0:
                print('Você perdeu!!')
                print(f'Você conseguiu {vitorias} vitórias consecutivas')
                condicao = False
            elif resultado % 2 == 1:
                print('Você ganhou!!')
                vitorias += 1
        if opcao == 'par':
            if resultado % 2 == 1:
                print('Você perdeu!!')
                print(f'Você conseguiu {vitorias} vitórias consecutivas')
                condicao = False
            elif resultado % 2 == 0:
                print('Você ganhou!!')
                vitorias += 1
jogo_impar_par()

""" Atividade 69 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada
o programa deverá perguintar se o usuário quer continuar ou não, no final mostre:

1. quantas pessoas possuem mais de 18 anos
2. quantos homens foram cadastrados
3. Quantas mulheres tem menos de 20 anos
"""

pessoas = []
contador_idade = 0
contador_homem = 0
contador_mulher = 0
while True:
    continuar = input('Você deseja adicionar mais alguém[S/N]? ').upper().strip()
    sleep(delay)
    if continuar == 'N' or continuar == 'Nao':
        print('Essas são as pessoas cadastradas')
        for pessoa in pessoas:
            print(pessoa)
            if pessoa['idade'] > 18:
                contador_idade += 1
            if pessoa['sexo'] == 'M':
                contador_homem += 1
            if pessoa['sexo'] == 'F' and pessoa['idade'] > 20:
                contador_mulher += 1
        print(f'Existem {contador_idade} pessoas maiores de 18 anos')
        print(f'Existem {contador_homem} homens cadastrados')
        print(f'Existem {contador_mulher} mulheres acima de 20 anos')
        break
    nova_pessoa_nome = input('Digite o nome: ')
    nova_pessoa_idade = int(input('Digite a idade: '))
    nova_pessoa_sexo = input('Digite o sexo[M/F]: ')
    pessoa = dict({'nome': nova_pessoa_nome, 'idade': nova_pessoa_idade, 'sexo': nova_pessoa_sexo})
    pessoas.append(pessoa)

""" Atividade 70 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final mostre:
1. Qual é o total gasto na compra
2. Quantos produtos custam mais de 1000 reais
3. Qual é o nome do produto mais barato
"""
produto_qtd = 0
produtos_lista = []
soma = 0
produtos = []
while True:
    continuar_produto = input('Você deseja adicionar mais algum produto[S/N]? ').upper().strip()
    sleep(delay)
    if continuar_produto == 'N' or continuar_produto == 'Nao':
        for produto in produtos:
            soma +=  produto['preço']
            produtos_lista.append(produto['preço']) 
            if produto['preço'] >= 1000:
                produto_qtd += 1
        menor_valor = min(produtos_lista)
        for produto in produtos: 
            if produto['preço'] == menor_valor:
                print(f'Este é o produto mais barato: ')
                print(produto['nome'])
       
        print(f'Esse é o total de valor em produtos =  {soma}')
        print(f'Existem {produto_qtd} produtos cadastrados que custa mais de 1000 reais.')
    nome_produto = input('Digite o nome: ')
    preco_valor = int(input('Digite o preço: '))
    produto = dict({'nome': nome_produto, 'preço': preco_valor})
    produtos.append(produto)