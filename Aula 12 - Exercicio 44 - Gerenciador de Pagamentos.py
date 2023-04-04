preco = float(input('Qual o preço do produto a ser comprado? R$'))
print('''[1] - Á VISTA DINHEIRO/CHEQUE
[2] - Á VISTA NO CARTÃO DE DÉBITO
[3] - EM ATÉ 2X NO CARTÃO DE CRÉDITO
[4] - EM 3X OU MAIS NO CARTÃO DE CRÉDITO''')
opcao = int(input('ESCOLHA SUA OPÇÃO DE PAGAMENTO: '))
if opcao == 1: # 10% de desconto
    print(f'Pagamento a vista no dinheiro/cheque tem 10% de desconto(R${preco * 0.1})', end=' ')
    print(f'e a compra fica em R${preco - (preco * 0.1)}')
elif opcao == 2: #5% de desconto
    print(f'Pagamento a vista no cartão tem 5% de desconto(R${preco * 0.05})', end=' ')
    print(f'e a compra fica em R${preco - (preco * 0.05)}')
elif opcao == 3: #sem desconto ou juros e pergunta o número de parcelas
    parc = int(input(f'Quantas parcelas?'))
    if parc == 1:
        print(f'Sua compra será á vista no cartão de crédito, não tendo alteração no valor.', end=' ')
        print(f'Fica em R${preco}')
    elif parc == 2:
        print(f'Pagamento em 2x no cartão de crédito não tem desconto, compra sai em 2 parcelas de', end=' ')
        print(f'R${preco / parc}, totalizando R${preco}')
    else:
        print(f'Número de parcelas não se encaixa nessa forma de pagamento, favor escolher nova opção!')
elif opcao == 4: #20% de juros e pergunta o número de parcelas
    parc2 = int(input(f'Quantas parcelas? '))
    print(f'Compra parcelada em {parc2}x no cartão é acrescentado 20% de juros(R${preco * 0.2}).', end=' ')
    print(f'Ficando {parc2} parcelas de R${preco / parc2 + (preco * 0.2) / parc2:.2f}, totalizando R${preco + (preco * 0.2)}')
else:
    print('Opção de pagamento inválida. Favor tente novamente.')