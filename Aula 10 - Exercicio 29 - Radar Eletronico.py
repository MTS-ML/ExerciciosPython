velocidade = int(input(f'Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'MULTADO! \nVocê excedeu o limite permitido de velocidade que é 80km/h')
    print(f'Multa de R${multa}.')
else:
    print("Está dentro do limite de velocidade, dirija com segurança e tenha um bom dia!")
