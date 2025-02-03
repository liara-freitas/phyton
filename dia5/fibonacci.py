N = int(input("quantos termos da série Fibonacci você quer ver? "))

termo1 =0
termo2 =1
contador = 0

if N <= 0:
    print ("Por favor, insira um número positivo.")
elif N == 1:
    print("Série Fibonacci até", N, "termo:")
    print (termo1)
else: 
  print("Série Fibonacci:")
  while contador < N:
     print(termo1)
     proximo_termo = termo1 + termo2
     termo1 = termo2
     termo2 = proximo_termo
     contador +=1