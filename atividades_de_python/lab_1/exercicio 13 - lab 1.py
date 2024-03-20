#Na cidade de Manaus, setembro de 2023 foi o mês mais quente do ano. 
#Uma medição durante 6 dias aferiu os seguintes valores: 28,3; 27,5; 29,8; 38,3; 39,3; 32,2 graus celsius. 
#A menor temperatura do período foi 27,5 graus celsius e a maior temperatura foi 39,2 graus  celsius.
#Curiosidade: O maior valor de temperatura é o maior já registrado no mês, nos últimos 33 anos, 
#ele supera os 39,0 °C registrado em 21/09/2015.
#Agora, escreva um programa que leia 6 (seis) valores de temperatura e como saída imprima a 
#menor temperatura e a maior temperatura registradas no período.

#Entrada	
dia1=28.3
dia2=27.5
dia3=38.3
dia4=39.3
dia5=29.8
dia6=32.2
#Saída	
#Temperatura Minima: 27.5 graus celsius
#Temperatura Maxima: 39.3 graus celsius

#dia1 = float(input("Digite a temperatura: "))
#dia2 = float(input("Digite a temperatura: "))
#dia3 = float(input("Digite a temperatura: "))
#dia4 = float(input("Digite a temperatura: "))
#dia5 = float(input("Digite a temperatura: "))
#dia6 = float(input("Digite a temperatura: "))

tempmin = min(dia1, dia2, dia3, dia4, dia5, dia6)
tempmax = max(dia1, dia2, dia3, dia4, dia5, dia6)

print("Temperatura Minima:", tempmin, "graus celsius")
print("Temperatura Maxima:", tempmax, "graus celsius")