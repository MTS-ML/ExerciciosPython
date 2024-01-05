resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss': # Usar while in para que dê certo o [0].
    n = int(input('Digite um número: '))
    soma += n # É o acumulador (acumula valores),
    quant += 1 # É o contador (soma + 1),
    if quant == 1:
        #maior = menor = n
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você somou {quant} números. A média entra eles é {media:.2f}.')
print(f'O maior número é {maior} e o menor é {menor}.')
print('Acabou')
