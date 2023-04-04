'''preco = float(input(f'Preço do produto? R$'))
disc = preco * 0.05
npreco =preco - disc
print(f'Produto custa R${preco}. O valor do desconto é de R${disc}, então o preço total é', end =' ')
print(f'R${npreco:.2f}.')

salario = float(input(f'Digite seu salário R$'))
aumento = salario * 0.15
nsalario = salario + aumento
print(f'Com salário de R${salario} e aumento de R${aumento}(15%). O novo salário fica R${nsalario:.2f}')'''

preco = float(input(f'Preço do produto: R$'))
avista = preco - (preco * 10 / 100)
parcelado = preco + (preco * 0.08)
print(f'O preço do produto é R${preco}\nPagando a vista (10% de desconto) sai por R${avista:.2f}\nPagando parcelado (8% de acréscimo) sai por R${parcelado:.2f}')
