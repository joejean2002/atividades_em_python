#6. Dado uma lista de strings, escreva um programa que retorne uma lista com as strings ordenadas pelo seu tamanho.
list_string = ["programação", "trainee_digital", "bemol", "vendas"]

strings_ordenadas = sorted(list_string, key=lambda x: len(x))

print("Lista de strings ordenada por tamanho:", strings_ordenadas)