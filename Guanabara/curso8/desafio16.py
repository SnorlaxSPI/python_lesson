# Cria um programa que leia um número Real qualquer
# pelo teclado e mostre na tela sua porção inteira
import math

numero_real = float(input('Digite um número: ')) 

#porcao_inteira = round(numero_real)
porcao_inteira = math.trunc(numero_real)

print(f'A porção inteira de {numero_real} é {porcao_inteira}')