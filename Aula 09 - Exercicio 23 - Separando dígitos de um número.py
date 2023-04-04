numero = int(input('Digite um número inteiro: '))
print(f'Analisando o número {numero}...')
u = numero // 1 % 10
print(f'Unidade: {u}')
d = numero // 10 % 10
print(f'Dezena: {d}')
c = numero // 100 % 10
print(f'Centena: {c}')
m = numero // 1000 % 10
print(f'Milhar: {m}')
