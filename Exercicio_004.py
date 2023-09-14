# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input("Insira a nota do primeiro bimestre:")) # Primeira variável
n2 = float(input("Insira a nota do segundo bimestre: ")) # Segunda variável
n3 = float(input("Insira a nota do terceiro bimestre: ")) # Terceira variável
n4 = float(input("Insira a nota do quarto bimestre:")) # Quarta variável

media = (n1 + n2 + n3 + n4)/4 # Fazendo a média
texto= "Sua média é: " #texto a ser exibido
print(texto, media) # saída

"""
A saída do código deve ser a seguinte:

Insira a nota do primeiro bimestre:4
Insira a nota do segundo bimestre: 5
Insira a nota do terceiro bimestre: 9
Insira a nota do quarto bimestre:10
Sua média é:  7.0
"""
