frase = str(input(f'Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find("A") + 1}.')
print(f'A última letra A apareceu na posição {frase.rfind("A") + 1}.')
print(len(frase) - frase.count(' ')) # Conta o número de letras sem o ' ' espaço.
