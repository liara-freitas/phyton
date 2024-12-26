qtd_itens = 8
valor_total = 120

desconto = (qtd_itens > 10) or (valor_total > 100)

print("Cliente tem direito ao desconto? " , desconto)