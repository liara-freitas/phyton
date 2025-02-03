import math

def distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    return math.sqrt((x2  - x1)**2 + (y2 - y1)**2)

x1 = float(input("Digite x1: "))
x2 = float(input("Digite x2: "))
y1 = float(input("Digite y1: "))
y1 = float(input("Digite y2: "))

dist = distancia ((x1 ,y1), (x2, y1))
print(f"A distância entre os pontos é: {dist}")