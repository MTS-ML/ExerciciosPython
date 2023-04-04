print(f'{"-=" * 11} \nProgressão Aritmética\n{"-=" * 11}')
primtermo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da P.A.: '))
termo = primtermo
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{primtermo} ->', end=' ')
        primtermo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} temos mostrados.')
