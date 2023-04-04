num = int(input(f'Digite um número inteiro: '))
total = 0
for l in range(1, num + 1):
    if num % l == 0:
        total += 1
        print(f'\033[36m', end=' ')
    else:
        print(f'\033[31m', end=' ')
    print(l, end=' ')
print(f'\n\033[mO número {num} foi divisível {total} vezes.')
if total == 2:
    print(f'\033[34mÉ\033[m um número PRIMO!')
else:
    print('\033[31mNÃO\033[m é um número PRIMO!')
