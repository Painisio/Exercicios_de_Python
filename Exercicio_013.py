"""
Tendo como dado de entrada a altura ( h ) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens:  (72.7×h)−58 
Para mulheres:  (62.1×h)−44.7
"""

h = float(input("Qual sua altura?")) # input da variavel altura
genero = input("Qual seu genero?") # input da varivel genero

# pra resolver apropriadamente a questão tive de usar o condicional logico (IF):

if genero == "homem": # se homem, passa a executar os calculos a baixo:
    peso_ideal = (72.7*h)-58

    txt = "Seu peso Ideal é: " #textinho
    print(txt, peso_ideal) # Saída

if genero == "mulher": # se mulher, passa a executar os calculos a baixo:
    peso_ideal = (62.1*h)-44.7

    txt = "Seu peso Ideal é: " #textinho
    print(txt, peso_ideal) # Saída

"""
Obtive a seguinte saida:

Qual sua altura?1.8
Qual seu genero?mulher
Seu peso Ideal é:  67.08
"""
