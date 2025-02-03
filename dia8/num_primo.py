def eh_primo(numero):
  if numero <=1:
    return False
  for i in range(2, numero):
    if numero % i ==0:
        return False
  return True

num= int(input("Digite um número inteiro: "))

if eh_primo(num):
   print(f"{num} é um número primo.")
else:
   print(f"{num} não é um número primo. ")