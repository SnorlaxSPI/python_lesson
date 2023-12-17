print(f'{"":=^33}')
print('Escreva um prograna que leia um')
print(f'{"":=^33}')
print('valor em metros e converta em cm')
print(f'{"":=^33}')

#metros = int(input('Digite um valor em metros: '))
#converter = (metros * 100)
#print(f'O valor de metros em centímetros é: {converter} cm')

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000

print(f'A medida de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm')

