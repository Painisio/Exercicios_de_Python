"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
→ o produto do dobro do primeiro com metade do segundo.
→ soma do triplo do primeiro com o terceiro.
→ terceiro elevado ao cubo.
"""

n1 = int(input("Insira um número Inteiro:")) # input da primeira variavel, numero inteiro
n2 = int(input("Insira outro número Inteiro:")) # input da segunda variavel, numero inteiro
n3 = float(input("Insira um número Real: ")) # input da terceira variavel, numero float

a = (2*n1)*(n2/2) # o produto do dobro do primeiro com metade do segundo.
b = 3 * n1 + n3 # soma do triplo do primeiro com o terceiro.
c = n3**3 # terceiro elevado ao cubo.

# Texto para apresentação dos resultados:

txt_a = "o produto do dobro do primeiro com metade do segundo:"
txt_b = "soma do triplo do primeiro com o terceiro: "
txt_c = "terceiro valor ao cubo:"

# Respectivas saídas:

print(txt_a, a)
print(txt_b, b)
print(txt_c, c)

"""
Código rodado, obtive as seguintes saídas no console:

Insira um número Inteiro:2
Insira outro número Inteiro:3
Insira um número Real9.9
o produto do dobro do primeiro com metade do segundo: 6.0
soma do triplo do primeiro com o terceiro:  15.9
terceiro valor ao cubo: 970.2990000000001

Após conferir na calculadora, constatei que estava tudo ok!
"""
