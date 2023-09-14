# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.  °C=5×((°F−32)/9)

G_F = float(input("Qual a temperatura em Fahrenheit?")) # input de variavel
txt = "A temperatura convertida em Célsius é: " # Texto pra apesentação do resultado na saída
G_C = 5*((G_F-32)/9) # cálculo seguindo a fórmula
print(txt, round(G_C, 2)) # Saída

"""
Obtive a segunte saída do código:

Qual a temperatura em Fahrenheit?200
A temperatura convertida em Célsius é:  93.33
"""
