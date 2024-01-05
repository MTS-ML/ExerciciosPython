tot18 = totH = totM20 = 0

print(f'{"-" * 20}\nCADASTRE UMA PESSOA\n{"-" * 20}')
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo in 'M':
        totH += 1
    if sexo in 'F' and idade < 20:
        totM20 += 1
    print('Usuário cadastrado')

    print(f'{"~" * 20}')

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print(f'{"~" * 20}')
    if opcao in 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Temos {totH} homen(s) cadastrado(s)')
print(f'Temos {totM20} mulhere(s) com menos de 20 anos.')
