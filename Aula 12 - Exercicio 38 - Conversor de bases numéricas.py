num = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
user = int(input('Sua opção: '))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)
if user == 1:
    print(f'O número {num} em BINÁRIO é: \033[4;34;40m{binario[2:]}\033[m') # Aparece 0b no Python para indicar que é BINÁRIO.
elif user == 2:
    print(f'O número {num} em OCTAL é: \033[4;34;40m{octal}\033[m')# Aparece 0o para no Python para indicar que é OCTAL.
elif user == 3:
    print(f'O número {num} em HEXADECIMAL é: \033[4;34;40m{hexadecimal[2:]}\033[m') # Aparece 0x no Python, para indicar que é HEXADECIMAL.
else:
    print(f'\033[31mOpção inválida!\033[m')
