r1 = float(input('Digite o primeiro segmento: '))
r2= float(input('Digite o segundo segmento: '))
r3= float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('OS segmentos acima podem formar um triângulo.')
else:
    print(f'Os segmentos acima não formam um triângulo.')
#PARA FORMAR UM TRIÂNGULO, NESSE EXERCÍCIO O TERCEIRO SEGMENTO TEM QUE SER MENOR QUE A SOMA DOS OUTROS 2
