c_o = float(input(f'Valor do ângulo do cateto oposto: '))
c_a = float(input(f'Valor do ângulo do cateto adjacente: '))
hip = (c_o ** 2 + c_a ** 2) ** (1/2) # HIPOTENUSA É A RAIZ QUADRADA DA SOMA DOS QUADRADOS DOS CATETOS
print(f'O cumprimento da hipotenusa é {hip:.2f}°')

from math import hypot
c_o = float(input(f'Cumprimento do cateto oposto: '))
c_a = float(input(f'Cumprimento do cateto adjacente: '))
print(f'Cumprimento da hipotenusa é {hypot(c_o, c_a):.2f}°')
