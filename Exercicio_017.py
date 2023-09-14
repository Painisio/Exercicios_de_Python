"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

#esse exercicio é meio que uma continuação do anterior (exercicio_016)...

import math

m2 = float(input("Quantos mestros quadrados pretende pintar?")) #input de variavel em float, os metros quadrados a serem pintados

litros = m2/6 #calculo dos litros necessários
q_latas18 = math.ceil(litros/18) #calculo da quantidade de latas de 18l
c_paint = 80.00 * q_latas18 #custo das latas de 18l

#respectivos textos
t_latas = "\nVocê precisará de: "
latas = "lata(s)."
t_reais = "Irá custar: R$: "

#respectivas saídas de código
print(t_latas, q_latas18, latas)
print(t_reais, c_paint)

q_latas36 = math.ceil(litros/3.6) #calculo das latas de 3.6l
c_paint36 = 80.00 * q_latas36 #custo das latas de 3.6l

#respectivas saídas
print(t_latas, q_latas36, latas)
print(t_reais, c_paint36)

resto = litros % 18

"""
Obtive as seguinte(s) saida(s) deste exercicio:

Quantos mestros quadrados pretende pintar?180

Você precisará de:  2 lata(s).
Irá custar: R$:  160.0

Você precisará de:  9 lata(s).
Irá custar: R$:  720.0

"""
