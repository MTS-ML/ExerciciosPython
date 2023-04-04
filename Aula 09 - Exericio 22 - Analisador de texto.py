nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome tem ao todos {len(nome) - nome.count(" ")} letras.') #CONTA QUANTOS ESPAÇOS TEM E OS REMOVE.
nome2 = nome.split()
print(f'Seu primeiro nome é {nome2[0]} e possui {len(nome2[0])} letras.')
