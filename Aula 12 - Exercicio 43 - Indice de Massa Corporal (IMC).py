peso = float(input('Qual o seu peso em Kg? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, você está \033[33mABAIXO\033[m DO PESO IDEAL!')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu IMC é {imc:.2f}, você está no \033[32mPESO IDEAL\033[m!')
elif imc >= 25 and imc <= 30:
    print(f'Seu IMC é {imc:.2f}, você está com \033[35mSOBREPESO\033[m!')
elif imc >= 30 and imc <= 40:
    print(f'Seu IMC é {imc:.2f}, você está \033[31mOBESO\033[m!')
else:
    print(f'Seu IMC é {imc:.2f}, você está com \033[4;31mOBESIDADE MÓRBIDA\033[m!')
