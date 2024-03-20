#5. Dado um número inteiro, escreva um programa para verificar se ele é um número primo.
def is_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

numero = int(input("Digite um número inteiro: "))

if is_primo(numero):
    print(numero, "é um número primo.")

else:
    print(numero, "não é um número primo.")