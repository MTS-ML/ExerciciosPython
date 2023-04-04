from math import trunc
n = float(input(f'Digite um número real: '))
print(f'A porção inteira do número digitado é: {trunc(n)}')
print(f'A porção inteira do número digitado é: {n:.0f}') # ARREDONDA PARA CIMA
print(f'A porção inteira do número digitado é: {int(n)}')

