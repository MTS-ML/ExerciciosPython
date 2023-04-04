times = ('Corinthians', 'Palmeiras','Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
'Curitiba', 'Avaí', 'Ponte preta', 'Atlético-GO')
print(f'Lista de times do brasileirão: {times}\n')
print(f'Os 5 primeiros colocados são: {times[:5]}\n')
print(f'Os 4 últimos colocados são: {times[-4:]}\n')
print(f'Times em ordem alfabética: {sorted(times)}\n')
print(f'O Chapecoense está na {times.index("Chapecoense")}ª posição.\n')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.\n')
