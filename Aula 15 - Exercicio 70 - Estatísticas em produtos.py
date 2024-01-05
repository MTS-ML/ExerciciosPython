print(f'{"-" * 13}\nLOJA DO BRUXO\n{"-" * 13}')
compra = p_maior_1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço R$'))
    cont += 1
    compra += preco
    if preco > 1000:
        p_maior_1000 += 1
    if cont == 1 or preco < menor:
        barato = produto
        menor = preco
    print(f'{"-" * 20}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${compra:.2f}')
print(f'Temos {p_maior_1000 } produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')
