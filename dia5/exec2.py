num = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, num+1):
  soma += i # Equivale a soma = soma + i

print("a soma dos número de 1 a", num, "é: ", soma)