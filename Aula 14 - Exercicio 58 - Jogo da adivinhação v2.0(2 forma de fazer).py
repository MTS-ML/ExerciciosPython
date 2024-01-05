from random import randint
pc = randint(1, 3)
acertou = False
tentativas = 0
while not acertou:
    user = int(input('Qual o seu palpite? '))
    tentativas += 1
    if user == pc:
        acertou = True
    else:
        if user < pc:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
print(f'Acertou na {tentativas}ª tentativas. Parabéns!')
