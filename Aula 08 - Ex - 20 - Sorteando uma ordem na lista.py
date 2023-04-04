from random import shuffle
a1 = str(input(f'Primeiro aluno(a): '))
a2 = str(input(f'Segundo aluno(a): '))
a3 = str(input(f'Terceiro aluno(a): '))
a4 = str(input(f'Quarto aluno(a): '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem do primeiro ao último é: {lista}')
