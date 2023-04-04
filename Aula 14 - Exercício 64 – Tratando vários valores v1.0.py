cont = soma = 0
n = int(input(f'Digite um número [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input(f'Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma deles é {soma}')
