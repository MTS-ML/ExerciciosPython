n1 = float(input(f'Digite a sua primeira nota: '))
n2 = float(input(f'Digite a sua segunda nota: '))
media = (n1 + n2) / 2
if media > 7:
    print(f'Sua média foi {media}. Parabéns, você foi \033[32mAPROVADO!\033[m \033[36m:)\033[m ')
elif media < 5:
    print(f'Sua média foi {media}. Infelizmente você foi \033[31mREPROVADO :(\033[m')
else: #Em outro exemplo, é possível fazer assim também: if 7 > media >=5: (média MENOR que 7 e media MAIOR ou IGUAL a 5). RECUPERAÇÃO
    print(f'Sua média foi {media}. Você está de \033[33mRECUPERAÇÃO!\033[m')
