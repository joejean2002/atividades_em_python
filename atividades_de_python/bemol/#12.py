#12. Crie um programa que calcule o delta de uma equação do segundo grau (ax² + bx + c = 0)

a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

delta = b**2 - 4*a*c

# Imprima o valor do delta
print(f"O valor do delta (Δ) é: {delta}")