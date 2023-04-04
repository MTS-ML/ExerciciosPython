valor = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o seu salário? R$'))
tempo = int(input('Em quantos anos irá pagar o imóvel? '))
prestacao = valor / (tempo * 12)
print(f'Prestação \033[4;34mR${prestacao:.2f}\033[m')
if prestacao > (salario * 0.3): # Verifica se a prestação é maior que 30% do salário
    print(f'Empréstimo \033[31mNEGADO\033[m, prestação excedeu 30%(\033[36mR${salario * 0.3}\033[m) do seu salário.')
else: #Se a prestção NÃO for maior que 30% do salário, empréstimo concedido
    print(f'Empréstimo \033[1;32mCONCEDIDO\033[m, a prestação não ultrapassa 30%\033[36m(R${salario * 0.3})\033[m do seu salário.')
