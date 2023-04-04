nome = str(input(f'Digite seu nome completo: ')).upper()
print('Muito prazer em te conhecer!')
divnome = nome.split()
print(f'Seu primeiro nome é: {divnome[0]}')
print(f'Seu último nome é: {divnome[-1]}')
print(f'Seu penúltimo nome é: {divnome[-2]}')

