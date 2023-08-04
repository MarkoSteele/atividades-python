condicao = True
while condicao:
    sexo = input('Digite o seu sexo[M/F]: ').strip().upper()
    if sexo == 'M' or sexo == 'F':
        print('Muito bem, resposta correta.')
        condicao = False
