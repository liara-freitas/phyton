entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

maior_numero = max(numeros)
menor_sumero= min(numeros)
soma_numeros = sum(numeros)
media_numeros = soma_numeros / len(numeros)

print("Maior número: ", maior_numero)
print("Menor número: ", menor_sumero)
print("Soma dos número: ", soma_numeros)
print("Média dos números: ", media_numeros)
