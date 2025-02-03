import random 

numero_secreto = random.randint(1,100)
tentativas = 0

while True:
    palpite = int (input("Adivinhe o número (entre 1 e 100): "))
    tentativas +=1

    if palpite == numero_secreto:
        print((f"Parabés! Você acertou em {tentativas} tentativas"))
        break
    elif palpite < numero_secreto:
        print("O número é maior.")
    else:
        print ("O número é menor.")        