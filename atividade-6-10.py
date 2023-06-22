""" Desafio 6 - faça um programa que recebe um valor inteiro, e imprima ele,
o valor anterior e o valor sucessor"""

numero = input('Digite um número inteiro: ')
numero_int = int(numero)
antecessor = numero_int - 1
sucessor = numero_int + 1
print('Este é o valor digitado: {}, o seu antecessor é: {} e o seu sucessor é {}'.format(numero_int, antecessor, sucessor))


""" Desafio 7 - Fazer uma média aritmética entre dois valores passados pelo usuário"""

primeira_nota = float(input('Digite a sua primeira nota: '))
segunda_nota = float(input('Digite a sua segunda nota: '))
resultado = ((primeira_nota + segunda_nota) / 2)
print(f'A média entre as suas duas notas fornecidas é {resultado:.1f}')


""" Desafio 8 -  Escreva um programa que leia um valor em metros e o
 exiba convertido em centimetros e milimetros """


valor_metros = int(input('DIgite um valor em metros: '))
valor_centimetro = valor_metros * 10
valor_milimetro =  valor_metros * 100
print('O valor digitado é {}m, o valor convertido para centimetros e milimetros respectivamente é: {}cm, {}mm.'.format(valor_metros, valor_centimetro, valor_milimetro))

""" Desafio 9 - receba um valor inteiro do usuário e imprima a tabuada deste valor """

valor = int(input('Digite um número inteiro para ver a sua tabuada: '))
contador = 0
print('-----------')
while contador <= 10:
    print(f'{valor} x {contador} = {valor * contador}')
    contador += 1
print('-----------') 


""" Desafio 10 - Receba um valor em float (dinheiro), e o converta para dolar e libras """

reais = float(input('Quanto dinheiro você tem na carteira: R$'))

print(f'Com este valor disponível na carteira você consegue comprar US${reais * 0.21:.2f} ou GBP{reais * 0.16:.2f}')
    