media = contador = cont_mulher = 0
h_maisvelho =''
for p in range(1, 5):
    print(f'{"-" * 5} {p}ª PESSOA {"-" * 5}')
    nome = str(input('Qual o seu nome: ')).strip().lower().capitalize()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()
    if p == 1 and sexo in 'Mm':
        h_maisvelho = nome
        maior = idade
    elif sexo in 'Mm' and idade > maior: # SEM ESSE AQUI, NÃO ESTAVA FUNCIONANADO CORRETAMENTE
            maior = idade
            h_maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        cont_mulher += 1
    media += idade
    contador += 1
print(f'{"-" * 40}')
print(f'A média de idade do grupo é de {media / contador:.2f} anos.')
print(f'O homem mais velho tem {maior} anos e se chama {h_maisvelho}.')
print(f'Ao todo são {cont_mulher} mulher(es) com menos de 20 anos.')
