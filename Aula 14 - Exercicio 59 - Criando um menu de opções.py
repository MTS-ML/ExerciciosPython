from time import sleep
maior = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
user = ''
while user != 5:
    print(f'''[1] SOMAR\n[2] MÚLTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\n{"=" * 40}''')
    user = int(input('>>>>> Qual a sua opção? '))
    if user == 1:
        print(f'A soma entre {n1} e {n2} é = {n1 + n2}')
    elif user == 2:
        print(f'A múltiplicação entre {n1} e {n2} é = {n1 * n2}')
    elif user == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior número entre {n1} e {n2} é o {maior}')
        elif n2 > n1:
            maior = n2
            print(f'O maior número entre {n1} e {n2} é o {maior}')
        else:
            print('Números iguais')
    elif user == 4:
        print('Digite os novos números')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif user == 5:
        print('Saindo do programa!')
    else:
        print('Opção inválida. Tente novamente!')
    sleep(1)
    print(f'{"=" * 40}')
    print('FIM do programa!')
