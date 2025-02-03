import random


print ("Bem-vindo ao Jogo de Adivinhação!")
print ("1. Fácil (10 tentativas)")
print ("2. Médio (7 tentativas)")
print ("3. Difícil (5 tentativas)")



while True:
    dificuldade = input("Digite o número da dificuldade desejada:")
    if dificuldade == "1":
        tentativas_totais = 10
        break
    elif dificuldade == "2":
        tentativas_totais =7
        break
    elif dificuldade == "3":
        tentativas_totais = 5
        break
    else:
        print("Opcao inválida. Por favor, escolha 1, 2 ou 3.")


pontuacoes = []

while True:
      numero_secreto = random.randint(1, 100)
      tentativas_restantes = tentativas_totais
      tentativas = 0
      palpites_feitos = []

      print("\nEu pensei em um número entre 1 e 100.")

    #Loop de Tentativas
      while tentativas_restantes > 0:
        palpite = input("\nDigite o seu palpite:")

        #Verificando se o input é um  número válido
        if not palpite.isdigit():
            print("Entrada inválida! Pr favor, digite um número inteiro entre 1 e 100")  
            continue
        
        palpite = int(palpite)

        if palpite < 1 or palpite > 100:
            print("O número deve estar entre 1 e 100.")
            continue
        
        if palpite in palpites_feitos:
            print("Você já tentou esse número. Tente outro.")
            continue
        else:
            palpites_feitos.append(palpite)

        tentativas +=1
        tentativas_restantes -=1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            pontuacao = tentativas_restantes * 10 * int(dificuldade)
            pontuacoes.append(pontuacao)
            print(f"Sua pontuacao nesta partida: {pontuacao} pontos.")
            break
        elif palpite < numero_secreto:
            print("O número é maior que esse.")
        else:
            print("O númerio é menor que esse.")
        
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Palpites já feitos: {palpites_feitos}")
      
      else:
          print(f"\nQue pena! Você não conseguiu adivinhar. O número era {numero_secreto}.")
          pontuacoes.append(0)
    
    #Exibindo o Placar
      print("\nPlacar:")
      for idx, pontos in enumerate(pontuacoes, start =1):
          print(f"Partida {idx}: {pontos} pontos")

      jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
      if jogar_novamente != 's':
        print("Obrigado por jogar! Até a próxima.")
        break