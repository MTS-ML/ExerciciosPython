km = float(input(f'Quantos km foram percorridos? '))
dias = int(input(f'Por quantos dias o carro foi alugado? '))
pagamento = (0.15 * km) + (60 * dias)
print(f'Rodando \033[1;34m{km}km\033[m em \033[1;34m{dias}\033[m dias, o total a ser pago é \033[4;30;46mR${pagamento}\033[m')
