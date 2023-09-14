# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Quanto você ganha por hora?")) # Primeira variavel, valor da hora trabalhada
horas_mes = int(input("Quantas horas você trabalha por mês?")) # Seguda variavel, horas trabalhadas no mês
salario = salario_hora * horas_mes # cálculo, nada de outro mundo
txt = " Reais." # Textinho pra definir a moeda em questão
print(round(salario, 2), txt) # Saída

"""
Quanto você ganha por hora?5.71
Quantas horas você trabalha por mês?210
1199.1  Reais.

Considerando o conhecimento que possuo hoje em Python eu colocaria uma variavel para seleção da moeda
em que se revebe o salário! 
"""
