from datetime import date
nascimento = int(input('Qual seu ano de nascimento? '))
sexo = str(input('Com qual sexo você se identifica?(M/F) ')).strip().upper()
ano = date.today().year
idade = ano - nascimento
print(f'Quem nasceu em \033[35m{nascimento}\033[m, tem\033[35m {idade} anos\033[m em\033[35m {ano} \033[m.')
if sexo == 'F':
    print('O alistamento militar é obrigatório somente para homens.')
elif idade < 18:
    print(f'Você tem \033[4;36m{idade} anos\033[m, precisará se alistar daqui a {18 - idade} anos.', end=' ')
    print(f'Você precisará se alistar no ano de {ano + (18 - idade)}.')
elif idade > 18:
    print(f'Você tem \033[4;31m{idade} anos\033[m, deveria ter se alistado há {idade - 18} anos.', end=' ')
    print(f'Você tinha que ter se alistado em {ano - (idade - 18)}.')
else:
    print(f'Você tem \033[4m{idade} anos\033[m. Está no ano de \033[4;34malis\033[32mtamen\033[33mto!\033[m')
