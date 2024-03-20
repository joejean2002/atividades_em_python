#3. Escreva um programa que receba uma string e retorne a mesma string, mas com as vogais removidas.

def remover_vogais(string):
    vogais = "aeiouAEIOU"
    nova_string= ""

    for let in string:
        if let not in vogais:
            nova_string += let

    return nova_string

string = input("Digite a frase: ")

nova_string = remover_vogais(string)

print(nova_string)