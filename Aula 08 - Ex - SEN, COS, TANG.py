from math import cos, sin, tan, radians
ang = float(input(f'Digite o valor em graus de um ângulo: '))
seno = (sin(radians(ang)))
cosseno = (cos(radians(ang)))
tangente = (tan(radians(ang)))
print(f'O ângulo de {ang}º tem o seno {seno:.2f}.\nO ângulo de {ang}º tem o cosseno {cosseno:.2f}.\nO ângulo de {ang}º tem a tangente de {tangente:.2f}.')
