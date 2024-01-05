frase = str(input(f'Digite uma frase: ')).upper()
separado = frase.split()
junto = ''.join(separado)
inverso = junto[:: -1]
'''inverso = ''
for palavra in range(len(junto) -1, -1, -1):
    inverso += junto[palavra]'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')
