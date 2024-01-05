print(f'{"-=" * 7}\nGERADOR DE P.A.\n {"-=" * 7}')
primtermo = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A.: '))
contador = 1
while contador <= 10:
    print(f'{primtermo} ->', end=' ')
    primtermo += razao # Ele printa o primtermo + a razao.
    contador += 1 # Aqui é o limitador, começa em 1 e a cada laço, soma +1, até chegar a 10.
print('FIM')
