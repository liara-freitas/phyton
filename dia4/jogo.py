import random

opcoes = ["pedra", "papel", "tesoura"]

usuario = input("Escolha pedra, papel ou tesoura: ").lower()
comp = random.choice(opcoes)

print (f"Você escolheu: {usuario}")
print (f"O computador escolheu: {comp}")

if usuario == comp:
    print("Empate!")
elif (usuario == "pedra" and comp == "tesoura") or \
     (usuario == "papel" and comp == "pedra") or \
     (usuario == "tesoura" and comp == "papel"):
  print("Você venceu!")
elif usuario in opcoes:
  print("Você perdeu!")
else:
   print("Escolha inválida!")