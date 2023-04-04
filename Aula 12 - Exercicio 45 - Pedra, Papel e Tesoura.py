from random import randint
print(f'{"-" *10}Jogando PEDRA, PAPEL e TESOURA!{"-" * 10}')
print('Suas opções:\n[1] PEDRA \n[2] PAPEL \n[3] TESOURA')
user = int(input('Escolha sua jogada: '))
print(f'\033[4;36m{"-=" * 10} \033[m')
pc = randint(1, 3)
if user == 1 and pc == 1:                       # PEDRA VS PEDRA
    print(f'USUÁRIO: \033[36mPEDRA\033[m \nCOMPUTADOR: \033[35mPEDRA\033[m \n\033[33mEMPATE!\033[m')
elif user == 1 and pc == 2:                     # PEDRA VS PAPEL
    print('USUÁRIO: \033[36mPEDRA\033[m \nCOMPUTADOR: \033[35mPAPEL\033[m \n\033[31mCOMPUTADOR VENCE!\033[m')
elif user == 1 and pc == 3:                     # PEDRA VS TESOURA
    print('USUÁRIO: \033[36mPEDRA\033[m \nCOMPUTADOR: \033[35mTESOURA\033[m \n\033[32mUSUÁRIO VENCE!\033[m')
elif user == 2 and pc == 1:                     # PAPEL VS PEDRA
    print('USUÁRIO: \033[36mPAPEL\033[m \nCOMPUTADOR: \033[35mPEDRA\033[m \n\033[32mUSUÁRIO VENCE!\033[m')
elif user == 2 and pc == 2:                     # PAPEL VS PAPEL
    print('USUÁRIO: \033[36mPAPEL\033[m \nCOMPUTADOR: \033[35mPAPEL\033[m \n\033[33mEMPATE!\033[m')
elif user == 2 and pc == 3:                     # PAPEL VS TESOURA
    print('USUÁRIO: \033[36mPAPEL\033[m \nCOMPUTADOR: \033[35mTESOURA\033[m \n\033[31mCOMPUTADOR VENCE!\033[m')
elif user == 3 and pc == 1:                     # TESOURA VS PEDRA
    print('USUÁRIO: \033[36mTESOURA\033[m \nCOMPUTADOR: \033[35mPEDRA\033[m \n\033[31mCOMPUTADOR VENCE!\033[m')
elif user == 3 and pc == 2:                     # TESOURA VS PAPEL
    print('USUÁRIO: \033[36mTESOURA\033[m \nCOMPUTADOR: \033[35mPAPEL\033[m \n\033[32mUSUÁRIO VENCE!\033[m')
elif user == 3 and pc == 3:                     # TESOURA VS TESOURA
    print('USUÁRIO: \033[36mTESOURA\033[m \nCOMPUTADOR: \033[35mTESOURA\033[m \n\033[33mEMPATE!\033[m')
else:                                           # JOGADA INVÁLIDA
    print('Escolha inválida. Tente novamente')
print(f'\033[4;36m{"-=" * 10}\033[m')
