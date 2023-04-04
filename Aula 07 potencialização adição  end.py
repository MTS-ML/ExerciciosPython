#nome = str(input('Qual o seu nome? '))
#print(f'Prazer em te conhecer {nome:10}!')
#print(f'Prazer em te conhecer {nome:>10}!') # Alinhamento a direita
#print(f'Prazer em te conhecer {nome:<10}!') #Alinhamento a esquerda
#print(f'Prazer em te conhecer {nome:^10}!') #Deixa centralizado
#print(f'Prazer em te conhecer {nome:=^10}!')
#SE O NOME TIVER MAIS QUE O NÚMERO DE ESPAÇOS DESEJADOS, NÃO ACONTECE NADA

x = int(input('Digite um número inteiro: '))
y = int(input('Digite outro número inteiro: '))
p = x ** y
m = x * y
d = x / y
a = x + y
s = x - y
divint = x // y
restdiv = x % y
print(f'O resultado da potencialização de {x} e {y} é: {p}.', end = "")
print(f' O resultado da múltiplicação de {x} e {y} é: {m}', end = '')
print(f' O resultado da divisão de {x} e {y} é : {d:.2f}')
print(f'O resultado da adição de {x} e {y} é: {a}')
print(f'O resultado da subtração de {x} e {y} é: {s}')
print(f' O resultado da divisão inteira de {x} e {y} é: {divint}')
print(f'O resultado do resto da divisão de {x} e {y} é: {restdiv}')
