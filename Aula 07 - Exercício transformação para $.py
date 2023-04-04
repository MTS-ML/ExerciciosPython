print('Transformação de valores!')
quant = float(input(f'Valor: '))
dolar = quant * 5.12
real = quant / 5.12
print(f'R${quant:.2f} em $ = ${dolar:.2f}')
print(f'U${quant:.2f} em R$ = R${real:.2f}')
