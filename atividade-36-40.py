""" Desafio 36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor, o salário do comprador e em quantos anos ele vai pagar.
 adicionando uma restrição para a aprovação(desafio pessoal): O dinheiro dedicado para o pagamento de 150% a cima do valor da casa deverá ser
 alcançado até o final do período em meses fornecido, porém so poderá ser obtido 30% do salario a cada mês
 """

try:

    valor_casa = float(input('Digite o valor da casa desejada: R$'))
    valor_aprovacao = valor_casa * 1.5
    salario = float(input('Digite o seu salário: R$'))
    salario_30 = (salario * 0.3)
    ano = int(input('Digite em quantos anos completos que você deseja pagar: '))
    meses = ano * 12
    montante = salario_30 * meses

    if montante >= valor_aprovacao:
        print(f'Você preenche o requisito necessário para a aprovação do empréstimo, logo será disponibilizado o valor para a aquisição da casa, sendo contabilizado a partir de hoje {meses} faturas no valor de R${salario_30:.2f}')
    else:
        print('Infelizmente você não preencheu o requisito necessário, tente novamente daqui 12 meses')
except:
    print('Por gentileza digite valores válidos!')




""" Desafio 37 -  Escreva um programa que leia um número inteiro e peça para que
o usuário escolha qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
from time import sleep
delay = 1
high_delay = 2

numero = int(input('Digite um número inteiro: '))
sleep(delay)
print('1 - Converter para base binária')
print('2 - Converter para base Octal')
print('3 - Converter para base hexadecimal')
opcao = int(input('Escolha uma das opções acima colocando o número da sua opção: '))
print('Convertendo o número digitado....')
sleep(high_delay)
if opcao == 1:
    num_bin = bin(numero)
    print(f"O número binário de {numero} é: {num_bin[2::]}")
elif opcao == 2:
    num_oct = oct(numero)
    print(f"O número binário de {numero} é: {num_oct[2::]}")
elif opcao == 3:
    num_hex = hex(numero)
    print(f"O número binário de {numero} é: {num_hex[2::]}")
else:
    print('Opção inválida')



""" Desafio 38 - Escreva um programa que leia dois números inteiros e compare-os
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais """

numero_1 = int(input('Digite o primeiro número: ')) 
numero_2 = int(input('Digite o segundo número: ')) 

if numero_1 == numero_2:
    print(f'O número {numero_2} é igual ao número {numero_1}.')
elif numero_1 > numero_2:
    print(f'O número {numero_1} é maior que o número {numero_2}.')
else:
    print(f'Os números informados são iguais.')


""" Desafio 39 -  Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar
se é a hora de se alistar ou se já passou do tempo de alistamento, o seu programa
deverá mostrar o tempo que falta ou que passou do prazo.
"""
data_nascimento = int(input('Digite a sua ano de nascimento: '))
ano_atual = 2023
idade = ano_atual - data_nascimento
if idade == 18:
    print('Você está no seu ano de alistamento militar, compareça ao quartel mais proximo.')
elif idade > 18:
    print(f'Você já passou do ano de alistamento, caso não tenha comparecido no ano {2023 - (idade - 18)}, entre em contato urgentemente com o serviço militar')
else:
    print(f'Você ainda não completou a idade necessária para o alistamento, daqui {18 - idade}  anos, compareça ao quartel mais próximo.')


""" Desafio 40 -  Crie um programa que leia duas notas de um aluno e calcule a
sua média mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5: Reprovado
- Média entre 5 e 6.9: Recuperação
- Média 7 ou superior: Aprovado """

nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))

media = (nota_1 + nota_2) / 2

if media < 5:
    print('Reprovado')
elif media >= 5 and media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')