while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(f'{"-" * 33}')
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
    print(f'{"-" * 33}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
