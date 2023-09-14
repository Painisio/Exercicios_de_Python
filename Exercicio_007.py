# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

side = float(input("Informe o Lado do quadrado:")) # entrada de variavel lado
area_of_square = side**2 # calculo pra achar a área do quadrado
duble_area = side*2 # calculo do dobro da área
text = "O dobro da área do quadrado é: " # texto pra ficar apresentavel a resposta!
print(text, duble_area) # saída

"""
Essa foi a primeira resolução que apresentei para esse problema, na época.
obtive a seguinte resolução:

Informe o Lado do quadrado:4
O dobro da área do quadrado é:  8.0

Como se pode ver há um erro na resolução da questão, não na parte lógica mas sim na parte matemática:
duble_area = side*2

O correto seria:
duble_area = area_of_square*2

Obtendo Como resultado: 

Informe o Lado do quadrado:4
O dobro da área do quadrado é:  32.0
"""

# Hoje resolveria de uma foema diferente!

side = float(input("Informe o Lado do quadrado:")) #igual ao original, explicado no código acima...
duble_area = 2*(side**2) # Aqui que entra o diferencial, pois todos os calculos são computados em uma única variavel
text = "O dobro da área do quadrado é: " # igual ao original
print(text, duble_area) # saida

# Acredito que assim o código fique mais legivel e ocupe menos espaço de memória!
