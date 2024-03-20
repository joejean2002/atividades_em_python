# Leitura das entradas
quantidade_de_jogos = int(input("Quantitade de jogos: "))
valor_unitario = float(input("Qual o valor unitario do jogo? "))
frete = float(input("Valor do Frete: "))

# Calculo do valor a ser pago, incluindo o frete:
total = (valor_unitario * quantidade_de_jogos) + frete 
 
# Impressao do valor total:
print(total)