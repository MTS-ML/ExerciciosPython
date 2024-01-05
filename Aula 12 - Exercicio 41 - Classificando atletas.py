from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Você tem {idade} anos.\nCategoria: MIRIM')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos.\nCategoria:INFANTIL')
elif idade > 14 and idade <=19:
    print(f'Você tem {idade} anos.\nCategoria: JÚNIOR')
elif idade > 19 and idade <= 25:
    print(f'Você tem {idade} anos.\nCategoria: SÊNIOR')
else:
    print(f'Você tem {idade} anos.\nCategoria: MASTER')
