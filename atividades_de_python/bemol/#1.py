#Traine Bemol Dia 21/10/2023

#1. Crie um programa que receba duas idades inteiras e imprima na tela a maior idade.
idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

if idade1 > idade2:
    maior_idade = idade1

else:
    maior_idade = idade2

print("A maior idade é:", maior_idade)