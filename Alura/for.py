print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativa = 3
rodada = 1

for rodada in range(1, total_de_tentativa + 1):
  #print("Tentativa", rodada, "de", total_de_tentativa)
  print("Tentativa {} de {}". format(rodada, total_de_tentativa))
  chute_str = input("Digite o seu número entre 1 e 100: ")
  print("Você digitou ", chute_str)
  chute = int(chute_str)
  
  if (chute < 1 or chute > 100):
    print("Você deve digitar o número entre 1 e 100!")
    continue

  acertou = chute == numero_secreto
  maior = chute > numero_secreto
  menor = chute < numero_secreto

  if (acertou):
    print("Você acertou")
    break
  else:
    if(maior):
      print("Você errou! O seu chute foi maior que o número secreto.")
    elif(menor):
      print("Você errou! O seu chute foi menor do que o número secreto.")
    
  rodada = rodada + 1
  
print("Fim do jogo")