def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci (n - 2)

n = int(input("Digite a posição na sequência de Fibonacci:"))
if n < 0:
  print("Posição inválida. Insira um número não negativo")
else:
  resultado = fibonacci(n)
  print(f"O {n} número da sequência de Fibonacci é {resultado}")