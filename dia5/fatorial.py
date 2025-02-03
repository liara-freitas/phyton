num = int(input("Digite um número interio positivo: "))

fatorial = 1
if num < 0:
  print ("Não existe fatorial de número negativo. ")

elif num == 0 or num ==1:
  print(f"O fatorial de {num} é 1.")

else: 
  for i in range(1, num+1):
    fatorial *= i

  print (f"O fatorial de {num} é {fatorial}")