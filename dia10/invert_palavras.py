frase = input("Digite uma frase: ")
palavras = frase.split()
frase_invertida = " ".join(reversed(palavras))
print(f"Frase invertida: {frase_invertida}")