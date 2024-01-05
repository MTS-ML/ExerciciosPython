print(f'''{"-=" * 12}
  10 TERMOS DE UMA P.A.
{"-=" * 12}''')
acumulador = 0
primtermo = int(input('Primeiro termo: ')) # Número que irá começar
razao = int(input('Razão: ')) # De quanto em quanto é a contagem
décimo = primtermo + (10 - 1) * razao # Fórmula matemática, seria o 1º termo, mais o termo desejado - 1 (no caso 10 - 1) vezes a razão.
for l in range(primtermo, décimo + razao, razao):
    print(f'{l} ->', end=' ')
print('ACABOU')
