"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
peso_ideal=(72.7×altura)−58
"""

altura = float(input("Qual sua altura?")) # input da primeira variavel, para fins de calculo usei altura em metros
peso_ideal = (72.7*altura)-58 # calculo exigido da questão!
txt = "Seu peso Ideal é: " # textinho pra ficar bacana...
print(txt, round(peso_ideal, 2)) # saída

"""
A saída obtida foi:

Qual sua altura?1.8
Seu peso Ideal é:  72.86
"""
