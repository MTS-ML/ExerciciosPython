from random import randint
v = 0
print(f'{"-=" * 12}\nVAMOS JOGAR PAR OU ÍMPAR\n{"-=" * 12}')
while True:
 pc = randint(1, 4)
 print(pc)
 jogador = int(input('Digite um número: '))
 total = jogador + pc
 tipo = ' '
 while tipo not in 'PI':
 tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
 print(f'{"~" * 50}')
 print(f'Você jogou {jogador} e o computador {pc}. Total = {total}.', end=' ')
 if tipo == 'P':
 if total % 2 == 0:
 print('Deu PAR.')
 print(f'\nVocê VENCEU!')
 print('Vamos jogar novamente...')
 v += 1
 else:
 print('Deu ÍMPAR.')
 print(f'\nVocê PERDEU!')
 break
 elif tipo == 'I':
 if total % 2 == 1:
 print('Deu ÍMPAR.')
 print('\nVocê VENCEU!')
 v += 1
 print('Vamos jogar novamente...')
 else:
 print('Deu PAR.')
 print(f'\nVocê PERDEU!')
 break
 print(f'{"~" * 50}')
print(f'{"-" * 20}')
print(f'GAME OVER!\nVocê venceu {v} vezes.')
