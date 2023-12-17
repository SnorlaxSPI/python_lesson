# Solicita ao usuário que digite as duas notas

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Calcula a média das duas notas
media = (nota1 + nota2) / 2

# Exibe a média na tela
print(f'A média entre {nota1:.1f} e {nota2:.1f} é: {media}')
