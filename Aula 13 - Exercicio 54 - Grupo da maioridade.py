from datetime import date
contadormaior = 0
contadormenor = 0
for pessoas in range(1, 8):
    ano = int(input(f'Em que ano a {pessoas}ª pessoa nasceu? '))
    idade = date.today().year - ano
    #print(f'Tem {idade} anos,', end=' ')
    if idade >= 18:
        contadormaior += 1
        #print('maior de idade.')
    else:
        contadormenor += 1
        #print('menor de idade.')
print(f'Temos {contadormaior} pessoa(s) maior(es) de idade.\n{contadormenor} pessoa(as) menor(es) de idade.')
