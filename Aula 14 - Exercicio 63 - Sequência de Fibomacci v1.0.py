print('-=' * 11)
print('Sequência de Fibonacci')
print('-=' * 11)
n = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
t3 = 0
seq = [0, 1]
contador = 2

while contador < n:
    t3 = t1 + t2
    seq.append(t3)
    t1 = t2
    t2 = t3
    contador += 1

if n == 0:
    seq = [0]
elif n == 1:
    seq = [0, 1]

print(f'Sequência: {seq}')

num = int(input("Digite um número inteiro: "))

if num in seq:
    print(f'O número {num} pertence à sequência de Fibonacci.')
else:
    print(f'O número {num} não pertence à sequência de Fibonacci.')

print('FIM')
