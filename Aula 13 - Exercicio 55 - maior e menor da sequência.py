maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
           maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso foi {maior}Kg.\nO menor peso peso foi {menor}Kg.')

#FIZ NOVAMENTE, ACRESCENTANDO O NOME DA PESSOA COM MAIOR PESO E O NOME DA PESSOA COM MENOR PESO.
'''maior = menor = 0
identidade = identidade2 = ''
for pessoas in range(1, 6):
    nome = str(input(f'Qual o nome da {pessoas}ª pessoa: ')).strip()
    peso = float(input(f'Qual o peso da {pessoas}ª pessoa: '))
    if pessoas == 1:
        identidade = identidade2 = nome
        maior = peso
        menor = peso
    else:
        if peso > maior:
            identidade = nome
            maior = peso
        elif peso < menor:
            identidade2 = nome
            menor = peso
print(f'O maior peso é de {identidade} e é {maior}Kg.')
print(f'O menor peso é dé {identidade2} e é {menor}Kg.')
print('Fim do programa')'''