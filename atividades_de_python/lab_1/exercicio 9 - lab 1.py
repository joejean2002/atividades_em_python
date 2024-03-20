from math import *
#valores de entrada
#Área do círculo e volume da esfera
#Escreva um programa que leia o valor de um raio r, inserido via teclado.
#Como saída, determine as seguintes informações, nesta ordem:
#Área de um círculo com o raio r.
#Volume de uma esfera com raio r.
#Arredonde os resultados com até 03 casas decimais de precisão.

raio = float(input("Digite o valo de um raio r: "))

#aplicacoes
area = pi * raio**2
vol = 3/4 * pi * raio**3

#saídas
print(round(area, 3))
print(round(vol, 3))