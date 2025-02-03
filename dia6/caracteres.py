frase = input("Digite uma frase: ").lower()
letras =  {}

for caractere in frase:
    if caractere.isalpha():
        if caractere in letras:
            letras[caractere] += 1
        else:
            letras[caractere] = 1

for letra, contagem in letras.items():
    print(f"A letra '{letra}' aparece {contagem} vez(es).")