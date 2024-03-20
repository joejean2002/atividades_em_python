#O lucro de Bilichilde
#Bilichilde é consultora de uma linha de cosméticos. Seu lucro sobre o valor total de vendas é de 30%.

#Escreva um programa que leia o total de vendas de Bilichilde. Como saída, determine o valor do lucro obtido (em reais) 
#arredondado em duas casas decimais de precisão.

#Dicas
#Valores percentuais devem ser divididos por 100 antes de serem multiplicados por uma expressão.
#Os valores em reais devem ser arredondados em duas casas decimais de precisão.
#Dentro do comando print, use o comando round(x, 2) para arredondar a resposta x com até duas casas decimais.

#Entrada	
#200.0  #1452.88  #450.50
#Saída	
#60.0  #435.86  #135.15

#entradas

total_vendas = float(input("Digite o valor total das vendas de Bilichilde: "))

total = total_vendas * 0.30

#saida
print(round(total, 2))