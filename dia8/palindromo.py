def eh_palindromo(texto):
  texto = ''.join(char.lower () for char in texto if char.isalnum())
  return texto == texto [::-1]

frase = input ("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
  print("É um palídromo.")
else:
  print("Não é um palíndromo.")
  