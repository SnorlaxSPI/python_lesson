import math

print(f'{"":=^33}')
print('Leia um número e mostre seu dobro ')
print(f'{"":=^33}')
print('triplo e sua raiz quadrada')
print(f'{"":=^33}')

numero = int(input('Digite um numero inteiro: '))

dobro = numero*2
triplo = numero*3
#raiz_quadrada = numero ** 0.5
raiz_quadrada = math.sqrt(numero)

print(f'Dobro: {dobro}')
print(f'Triplo: {triplo}')
print(f'A raiz quadrada de {numero} é {raiz_quadrada:.2f}')
#print('A raiz de {} é igual a {}'.format(numero, raiz_quadrada))

