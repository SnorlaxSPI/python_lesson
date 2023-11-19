print(f'{"":=^33}')
print('Ler um número inteiro e mostrar ')
print(f'{"":=^33}')
print('na tela sucessor e antecessor')
print(f'{"":=^33}')

# Solicita ao usuário que digite um número inteiro
numero = int(input('Digite um número inteiro: '))

# Calcula o anteessor e o sucessor do número digitado
antecessor = numero - 1
sucessor = numero + 1

# Exibe os resultados na tela
print('Antecessor:', antecessor)
print('Número digitado', numero)
print('Sucessor:', sucessor)
