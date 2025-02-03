def soma_lista(lista):
  if not lista:
    return 0
  else: 
    return lista[0] + soma_lista(lista[1:])

entrada = input("Digite uma lista de números separados por espaço: ")
lista = [int(num) for num in entrada.split()]
resultado = soma_lista(lista)
print(f"A soma dos elementos da lista é {resultado}")
