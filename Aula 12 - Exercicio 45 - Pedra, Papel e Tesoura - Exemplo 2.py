from random import randint
print(f'{"-" *10}PEDRA, PAPEL e TESOURA!{"-" * 10}')
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
user = int(input('Escolha sua jogada: '))
itens = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0, 2)
print(f'USUÁRIO: {itens[user]} \nCOMPUTADOR: {itens[pc]}')
if user == 0: # USUÁRIO ESCOLHE PEDRA
    if pc == 0: #PEDRA VS PEDRA
        print('EMPATE')
    elif pc == 1: # PEDRA VS PAPEL
        print('COMPUTADOR VENCE!')
    else: # PEDRA VS TESOURA
        print('USUÁRIO VENCE!')
elif user == 1: # USUÁRIO ESCOLHE PAPEL
    if pc == 0: # PAPEL VS PEDRA
        print('USUÁRIO VENCE!')
    elif pc == 1: # PAPEL VS PAPEL
        print('EMPATE')
    else: # PAPEL VS TESOURA
        print('COMPUTADOR VENCE!')
elif user == 2: # USUÁRIO ESCOLHE TESOURA
    if pc == 0: # TESOURA VS PEDRA
        print('COMPUTADOR VENCE!')
    elif pc == 1: #TESOURA VS PAPEL
        print('USUÁRIO VENCE!')
    else: # TESOURA VS TESOURA
        print('EMPATE')
else:
    print('Jogada inválida. Tente novamente!')
