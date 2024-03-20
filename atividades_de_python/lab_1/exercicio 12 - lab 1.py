quant = float(input("digite a quantidade que foi abastecido: "))
valor_litro = 2.86
troca_oleo = 50.00

tot = ((quant * valor_litro) + troca_oleo)

preco_tot = tot + (tot * 0.34)

print(round(preco_tot, 2))