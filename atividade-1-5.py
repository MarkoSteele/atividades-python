""" Desafio 1 - criar um programa que escreva 'Olá, mundo' """

print('Olá, Mundo!')  # Olá, Mundo!


""" Desafio 2 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas """

nome = input('Digite o seu nome: ')
print(f'Olá seja bem-vindo(a) {nome}')  # Olá seja bem-vindo(a) Marcus


""" Desafio 3 - Faça um programa que some dois valores informados por um usuário """

num_1 = input('Digite um número inteiro: ')  # 3
num_2 = input('Digite um segundo número inteiro: ')  # 2
soma = int(num_1) + int(num_2)  # convertendo para inteiro (o valor vem em str do input)
print(f'A soma dos valores {num_1} e {num_2} é: {soma}')  # 5

""" Desafio 4 - Faça um programa que mostre valores sobre uma variável
(tipo, se possui espaços, é numero?, é alfabético?, é alfanumérico?,
está em maiusculas?, está em minusculas? está capitalizada?) """

variavel = input("Digite um número ou uma palavra qualquer: ")
print(type(variavel))  # Mostrando o tipo
print(f'A variavel é Numérica? {variavel.isnumeric()}')  # Verificando se a variavel possui um valor numérico (mesmo sendo str)
print(f'A variavel é Alfabética? {variavel.isalpha()}')
print(f'A variavel é Alfanumérico? {variavel.isalnum()}')
print(f'A variavel é Maiuscula? {variavel.isupper()}')
print(f'A variavel é Minuscula? {variavel.islower()}')  
print(f'A variavel só tem espaços? {variavel.isspace()}')  # verifica se só possui espaços na variável
print(f'A variavel está capitalizada? {variavel.istitle()}')


""" Desafio 5 - Receba um valor do usuário e imprima o dobro, o triplo e a raiz quadrada do valor"""

numero = input('Digite um valor numérico: ')
numero_int = int(numero)
print(f'O dobro do valor {numero_int} é: {numero_int * 2}')  
print(f'O triplo do valor {numero_int} é: {numero_int * 3}')
print(f'A raiz quadrada do valor {numero_int} é: {numero_int ** 0.5}')
