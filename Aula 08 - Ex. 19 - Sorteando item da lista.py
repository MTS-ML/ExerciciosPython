from random import choice
a1 = str(input(f'Digite o nome do primeiro aluno: '))
a2 = str(input(f'Digite o nome do segundo aluno: '))
a3 = str(input(f'Digite o nome do terceiro aluno: '))
a4 = str(input(f'Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
print(f'O aluno sorteado foi {choice(lista)}.')
