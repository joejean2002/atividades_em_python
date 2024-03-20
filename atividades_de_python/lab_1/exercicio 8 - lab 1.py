from math import *
#leitura de entredas a, b e c
a = float(input("Digite o lado de A: "))
b = float(input("Digite o lado de B: "))
c = float(input("Digite o lado de C: "))

#calculo do semiperimetro
s = (a + b + c) / 2

#calculo da area
area = sqrt(s * (s - a) * (s - b) * (s - c))

#saidas com 5 casas decimais
print(round(area, 5))