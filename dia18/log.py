import logging

logging.basicConfig(level=logging.DEBUG)

def multiplicar(a, b):
  logging.debug(f"Multiplicar {a} por {b}")
  return a * b

resultado = multiplicar(5, 6)
print(resultado)