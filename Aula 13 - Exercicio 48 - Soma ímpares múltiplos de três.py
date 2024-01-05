soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # Contador normalmente conta +1 "é mais um que eu achei". Normalmente soma 1.
        soma += c # O acumulador normalmente vai acumulando OS VALORES. Normalmente soma o VALOR.
print(f'Os números ímpares múltiplos de três no intervalo de 1 até 500 são: {c}', end='')
print(f'\nA soma dos {cont} valores solicitados é: {soma}')


'''for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')'''
