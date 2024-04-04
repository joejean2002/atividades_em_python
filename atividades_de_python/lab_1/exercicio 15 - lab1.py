from math import *
#Entradas

a = float(input("Digite a distancia a: "))
b = float(input("Digite a distancia b: "))
y = radians(float(input("Digite o valor do angulo y entre a e b: ")))

c = a**2 + b**2 - 2*a*b * cos(y)
valor_c = c**0.5

print(round(valor_c, 2))