larg = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))

# Cálculo da área
area= larg * alt

print(f'Sua parede tem dimensão de {larg} x {alt} e sua área é de {area}m²')

# Cálculo da quantidade de tinta
tinta= area/2

print(f'Para pintar essa parede, você precisará de {tinta}l!')