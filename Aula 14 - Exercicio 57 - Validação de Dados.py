'''sexo = str(input(f'Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo != 'M' or sexo != 'F': # Dessa forma o código não funciona.
    sexo = str(input(f'Informação incorreta. Tente novamente.\nInforme o seu sexo: [M/F] ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso.')
print(f'Fim do programa.')'''
sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação incorreta. Informe o seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
