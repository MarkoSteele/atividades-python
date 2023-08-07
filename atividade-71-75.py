""" atividade 56
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
do programa, mostre:

A média de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres tem menos de 20 anos
"""
pessoas = []
idades = []
    # Criação das pessoas
for pessoa in range(0, 5):
    pessoa = []
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo (M/F): ')
    pessoa.append(nome)
    pessoa.append(idade)
    pessoa.append(sexo)
    pessoas.append(pessoa)
    idades.append(pessoa[1])
print(pessoas)

    # Soma das idades 
print(f'A média de idade é {int(sum(idades))/ len(pessoas)}')
maior_idade = max(idades)
for p in pessoas:
    # Pessoa com maior idade
    if maior_idade == p[1]:
        print(f'Está é o nome da pessoa com a maior idade {p[0]}')
print('Mulheres: ')
for p in pessoas:
    # Verificando o genero 
    
    if p[2] == 'F':
        print(p[0])

""" atividade 57
Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores "M" ou "F", caso
esteja errado, peça a digitação novamente até que seja inserido um valor correto
"""

condicao = True
while condicao:
    sexo = input('Digite o seu sexo[M/F]: ').strip().upper()
    if sexo == 'M' or sexo == 'F':
        print('Muito bem, resposta correta.')
        condicao = False


""" atividade 58
Faça um desafio onde o computador vai gerar um numero entre 0 e 10, so que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer
"""
import random
contador = 0
numero_aleatorio = random.randint(1, 10)
c = True
while c:
    palpite = int(input('Digite o seu palpite: '))
    contador += 1
    if palpite == numero_aleatorio:
        print('Parabéns você acertou!!')
        print(f'Você realizou {contador} tentativas')
        c = False
    else:
        print('Infelizmente você errou o palpite, tente novamente.')
        print(f'Você realizou {contador} tentativas')



""" atividade 59
Crie um programa que leia dois valores e mostre um menu como ao lado na tela e seu programa
deverá realizar a operação solicitada em cada caso
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair
"""

from time import sleep
delay = 1
c2 = True

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um segundo valor: '))
while c2:

    sleep(delay)
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos Números")
    print("[5] Sair")
    escolha = int(input('Digite a opção desejada: '))
    match escolha:
        case 1:
            print(f'A soma entre os dois valores digitados é {valor1 + valor2}')
        case 2:
            print(f'A multiplicação entre os dois valores digitados é {valor1 * valor2}')
        case 3:

            valores = [valor1, valor2]
            print(f'Este é o maior valor entre os dois {max(valores)}')
        case 4:
            valor1 = int(input('Digite um novo valor: '))
            valor2 = int(input('Digite um segundo novo valor: '))
            print('Valores alterados')
        case 5:
            print('Volte sempre!!')
            c2 = False


""" atividade 60
Faça um programa que leia qualquer número e mostre o seu fatorial
"""
resultado = 1
fatorial = int(input('Digite um número para saber o seu valor fatorial: '))
while fatorial >= 1:
    resultado *= fatorial
    fatorial -= 1
print(f'O valor fatorial de {fatorial} é {resultado}') 
