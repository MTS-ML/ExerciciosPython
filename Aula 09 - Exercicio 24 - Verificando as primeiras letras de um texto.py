cidade = str(input(f'Qual cidade você mora? ')).strip().upper()
#teste = cidade.split()
#print('SANTO' in teste[0])# Nesse exemplo, se escrever SantoS ele da True, então está errado.
print(cidade[:6] == 'SANTO' + ' ')
