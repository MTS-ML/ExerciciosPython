temp = float(input(f'Digite um número para ve-lo em ºC e em ºF: '))
fahrenheit = temp * 1.8 + 32
celsius = (temp - 32) / 1.8
print(f'A temperatura em Celsius é {celsius:.2f}ºC e em Fahrenheit é {fahrenheit:.2f}ºF')
