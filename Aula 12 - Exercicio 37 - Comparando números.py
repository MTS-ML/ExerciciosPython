x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
if x > y:
    print(f'O primeiro valor digitado({x}) é maior que o segundo({y}).')
elif x < y:
    print(f'O segundo valor digitado({y}) é maior que o primeiro({x}).')
elif x == y:
    print('Não existe valor maior, os dois são iguais.')
else:
    print('Valor digitado incorreto, favor recomeçar!')
