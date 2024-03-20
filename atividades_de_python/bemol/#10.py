#10. Crie um programa que receba 10 números e ordene em ordem crescente.

numeros = []

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

numeros_ordenados = sorted(numeros)

print("Números em ordem crescente:", numeros_ordenados)