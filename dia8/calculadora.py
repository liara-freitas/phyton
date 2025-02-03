def somar(a, b):
  return a + b

def subtrair (a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir (a, b):
  if b !=0:
    return a/b
  else:
    return "Erro: Divisão por zero!"
  
numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /):")

if operacao == '+':
    resultado = somar(numero1, numero2)
elif operacao == '-':
  resultado = subtrair(numero1, numero2)
elif operacao == '*':
    resultado = multiplicar(numero1, numero2)
elif operacao == '/':
    resultado = dividir(numero1, numero2)
else: resultado = "Operação inválida!"

print("Resultado: ", resultado)