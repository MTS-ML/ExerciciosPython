dist = int(input('Qual a distância da sua viagem?  '))
print(f'Você está prestes a começar uma viagem de {dist}km.')
preco = dist * 0.5 #PREÇO PARA VIAGENS ATÉ 200KM
preco2 = dist * 0.45 #PREÇO PARA VIAGENS ACIMA DE 200KM.
if dist > 200:
    print(f'O preço da passagem é R${preco2}')
else:
    print(f'O preço da passagem é R${preco}')
