#4. Escreva um programa que imprima na tela os primeiros 10 números da sequência de Fibonacci.

a, b = 0, 1

for _ in range(10):
    print(a)
    a, b = b, a + b