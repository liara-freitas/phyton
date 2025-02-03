try:
  numero = int(input("Digite um número inteiro: "))
  resultado = 100 / numero
except ValueError:
  print("Erro: Entrada inválida. Por favor, digite um número inteiro")

except ZeroDivisionError:
  print("Erro: Divisão por zero não é permitida.")

else:
  print(f"O resultado é: {resultado}")
finally:
  print("Operação de divisão finalizada.")