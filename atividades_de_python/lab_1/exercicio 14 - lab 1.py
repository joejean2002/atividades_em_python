#Média ponderada
#Escreva um programa que leia quatro notas de um aluno. Como saída, imprima a média ponderada, 
#sabendo que os pesos das avaliações são respectivamente: 1, 2, 3 e 4.
#Arredonde os resultados com até 02 casas decimais de precisão.

#entrada
n1 = float(input("Digite a nota: "))
n2 = float(input("Digite a nota: "))
n3 = float(input("Digite a nota: "))
n4 = float(input("Digite a nota: "))

media = ((n1 * 1) + (n2 * 2) + (n3 * 3) + (n4 * 4)) / 10

print(round(media, 2))