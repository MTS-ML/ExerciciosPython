acumulador = 0
contador = 0
for l in range(1, 7):
    user = int(input(f'Digite o {l}º número: '))
    if user % 2 == 0:
        acumulador += user
        contador += 1
print(f'Foram digitados {contador} números pares.\nA soma deles é {acumulador}.')
