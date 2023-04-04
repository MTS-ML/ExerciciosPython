a = str(input('Digite o primeiro valor: '))
b = str(input('Digite o segundo valor: '))
c = str(input('Digite o terceiro valor: '))
#Verificando quem é o menor
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
#Verificando quem é o maior
maior = a
if c > b and c > a:
    maior = c
if b > c and b > a:
    maior = a
print(f'A maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')