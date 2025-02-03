valor_emprestimo = float(input("Digite o valor do empréstimo: R$"))
renda_mensal = float (input("Digite sua renda mensal: R$"))
numero_parcelas = int (input("Digite o número de parcelas: "))

valor_parcela = valor_emprestimo  / numero_parcelas

limite_parcela = renda_mensal * 0.3

if valor_parcela <= limite_parcela:
    print("Empréstimo aprovado. ")
    print(f"Valor da parcela: R${valor_parcela:.2f}")

else:
    print("Empréstimo negado")
    print (f"Valor da parcela R${valor_parcela:.2f} excede 30% da renda mensal.")