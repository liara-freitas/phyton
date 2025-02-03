def imprimir_triangulo(n):
  if n > 0:
    imprimir_triangulo(n-1)
    print('*' * n)

linhas = int(input("Digite o número de linhas para o triângulo: "))
if linhas <=0:
  print("Número de linhas deve ser positivo")
else:
  imprimir_triangulo(linhas)