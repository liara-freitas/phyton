def calculadora():
  try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input ("Digite o operador (+, -, *, /): ")

    if operador == '+':
      resultado = num1 + num2
    elif operador == '-':
      resultado = num1 - num2
    elif operador == '*':
      resultado = num1 * num2
    elif operador == '/':
      resultado  = num1 / num2
    else:
      raise ValueError("Operador inválido.")
  except ValueError as ve:
    print(f"Erro de valor: {ve}")
  except ZeroDivisionError:
    print("Erro Divisão por zero.")
  else:
    print(f"O resultado é: {resultado}")

calculadora()