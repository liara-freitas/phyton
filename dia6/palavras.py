texto = input("Digite um texto:").lower()
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
print ("\nContagem de palavras:")
for palavra, contagem in contagem_palavras.items():
    print(f"A plavra '{palavra}' aparece {contagem} vez(es).")
