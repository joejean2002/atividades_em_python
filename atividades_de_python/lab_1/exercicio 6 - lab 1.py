#Entradas da temperatura em Celsius
temperatura = float(input("Qual a temperatura em Celsius? "))

a = 273.15
conversion_kelvin = temperatura + a

print(round(conversion_kelvin, 2))