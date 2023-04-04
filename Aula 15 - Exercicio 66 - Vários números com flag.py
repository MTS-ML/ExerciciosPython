acumulador = contador = 0
while True:
    n = int(input('Digite um número. [999] para parar: '))
    if n == 999:
        break
    contador += 1
    acumulador += n
print(f'A soma dos {contador} valores foi {acumulador}')
print('Fim do programa')
