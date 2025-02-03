num1 = input("Digite número separados por espaço para o primeiro conjunto ").split()
num2 = input("Digite número separados por espaço para o segundo conjunto ").split()

conjunto1 = set(num1)
conjunto2 = set(num2)

uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)

print("União dos conujntos: ", uniao )
print("Interseção dos conjuntos: ", intersecao)