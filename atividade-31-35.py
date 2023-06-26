""" Desafio 31 -  Escreva um programa que pergunte a distância de uma viagem
em KM. Calcule o preço da passagem, cobrando 0.5 reais por KM para viagens até
200KM e cobre 0.45 reais para viagens mais longas"""

""" distancia = int(input('Digite a distância da viagem: '))
if distancia <= 200:
    valor = distancia * 0.5
    print(f'O valor da viagem será de {valor}')
else:
    valor = distancia * 0.45
    print(f'O valor da viagem será de {valor}') """




""" Desafio 32 -  Faça um programa que leia um ano qualquer e mostre se ele é bissexto"""

""" ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('O ano digitado é bissexto.')
else:
    print('O ano digitado não é bisexto.') """


""" Desafio 33 -  Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor"""

try:
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    numero_3 = int(input('Digite o terceiro número: '))

    if numero_1 > numero_2 and numero_2 > numero_3:
        print(f'A ordem dos números é {numero_1}, {numero_2} e {numero_3}')
    elif numero_1 > numero_2 and numero_2 < numero_3:
        print(f'A ordem dos números é {numero_1}, {numero_3} e {numero_2}')
    elif numero_1 < numero_2 and numero_2 < numero_3:
        print(f'A ordem dos números é {numero_3}, {numero_2} e {numero_1}')
    elif numero_1 > numero_2 and numero_1 < numero_3:
        print(f'A ordem dos números é {numero_3}, {numero_1} e {numero_2}')
    elif numero_1 < numero_2 and numero_1 > numero_3:
        print(f'A ordem dos números é {numero_2}, {numero_1} e {numero_3}')
    elif numero_1 < numero_2 and numero_1 < numero_3:
        print(f'A ordem dos números é {numero_2}, {numero_3} e {numero_1}')
except:
    print('Digite valores válidos.')





""" Desafio 34 -  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
para salários superiores a 1250 reais. calcule um aumento de 10%, para os inferiores ou iguais o aumento é de 15%"""

salario = float(input('Digite o seu salário: '))

if salario > 1250:
    aumento = salario * 1.1
    print(f'O seu salário com o ajuste é {aumento:.2f}')
else:
    aumento = salario * 1.15
    print(f'O seu salário com o ajuste é {aumento:.2f}') 



""" Desafio 35 -  Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo"""

try:
    primeira_reta = int(input('Digite o valor da primeira reta: '))
    segunda_reta = int(input('Digite o valor da segunda reta: '))
    terceira_reta = int(input('Digite o valor da terceira reta: '))
    f_s_t = primeira_reta > segunda_reta and segunda_reta > terceira_reta
    f_t_s = primeira_reta > segunda_reta and segunda_reta < terceira_reta
    s_t_f = primeira_reta < segunda_reta and primeira_reta < terceira_reta
    s_f_t = primeira_reta < segunda_reta and primeira_reta > terceira_reta
    t_s_f = primeira_reta < segunda_reta and segunda_reta < terceira_reta
    t_f_s = primeira_reta > segunda_reta and primeira_reta < terceira_reta
    msg_positiva = 'Pode ser construído um triângulo'
    msg_negativa = 'Infelizmente as medidas não cumprem os requisitos mínimos para a construção de um triângulo'

    if f_s_t or f_t_s:
        soma = segunda_reta + terceira_reta
        if soma > primeira_reta:
            print(msg_positiva)
        else:
            print(msg_negativa)
    elif s_t_f or s_f_t:
        soma = terceira_reta + primeira_reta
        if soma > segunda_reta:
            print(msg_positiva)
        else:
            print(msg_negativa)
    elif t_s_f or t_f_s:
        soma = segunda_reta + primeira_reta
        if soma > terceira_reta:
            print(msg_positiva)
        else:
            print(msg_negativa)
except:
    print('Digite valores válidos.')
