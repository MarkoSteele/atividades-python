""" Desafio 11 - Pegar dois valores (largura e altura) e realizar o calculo da area deles """

largura = float(input('Digite o valor da Largura: '))
altura = float(input('Digite o valor da Altura: '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura} x {altura} e a sua área é: {area}m\u00b2')
print(f'Para pintar essa parede, será necessário {area/2} Litros')


""" Desafio 12 - Pegar o valor do produto com o usuário e realizar o desconto de 5% nele """

produto = float(input('Digite o valor do produto: R$'))
desconto = produto * 0.95
print(f'O valor do produto era {produto} e com o desconto de 5% vai custar R${desconto}') 

""" Desafio 13 - Pegar o valor do salario com o usuário e realizar um aumento de 15% nele """

salario = float(input('Digite o valor do produto: R$'))
aumento = salario * 1.15
print(f'O valor do salário era {salario} e com o aumento de 15% é R${round(aumento):.2f}') 


""" Desafio 14 - Pegar o valor da temperatura com o usuário e realize a conversão dele para
°F e K"""

temperatura_c = float(input("Digite o valor da temperatura em °C: "))
temperatura_f = (temperatura_c * 9/5) + 32
temperatura_k = temperatura_c + 273,15

print(f'O valor da temperatura {temperatura_c}°C convertida em Fahrenheit é: {temperatura_f}°F e a sua conversão para Kelvin é: {temperatura_k}K')



""" Desafio 15 - Pegar a quantidade de dias que um carro foi alugado com o usuário e realize um calculo de custo sobre ele """

dias_alugados = int(input("Quantos dias o carro foi alugado? "))
km_rodado = float(input("Quantos Km o carro rodou? "))
resultado = (60 * dias_alugados) + (km_rodado * 0.15)
print(f'O valor a ser pago é {resultado}')