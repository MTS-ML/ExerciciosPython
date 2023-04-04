salario = float(input(f'Qual o salário do funcionário? R$ '))
if salario <= 1250:
     print(f'Seu salário é de R${salario}, com aumento de 15%(R${salario * 0.15}), o funcionário passa a receber R${(salario * 0.15) + salario}')
else:
    print(f'Seu salário é de R${salario}, com aumento de 10%(R${salario * 0.1}), o funcionário passa a receber R${(salario * 0.1) + salario}')
