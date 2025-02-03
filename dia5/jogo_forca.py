
palavra_secreta = 'python'

letras_descobertas = ["_"] * len(palavra_secreta)

tentativas = 6

while tentativas > 0 and "_" in letras_descobertas:
    print("\nPalavra:", " ".join(letras_descobertas))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:  # Se a letra estiver na palavra secreta
        acertou = False
        for idx, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta and letras_descobertas[idx] == "_":
                letras_descobertas[idx] = letra
                acertou = True
        print("Boa, você acertou a letra!")
    else:  # Reduz tentativas apenas se a letra não estiver na palavra
        tentativas -= 1
        print(f"Errou! Você tem {tentativas} tentativas restantes.")

    if "_" not in letras_descobertas:
        print("\nParabéns! Você adivinhou a palavra:", palavra_secreta)
        break

if "_" in letras_descobertas:
    print("\nQue pena! Você não conseguiu adivinhar a palavra. A palavra era:", palavra_secreta)