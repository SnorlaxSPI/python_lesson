from math import radians, sin, cos, tan

angulo_graus = float(input('Digite um valor do ângulo em graus: '))

angulo_radianos = radians(angulo_graus)

seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print(f'Ângulo: {angulo_graus} graus')
print(f'Seno: {seno:.4f}')
print(f'Cosseno: {cosseno:.4f}')
print(f'Tangente: {tangente:.4f}')
