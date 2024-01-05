#Da forma que o Guanabara fez, na hora do print(f'O número digitado foi {tupla[num]') se digitar um valor maior que 20
#de cara, ele já pula a interação e procura dentro da tupla o n (no caso se colocar 21), então da erro, porque so vai até
#o índice 20. Melhor forma de resolução que achei foi colocando um while True, dentro de outro while True.

tupla = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
        'SEIS',  'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE',
        'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE',
        'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Número inválido.', end=' ')
    print(f'O número digitado foi \033[34m{tupla[num]}\033[m\n') # Mostra o índice da tupla e pula uma linha para mostrar
# o Deseja continuar? [S/N].
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('~' * 30)
print('PROGRAMA ENCERRADO')
