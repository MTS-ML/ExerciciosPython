from random import randint
pc = randint(0, 5)
user = int(input(f'Digite um número inteiro de 0 a 5: '))
if user == pc:
    print(f'PARABÉNS, você VENCEU! Escolheu o número {user} e acertou com o computador! :)')
else:
    print(f'Computador VENCEU, você escolheu o número {user} e o computador o número {pc} :(')
