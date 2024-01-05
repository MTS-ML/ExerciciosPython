n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print(f' A soma entre \033[36m{n1}\033[m e \033[32m{n2}\033[m vale \033[4;31m{n1 + n2}\033[m.')

n1 = bool(input('Digite um valor: '))
print(f'\033[4;30;46m{n1}\033[m')

palavra = input('Digite algo: ')

print(f'''O tipo promitivo desse valor é {type(palavra)}')
Só tem espaços? {palavra.isspace()}')
É um número: {palavra.isnumeric()}')
É alfabético? {palavra.isalpha()}')
É alfnumérico? {palavra.isalnum()}')
Está em maiúsculas? {palavra.isupper()}
Está em minúsculas? {palavra.islower()}
Está capitalizada? {palavra.istitle()}''')
