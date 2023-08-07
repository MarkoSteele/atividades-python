""" Atividade 61 e 62
Leia o primeiro Termo e a razão de uma PA, Mostre os 10
primeiros termos usando uma estrutura While

Realize um upgrade perguntando se o usuário quer adicionar
mais alguns termos e caso ele não queira, encerre o programa
e antes disso mostre os termos da PA
"""
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termos = []
def cria_pa(a1, r):
    condicao = True
    an = a1
    contador = 0
    while contador <= 10:
        an += r
        print(an)
        contador += 1
        termos.append(an)
    while condicao:
        opcao = input('Deseja adicionar mais termos?').lower()
        if opcao == 's' or opcao == 'sim':
          resposta = input(f'Este é o ultimo termo {termos[-1]} e está é a razão {r}, logo o próximo termo seria {termos[-1] + r}, deseja adiciona-lo?').lower()
          if resposta == 's' or opcao == 'sim':
              termos.append(termos[-1] + r)
        else:
            print(termos)
            print('Obrigado por usar o nosso sistema!')
            break
cria_pa(primeiro_termo, razao)



""" Atividade 63 
Escreva um programa que leia um número inteiro qualquer e mostre na tela
os 6 primeiros números de uma sequencia fibonacci
"""
entrada = int(input('Digite um número: '))
qtd_termos = int(input('Digite a quantidade de termos desejados: '))
def sequencia_fibonacci(n):
    sequencia = []
    sequencia.append(n)
    sequencia.append(n)
    sequencia.append(n + n)
    while True:
        novo_num = round((sequencia[-1]) + (sequencia[-2]))
        sequencia.append(novo_num)
        if len(sequencia) == qtd_termos:
            break 
    print(sequencia)
sequencia_fibonacci(entrada)


""" Atividade 64 
Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que a
 condição de parada. No final, mostre quantos números foram digitados
 e qual foi a soma entre eles
 """

def le_num():
    lista_de_num = []
    while True:
        numero = int(input('Digite um número: '))
        if numero ==  999:
            print(f'O somatório é: {sum(lista_de_num)}')
            print(f'Você digitou {len(lista_de_num)} números,', lista_de_num)
            break
        lista_de_num.append(numero)
le_num()


""" Atividade 65 
Crie um programa que leia 5 números inteiros pelo teclado. No final da execução
, mostre a média entre todos os valores e qual foi o maior e o menor valor lido
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
"""

def gera_num():
    lista_de_numeros = []
    while True:
        numero = int(input('Digite um número: '))
        if len(lista_de_numeros) == 5 or len(lista_de_numeros) == 10:
            print(f'O maior número digitado é: {max(lista_de_numeros)}')
            print(f'O menor número digitado é: {min(lista_de_numeros)}')
            print(f'Você digitou {len(lista_de_numeros)} números,', lista_de_numeros)
            nova_resposta = input('Deseja continuar? ').lower()
            if nova_resposta == 'não' or nova_resposta == 'nao':
                break
        lista_de_numeros.append(numero)
        if len(lista_de_numeros) == 15:
            print('Programa encerrou')
            print(f'Esses foram os números digitados {lista_de_numeros}')
            break
            
gera_num()