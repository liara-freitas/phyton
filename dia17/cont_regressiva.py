def contagem_regressiva(n):
  if n <=0:
    print("Contagem finalizada!")
  else:
    print(n)
    contagem_regressiva(n-1)

numero = int(input("Digite um número para iniciar a contagem regressiva: "))
contagem_regressiva(numero)