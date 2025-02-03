from wsgiref.validate import validator


distancia = float (input("Digite a distância percorrida em km: "))

tarifa_basica = 8.00
custo_km = 0.75

total = tarifa_basica + (custo_km * distancia)

print(f"Valor total da corida: R${total:.2f}")