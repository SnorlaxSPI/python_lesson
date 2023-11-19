#print("*********************************")
#print("Bem vindo no jogo de adivinhação!")
#print("*********************************")

print(f'{"":*^33}')
print('Bem vindo no jogo de adivinhação!')
print(f'{"":*^33}')

numero_secreto = 42

chute_str = input("Digite o seu número: ")

chute = int(chute_str)

print("Você digitou ", chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (numero_secreto == chute):
  print("Você acertou")
else:
  if(maior):
    print("Você errou! O seu chute foi maior que o número secreto.")
  elif(menor):
    print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo")