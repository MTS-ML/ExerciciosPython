from random import randint
print("""Sou o seu computador...
Acabei de pensar em um número entre 1 e 3.
Será que consegue adivinhar qual foi?""")
pc = randint(1, 3)
user = 0
tentativa = 0
pc = randint(1, 10)
while user != pc:
    print(pc)
    user = int(input(f'Qual é seu palpite? '))
    tentativa += 1
    if user < pc:
        print('Mais... Tente mais uma vez.')
    elif user > pc:
            print('Menos... Tente mais uma vez.')
print(f'Acertou! Na {tentativa}ª tentativa.')
